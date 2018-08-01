import os
import re
import unittest
from typing import List, Dict, Any

from pyjsg.jsglib.loader import loads, is_valid, logger
from pyjsg.validate_json import JSGPython


class PythonGeneratorUtils(unittest.TestCase):
    cwd = os.path.abspath(os.path.join(os.path.dirname(__file__), 'py'))
    save_output_files: bool = False
    save_all_output_files: bool = False

    def tearDown(self):
        self.assertFalse(self.save_output_files, "save_output_files is True")
        if self.save_all_output_files:
            print("Warning: tests.test_python_generator.utils save_all_output_files is True")

    @staticmethod
    def _strip_details(txt: str) -> str:
        txt = re.sub(r'(# Auto generated from JSGPython by PyJSG version ).*', r'\1', txt)
        return re.sub(r'(# Generation date:).*', r'\1', txt).strip()

    def do_test(self, jsg: str, test_file: str, module, passing_json: List[str], failing_vars: Dict[str, Any],
                failing_json: List[str] = None, print_python: bool = False) -> None:
        x = JSGPython(jsg, print_python=print_python)
        py_file = os.path.join(self.cwd, test_file + '.py')
        with open(py_file) as f:
            expected = self._strip_details(f.read())
        actual = self._strip_details(x.python)
        if expected != actual:
            if self.save_output_files or self.save_all_output_files:
                with open(py_file, 'w') as f:
                    f.write(x.python)
                    print(f"***** {py_file} updated *****")
            self.maxDiff = None
            self.assertEqual(expected, actual)

        for p in passing_json:
            json_doc = loads(p, module)
            log = logger()
            doc_is_valid = is_valid(json_doc, log)
            self.assertTrue(doc_is_valid, log.getvalue())

        for f in failing_json if failing_json else []:
            doc_is_valid = True
            json_doc = None
            error = ""
            try:
                json_doc = loads(f, module)
            except ValueError as e:
                doc_is_valid = False
                error = e
            if doc_is_valid:
                log = logger()
                doc_is_valid = is_valid(json_doc, log)
                error = log.getvalue()
            self.assertFalse(doc_is_valid, f)

        for k, v in failing_vars.items():
            with self.assertRaises(ValueError):
                vv = f'"{v}"' if isinstance(v, str) else str(v)
                loads(f'{{"{k}": {vv}}}', module)

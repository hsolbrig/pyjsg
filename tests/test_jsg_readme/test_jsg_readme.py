import sys
import os
import unittest

from importlib import import_module

from pyjsg.jsglib.jsg import load, JSGException
from pyjsg.jsglib.logger import Logger
from pyjsg.parser_impl.generate_python import generate
from jsonasobj import load as json_load

log = Logger(sys.stdout)


class JSGReadMeTestCase(unittest.TestCase):

    log = Logger(sys.stdout)

    def eval_for_error(self, fn: str, mod, error: str):
        fn_in_json = json_load(fn)
        expected = fn_in_json._ERROR
        del fn_in_json._ERROR
        with self.assertRaises(JSGException) as context:
            r = load(fn, mod)
        self.assertEqual(expected, str(context.exception))

    def eval_python(self, cwd: str, dirpath: str, fn: str) -> None:
        basefile = fn.rsplit('.', 1)[0]
        outfile = os.path.abspath(os.path.join(cwd, "py", basefile + ".py"))
        generate([os.path.relpath(os.path.join(dirpath, fn)), "-o", outfile])
        mod = import_module("tests.test_jsg_readme.py." + basefile)
        num_evaluated = 0
        for dirpath, _, filenames in os.walk(os.path.join(cwd, "json")):
            for filename in filenames:
                if filename.startswith(basefile) and filename.endswith(".json"):
                    num_evaluated += 1
                    full_fn = os.path.join(dirpath, filename)
                    if "_f" not in os.path.basename(full_fn):
                        r = load(full_fn, mod)
                        self.assertTrue(r._is_valid(log))
                    else:
                        self.eval_for_error(full_fn, mod, "ValueError: Unknown attribute: text=left in 2017")
        # TODO: complete this test
        # self.assertTrue(num_evaluated > 0, f"{fn} has no json equivalents")

    def test_jsg_readme(self):
        cwd = os.path.abspath(os.path.dirname(__file__))
        num_evaluated = 0
        for dirpath, _, filenames in os.walk(os.path.join(cwd, "jsg")):
            for fn in filenames:
                if fn.endswith(".jsg"):
                    num_evaluated += 1
                    self.eval_python(cwd, dirpath, fn)
        self.assertEqual(6, num_evaluated)


if __name__ == '__main__':
    unittest.main()

import os
import unittest
from contextlib import redirect_stdout
from io import StringIO

files = []


class JSGTestCase(unittest.TestCase):
    def test_input_files(self):
        from pyjsg.parser_impl.generate_python import generate
        base = os.path.abspath(os.path.dirname(__file__))
        ntested = 0
        for dirpath, _, filenames in os.walk(os.path.join(base, "jsg")):
            outf = StringIO()
            with redirect_stdout(outf):
                for fn in filenames:
                    if fn.endswith(".jsg") and (not files or fn in files):
                        infile = os.path.relpath(os.path.join(dirpath, fn))
                        outfile = os.path.relpath(os.path.join(base, "py", fn.rsplit('.', 1)[0] + '.py'))
                        self.assertEqual(0, generate([infile, "-o", outfile, "-e", "-nh"]))
                        ntested += 1
        if files:
            print("WARNING: all jsg files were not tested")
            self.assertEqual(len(files), ntested)
        else:
            self.assertEqual(24, ntested)

if __name__ == '__main__':
    unittest.main()

import os
import unittest
from contextlib import redirect_stdout
from io import StringIO

from pyjsg.parser_impl.generate_python import generate


class EOptionTestCase(unittest.TestCase):
    def test_e_option(self):
        """ Test the '-e' option """
        shexj_jsg = os.path.join(os.path.dirname(__file__), '..', '..', 'tests', 'test_basics', 'jsg', 'ShExJ.jsg')
        outf = StringIO()
        with redirect_stdout(outf):
            # Should not fail
            self.assertEqual(0, generate([shexj_jsg, "-e"]))


if __name__ == '__main__':
    unittest.main()

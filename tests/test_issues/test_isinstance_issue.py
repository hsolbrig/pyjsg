
import unittest
from typing import Union

import os

from pyjsg.jsglib import isinstance_


class IsInstanceTestCase(unittest.TestCase):
    def test_isinstance_issue(self):
        from pyjsg.jsglib.loader import isinstance_
        x = Union[int, str]
        with self.assertRaises(TypeError):
            isinstance(17, x)
        self.assertTrue(isinstance_(17, x))

    def test_issue_with_shexj(self):
        from pyjsg.parser_impl.generate_python import generate
        data_root = os.path.join(os.path.split(os.path.abspath(__file__))[0], '..', 'test_basics')
        jsg_path = os.path.relpath(os.path.join(data_root, 'jsg', 'ShExJ.jsg'))
        py_path = os.path.abspath(os.path.join(data_root, 'py', 'ShExJ.py'))
        self.assertEqual(0, generate([jsg_path, "-o", py_path, "-e", "-nh"]))
        from tests.test_basics.py import ShExJ
        self.assertTrue(isinstance_(ShExJ.IRIREF("http://foo.bar"), ShExJ.shapeExprLabel))

if __name__ == '__main__':
    unittest.main()

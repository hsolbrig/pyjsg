
import unittest
from typing import cast

from pyjsg.parser_impl.jsg_ebnf_parser import JSGEbnf

from tests.parser import parse


class EBNFTestCase(unittest.TestCase):
    tests = [('*', 0, None, "List[k]"),
             ('?', 0, 1, "Optional[k]"),
             ('+', 1, None, "List[k]"),
             ('{0}', 0, 0, "None"),
             ('{1}', 1, 1, "k"),
             ('{1,}', 1, None, "List[k]"),
             ('{2}', 2, 2, "List[k]"),
             ('{2,}', 2, None, "List[k]"),
             ('{3,*}', 3, None, "List[k]"),
             ('{3,7}', 3, 7, "List[k]")]

    def test1(self):
        for text, min_, max_, ptype in self.tests:
            t = cast(JSGEbnf, parse(text, "ebnfSuffix", JSGEbnf))
            self.assertEqual(min_, t.min)
            self.assertEqual(max_, t.max)
            self.assertEqual(ptype, t.python_type("k"))


if __name__ == '__main__':
    unittest.main()

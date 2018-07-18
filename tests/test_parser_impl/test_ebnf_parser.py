import unittest
from dataclasses import dataclass
from typing import cast, Optional

from pyjsg.parser_impl.jsg_ebnf_parser import JSGEbnf
from pyjsg.parser_impl.jsg_valuetype_parser import JSGValueType

from tests.test_basics.parser import parse


@dataclass
class testentry:
    text: str
    min: int
    max: Optional[int]
    ptype: str
    oneopt: bool
    mult: bool
    stype: str

class EBNFTestCase(unittest.TestCase):
    tests = [testentry('*', 0, None, "List[k]", False, True, "ArrayFactory('{name}', _CONTEXT, k, 0, None)"),
             testentry('?', 0, 1, "Optional[k]", True, False, "Optional[k]"),
             testentry('+', 1, None, "List[k]", False, True, "ArrayFactory('{name}', _CONTEXT, k, 1, None)"),
             testentry('{0}', 0, 0, "type(None)", False, False, "type(None)"),
             testentry('{0, 1}', 0, 1, "Optional[k]", True, False, "Optional[k]"),
             testentry('{1}', 1, 1, "k", False, False, "k"),
             testentry('{1, }', 1, None, "List[k]", False, True, "ArrayFactory('{name}', _CONTEXT, k, 1, None)"),
             testentry('{2}', 2, 2, "List[k]", False, True, "ArrayFactory('{name}', _CONTEXT, k, 2, 2)"),
             testentry('{2 ,}', 2, None, "List[k]", False, True, "ArrayFactory('{name}', _CONTEXT, k, 2, None)"),
             testentry('{ 3 , * }', 3, None, "List[k]", False, True, "ArrayFactory('{name}', _CONTEXT, k, 3, None)"),
             testentry('{3,7}', 3, 7, "List[k]", False, True, "ArrayFactory('{name}', _CONTEXT, k, 3, 7)")]

    def test_basics(self):
        ty = cast(JSGValueType, parse('"[a-z]+"', 'valueType', JSGValueType))
        for te in self.tests:
            t = cast(JSGEbnf, parse(te.text, "ebnfSuffix", JSGEbnf))
            self.assertEqual(str(t), te.text.replace(' ', ''))
            self.assertEqual(te.min, t.min, te.text)
            self.assertEqual(te.max, t.max, te.text)
            self.assertEqual(te.ptype, t.python_cardinality("k"), te.text)
            self.assertEqual(te.stype, t.signature_cardinality("k"), te.text)
            self.assertEqual(te.oneopt, t.one_optional_element, te.text)
            self.assertEqual(te.mult, t.multiple_elements, te.text)

    def test_double_optional(self):
        t = cast(JSGEbnf, parse('?', 'ebnfSuffix', JSGEbnf))
        self.assertEqual('Optional[k]', t.python_cardinality('Optional[k]'))
        self.assertEqual('Optional[k]', t.signature_cardinality('Optional[k]'))

    def test_all_optional(self):
        t = cast(JSGEbnf, parse('?', 'ebnfSuffix', JSGEbnf))
        self.assertEqual('Optional[k]', t.python_cardinality('k', True))
        self.assertEqual("Optional[k]", t.signature_cardinality('k', True))
        t = cast(JSGEbnf, parse('+', 'ebnfSuffix', JSGEbnf))
        self.assertEqual('Optional[List[k]]', t.python_cardinality('k', True))
        self.assertEqual("Optional[ArrayFactory('{name}', _CONTEXT, k, 1, None)]", t.signature_cardinality('k', True))

if __name__ == '__main__':
    unittest.main()

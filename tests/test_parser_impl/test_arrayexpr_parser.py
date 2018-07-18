
import unittest
from typing import cast

from pyjsg.parser_impl.jsg_arrayexpr_parser import JSGArrayExpr
from tests.test_basics.parser import parse


class ArrayExprTestCase(unittest.TestCase):
    def check(self, t: JSGArrayExpr, expected) -> None:
        tup = (str(t), t.python_type(), t.dependency_list(), t.signature_type(), t.mt_value(), t.members_entries())
        self.assertEqual(expected, tup)

    def test_basics(self):
        t = cast(JSGArrayExpr, parse("id [@string] ", "arrayDef", JSGArrayExpr))
        self.check(t,
              ('arrayExpr: [valueType: builtinValueType: @string]',
               'List[str]',
                [],
                "ArrayFactory('{name}', _CONTEXT, String, 0, None)",
                'None',
                []))

        t = cast(JSGArrayExpr, parse("id [@int] ", "arrayDef", JSGArrayExpr))
        self.check(t,
              ('arrayExpr: [valueType: builtinValueType: @int]',
               'List[int]',
               [],
               "ArrayFactory('{name}', _CONTEXT, Integer, 0, None)",
               'None',
               [])
              )

        t = cast(JSGArrayExpr, parse("id [.] ", "arrayDef", JSGArrayExpr))
        self.check(t,
              ('arrayExpr: [valueType: builtinValueType: AnyType]',
               'List[object]',
               [],
               "ArrayFactory('{name}', _CONTEXT, AnyType, 0, None)",
               'None',
               [])
              )

        t = cast(JSGArrayExpr, parse("id [(Aa|BB|'foo')] ", "arrayDef", JSGArrayExpr))
        self.check(t,
              ("arrayExpr: [valueType: ((STRING: pattern: r'foo') | Undefined(Aa) | BB)]",
               'List[Union[str, Undefined(Aa), str]]',
               ['_Anon1', 'Aa', 'BB'],
               "ArrayFactory('{name}', _CONTEXT, Union[_Anon1, Undefined(Aa), BB], 0, None)",
               'None',
               [])
              )

        t = cast(JSGArrayExpr, parse("id [(Aa|BB|'foo'){0,}] ", "arrayDef", JSGArrayExpr))
        self.check(t,
              ("arrayExpr: [valueType: ((STRING: pattern: r'foo') | Undefined(Aa) | BB){0,}]",
                'List[Union[str, Undefined(Aa), str]]',
               ['_Anon1', 'Aa', 'BB'],
               "ArrayFactory('{name}', _CONTEXT, Union[_Anon1, Undefined(Aa), BB], 0, None)",
               'None',
               [])
              )

    def test_options(self):
        txt = "exclusions [(objectValue|LanguageStem) +]"
        t = cast(JSGArrayExpr, parse(txt, "arrayDef", JSGArrayExpr))
        self.check(t,
                   ('arrayExpr: [valueType: (Undefined(objectValue) | Undefined(LanguageStem))+]',
                    'List[Union[Undefined(objectValue), Undefined(LanguageStem)]]',
                    ['objectValue', 'LanguageStem'],
                    "ArrayFactory('{name}', _CONTEXT, Union[Undefined(objectValue), Undefined(LanguageStem)], 1, None)",
                    'None',
                    [])
                   )

    def test_multi_types(self):
        txt = "x [objectValue | languageStem {3,7}]"
        t = cast(JSGArrayExpr, parse(txt, "arrayDef", JSGArrayExpr))
        self.check(t,
                   ('arrayExpr: [(valueType: ID: objectValue | valueType: ID: '
                    'languageStem){3,7}]',
                    'List[Union[Undefined(objectValue), Undefined(languageStem)]]',
                    ['objectValue', 'languageStem'],
                    "ArrayFactory('{name}', _CONTEXT, Union[Undefined(objectValue), Undefined(languageStem)], 3, 7)",
                    'None',
                    [])
                   )


if __name__ == '__main__':
    unittest.main()


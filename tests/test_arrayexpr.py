
import unittest
from typing import cast

from pyjsg.parser_impl.jsg_arrayexpr_parser import JSGArrayExpr
from tests.parser import parse


class ArrayExprTestCase(unittest.TestCase):
    def test_basics(self):
        t = cast(JSGArrayExpr, parse("id [@string] ", "arrayDef", JSGArrayExpr))
        self.assertEqual("k = List[str]", t.as_python('k').strip())
        t = cast(JSGArrayExpr, parse("id [@int] ", "arrayDef", JSGArrayExpr))
        self.assertEqual("k = List[int]", t.as_python('k').strip())
        t = cast(JSGArrayExpr, parse("id [.] ", "arrayDef", JSGArrayExpr))
        self.assertEqual("k = List[object]", t.as_python('k').strip())
        t = cast(JSGArrayExpr, parse("id [(Aa|BB|'foo')] ", "arrayDef", JSGArrayExpr))
        self.assertEqual("k = List[Union[_Anon1, Aa, BB]]", t.as_python('k').strip())
        t = cast(JSGArrayExpr, parse("id [(Aa|BB|'foo'){0,}] ", "arrayDef", JSGArrayExpr))
        self.assertEqual("k = List[Union[_Anon1, Aa, BB]]", t.as_python('k').strip())

    def test_options(self):
        txt = "exclusions [(objectValue|LanguageStem) +]"
        t = cast(JSGArrayExpr, parse(txt, "arrayDef", JSGArrayExpr))
        self.assertEqual("arrayExpr: [valueType: (objectValue | LanguageStem)+]", str(t))
        self.assertEqual("k = List[Union[objectValue, LanguageStem]]", t.as_python('k').strip())
        self.assertEqual(['objectValue', 'LanguageStem'], t.dependency_list())

if __name__ == '__main__':
    unittest.main()


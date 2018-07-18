import unittest
from typing import cast

from pyjsg.parser_impl.jsg_doc_parser import JSGDocParser
from pyjsg.parser_impl.jsg_pairdef_parser import JSGPairDef
from tests.test_basics.parser import parse

tests = [("x1 : INT", "INT", "str", ["INT"], ['x1: str = None'], [('x1', 'INT')],
          "pairDef: x1 : valueType: LEXER_ID_REF: INT"),
         ("x2 : INT?", "Optional[INT]", "Optional[str]", ["INT"], ['x2: Optional[str] = None'], [
             ('x2', 'Optional[INT]')], "pairDef: x2 : valueType: LEXER_ID_REF: INT?"),
         ("x3 : INT+", "ArrayFactory('{name}', _CONTEXT, INT, 1, None)", "List[str]", ["INT"],
          ['x3: List[str] = None'], [('x3', "ArrayFactory('x3', _CONTEXT, INT, 1, None)")],
          "pairDef: x3 : valueType: LEXER_ID_REF: INT+"),
         ("x4 : INT*", "ArrayFactory('{name}', _CONTEXT, INT, 0, None)", "List[str]",
          ["INT"], ['x4: List[str] = None'], [("x4", "ArrayFactory('x4', _CONTEXT, INT, 0, None)")],
          "pairDef: x4 : valueType: LEXER_ID_REF: INT*"),
         ("x5 : INT{1}", "INT",  "str", ["INT"], ['x5: str = None'], [("x5", "INT")],
          "pairDef: x5 : valueType: LEXER_ID_REF: INT{1}"),
         ("x6 : INT{1, 1}", "INT", "str", ["INT"], ['x6: str = None'], [("x6", "INT")],
          "pairDef: x6 : valueType: LEXER_ID_REF: INT{1,1}"),
         ("x7 : INT{1,}", "ArrayFactory('{name}', _CONTEXT, INT, 1, None)",
          "List[str]", ["INT"], ['x7: List[str] = None'], [("x7", "ArrayFactory('x7', _CONTEXT, INT, 1, None)")],
          "pairDef: x7 : valueType: LEXER_ID_REF: INT{1,}")]

initializers = {
    "x1 : INT": ['self.x1 = x1'],
    "x2 : INT?": ['self.x2 = x2'],
    "x3 : INT+": ["self.x3 = x3"],
    "x4 : INT*": ["self.x4 = x4"],
    "x5 : INT{1}": ['self.x5 = x5'],
    "x6 : INT{1, 1}": ['self.x6 = x6'],
    "x7 : INT{1,}": ["self.x7 = x7"]
}

builtins = [("k : @string", ["k: str = None"], ['self.k = k'],
             'pairDef: k : valueType: builtinValueType: @string')]


class PairDefTestCase(unittest.TestCase):
    def test_simple_pairdef(self):
        for text, sig, py, deps, sigs, memins, v in tests:
            t = cast(JSGPairDef, parse(text, "pairDef", JSGPairDef))
            self.assertEqual(v, str(t))
            self.assertEqual(sig, t.signature_type(), text)
            self.assertEqual(py, t.python_type(), text)
            self.assertEqual(deps, t.dependency_list(), text)
            self.assertEqual(sigs, t.signatures(), text)
            self.assertEqual(memins, t.members_entries(), text)
            self.assertEqual(initializers[text], t.initializers())

    def test_odd_identifiers(self):
        t = cast(JSGPairDef, parse("'regString' : INT", "pairDef", JSGPairDef))
        self.assertEqual('pairDef: regString : valueType: LEXER_ID_REF: INT', str(t))
        self.assertEqual([('regString', 'INT')], t.members_entries())
        self.assertEqual([('regString', 'Optional[INT]')], t.members_entries(True))
        self.assertEqual(['regString: str = None'], t.signatures())
        self.assertEqual(['self.regString = regString'], t.initializers())
        self.assertEqual("pairDef: regString : valueType: LEXER_ID_REF: INT", str(t))

        t = cast(JSGPairDef, parse("'def' : INT", "pairDef", JSGPairDef))
        self.assertEqual('pairDef: def : valueType: LEXER_ID_REF: INT', str(t))
        self.assertEqual([('def', 'INT')], t.members_entries())
        self.assertEqual(['def_: str = None'], t.signatures())
        self.assertEqual(["setattr(self, 'def', def_ if def_ is not None else _kwargs.get('def', None))"],
                         t.initializers())
        self.assertEqual("pairDef: def : valueType: LEXER_ID_REF: INT", str(t))

        t = cast(JSGPairDef, parse("'a var' : @number", "pairDef", JSGPairDef))
        self.assertEqual("pairDef: a var : valueType: builtinValueType: @number", str(t))
        self.assertEqual([('a var', 'Number')], t.members_entries())
        self.assertEqual([], t.signatures())
        self.assertEqual(["setattr(self, 'a var', _kwargs.get('a var', None))"], t.initializers())

    def test_pairdef_shorthand(self):
        text = "(x1 'v 2' 'class') : @number {3,17}"
        t = cast(JSGPairDef, parse(text, "pairDef", JSGPairDef))
        self.assertEqual(['x1: List[float] = None', 'class_: List[float] = None'], t.signatures())
        self.assertEqual([
            'self.x1 = x1',
            "setattr(self, 'v 2', _kwargs.get('v 2', None))",
            "setattr(self, 'class', class_ if class_ is not None else "
            "_kwargs.get('class', None))"],
                         t.initializers())
        self.assertEqual("pairDef: (x1 | v 2 | class) : valueType: builtinValueType: @number{3,17}", str(t))
        self.assertEqual([], t.dependency_list())

        text = "(x1 'v 2' 'class') : @bool ?"
        t = cast(JSGPairDef, parse(text, "pairDef", JSGPairDef))
        self.assertEqual(['x1: Optional[bool] = None', 'class_: Optional[bool] = None'], t.signatures())
        self.assertEqual([
            'self.x1 = x1',
            "setattr(self, 'v 2', _kwargs.get('v 2', None))",
            "setattr(self, 'class', class_ if class_ is not None else _kwargs.get('class', None))"], t.initializers())
        self.assertEqual("pairDef: (x1 | v 2 | class) : valueType: builtinValueType: @bool?", str(t))
        self.assertEqual([], t.dependency_list())
        self.assertEqual([('x1', 'Optional[Boolean]'),
                          ('v 2', 'Optional[Boolean]'),
                          ('class', 'Optional[Boolean]')], t.members_entries())

        text = "(x1 'v 2' 'class') : @null"
        t = cast(JSGPairDef, parse(text, "pairDef", JSGPairDef))
        self.assertEqual(['x1: type(None) = EmptyAny', 'class_: type(None) = EmptyAny'], t.signatures())
        self.assertEqual([
            'self.x1 = x1',
             "setattr(self, 'v 2', _kwargs.get('v 2', EmptyAny))",
             "setattr(self, 'class', class_ if class_ is not EmptyAny else _kwargs.get('class', EmptyAny))"],
            t.initializers())
        self.assertEqual("pairDef: (x1 | v 2 | class) : valueType: builtinValueType: @null", str(t))
        self.assertEqual([], t.dependency_list())
        self.assertEqual([('x1', 'JSGNull'), ('v 2', 'JSGNull'), ('class', 'JSGNull')], t.members_entries())
        text = "(def 'v 2' class) : @null"
        t = cast(JSGPairDef, parse(text, "pairDef", JSGPairDef))
        self.assertEqual([
            "setattr(self, 'def', def_ if def_ is not EmptyAny else _kwargs.get('def', "
             'EmptyAny))',
             "setattr(self, 'v 2', _kwargs.get('v 2', EmptyAny))",
             "setattr(self, 'class', class_ if class_ is not EmptyAny else "
             "_kwargs.get('class', EmptyAny))"], t.initializers())

    def test_pairdef_valuetype_ref(self):
        text = "nonobj = {a:@string b:@number?};  obj = {nonobj}"
        t = cast(JSGPairDef, parse(text, "grammarElt", JSGPairDef))
        self.assertEqual(['a: Optional[float] = None', 'b: Optional[float] = None'], t.signatures())

    def test_pairdef_builtins(self):
        for text, sig, init, s in builtins:
            t = cast(JSGPairDef, parse(text, "pairDef", JSGPairDef))
            self.assertEqual(sig, t.signatures())
            self.assertEqual(init, t.initializers())
            self.assertEqual(s, str(t))
            self.assertEqual([], t.dependency_list())
            self.assertEqual([('k', 'String')], t.members_entries())

    def test_pairdef_reference(self):
        text = """
Patient {name: @string+ age: @int}
b {Patient*}
"""
        d = cast(JSGDocParser, parse(text, "doc", JSGDocParser))
        self.assertIsNotNone(d)
        t = d._context.reference('b')
        self.assertEqual('objectExpr: simple object', str(t))
        self.assertEqual(['name: List[str] = None', 'age: int = None'], t.signatures())
        self.assertEqual(['self.name = name', 'self.age = age'], t.initializers())
        self.assertEqual(['Patient'], t.dependency_list())
        self.assertEqual([
            ('name', "ArrayFactory('{name}', _CONTEXT, ArrayFactory('name', _CONTEXT, String, 1, None), 0, None)"),
             ('age', "ArrayFactory('{name}', _CONTEXT, Integer, 0, None)")], t.members_entries())
        self.assertEqual('None', t.mt_value())


if __name__ == '__main__':
    unittest.main()

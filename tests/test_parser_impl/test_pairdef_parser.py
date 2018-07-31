import unittest
from typing import cast

from pyjsg.parser_impl.jsg_doc_parser import JSGDocParser
from pyjsg.parser_impl.jsg_pairdef_parser import JSGPairDef
from tests.test_basics.parser import parse

tests = [("x1 : INT", "INT", "str", ["INT"], ['x1: str = None'], [('x1', 'INT')],
          "pairDef: x1 : valueType: LEXER_ID_REF: INT"),
         ("x2 : INT?", "typing.Optional[INT]", "typing.Optional[str]", ["INT"], ['x2: typing.Optional[str] = None'], [
             ('x2', 'typing.Optional[INT]')], "pairDef: x2 : valueType: LEXER_ID_REF: INT?"),
         ("x3 : INT+", "jsg.ArrayFactory('{name}', _CONTEXT, INT, 1, None)", "typing.List[str]", ["INT"],
          ['x3: typing.List[str] = None'], [('x3', "jsg.ArrayFactory('x3', _CONTEXT, INT, 1, None)")],
          "pairDef: x3 : valueType: LEXER_ID_REF: INT+"),
         ("x4 : INT*", "jsg.ArrayFactory('{name}', _CONTEXT, INT, 0, None)", "typing.List[str]",
          ["INT"], ['x4: typing.List[str] = None'], [("x4", "jsg.ArrayFactory('x4', _CONTEXT, INT, 0, None)")],
          "pairDef: x4 : valueType: LEXER_ID_REF: INT*"),
         ("x5 : INT{1}", "INT",  "str", ["INT"], ['x5: str = None'], [("x5", "INT")],
          "pairDef: x5 : valueType: LEXER_ID_REF: INT{1}"),
         ("x6 : INT{1, 1}", "INT", "str", ["INT"], ['x6: str = None'], [("x6", "INT")],
          "pairDef: x6 : valueType: LEXER_ID_REF: INT{1,1}"),
         ("x7 : INT{1,}", "jsg.ArrayFactory('{name}', _CONTEXT, INT, 1, None)",
          "typing.List[str]", ["INT"], ['x7: typing.List[str] = None'], [("x7", "jsg.ArrayFactory('x7', _CONTEXT, INT, 1, None)")],
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
        t = cast(JSGPairDef, parse("'String' : INT", "pairDef", JSGPairDef))
        self.assertEqual('pairDef: String : valueType: LEXER_ID_REF: INT', str(t))
        self.assertEqual([('String', 'INT')], t.members_entries())
        self.assertEqual([('String', 'typing.Optional[INT]')], t.members_entries(True))
        self.assertEqual(['String: str = None'], t.signatures())
        self.assertEqual(['self.String = String'], t.initializers())
        self.assertEqual("pairDef: String : valueType: LEXER_ID_REF: INT", str(t))

        t = cast(JSGPairDef, parse("'def' : INT", "pairDef", JSGPairDef))
        self.assertEqual('pairDef: def : valueType: LEXER_ID_REF: INT', str(t))
        self.assertEqual([('def', 'INT')], t.members_entries())
        self.assertEqual(['def_: str = None'], t.signatures())
        self.assertEqual(["setattr(self, 'def', def_ if def_ is not None else _kwargs.get('def', None))"],
                         t.initializers())
        self.assertEqual("pairDef: def : valueType: LEXER_ID_REF: INT", str(t))

        t = cast(JSGPairDef, parse("'a var' : @number", "pairDef", JSGPairDef))
        self.assertEqual("pairDef: a var : valueType: builtinValueType: @number", str(t))
        self.assertEqual([('a var', 'jsg.Number')], t.members_entries())
        self.assertEqual([], t.signatures())
        self.assertEqual(["setattr(self, 'a var', _kwargs.get('a var', None))"], t.initializers())

    def test_pairdef_shorthand(self):
        text = "(x1 'v 2' 'class') : @number {3,17}"
        t = cast(JSGPairDef, parse(text, "pairDef", JSGPairDef))
        self.assertEqual(['x1: typing.List[float] = None', 'class_: typing.List[float] = None'], t.signatures())
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
        self.assertEqual(['x1: typing.Optional[bool] = None', 'class_: typing.Optional[bool] = None'], t.signatures())
        self.assertEqual([
            'self.x1 = x1',
            "setattr(self, 'v 2', _kwargs.get('v 2', None))",
            "setattr(self, 'class', class_ if class_ is not None else _kwargs.get('class', None))"], t.initializers())
        self.assertEqual("pairDef: (x1 | v 2 | class) : valueType: builtinValueType: @bool?", str(t))
        self.assertEqual([], t.dependency_list())
        self.assertEqual([('x1', 'typing.Optional[jsg.Boolean]'),
                          ('v 2', 'typing.Optional[jsg.Boolean]'),
                          ('class', 'typing.Optional[jsg.Boolean]')], t.members_entries())

        text = "(x1 'v 2' 'class') : @null"
        t = cast(JSGPairDef, parse(text, "pairDef", JSGPairDef))
        self.assertEqual(['x1: type(None) = jsg.Empty', 'class_: type(None) = jsg.Empty'], t.signatures())
        self.assertEqual([
            'self.x1 = x1',
             "setattr(self, 'v 2', _kwargs.get('v 2', jsg.Empty))",
             "setattr(self, 'class', class_ if class_ is not jsg.Empty else _kwargs.get('class', jsg.Empty))"],
            t.initializers())
        self.assertEqual("pairDef: (x1 | v 2 | class) : valueType: builtinValueType: @null", str(t))
        self.assertEqual([], t.dependency_list())
        self.assertEqual([('x1', 'jsg.JSGNull'), ('v 2', 'jsg.JSGNull'), ('class', 'jsg.JSGNull')], t.members_entries())
        text = "(def 'v 2' class) : @null"
        t = cast(JSGPairDef, parse(text, "pairDef", JSGPairDef))
        self.assertEqual([
            "setattr(self, 'def', def_ if def_ is not jsg.Empty else _kwargs.get('def', "
             'jsg.Empty))',
             "setattr(self, 'v 2', _kwargs.get('v 2', jsg.Empty))",
             "setattr(self, 'class', class_ if class_ is not jsg.Empty else "
             "_kwargs.get('class', jsg.Empty))"], t.initializers())

    def test_pairdef_valuetype_ref(self):
        text = "nonobj = {a:@string b:@number?};  obj = {nonobj}"
        t = cast(JSGPairDef, parse(text, "grammarElt", JSGPairDef))
        self.assertEqual(['a: typing.Optional[float] = None', 'b: typing.Optional[float] = None'], t.signatures())

    def test_pairdef_builtins(self):
        for text, sig, init, s in builtins:
            t = cast(JSGPairDef, parse(text, "pairDef", JSGPairDef))
            self.assertEqual(sig, t.signatures())
            self.assertEqual(init, t.initializers())
            self.assertEqual(s, str(t))
            self.assertEqual([], t.dependency_list())
            self.assertEqual([('k', 'jsg.String')], t.members_entries())

    def test_pairdef_reference(self):
        text = """
Patient {name: @string+ age: @int}
b {Patient*}
"""
        d = cast(JSGDocParser, parse(text, "doc", JSGDocParser))
        self.assertIsNotNone(d)
        t = d._context.reference('b')
        self.assertEqual('objectExpr: simple object', str(t))
        self.assertEqual(['name: typing.List[str] = None', 'age: int = None'], t.signatures())
        self.assertEqual(['self.name = name', 'self.age = age'], t.initializers())
        self.assertEqual(['Patient'], t.dependency_list())
        self.assertEqual([
            ('name', "jsg.ArrayFactory('name', _CONTEXT, jsg.ArrayFactory('name', _CONTEXT, jsg.String, 1, None), 0, None)"),
             ('age', "jsg.ArrayFactory('age', _CONTEXT, jsg.Integer, 0, None)")], t.members_entries())
        self.assertEqual('None', t.mt_value())


if __name__ == '__main__':
    unittest.main()

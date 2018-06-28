
import unittest
from typing import cast

from pyjsg.parser_impl.jsg_pairdef_parser import JSGPairDef
from tests.test_basics.parser import parse

tests = [("x1 : INT", ['x1: INT = None'], ['self.x1 = x1'], "pairDef: x1 : valueType: LEXER_ID_REF: INT"),
         ("x2 : INT?", ['x2: Optional[INT] = None'], ['self.x2 = x2'], "pairDef: x2 : valueType: LEXER_ID_REF: INT?"),
         ("x3 : INT+", ['x3: List[INT] = None'], ["self.x3 = JSGArray('x3', _CONTEXT, INT, 1, None, x3)"],
          "pairDef: x3 : valueType: LEXER_ID_REF: INT+"),
         ("x4 : INT*", ['x4: List[INT] = None'], ["self.x4 = JSGArray('x4', _CONTEXT, INT, 0, None, x4)"],
          "pairDef: x4 : valueType: LEXER_ID_REF: INT*"),
         ("x5 : INT{1}", ['x5: INT = None'], ['self.x5 = x5'], "pairDef: x5 : valueType: LEXER_ID_REF: INT{1}"),
         ("x6 : INT{1, 1}", ['x6: INT = None'], ['self.x6 = x6'], "pairDef: x6 : valueType: LEXER_ID_REF: INT{1,1}"),
         ("x7 : INT{1,}", ['x7: List[INT] = None'], ["self.x7 = JSGArray('x7', _CONTEXT, INT, 1, None, x7)"],
          "pairDef: x7 : valueType: LEXER_ID_REF: INT{1,}")]

builtins = [("k : @string", ["k: str = None"], ['self.k = String(k)'],
             'pairDef: k : valueType: builtinValueType: String')]


class PairDefTestCase(unittest.TestCase):
    def test_simple_pairdef(self):
        for text, sig, init, s in tests:
            t = cast(JSGPairDef, parse(text, "pairDef", JSGPairDef))
            self.assertEqual(sig, t.signature())
            self.assertEqual(init, t.initializer())
            self.assertEqual(s, str(t))
            self.assertEqual(['INT'], t.dependency_list())
            
    def test_odd_identifiers(self):
        t = cast(JSGPairDef, parse("'regString' : INT", "pairDef", JSGPairDef))
        self.assertEqual(['regString: INT = None'], t.signature())
        self.assertEqual(['self.regString = regString'], t.initializer())
        self.assertEqual("pairDef: regString : valueType: LEXER_ID_REF: INT", str(t))
        t = cast(JSGPairDef, parse("'def' : INT", "pairDef", JSGPairDef))
        self.assertEqual(['def_: INT = None'], t.signature())
        self.assertEqual(['self.def = def_'], t.initializer())
        self.assertEqual("pairDef: def : valueType: LEXER_ID_REF: INT", str(t))
        t = cast(JSGPairDef, parse("'a var' : @number", "pairDef", JSGPairDef))
        self.assertEqual([], t.signature())
        self.assertEqual(["setattr(self, 'a var', Number(_kwargs.pop('a var', None)))"], t.initializer())
        self.assertEqual("pairDef: a var : valueType: builtinValueType: Number", str(t))

    def test_pairdef_shorthand(self):
        text = "(x1 'v 2' 'class') : @number {3,17}"
        t = cast(JSGPairDef, parse(text, "pairDef", JSGPairDef))
        self.assertEqual(['x1: List[float] = None', 'class_: List[float] = None'], t.signature())
        self.assertEqual(["self.x1 = JSGArray('x1', _CONTEXT, Number, 3, 17, x1)",
                          "setattr(self, 'v 2', JSGArray('v 2', _CONTEXT, Number, 3, 17, "
                          "_kwargs.pop('v 2', None)))",
                          "self.class = JSGArray('class', _CONTEXT, Number, 3, 17, class_)"], t.initializer())
        self.assertEqual("pairDef: (x1 | v 2 | class) : valueType: builtinValueType: Number{3,17}", str(t))
        self.assertEqual([], t.dependency_list())

        text = "(x1 'v 2' 'class') : @bool ?"
        t = cast(JSGPairDef, parse(text, "pairDef", JSGPairDef))
        self.assertEqual(['x1: Optional[bool] = None', 'class_: Optional[bool] = None'], t.signature())
        self.assertEqual(['self.x1 = Boolean(x1)', "setattr(self, 'v 2', Boolean(_kwargs.pop('v 2', None)))",
                          'self.class = Boolean(class_)'], t.initializer())
        self.assertEqual("pairDef: (x1 | v 2 | class) : valueType: builtinValueType: Boolean?", str(t))
        self.assertEqual([], t.dependency_list())

        text = "(x1 'v 2' 'class') : @null"
        t = cast(JSGPairDef, parse(text, "pairDef", JSGPairDef))
        self.assertEqual(['x1: JSGNull = None', 'class_: JSGNull = None'], t.signature())
        self.assertEqual(['self.x1 = JSGNull(x1)', "setattr(self, 'v 2', JSGNull(_kwargs.pop('v 2', None)))",
                          'self.class = JSGNull(class_)'], t.initializer())
        self.assertEqual("pairDef: (x1 | v 2 | class) : valueType: builtinValueType: JSGNull", str(t))
        self.assertEqual([], t.dependency_list())

    def test_pairdef_valuetype_ref(self):
        text = "nonobj = {a:@string b:@number?};  obj = {nonobj}"
        t = cast(JSGPairDef, parse(text, "grammarElt", JSGPairDef))
        self.assertEqual(['a: Optional[float] = None', 'b: Optional[float] = None'], t.signature())

    def test_pairdef_builtins(self):
        for text, sig, init, s in builtins:
            t = cast(JSGPairDef, parse(text, "pairDef", JSGPairDef))
            self.assertEqual(sig, t.signature())
            self.assertEqual(init, t.initializer())
            self.assertEqual(s, str(t))
            self.assertEqual([], t.dependency_list())


if __name__ == '__main__':
    unittest.main()

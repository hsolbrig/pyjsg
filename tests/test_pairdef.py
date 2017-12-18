# Copyright (c) 2017, Mayo Clinic
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without modification,
# are permitted provided that the following conditions are met:
#
# Redistributions of source code must retain the above copyright notice, this
#     list of conditions and the following disclaimer.
#
#     Redistributions in binary form must reproduce the above copyright notice,
#     this list of conditions and the following disclaimer in the documentation
#     and/or other materials provided with the distribution.
#
#     Neither the name of the Mayo Clinic nor the names of its contributors
#     may be used to endorse or promote products derived from this software
#     without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED.
# IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT,
# INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, 
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
# LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE
# OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED
# OF THE POSSIBILITY OF SUCH DAMAGE.

import unittest
from typing import cast

from pyjsg.parser_impl.jsg_pairdef_parser import JSGPairDef
from tests.parser import parse

tests = [("x1 : INT", ['x1: INT = None'], ['self.x1 = x1'], "pairDef: x1 : valueType: LEXER_ID_REF: INT"),
         ("x2 : INT?", ['x2: Optional[INT] = None'], ['self.x2 = x2'], "pairDef: x2 : valueType: LEXER_ID_REF: INT?"),
         ("x3 : INT+", ['x3: List[INT] = None'], ['self.x3 = x3'], "pairDef: x3 : valueType: LEXER_ID_REF: INT+"),
         ("x4 : INT*", ['x4: List[INT] = None'], ['self.x4 = x4'], "pairDef: x4 : valueType: LEXER_ID_REF: INT*"),
         ("x5 : INT{1}", ['x5: INT = None'], ['self.x5 = x5'], "pairDef: x5 : valueType: LEXER_ID_REF: INT{1}"),
         ("x6 : INT{1, 1}", ['x6: INT = None'], ['self.x6 = x6'], "pairDef: x6 : valueType: LEXER_ID_REF: INT{1,1}"),
         ("x7 : INT{1,}", ['x7: List[INT] = None'], ['self.x7 = x7'], "pairDef: x7 : valueType: LEXER_ID_REF: INT{1,}"),]

builtins = [("k : @string", ["k: str = None"], ['self.k = jsg.String(k)'], 'pairDef: k : valueType: builtinValueType: jsg.String')]


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
        self.assertEqual(["setattr(self, 'a var', jsg.Number(_kwargs.pop('a var', None)))"], t.initializer())
        self.assertEqual("pairDef: a var : valueType: builtinValueType: jsg.Number", str(t))

    def test_pairdef_shorthand(self):
        text = "(x1 'v 2' 'class') : @number {3,17}"
        t = cast(JSGPairDef, parse(text, "pairDef", JSGPairDef))
        self.assertEqual(['x1: List[float] = None', 'class_: List[float] = None'], t.signature())
        self.assertEqual(['self.x1 = jsg.Number(x1)', "setattr(self, 'v 2', jsg.Number(_kwargs.pop('v 2', None)))", 'self.class = jsg.Number(class_)'], t.initializer())
        self.assertEqual("pairDef: (x1 | v 2 | class) : valueType: builtinValueType: jsg.Number{3,17}", str(t))
        self.assertEqual([], t.dependency_list())

        text = "(x1 'v 2' 'class') : @bool ?"
        t = cast(JSGPairDef, parse(text, "pairDef", JSGPairDef))
        self.assertEqual(['x1: Optional[bool] = None', 'class_: Optional[bool] = None'], t.signature())
        self.assertEqual(['self.x1 = jsg.Boolean(x1)', "setattr(self, 'v 2', jsg.Boolean(_kwargs.pop('v 2', None)))", 'self.class = jsg.Boolean(class_)'], t.initializer())
        self.assertEqual("pairDef: (x1 | v 2 | class) : valueType: builtinValueType: jsg.Boolean?", str(t))
        self.assertEqual([], t.dependency_list())

        text = "(x1 'v 2' 'class') : @null"
        t = cast(JSGPairDef, parse(text, "pairDef", JSGPairDef))
        self.assertEqual(['x1: jsg.JSGNull = None', 'class_: jsg.JSGNull = None'], t.signature())
        self.assertEqual(['self.x1 = jsg.JSGNull(x1)', "setattr(self, 'v 2', jsg.JSGNull(_kwargs.pop('v 2', None)))", 'self.class = jsg.JSGNull(class_)'], t.initializer())
        self.assertEqual("pairDef: (x1 | v 2 | class) : valueType: builtinValueType: jsg.JSGNull", str(t))
        self.assertEqual([], t.dependency_list())

    def test_pairdef_valuetype_ref(self):
        text = "nonobj = {a:@string b:@number?};  obj = {nonobj}"
        t = cast(JSGPairDef, parse(text, "grammarElt", JSGPairDef))
        print(t.signature())

    def test_pairdef_builtins(self):
        for text, sig, init, s in builtins:
            t = cast(JSGPairDef, parse(text, "pairDef", JSGPairDef))
            self.assertEqual(sig, t.signature())
            self.assertEqual(init, t.initializer())
            self.assertEqual(s, str(t))
            self.assertEqual([], t.dependency_list())





if __name__ == '__main__':
    unittest.main()

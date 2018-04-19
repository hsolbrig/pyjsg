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

from pyjsg.parser_impl.jsg_objectexpr_parser import JSGObjectExpr
from pyjsg.parser_impl.jsg_valuetype_parser import JSGValueType
from tests.parser import parse

builtin_tests = [("@string", "jsg.String", "str"),
                 ("@number", "jsg.Number", "float"),
                 ("@int", "jsg.Integer", "int"),
                 ("@bool", "jsg.Boolean", "bool"),
                 ("@null", "jsg.JSGNull", "jsg.JSGNull"),
                 ("@array", "jsg.Array", "list"),
                 ("@object", "jsg.Object", "object")]

ref_tests = [("A", "ID"),
             ("a", "ID"),
             ("ABCt", "ID"),
             ("aNID", "ID"),
             ("AA", "LEXER_ID_REF"),
             ("HEX_NUM", "LEXER_ID_REF")]


class ValueTypeTestCase(unittest.TestCase):
    def test_builtins(self):
        for text, base, typ_ in builtin_tests:
            t = cast(JSGValueType, parse(text, "valueType", JSGValueType))
            self.assertEqual(typ_, t.typeid)
            self.assertEqual("valueType: builtinValueType: {}".format(t.basetype), str(t))
            self.assertEqual("{} = {}".format('k', base), t.as_python('k').strip())

    def test_refs(self):
        for text, typ in ref_tests:
            t = cast(JSGValueType, parse(text, "valueType", JSGValueType))
            self.assertEqual(text, t.typeid)
            self.assertEqual("valueType: {}: {}".format(typ, t.typeid), str(t))
            self.assertEqual("{} = {}".format('k', text), t.as_python('k').strip())

    def test_ref_escapes(self):
        self.assertEqual("Class", cast(JSGValueType, parse("Class", "valueType", JSGValueType)).typeid)
        t = cast(JSGValueType, parse("class", "valueType", JSGValueType))
        self.assertEqual("class_", t.typeid)
        self.assertEqual('k = class_', t.as_python('k').strip())

    def test_literals(self):
        t = cast(JSGValueType, parse("'literal'", "valueType", JSGValueType))
        self.assertEqual("_Anon1", t.typeid)
        self.assertEqual("valueType: STRING: pattern: r'literal'", str(t))

    def test_any(self):
        t = cast(JSGValueType, parse("id = .;", "valueTypeMacro", JSGValueType))
        self.assertEqual("object", t.typeid)
        self.assertEqual("valueType: builtinValueType: jsg.AnyType", str(t))

    def test_alternatives(self):
        t = cast(JSGValueType, parse("id = ('x'|'y') ;", "valueTypeMacro", JSGValueType))
        self.assertEqual("_Anon1", t.typeid)
        self.assertEqual("valueType: STRING: pattern: r'(x)|(y)'", str(t))
        t = cast(JSGValueType, parse("id = (Aa | Bb | (Cc | Dd)) ;", "valueTypeMacro", JSGValueType))
        self.assertEqual("Union[Aa, Bb, Union[Cc, Dd]]", t.typeid)
        self.assertEqual(t.dependency_list(), ['Aa', 'Bb', 'Cc','Dd'])
        self.assertEqual("valueType: (Aa | Bb | Union[Cc, Dd])", str(t))
        self.assertEqual("k = Union[Aa, Bb, Union[Cc, Dd]]", t.as_python('k').strip())
        t = cast(JSGValueType, parse("id = (Aa | Bb | 'foo' | (Cc | Dd) | 'bar') ;", "valueTypeMacro", JSGValueType))
        self.assertEqual("Union[_Anon1, Aa, Bb, Union[Cc, Dd]]", t.typeid)
        self.assertEqual(['_Anon1', 'Aa', 'Bb', 'Cc', 'Dd'], t.dependency_list())
        self.assertEqual("valueType: ((STRING: pattern: r'(foo)|(bar)') | Aa | Bb | Union[Cc, Dd])", str(t))
        self.assertEqual("k = Union[_Anon1, Aa, Bb, Union[Cc, Dd]]", t.as_python('k').strip())


    def test_objectmacro(self):
        t = cast(JSGObjectExpr, parse("stringFacet = (length minlength maxlength):INTEGER pattern:STRING flags:STRING? ;", "objectMacro", JSGObjectExpr))
        self.assertEqual("""class stringFacet(jsg.JSGObject):
    _reference_types = []
    _members = {'length': INTEGER,
                'minlength': INTEGER,
                'maxlength': INTEGER,
                'pattern': STRING,
                'flags': Optional[STRING]}
    _strict = True
    
    def __init__(self,
                 length: INTEGER = None,
                 minlength: INTEGER = None,
                 maxlength: INTEGER = None,
                 pattern: STRING = None,
                 flags: Optional[STRING] = None,
                 **_kwargs: Dict[str, object]):
        self._context = _CONTEXT
        self.length = length
        self.minlength = minlength
        self.maxlength = maxlength
        self.pattern = pattern
        self.flags = flags
        super().__init__(self._context, **_kwargs)""", t.as_python('stringFacet').strip())
        self.assertEqual(['INTEGER', 'STRING', 'STRING'], t.dependency_list())

        t = cast(JSGObjectExpr, parse("stringFacet = (length minlength maxlength):INTEGER pattern:STRING | flags:STRING? ;", "objectMacro", JSGObjectExpr))
        self.assertEqual("""class stringFacet(jsg.JSGObject):
    _reference_types = [_Anon1_1_, _Anon1_2_]
    _members = {'length': INTEGER,
                'minlength': INTEGER,
                'maxlength': INTEGER,
                'pattern': STRING,
                'flags': Optional[STRING]}
    _strict = True
    
    def __init__(self,
                 opt_: Union[_Anon1_1_, _Anon1_2_] = None,
                 **_kwargs: Dict[str, object]):
        self._context = _CONTEXT
        self.length = opt_.length if isinstance(opt_, _Anon1_1_) else None
        self.minlength = opt_.minlength if isinstance(opt_, _Anon1_1_) else None
        self.maxlength = opt_.maxlength if isinstance(opt_, _Anon1_1_) else None
        self.pattern = opt_.pattern if isinstance(opt_, _Anon1_1_) else None
        self.flags = opt_.flags if opt_ else None if isinstance(opt_, _Anon1_2_) else None
        super().__init__(self._context, **_kwargs)""", t.as_python('stringFacet').strip())
        self.assertEqual({'_Anon1_1_', '_Anon1_2_', 'STRING', 'INTEGER'}, t.dependencies())

        t = cast(JSGObjectExpr, parse("x = a:@number | b:@null | ;", "objectMacro", JSGObjectExpr))
        self.assertEqual("""class stringFacet(jsg.JSGObject):
    _reference_types = [_Anon1_1_, _Anon1_2_, _Anon1_3_]
    _members = {'a': float,
                'b': jsg.JSGNull}
    _strict = True
    
    def __init__(self,
                 opt_: Union[_Anon1_1_, _Anon1_2_, _Anon1_3_] = None,
                 **_kwargs: Dict[str, object]):
        self._context = _CONTEXT
        self.a = jsg.Number(opt_.a) if isinstance(opt_, _Anon1_1_) else jsg.Number(None)
        self.b = jsg.JSGNull(opt_.b) if isinstance(opt_, _Anon1_2_) else jsg.JSGNull(None)
        super().__init__(self._context, **_kwargs)""", t.as_python('stringFacet').strip())
        self.assertEqual({'_Anon1_1_', '_Anon1_2_', '_Anon1_3_'}, t.dependencies())


if __name__ == '__main__':
    unittest.main()

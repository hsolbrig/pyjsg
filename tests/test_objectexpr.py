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
from tests.parser import parse

t1 = "id {a:INT} "
r1 = """class k(jsg.JSGObject):
    _reference_types = []
    _members = {'a': INT}
    _strict = True
    
    def __init__(self,
                 a: INT = None,
                 **_kwargs: Dict[str, object]):
        self._context = _CONTEXT
        self.a = a
        super().__init__(self._context, **_kwargs)"""
t2 = "labeledNodeConstraint   { first:INTEGER? numericFacet* last:STRING+}"
r2 = """class k(jsg.JSGObject):
    _reference_types = [numericFacet]
    _members = {'first': Optional[INTEGER],
                'numericFacet': List[numericFacet],
                'last': List[STRING]}
    _strict = True
    
    def __init__(self,
                 first: Optional[INTEGER] = None,
                 numericFacet: List[numericFacet] = None,
                 last: List[STRING] = None,
                 **_kwargs: Dict[str, object]):
        self._context = _CONTEXT
        self.first = first
        self.numericFacet = numericFacet
        self.last = last
        super().__init__(self._context, **_kwargs)"""

t3 = "openShape {a: @int b:@string, | c: @int | d: @string,}"
r3 = """class k(jsg.JSGObject):
    _reference_types = [_Anon1_1_, _Anon1_2_, _Anon1_3_]
    _members = {'a': int,
                'b': str,
                'c': int,
                'd': str}
    _strict = True
    
    def __init__(self,
                 opt_: Union[_Anon1_1_, _Anon1_2_, _Anon1_3_] = None,
                 **_kwargs: Dict[str, object]):
        self._context = _CONTEXT
        self.a = jsg.Integer(opt_.a) if isinstance(opt_, _Anon1_1_) else jsg.Integer(None)
        self.b = jsg.String(opt_.b) if isinstance(opt_, _Anon1_1_) else jsg.String(None)
        self.c = jsg.Integer(opt_.c) if isinstance(opt_, _Anon1_2_) else jsg.Integer(None)
        self.d = jsg.String(opt_.d) if isinstance(opt_, _Anon1_3_) else jsg.String(None)
        super().__init__(self._context, **_kwargs)"""

tests = [(t1, r1), (t2, r2), (t3, r3)]

anon_nonvar = """Schema           {
  "@context":"http://www.w3.org/ns/shex.jsonld",}"""
anon_nonvar_r = """class Schema(jsg.JSGObject):
    _reference_types = []
    _members = {'@context': _Anon1}
    _strict = False
    
    def __init__(self,
                 **_kwargs: Dict[str, object]):
        self._context = _CONTEXT
        setattr(self, '@context', _kwargs.pop('@context', None))
        super().__init__(self._context, **_kwargs)"""


class ObjectExprTestCase(unittest.TestCase):
    def test_simple(self):
        for test, result in tests:
            self.maxDiff = None
            r = cast(JSGObjectExpr, parse(test, "objectDef", JSGObjectExpr))
            self.assertEqual(result, r.as_python('k').strip())

    def test_anon_nonvar(self):
        r = cast(JSGObjectExpr, parse(anon_nonvar, "objectDef", JSGObjectExpr))
        self.maxDiff = None
        self.assertEqual(anon_nonvar_r, r.as_python("Schema").strip())


if __name__ == '__main__':
    unittest.main()
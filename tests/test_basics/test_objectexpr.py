import unittest

from typing import cast

from pyjsg.parser_impl.jsg_objectexpr_parser import JSGObjectExpr
from tests.test_basics.parser import parse

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
        self.last = jsg_array.JSGArray(_CONTEXT, STRING, 1, None, last)
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

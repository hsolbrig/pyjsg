# Auto generated from jsg/OneOf.jsg by PyJSG version 1.0.0
# Generation date: 2017-05-15 11:10
#
from typing import Optional, Dict, List, Union, _ForwardRef

from pyjsg.jsglib.jsg import *
from pyjsg.jsglib.typing_patch import fix_forwards

# .TYPE and .IGNORE settings
_CONTEXT = JSGContext()
OneOft_ = _ForwardRef('OneOf')
tripleExprt_ = _ForwardRef('tripleExpr')


class _Anon1(JSGString):
    pattern = JSGPattern(r'unbounded')


class IRI(String):
    pattern = JSGPattern(r'')


class BNODE(String):
    pattern = JSGPattern(r'')


class INTEGER(String):
    pattern = JSGPattern(r'')

class EachOf(JSGObject):
    _reference_types = []
    
    def __init__(self,
                 **_kwargs: Dict[str, object]):
        self._context = _CONTEXT
        super().__init__(self._context, **_kwargs)


class TripleConstraint(JSGObject):
    _reference_types = []
    
    def __init__(self,
                 **_kwargs: Dict[str, object]):
        self._context = _CONTEXT
        super().__init__(self._context, **_kwargs)


tripleExprLabel = Union[IRI, BNODE]

tripleExpr = Union[EachOf, OneOft_, tripleExprLabel]

class OneOf(JSGObject):
    _reference_types = []
    
    def __init__(self,
                 id: Optional[tripleExprLabel] = None,
                 expressions: List[tripleExprt_] = None,
                 min: Optional[INTEGER] = None,
                 max: Optional[Union[_Anon1, INTEGER]] = None,
                 **_kwargs: Dict[str, object]):
        self._context = _CONTEXT
        self.id = id
        self.expressions = expressions
        self.min = min
        self.max = max
        super().__init__(self._context, **_kwargs)


fix_forwards(locals())

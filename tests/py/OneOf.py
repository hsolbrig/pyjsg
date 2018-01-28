# Auto generated from jsg/OneOf.jsg by PyJSG version 0.5.2
# Generation date: 2018-01-28 17:28
#
from typing import Optional, Dict, List, Union, _ForwardRef

from pyjsg.jsglib import jsg
from pyjsg.jsglib.jsg import isinstance_

# .TYPE and .IGNORE settings
_CONTEXT = jsg.JSGContext()
_CONTEXT.TYPE_EXCEPTIONS.append("EachOf")
_CONTEXT.TYPE_EXCEPTIONS.append("TripleConstraint")
_CONTEXT.TYPE_EXCEPTIONS.append("OneOf")




class _Anon1(jsg.JSGString):
    pattern = jsg.JSGPattern(r'unbounded')


class IRI(jsg.String):
    pattern = jsg.JSGPattern(r'')


class BNODE(jsg.String):
    pattern = jsg.JSGPattern(r'')


class INTEGER(jsg.String):
    pattern = jsg.JSGPattern(r'')

class EachOf(jsg.JSGObject):
    _reference_types = []
    _members = {}
    _strict = True
    
    def __init__(self,
                 **_kwargs: Dict[str, object]):
        self._context = _CONTEXT
        super().__init__(self._context, **_kwargs)


class TripleConstraint(jsg.JSGObject):
    _reference_types = []
    _members = {}
    _strict = True
    
    def __init__(self,
                 **_kwargs: Dict[str, object]):
        self._context = _CONTEXT
        super().__init__(self._context, **_kwargs)


tripleExprLabel = Union[IRI, BNODE]

tripleExpr = Union[EachOf, "OneOf", tripleExprLabel]

class OneOf(jsg.JSGObject):
    _reference_types = []
    _members = {'id': Optional[tripleExprLabel],
                'expressions': List["tripleExpr"],
                'min': Optional[INTEGER],
                'max': Optional[Union[_Anon1, INTEGER]]}
    _strict = True
    
    def __init__(self,
                 id: Optional[tripleExprLabel] = None,
                 expressions: List["tripleExpr"] = None,
                 min: Optional[INTEGER] = None,
                 max: Optional[Union[_Anon1, INTEGER]] = None,
                 **_kwargs: Dict[str, object]):
        self._context = _CONTEXT
        self.id = id
        self.expressions = expressions
        self.min = min
        self.max = max
        super().__init__(self._context, **_kwargs)


_CONTEXT.NAMESPACE = locals()

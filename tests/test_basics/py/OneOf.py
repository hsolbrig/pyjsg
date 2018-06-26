# Auto generated from tests/test_basics/jsg/OneOf.jsg by PyJSG version 0.6.0
# Generation date: 2018-06-26 12:40
#
import sys
from typing import Optional, Dict, List, Union
if sys.version_info < (3, 7):
    from typing import _ForwardRef as ForwardRef
    from pyjsg.jsglib import typing_patch_36
else:
    from typing import ForwardRef
    from pyjsg.jsglib import typing_patch_37

from pyjsg.jsglib import jsg, jsg_array
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

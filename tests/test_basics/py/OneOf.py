# Auto generated from tests/test_basics/jsg/OneOf.jsg by PyJSG version 0.7.0
# Generation date: 2018-07-18 09:39
#
import sys
from typing import Optional, Dict, List, Union, Any
from jsonasobj import JsonObj

if sys.version_info < (3, 7):
    from typing import _ForwardRef as ForwardRef
    from pyjsg.jsglib import typing_patch_36
else:
    from typing import ForwardRef
    from pyjsg.jsglib import typing_patch_37

from pyjsg.jsglib import *

# .TYPE and .IGNORE settings
_CONTEXT = JSGContext()
_CONTEXT.TYPE_EXCEPTIONS.append("EachOf")
_CONTEXT.TYPE_EXCEPTIONS.append("TripleConstraint")
_CONTEXT.TYPE_EXCEPTIONS.append("OneOf")


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
    _members = {}
    _strict = True

    def __init__(self,
                 **_kwargs: Dict[str, object]):
        super().__init__(_CONTEXT, **_kwargs)


class TripleConstraint(JSGObject):
    _reference_types = []
    _members = {}
    _strict = True

    def __init__(self,
                 **_kwargs: Dict[str, object]):
        super().__init__(_CONTEXT, **_kwargs)



tripleExprLabel = Union[IRI, BNODE]

tripleExpr = Union[EachOf, "OneOf", Union[IRI, BNODE]]
class OneOf(JSGObject):
    _reference_types = []
    _members = {'id': Optional[Union[IRI, BNODE]],
                'expressions': ArrayFactory('expressions', _CONTEXT, Union[EachOf, "OneOf", Union[IRI, BNODE]], 2, None),
                'min': Optional[INTEGER],
                'max': Optional[Union[_Anon1, INTEGER]]}
    _strict = True

    def __init__(self,
                 id: Optional[Union[str, str]] = None,
                 expressions: List[Union[EachOf, "OneOf", Union[str, str]]] = None,
                 min: Optional[str] = None,
                 max: Optional[Union[str, str]] = None,
                 **_kwargs: Dict[str, object]):
        super().__init__(_CONTEXT, **_kwargs)
        self.id = id
        self.expressions = expressions
        self.min = min
        self.max = max


_CONTEXT.NAMESPACE = locals()

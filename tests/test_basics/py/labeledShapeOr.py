# Auto generated from tests/test_basics/jsg/labeledShapeOr.jsg by PyJSG version 0.7.0
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
_CONTEXT.TYPE_EXCEPTIONS.append("shapeExprLabel")
_CONTEXT.TYPE_EXCEPTIONS.append("labeledShapeOr")


class _Anon1(JSGString):
    pattern = JSGPattern(r'ShapeOr')


class SHAPEEXPR(JSGString):
    pattern = JSGPattern(r'[a-z]')


class shapeExprLabel(JSGObject):
    _reference_types = []
    _members = {}
    _strict = True

    def __init__(self,
                 **_kwargs: Dict[str, object]):
        super().__init__(_CONTEXT, **_kwargs)


class labeledShapeOr(JSGObject):
    _reference_types = []
    _members = {'type': _Anon1,
                'id': shapeExprLabel,
                'shapeExprs': ArrayFactory('shapeExprs', _CONTEXT, SHAPEEXPR, 2, None)}
    _strict = True

    def __init__(self,
                 type: str = None,
                 id: shapeExprLabel = None,
                 shapeExprs: List[str] = None,
                 **_kwargs: Dict[str, object]):
        super().__init__(_CONTEXT, **_kwargs)
        self.type = type
        self.id = id
        self.shapeExprs = shapeExprs


_CONTEXT.NAMESPACE = locals()

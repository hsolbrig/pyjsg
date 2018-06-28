# Auto generated from test_basics/jsg/labeledShapeOr.jsg by PyJSG version 0.7.0
# Generation date: 2018-06-28 11:40
#
import sys
from typing import Optional, Dict, List, Union
if sys.version_info < (3, 7):
    from typing import _ForwardRef as ForwardRef
    from pyjsg.jsglib import typing_patch_36
else:
    from typing import ForwardRef
    from pyjsg.jsglib import typing_patch_37

from pyjsg.jsglib import *
from pyjsg.jsglib.jsg import isinstance_

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
        self._context = _CONTEXT
        super().__init__(self._context, **_kwargs)


class labeledShapeOr(JSGObject):
    _reference_types = []
    _members = {'type': _Anon1,
                'id': shapeExprLabel,
                'shapeExprs': List[SHAPEEXPR]}
    _strict = True
    
    def __init__(self,
                 type: _Anon1 = None,
                 id: shapeExprLabel = None,
                 shapeExprs: List[SHAPEEXPR] = None,
                 **_kwargs: Dict[str, object]):
        self._context = _CONTEXT
        self.type = type
        self.id = id
        self.shapeExprs = shapeExprs
        super().__init__(self._context, **_kwargs)


_CONTEXT.NAMESPACE = locals()

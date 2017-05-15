# Auto generated from jsg/labeledShapeOr.jsg by PyJSG version 1.0.0
# Generation date: 2017-05-15 11:10
#
from typing import Optional, Dict, List, Union, _ForwardRef

from pyjsg.jsglib.jsg import *
from pyjsg.jsglib.typing_patch import fix_forwards

# .TYPE and .IGNORE settings
_CONTEXT = JSGContext()


class _Anon1(JSGString):
    pattern = JSGPattern(r'ShapeOr')


class SHAPEEXPR(JSGString):
    pattern = JSGPattern(r'[a-z]')

class shapeExprLabel(JSGObject):
    _reference_types = []
    
    def __init__(self,
                 **_kwargs: Dict[str, object]):
        self._context = _CONTEXT
        super().__init__(self._context, **_kwargs)


class labeledShapeOr(JSGObject):
    _reference_types = []
    
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


fix_forwards(locals())

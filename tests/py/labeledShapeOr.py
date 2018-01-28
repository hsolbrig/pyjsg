# Auto generated from jsg/labeledShapeOr.jsg by PyJSG version 0.5.2
# Generation date: 2018-01-28 17:28
#
from typing import Optional, Dict, List, Union, _ForwardRef

from pyjsg.jsglib import jsg
from pyjsg.jsglib.jsg import isinstance_

# .TYPE and .IGNORE settings
_CONTEXT = jsg.JSGContext()
_CONTEXT.TYPE_EXCEPTIONS.append("shapeExprLabel")
_CONTEXT.TYPE_EXCEPTIONS.append("labeledShapeOr")




class _Anon1(jsg.JSGString):
    pattern = jsg.JSGPattern(r'ShapeOr')


class SHAPEEXPR(jsg.JSGString):
    pattern = jsg.JSGPattern(r'[a-z]')

class shapeExprLabel(jsg.JSGObject):
    _reference_types = []
    _members = {}
    _strict = True
    
    def __init__(self,
                 **_kwargs: Dict[str, object]):
        self._context = _CONTEXT
        super().__init__(self._context, **_kwargs)


class labeledShapeOr(jsg.JSGObject):
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

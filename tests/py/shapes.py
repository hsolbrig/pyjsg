# Auto generated from jsg/shapes.jsg by PyJSG version 1.0.0
# Generation date: 2017-05-15 11:10
#
from typing import Optional, Dict, List, Union, _ForwardRef

from pyjsg.jsglib.jsg import *
from pyjsg.jsglib.typing_patch import fix_forwards

# .TYPE and .IGNORE settings
_CONTEXT = JSGContext()
ShapeAndt_ = _ForwardRef('ShapeAnd')
ShapeNott_ = _ForwardRef('ShapeNot')
ShapeOrt_ = _ForwardRef('ShapeOr')
shapeExprt_ = _ForwardRef('shapeExpr')


class _Anon1(JSGString):
    pattern = JSGPattern(r'ShapeNot')

class ShapeExternal(JSGObject):
    _reference_types = []
    
    def __init__(self,
                 **_kwargs: Dict[str, object]):
        self._context = _CONTEXT
        super().__init__(self._context, **_kwargs)


class NodeConstraint(JSGObject):
    _reference_types = []
    
    def __init__(self,
                 **_kwargs: Dict[str, object]):
        self._context = _CONTEXT
        super().__init__(self._context, **_kwargs)


class Shape(JSGObject):
    _reference_types = []
    
    def __init__(self,
                 **_kwargs: Dict[str, object]):
        self._context = _CONTEXT
        super().__init__(self._context, **_kwargs)


shapeExprLabel = String

class labeledShapeNot(JSGObject):
    _reference_types = []
    
    def __init__(self,
                 type: _Anon1 = None,
                 id: shapeExprLabel = None,
                 shapeExpr: shapeExprt_ = None,
                 **_kwargs: Dict[str, object]):
        self._context = _CONTEXT
        self.type = type
        self.id = id
        self.shapeExpr = shapeExpr
        super().__init__(self._context, **_kwargs)


shapeExpr = Union[ShapeOrt_, ShapeAndt_, ShapeNott_, NodeConstraint, Shape, shapeExprLabel, ShapeExternal]

class ShapeOr(JSGObject):
    _reference_types = []
    
    def __init__(self,
                 shapeExprs: List[shapeExprt_] = None,
                 **_kwargs: Dict[str, object]):
        self._context = _CONTEXT
        self.shapeExprs = shapeExprs
        super().__init__(self._context, **_kwargs)


class ShapeAnd(JSGObject):
    _reference_types = []
    
    def __init__(self,
                 shapeExprs: List[shapeExprt_] = None,
                 **_kwargs: Dict[str, object]):
        self._context = _CONTEXT
        self.shapeExprs = shapeExprs
        super().__init__(self._context, **_kwargs)


class ShapeNot(JSGObject):
    _reference_types = []
    
    def __init__(self,
                 shapeExpr: shapeExprt_ = None,
                 **_kwargs: Dict[str, object]):
        self._context = _CONTEXT
        self.shapeExpr = shapeExpr
        super().__init__(self._context, **_kwargs)


labeledShapeExpr = Union[labeledShapeNot, shapeExprLabel]

fix_forwards(locals())

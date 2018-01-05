# Auto generated from jsg/shapes.jsg by PyJSG version 0.4.1
# Generation date: 2018-01-05 13:51
#
from typing import Optional, Dict, List, Union, _ForwardRef

from pyjsg.jsglib import jsg
from pyjsg.jsglib.jsg import isinstance_

# .TYPE and .IGNORE settings
_CONTEXT = jsg.JSGContext()
_CONTEXT.TYPE_EXCEPTIONS.append("ShapeExternal")
_CONTEXT.TYPE_EXCEPTIONS.append("NodeConstraint")
_CONTEXT.TYPE_EXCEPTIONS.append("Shape")
_CONTEXT.TYPE_EXCEPTIONS.append("labeledShapeNot")
_CONTEXT.TYPE_EXCEPTIONS.append("ShapeOr")
_CONTEXT.TYPE_EXCEPTIONS.append("ShapeAnd")
_CONTEXT.TYPE_EXCEPTIONS.append("ShapeNot")




class _Anon1(jsg.JSGString):
    pattern = jsg.JSGPattern(r'ShapeNot')

class ShapeExternal(jsg.JSGObject):
    _reference_types = []
    _members = {}
    _strict = True
    
    def __init__(self,
                 **_kwargs: Dict[str, object]):
        self._context = _CONTEXT
        super().__init__(self._context, **_kwargs)


class NodeConstraint(jsg.JSGObject):
    _reference_types = []
    _members = {}
    _strict = True
    
    def __init__(self,
                 **_kwargs: Dict[str, object]):
        self._context = _CONTEXT
        super().__init__(self._context, **_kwargs)


class Shape(jsg.JSGObject):
    _reference_types = []
    _members = {}
    _strict = True
    
    def __init__(self,
                 **_kwargs: Dict[str, object]):
        self._context = _CONTEXT
        super().__init__(self._context, **_kwargs)


shapeExprLabel = jsg.String

class labeledShapeNot(jsg.JSGObject):
    _reference_types = []
    _members = {'type': _Anon1,
                'id': shapeExprLabel,
                'shapeExpr': "shapeExpr"}
    _strict = True
    
    def __init__(self,
                 type: _Anon1 = None,
                 id: shapeExprLabel = None,
                 shapeExpr: "shapeExpr" = None,
                 **_kwargs: Dict[str, object]):
        self._context = _CONTEXT
        self.type = type
        self.id = id
        self.shapeExpr = shapeExpr
        super().__init__(self._context, **_kwargs)


shapeExpr = Union["ShapeOr", "ShapeAnd", "ShapeNot", NodeConstraint, Shape, shapeExprLabel, ShapeExternal]

class ShapeOr(jsg.JSGObject):
    _reference_types = []
    _members = {'shapeExprs': List["shapeExpr"]}
    _strict = True
    
    def __init__(self,
                 shapeExprs: List["shapeExpr"] = None,
                 **_kwargs: Dict[str, object]):
        self._context = _CONTEXT
        self.shapeExprs = shapeExprs
        super().__init__(self._context, **_kwargs)


class ShapeAnd(jsg.JSGObject):
    _reference_types = []
    _members = {'shapeExprs': List["shapeExpr"]}
    _strict = True
    
    def __init__(self,
                 shapeExprs: List["shapeExpr"] = None,
                 **_kwargs: Dict[str, object]):
        self._context = _CONTEXT
        self.shapeExprs = shapeExprs
        super().__init__(self._context, **_kwargs)


class ShapeNot(jsg.JSGObject):
    _reference_types = []
    _members = {'shapeExpr': "shapeExpr"}
    _strict = True
    
    def __init__(self,
                 shapeExpr: "shapeExpr" = None,
                 **_kwargs: Dict[str, object]):
        self._context = _CONTEXT
        self.shapeExpr = shapeExpr
        super().__init__(self._context, **_kwargs)


labeledShapeExpr = Union[labeledShapeNot, shapeExprLabel]

_CONTEXT.NAMESPACE = locals()

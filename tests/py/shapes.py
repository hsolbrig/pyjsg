# Auto generated from jsg/shapes.jsg by PyJSG version 0.1.0-DEV
# Generation date: 2017-03-22 18:52
#
from typing import Optional, Dict, List, Union, _ForwardRef

from jsglib.jsg import JSGString, JSGPattern, JSGObject, JSGContext
from jsglib.typing_patch import fix_forwards

# .TYPE and .IGNORE settings
_CONTEXT = JSGContext()




ShapeAndt_ = _ForwardRef('ShapeAnd')
ShapeNott_ = _ForwardRef('ShapeNot')
ShapeOrt_ = _ForwardRef('ShapeOr')


class shapeExprLabel(JSGString):
    pattern = JSGPattern(r'[a-z]+')

class ShapeExternal(JSGObject):
    def __init__(self,
                 **_extra: Dict[str, object]):
        JSGObject.__init__(self, _CONTEXT, **_extra)
        


class NodeConstraint(JSGObject):
    def __init__(self,
                 **_extra: Dict[str, object]):
        JSGObject.__init__(self, _CONTEXT, **_extra)
        


class Shape(JSGObject):
    def __init__(self,
                 **_extra: Dict[str, object]):
        JSGObject.__init__(self, _CONTEXT, **_extra)
        


class labeledShapeNot(JSGObject):
    def __init__(self,
                 type: str = None,
                 id: shapeExprLabel = None,
                 shapeExpr: Union[ShapeOrt_, ShapeAndt_, ShapeNott_, NodeConstraint, Shape, shapeExprLabel, ShapeExternal] = None,
                 **_extra: Dict[str, object]):
        JSGObject.__init__(self, _CONTEXT, **_extra)
        self.type = "ShapeNot"
        self.id = id
        self.shapeExpr = shapeExpr


class ShapeOr(JSGObject):
    def __init__(self,
                 shapeExprs: List[Union[ShapeOrt_, ShapeAndt_, ShapeNott_, NodeConstraint, Shape, shapeExprLabel, ShapeExternal]] = None,
                 **_extra: Dict[str, object]):
        JSGObject.__init__(self, _CONTEXT, **_extra)
        self.shapeExprs = shapeExprs


class ShapeAnd(JSGObject):
    def __init__(self,
                 shapeExprs: List[Union[ShapeOrt_, ShapeAndt_, ShapeNott_, NodeConstraint, Shape, shapeExprLabel, ShapeExternal]] = None,
                 **_extra: Dict[str, object]):
        JSGObject.__init__(self, _CONTEXT, **_extra)
        self.shapeExprs = shapeExprs


class ShapeNot(JSGObject):
    def __init__(self,
                 shapeExpr: Union[ShapeOrt_, ShapeAndt_, ShapeNott_, NodeConstraint, Shape, shapeExprLabel, ShapeExternal] = None,
                 **_extra: Dict[str, object]):
        JSGObject.__init__(self, _CONTEXT, **_extra)
        self.shapeExpr = shapeExpr


fix_forwards(globals())

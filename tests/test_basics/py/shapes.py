# Auto generated from tests/test_basics/jsg/shapes.jsg by PyJSG version 0.7.0
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
_CONTEXT.TYPE_EXCEPTIONS.append("ShapeExternal")
_CONTEXT.TYPE_EXCEPTIONS.append("NodeConstraint")
_CONTEXT.TYPE_EXCEPTIONS.append("Shape")
_CONTEXT.TYPE_EXCEPTIONS.append("labeledShapeNot")
_CONTEXT.TYPE_EXCEPTIONS.append("ShapeOr")
_CONTEXT.TYPE_EXCEPTIONS.append("ShapeAnd")
_CONTEXT.TYPE_EXCEPTIONS.append("ShapeNot")


class _Anon1(JSGString):
    pattern = JSGPattern(r'ShapeNot')


class ShapeExternal(JSGObject):
    _reference_types = []
    _members = {}
    _strict = True

    def __init__(self,
                 **_kwargs: Dict[str, object]):
        super().__init__(_CONTEXT, **_kwargs)


class NodeConstraint(JSGObject):
    _reference_types = []
    _members = {}
    _strict = True

    def __init__(self,
                 **_kwargs: Dict[str, object]):
        super().__init__(_CONTEXT, **_kwargs)


class Shape(JSGObject):
    _reference_types = []
    _members = {}
    _strict = True

    def __init__(self,
                 **_kwargs: Dict[str, object]):
        super().__init__(_CONTEXT, **_kwargs)



shapeExprLabel = String
class labeledShapeNot(JSGObject):
    _reference_types = []
    _members = {'type': _Anon1,
                'id': String,
                'shapeExpr': Union["ShapeOr", "ShapeAnd", "ShapeNot", NodeConstraint, Shape, String, ShapeExternal]}
    _strict = True

    def __init__(self,
                 type: str = None,
                 id: str = None,
                 shapeExpr: Union["ShapeOr", "ShapeAnd", "ShapeNot", NodeConstraint, Shape, str, ShapeExternal] = None,
                 **_kwargs: Dict[str, object]):
        super().__init__(_CONTEXT, **_kwargs)
        self.type = type
        self.id = id
        self.shapeExpr = shapeExpr



labeledShapeExpr = Union[labeledShapeNot, String]

shapeExpr = Union["ShapeOr", "ShapeAnd", "ShapeNot", NodeConstraint, Shape, String, ShapeExternal]
class ShapeOr(JSGObject):
    _reference_types = []
    _members = {'shapeExprs': ArrayFactory('shapeExprs', _CONTEXT, Union["ShapeOr", "ShapeAnd", "ShapeNot", NodeConstraint, Shape, String, ShapeExternal], 2, None)}
    _strict = True

    def __init__(self,
                 shapeExprs: List[Union["ShapeOr", "ShapeAnd", "ShapeNot", NodeConstraint, Shape, str, ShapeExternal]] = None,
                 **_kwargs: Dict[str, object]):
        super().__init__(_CONTEXT, **_kwargs)
        self.shapeExprs = shapeExprs


class ShapeAnd(JSGObject):
    _reference_types = []
    _members = {'shapeExprs': ArrayFactory('shapeExprs', _CONTEXT, Union[ShapeOr, "ShapeAnd", "ShapeNot", NodeConstraint, Shape, String, ShapeExternal], 2, None)}
    _strict = True

    def __init__(self,
                 shapeExprs: List[Union[ShapeOr, "ShapeAnd", "ShapeNot", NodeConstraint, Shape, str, ShapeExternal]] = None,
                 **_kwargs: Dict[str, object]):
        super().__init__(_CONTEXT, **_kwargs)
        self.shapeExprs = shapeExprs


class ShapeNot(JSGObject):
    _reference_types = []
    _members = {'shapeExpr': Union[ShapeOr, ShapeAnd, "ShapeNot", NodeConstraint, Shape, String, ShapeExternal]}
    _strict = True

    def __init__(self,
                 shapeExpr: Union[ShapeOr, ShapeAnd, "ShapeNot", NodeConstraint, Shape, str, ShapeExternal] = None,
                 **_kwargs: Dict[str, object]):
        super().__init__(_CONTEXT, **_kwargs)
        self.shapeExpr = shapeExpr


_CONTEXT.NAMESPACE = locals()

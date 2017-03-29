# Auto generated from jsg/schema.jsg by PyJSG version 0.1.0-DEV
# Generation date: 2017-03-19 12:05
#
from typing import Optional, Dict, Union

from jsglib import JSGObject, JSGContext
from jsglib import fix_forwards

# .TYPE and .IGNORE settings
_CONTEXT = JSGContext()





class Schema(JSGObject):
    def __init__(self,
                 startActs: Optional[SemAct],
                 start: Optional[Union[ShapeOr, ShapeAnd, ShapeNot, NodeConstraint, Shape, shapeExprLabel, ShapeExternal, labeledShapeOr, labeledShapeAnd, labeledShapeNot, labeledNodeConstraint, labeledShape, shapeExprLabel, labeledShapeExternal]],
                 shapes: Optional[Union[labeledShapeOr, labeledShapeAnd, labeledShapeNot, labeledNodeConstraint, labeledShape, shapeExprLabel, labeledShapeExternal]],
                 **_: Dict[str, object]):
        JSGObject.__init__(self)
        setattr(self, '@context', "https://shexspec.github.io/context.jsonld")
        startActs = startActs
        start = start
        shapes = shapes


fix_forwards(globals())

# Auto generated from jsg/labeledShapeOr.jsg by PyJSG version 0.1.1
# Generation date: 2017-03-29 13:55
#
from typing import Optional, Dict, List, Union, _ForwardRef

from pyjsg.jsglib.jsg import JSGString, JSGPattern, JSGObject, JSGContext
from pyjsg.jsglib.typing_patch import fix_forwards

# .TYPE and .IGNORE settings
_CONTEXT = JSGContext()






class shapeExpr(JSGString):
    pattern = JSGPattern(r'[a-z]')

class shapeExprLabel(JSGObject):
    def __init__(self,
                 **_extra: Dict[str, object]):
        JSGObject.__init__(self, _CONTEXT, **_extra)
        


class labeledShapeOr(JSGObject):
    def __init__(self,
                 type: str = None,
                 id: shapeExprLabel = None,
                 shapeExprs: List[shapeExpr] = None,
                 **_extra: Dict[str, object]):
        JSGObject.__init__(self, _CONTEXT, **_extra)
        self.type = "ShapeOr"
        self.id = id
        self.shapeExprs = shapeExprs


fix_forwards(globals())

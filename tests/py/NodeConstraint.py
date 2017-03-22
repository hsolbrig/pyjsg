# Auto generated from jsg/NodeConstraint.jsg by PyJSG version 0.1.0-DEV
# Generation date: 2017-03-22 13:51
#
from typing import Optional, Dict, List, Union, _ForwardRef

from jsglib.jsg import JSGString, JSGPattern, JSGObject, JSGContext
from jsglib.typing_patch import fix_forwards

# .TYPE and .IGNORE settings
_CONTEXT = JSGContext()






class _A1(JSGString):
    pattern = JSGPattern(r'iri|bnode|nonliteral|literal')


class IRI(JSGString):
    pattern = JSGPattern(r'[0-9]')

class NodeConstraint(JSGObject):
    def __init__(self,
                 nodeKind: Optional[_A1] = None,
                 datatype: Optional[IRI] = None,
                 **_: Dict[str, object]):
        JSGObject.__init__(self, _CONTEXT)
        self.nodeKind = nodeKind
        self.datatype = datatype


fix_forwards(globals())

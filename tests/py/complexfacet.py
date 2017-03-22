# Auto generated from jsg/complexfacet.jsg by PyJSG version 0.1.0-DEV
# Generation date: 2017-03-22 13:51
#
from typing import Optional, Dict, List, Union, _ForwardRef

from jsglib.jsg import JSGString, JSGPattern, JSGObject, JSGContext
from jsglib.typing_patch import fix_forwards

# .TYPE and .IGNORE settings
_CONTEXT = JSGContext()






class INTEGER(JSGString):
    pattern = JSGPattern(r'[0-9]*')


class DECIMAL(JSGString):
    pattern = JSGPattern(r'[0-9]*')


class DOUBLE(JSGString):
    pattern = JSGPattern(r'[0-9]*')


class STRING(JSGString):
    pattern = JSGPattern(r'[a-z]*')

class labeledNodeConstraint(JSGObject):
    def __init__(self,
                 first: Optional[INTEGER] = None,
                 mininclusive: Optional[Union[INTEGER, DECIMAL, DOUBLE]] = None,
                 minexclusive: Optional[Union[INTEGER, DECIMAL, DOUBLE]] = None,
                 maxinclusive: Optional[Union[INTEGER, DECIMAL, DOUBLE]] = None,
                 maxexclusive: Optional[Union[INTEGER, DECIMAL, DOUBLE]] = None,
                 last: List[STRING] = None,
                 **_: Dict[str, object]):
        JSGObject.__init__(self, _CONTEXT)
        self.first = first
        self.mininclusive = mininclusive
        self.minexclusive = minexclusive
        self.maxinclusive = maxinclusive
        self.maxexclusive = maxexclusive
        self.last = last


fix_forwards(globals())

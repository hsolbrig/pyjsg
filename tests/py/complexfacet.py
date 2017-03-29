# Auto generated from jsg/complexfacet.jsg by PyJSG version 0.1.1
# Generation date: 2017-03-29 13:55
#
from typing import Optional, Dict, List, Union, _ForwardRef

from pyjsg.jsglib.jsg import JSGString, JSGPattern, JSGObject, JSGContext
from pyjsg.jsglib.typing_patch import fix_forwards

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
                 **_extra: Dict[str, object]):
        JSGObject.__init__(self, _CONTEXT, **_extra)
        self.first = first
        self.mininclusive = mininclusive
        self.minexclusive = minexclusive
        self.maxinclusive = maxinclusive
        self.maxexclusive = maxexclusive
        self.last = last


fix_forwards(globals())

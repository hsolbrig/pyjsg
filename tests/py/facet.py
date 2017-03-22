# Auto generated from jsg/facet.jsg by PyJSG version 0.1.0-DEV
# Generation date: 2017-03-22 18:52
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
    pattern = JSGPattern(r'[A-Z]*')

class labeledNodeConstraint(JSGObject):
    def __init__(self,
                 first: Optional[INTEGER] = None,
                 length: Optional[INTEGER] = None,
                 minlength: Optional[INTEGER] = None,
                 maxlength: Optional[INTEGER] = None,
                 pattern: Optional[STRING] = None,
                 flags: Optional[STRING] = None,
                 mininclusive: Optional[DOUBLE] = None,
                 minexclusive: Optional[DOUBLE] = None,
                 maxinclusive: Optional[DOUBLE] = None,
                 maxexclusive: Optional[DOUBLE] = None,
                 totaldigits: Optional[INTEGER] = None,
                 fractiondigits: Optional[INTEGER] = None,
                 last: List[STRING] = None,
                 **_extra: Dict[str, object]):
        JSGObject.__init__(self, _CONTEXT, **_extra)
        self.first = first
        self.length = length
        self.minlength = minlength
        self.maxlength = maxlength
        self.pattern = pattern
        self.flags = flags
        self.mininclusive = mininclusive
        self.minexclusive = minexclusive
        self.maxinclusive = maxinclusive
        self.maxexclusive = maxexclusive
        self.totaldigits = totaldigits
        self.fractiondigits = fractiondigits
        self.last = last


fix_forwards(globals())

# Auto generated from jsg/facet.jsg by PyJSG version 1.0.0
# Generation date: 2017-05-15 11:10
#
from typing import Optional, Dict, List, Union, _ForwardRef

from pyjsg.jsglib.jsg import *
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
    pattern = JSGPattern(r'[A-Z]*')

class stringFacet(JSGObject):
    _reference_types = []
    
    def __init__(self,
                 length: Optional[INTEGER] = None,
                 minlength: Optional[INTEGER] = None,
                 maxlength: Optional[INTEGER] = None,
                 pattern: STRING = None,
                 flags: Optional[STRING] = None,
                 **_kwargs: Dict[str, object]):
        self._context = _CONTEXT
        self.length = length
        self.minlength = minlength
        self.maxlength = maxlength
        self.pattern = pattern
        self.flags = flags
        super().__init__(self._context, **_kwargs)


class numericFacet(JSGObject):
    _reference_types = []
    
    def __init__(self,
                 mininclusive: Optional[DOUBLE] = None,
                 minexclusive: Optional[DOUBLE] = None,
                 maxinclusive: Optional[DOUBLE] = None,
                 maxexclusive: Optional[DOUBLE] = None,
                 totaldigits: Optional[INTEGER] = None,
                 fractiondigits: Optional[INTEGER] = None,
                 **_kwargs: Dict[str, object]):
        self._context = _CONTEXT
        self.mininclusive = mininclusive
        self.minexclusive = minexclusive
        self.maxinclusive = maxinclusive
        self.maxexclusive = maxexclusive
        self.totaldigits = totaldigits
        self.fractiondigits = fractiondigits
        super().__init__(self._context, **_kwargs)


class xsFacet(JSGObject):
    _reference_types = [stringFacet, numericFacet]
    
    def __init__(self,
                 choice: Union[stringFacet, numericFacet] = None,
                 **_kwargs: Dict[str, object]):
        self._context = _CONTEXT
        self.stringFacet = stringFacet
        self.numericFacet = numericFacet
        
        self.length = choice.length if choice else None if isinstance(choice, stringFacet) else None
        self.minlength = choice.minlength if choice else None if isinstance(choice, stringFacet) else None
        self.maxlength = choice.maxlength if choice else None if isinstance(choice, stringFacet) else None
        self.pattern = choice.pattern if isinstance(choice, stringFacet) else None
        self.flags = choice.flags if choice else None if isinstance(choice, stringFacet) else None
        
        self.mininclusive = choice.mininclusive if choice else None if isinstance(choice, numericFacet) else None
        self.minexclusive = choice.minexclusive if choice else None if isinstance(choice, numericFacet) else None
        self.maxinclusive = choice.maxinclusive if choice else None if isinstance(choice, numericFacet) else None
        self.maxexclusive = choice.maxexclusive if choice else None if isinstance(choice, numericFacet) else None
        self.totaldigits = choice.totaldigits if choice else None if isinstance(choice, numericFacet) else None
        self.fractiondigits = choice.fractiondigits if choice else None if isinstance(choice, numericFacet) else None
        super().__init__(self._context, **_kwargs)


class labeledNodeConstraint(JSGObject):
    _reference_types = [xsFacet]
    
    def __init__(self,
                 first: Optional[INTEGER] = None,
                 xsFacet: List[xsFacet] = None,
                 last: List[STRING] = None,
                 **_kwargs: Dict[str, object]):
        self._context = _CONTEXT
        self.first = first
        self.xsFacet = xsFacet
        self.last = last
        super().__init__(self._context, **_kwargs)


fix_forwards(locals())

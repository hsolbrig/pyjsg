# Auto generated from jsg/facet.jsg by PyJSG version 0.5.0
# Generation date: 2018-01-27 10:29
#
from typing import Optional, Dict, List, Union, _ForwardRef

from pyjsg.jsglib import jsg
from pyjsg.jsglib.jsg import isinstance_

# .TYPE and .IGNORE settings
_CONTEXT = jsg.JSGContext()
_CONTEXT.TYPE_EXCEPTIONS.append("stringFacet")
_CONTEXT.TYPE_EXCEPTIONS.append("numericFacet")
_CONTEXT.TYPE_EXCEPTIONS.append("xsFacet")
_CONTEXT.TYPE_EXCEPTIONS.append("labeledNodeConstraint")




class INTEGER(jsg.JSGString):
    pattern = jsg.JSGPattern(r'[0-9]*')


class DECIMAL(jsg.JSGString):
    pattern = jsg.JSGPattern(r'[0-9]*')


class DOUBLE(jsg.JSGString):
    pattern = jsg.JSGPattern(r'[0-9]*')


class STRING(jsg.JSGString):
    pattern = jsg.JSGPattern(r'[A-Z]*')

class stringFacet(jsg.JSGObject):
    _reference_types = []
    _members = {'length': Optional[INTEGER],
                'minlength': Optional[INTEGER],
                'maxlength': Optional[INTEGER],
                'pattern': STRING,
                'flags': Optional[STRING]}
    _strict = True
    
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


class numericFacet(jsg.JSGObject):
    _reference_types = []
    _members = {'mininclusive': Optional[DOUBLE],
                'minexclusive': Optional[DOUBLE],
                'maxinclusive': Optional[DOUBLE],
                'maxexclusive': Optional[DOUBLE],
                'totaldigits': Optional[INTEGER],
                'fractiondigits': Optional[INTEGER]}
    _strict = True
    
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


class xsFacet(jsg.JSGObject):
    _reference_types = [stringFacet, numericFacet]
    _members = {'length': Optional[INTEGER],
                'minlength': Optional[INTEGER],
                'maxlength': Optional[INTEGER],
                'pattern': STRING,
                'flags': Optional[STRING],
                'mininclusive': Optional[DOUBLE],
                'minexclusive': Optional[DOUBLE],
                'maxinclusive': Optional[DOUBLE],
                'maxexclusive': Optional[DOUBLE],
                'totaldigits': Optional[INTEGER],
                'fractiondigits': Optional[INTEGER]}
    _strict = True
    
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


class labeledNodeConstraint(jsg.JSGObject):
    _reference_types = [xsFacet]
    _members = {'first': Optional[INTEGER],
                'xsFacet': List[xsFacet],
                'last': List[STRING]}
    _strict = True
    
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


_CONTEXT.NAMESPACE = locals()

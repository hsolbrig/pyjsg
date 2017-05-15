# Auto generated from jsg/complexfacet.jsg by PyJSG version 1.0.0
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
    pattern = JSGPattern(r'[a-z]*')

numericLiteral = Union[INTEGER, DECIMAL, DOUBLE]

class numericFacet(JSGObject):
    _reference_types = []
    
    def __init__(self,
                 mininclusive: Optional[numericLiteral] = None,
                 minexclusive: Optional[numericLiteral] = None,
                 maxinclusive: Optional[numericLiteral] = None,
                 maxexclusive: Optional[numericLiteral] = None,
                 **_kwargs: Dict[str, object]):
        self._context = _CONTEXT
        self.mininclusive = mininclusive
        self.minexclusive = minexclusive
        self.maxinclusive = maxinclusive
        self.maxexclusive = maxexclusive
        super().__init__(self._context, **_kwargs)


class labeledNodeConstraint1(JSGObject):
    _reference_types = [numericFacet]
    
    def __init__(self,
                 first: Optional[INTEGER] = None,
                 numericFacet: Optional[numericFacet] = None,
                 last: List[STRING] = None,
                 **_kwargs: Dict[str, object]):
        self._context = _CONTEXT
        self.first = first
        self.mininclusive = numericFacet.mininclusive if numericFacet else None
        self.minexclusive = numericFacet.minexclusive if numericFacet else None
        self.maxinclusive = numericFacet.maxinclusive if numericFacet else None
        self.maxexclusive = numericFacet.maxexclusive if numericFacet else None
        self.last = last
        super().__init__(self._context, **_kwargs)


class labeledNodeConstraint2(JSGObject):
    _reference_types = [numericFacet]
    
    def __init__(self,
                 first: int = None,
                 numericFacet: numericFacet = None,
                 last: str = None,
                 **_kwargs: Dict[str, object]):
        self._context = _CONTEXT
        self.first = Integer(first)
        self.mininclusive = numericFacet.mininclusive if numericFacet else None
        self.minexclusive = numericFacet.minexclusive if numericFacet else None
        self.maxinclusive = numericFacet.maxinclusive if numericFacet else None
        self.maxexclusive = numericFacet.maxexclusive if numericFacet else None
        self.last = String(last)
        super().__init__(self._context, **_kwargs)


class labeledNodeCOnstraint3(JSGObject):
    _reference_types = [numericFacet]
    
    def __init__(self,
                 first: List[INTEGER] = None,
                 numericFacet: List[numericFacet] = None,
                 last: List[STRING] = None,
                 **_kwargs: Dict[str, object]):
        self._context = _CONTEXT
        self.first = first
        self.numericFacet = numericFacet
        self.last = last
        super().__init__(self._context, **_kwargs)


fix_forwards(locals())

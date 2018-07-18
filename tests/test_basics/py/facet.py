# Auto generated from tests/test_basics/jsg/facet.jsg by PyJSG version 0.7.0
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
_CONTEXT.TYPE_EXCEPTIONS.append("stringFacet")
_CONTEXT.TYPE_EXCEPTIONS.append("numericFacet")
_CONTEXT.TYPE_EXCEPTIONS.append("xsFacet")
_CONTEXT.TYPE_EXCEPTIONS.append("labeledNodeConstraint")


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
    _members = {'length': Optional[INTEGER],
                'minlength': Optional[INTEGER],
                'maxlength': Optional[INTEGER],
                'pattern': STRING,
                'flags': Optional[STRING]}
    _strict = True

    def __init__(self,
                 length: Optional[str] = None,
                 minlength: Optional[str] = None,
                 maxlength: Optional[str] = None,
                 pattern: str = None,
                 flags: Optional[str] = None,
                 **_kwargs: Dict[str, object]):
        super().__init__(_CONTEXT, **_kwargs)
        self.length = length
        self.minlength = minlength
        self.maxlength = maxlength
        self.pattern = pattern
        self.flags = flags


class numericFacet(JSGObject):
    _reference_types = []
    _members = {'mininclusive': Optional[DOUBLE],
                'minexclusive': Optional[DOUBLE],
                'maxinclusive': Optional[DOUBLE],
                'maxexclusive': Optional[DOUBLE],
                'totaldigits': Optional[INTEGER],
                'fractiondigits': Optional[INTEGER]}
    _strict = True

    def __init__(self,
                 mininclusive: Optional[str] = None,
                 minexclusive: Optional[str] = None,
                 maxinclusive: Optional[str] = None,
                 maxexclusive: Optional[str] = None,
                 totaldigits: Optional[str] = None,
                 fractiondigits: Optional[str] = None,
                 **_kwargs: Dict[str, object]):
        super().__init__(_CONTEXT, **_kwargs)
        self.mininclusive = mininclusive
        self.minexclusive = minexclusive
        self.maxinclusive = maxinclusive
        self.maxexclusive = maxexclusive
        self.totaldigits = totaldigits
        self.fractiondigits = fractiondigits


class xsFacet(JSGObject):
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
                 length: Optional[str] = None,
                 minlength: Optional[str] = None,
                 maxlength: Optional[str] = None,
                 pattern: str = None,
                 flags: Optional[str] = None,
                 mininclusive: Optional[str] = None,
                 minexclusive: Optional[str] = None,
                 maxinclusive: Optional[str] = None,
                 maxexclusive: Optional[str] = None,
                 totaldigits: Optional[str] = None,
                 fractiondigits: Optional[str] = None,
                 **_kwargs: Dict[str, object]):
        super().__init__(_CONTEXT, **_kwargs)
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


class labeledNodeConstraint(JSGObject):
    _reference_types = [xsFacet]
    _members = {'first': Optional[INTEGER],
                'length': ArrayFactory('{name}', _CONTEXT, Optional[INTEGER], 0, None),
                'minlength': ArrayFactory('{name}', _CONTEXT, Optional[INTEGER], 0, None),
                'maxlength': ArrayFactory('{name}', _CONTEXT, Optional[INTEGER], 0, None),
                'pattern': ArrayFactory('{name}', _CONTEXT, STRING, 0, None),
                'flags': ArrayFactory('{name}', _CONTEXT, Optional[STRING], 0, None),
                'mininclusive': ArrayFactory('{name}', _CONTEXT, Optional[DOUBLE], 0, None),
                'minexclusive': ArrayFactory('{name}', _CONTEXT, Optional[DOUBLE], 0, None),
                'maxinclusive': ArrayFactory('{name}', _CONTEXT, Optional[DOUBLE], 0, None),
                'maxexclusive': ArrayFactory('{name}', _CONTEXT, Optional[DOUBLE], 0, None),
                'totaldigits': ArrayFactory('{name}', _CONTEXT, Optional[INTEGER], 0, None),
                'fractiondigits': ArrayFactory('{name}', _CONTEXT, Optional[INTEGER], 0, None),
                'last': ArrayFactory('last', _CONTEXT, STRING, 1, None)}
    _strict = True

    def __init__(self,
                 first: Optional[str] = None,
                 length: Optional[str] = None,
                 minlength: Optional[str] = None,
                 maxlength: Optional[str] = None,
                 pattern: str = None,
                 flags: Optional[str] = None,
                 mininclusive: Optional[str] = None,
                 minexclusive: Optional[str] = None,
                 maxinclusive: Optional[str] = None,
                 maxexclusive: Optional[str] = None,
                 totaldigits: Optional[str] = None,
                 fractiondigits: Optional[str] = None,
                 last: List[str] = None,
                 **_kwargs: Dict[str, object]):
        super().__init__(_CONTEXT, **_kwargs)
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


_CONTEXT.NAMESPACE = locals()

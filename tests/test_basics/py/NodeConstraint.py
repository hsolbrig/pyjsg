# Auto generated from test_basics/jsg/NodeConstraint.jsg by PyJSG version 0.7.0
# Generation date: 2018-06-28 11:40
#
import sys
from typing import Optional, Dict, List, Union
if sys.version_info < (3, 7):
    from typing import _ForwardRef as ForwardRef
    from pyjsg.jsglib import typing_patch_36
else:
    from typing import ForwardRef
    from pyjsg.jsglib import typing_patch_37

from pyjsg.jsglib import *
from pyjsg.jsglib.jsg import isinstance_

# .TYPE and .IGNORE settings
_CONTEXT = JSGContext()
_CONTEXT.TYPE_EXCEPTIONS.append("stringFacet_1_")
_CONTEXT.TYPE_EXCEPTIONS.append("stringFacet_2_")
_CONTEXT.TYPE_EXCEPTIONS.append("numericFacet")
_CONTEXT.TYPE_EXCEPTIONS.append("xsFacet_2_")
_CONTEXT.TYPE_EXCEPTIONS.append("stringFacet")
_CONTEXT.TYPE_EXCEPTIONS.append("xsFacet_1_")
_CONTEXT.TYPE_EXCEPTIONS.append("xsFacet")
_CONTEXT.TYPE_EXCEPTIONS.append("NodeConstraint")




class _Anon1(JSGString):
    pattern = JSGPattern(r'(iri)|(bnode)|(nonliteral)|(literal)')


class IRI(JSGString):
    pattern = JSGPattern(r'[0-9]')

class stringFacet_1_(JSGObject):
    _reference_types = []
    _members = {'length': int,
                'minlength': int,
                'maxlength': int}
    _strict = True
    
    def __init__(self,
                 length: int = None,
                 minlength: int = None,
                 maxlength: int = None,
                 **_kwargs: Dict[str, object]):
        self._context = _CONTEXT
        self.length = Integer(length)
        self.minlength = Integer(minlength)
        self.maxlength = Integer(maxlength)
        super().__init__(self._context, **_kwargs)


class stringFacet_2_(JSGObject):
    _reference_types = []
    _members = {'pattern': str,
                'flags': Optional[str]}
    _strict = True
    
    def __init__(self,
                 pattern: str = None,
                 flags: Optional[str] = None,
                 **_kwargs: Dict[str, object]):
        self._context = _CONTEXT
        self.pattern = String(pattern)
        self.flags = String(flags)
        super().__init__(self._context, **_kwargs)


class numericFacet(JSGObject):
    _reference_types = []
    _members = {'mininclusive': int,
                'minexclusive': int,
                'maxinclusive': int,
                'maxexclusive': int,
                'totaldigits': int,
                'fractiondigits': int}
    _strict = True
    
    def __init__(self,
                 mininclusive: int = None,
                 minexclusive: int = None,
                 maxinclusive: int = None,
                 maxexclusive: int = None,
                 totaldigits: int = None,
                 fractiondigits: int = None,
                 **_kwargs: Dict[str, object]):
        self._context = _CONTEXT
        self.mininclusive = Integer(mininclusive)
        self.minexclusive = Integer(minexclusive)
        self.maxinclusive = Integer(maxinclusive)
        self.maxexclusive = Integer(maxexclusive)
        self.totaldigits = Integer(totaldigits)
        self.fractiondigits = Integer(fractiondigits)
        super().__init__(self._context, **_kwargs)


class xsFacet_2_(JSGObject):
    _reference_types = [numericFacet]
    _members = {'mininclusive': int,
                'minexclusive': int,
                'maxinclusive': int,
                'maxexclusive': int,
                'totaldigits': int,
                'fractiondigits': int}
    _strict = True
    
    def __init__(self,
                 numericFacet: numericFacet = None,
                 **_kwargs: Dict[str, object]):
        self._context = _CONTEXT
        self.mininclusive = Integer(numericFacet.mininclusive)
        self.minexclusive = Integer(numericFacet.minexclusive)
        self.maxinclusive = Integer(numericFacet.maxinclusive)
        self.maxexclusive = Integer(numericFacet.maxexclusive)
        self.totaldigits = Integer(numericFacet.totaldigits)
        self.fractiondigits = Integer(numericFacet.fractiondigits)
        super().__init__(self._context, **_kwargs)


class stringFacet(JSGObject):
    _reference_types = [stringFacet_1_, stringFacet_2_]
    _members = {'length': int,
                'minlength': int,
                'maxlength': int,
                'pattern': str,
                'flags': Optional[str]}
    _strict = True
    
    def __init__(self,
                 opt_: Union[stringFacet_1_, stringFacet_2_] = None,
                 **_kwargs: Dict[str, object]):
        self._context = _CONTEXT
        self.length = Integer(opt_.length) if isinstance(opt_, stringFacet_1_) else Integer(None)
        self.minlength = Integer(opt_.minlength) if isinstance(opt_, stringFacet_1_) else Integer(None)
        self.maxlength = Integer(opt_.maxlength) if isinstance(opt_, stringFacet_1_) else Integer(None)
        self.pattern = String(opt_.pattern) if isinstance(opt_, stringFacet_2_) else String(None)
        self.flags = String(opt_.flags) if opt_ else String(None) if isinstance(opt_, stringFacet_2_) else String(None)
        super().__init__(self._context, **_kwargs)


class xsFacet_1_(JSGObject):
    _reference_types = [stringFacet]
    _members = {'length': int,
                'minlength': int,
                'maxlength': int,
                'pattern': str,
                'flags': Optional[str]}
    _strict = True
    
    def __init__(self,
                 stringFacet: stringFacet = None,
                 **_kwargs: Dict[str, object]):
        self._context = _CONTEXT
        self.length = Integer(stringFacet.length)
        self.minlength = Integer(stringFacet.minlength)
        self.maxlength = Integer(stringFacet.maxlength)
        self.pattern = String(stringFacet.pattern)
        self.flags = String(stringFacet.flags) if stringFacet else String(None)
        super().__init__(self._context, **_kwargs)


class xsFacet(JSGObject):
    _reference_types = [xsFacet_1_, xsFacet_2_]
    _members = {'length': int,
                'minlength': int,
                'maxlength': int,
                'pattern': str,
                'flags': Optional[str],
                'mininclusive': int,
                'minexclusive': int,
                'maxinclusive': int,
                'maxexclusive': int,
                'totaldigits': int,
                'fractiondigits': int}
    _strict = True
    
    def __init__(self,
                 opt_: Union[xsFacet_1_, xsFacet_2_] = None,
                 **_kwargs: Dict[str, object]):
        self._context = _CONTEXT
        self.length = Integer(opt_.length) if isinstance(opt_, xsFacet_1_) else Integer(None)
        self.minlength = Integer(opt_.minlength) if isinstance(opt_, xsFacet_1_) else Integer(None)
        self.maxlength = Integer(opt_.maxlength) if isinstance(opt_, xsFacet_1_) else Integer(None)
        self.pattern = String(opt_.pattern) if isinstance(opt_, xsFacet_1_) else String(None)
        self.flags = String(opt_.flags) if opt_ else String(None) if isinstance(opt_, xsFacet_1_) else String(None)
        self.mininclusive = Integer(opt_.mininclusive) if isinstance(opt_, xsFacet_2_) else Integer(None)
        self.minexclusive = Integer(opt_.minexclusive) if isinstance(opt_, xsFacet_2_) else Integer(None)
        self.maxinclusive = Integer(opt_.maxinclusive) if isinstance(opt_, xsFacet_2_) else Integer(None)
        self.maxexclusive = Integer(opt_.maxexclusive) if isinstance(opt_, xsFacet_2_) else Integer(None)
        self.totaldigits = Integer(opt_.totaldigits) if isinstance(opt_, xsFacet_2_) else Integer(None)
        self.fractiondigits = Integer(opt_.fractiondigits) if isinstance(opt_, xsFacet_2_) else Integer(None)
        super().__init__(self._context, **_kwargs)


class NodeConstraint(JSGObject):
    _reference_types = [xsFacet]
    _members = {'nodeKind': Optional[_Anon1],
                'datatype': Optional[IRI],
                'length': Optional[int],
                'minlength': Optional[int],
                'maxlength': Optional[int],
                'pattern': Optional[str],
                'flags': Optional[str],
                'mininclusive': Optional[int],
                'minexclusive': Optional[int],
                'maxinclusive': Optional[int],
                'maxexclusive': Optional[int],
                'totaldigits': Optional[int],
                'fractiondigits': Optional[int]}
    _strict = True
    
    def __init__(self,
                 nodeKind: Optional[_Anon1] = None,
                 datatype: Optional[IRI] = None,
                 xsFacet: Optional[xsFacet] = None,
                 **_kwargs: Dict[str, object]):
        self._context = _CONTEXT
        self.nodeKind = nodeKind
        self.datatype = datatype
        self.length = Integer(xsFacet.length) if xsFacet else Integer(None)
        self.minlength = Integer(xsFacet.minlength) if xsFacet else Integer(None)
        self.maxlength = Integer(xsFacet.maxlength) if xsFacet else Integer(None)
        self.pattern = String(xsFacet.pattern) if xsFacet else String(None)
        self.flags = String(xsFacet.flags) if xsFacet else String(None)
        self.mininclusive = Integer(xsFacet.mininclusive) if xsFacet else Integer(None)
        self.minexclusive = Integer(xsFacet.minexclusive) if xsFacet else Integer(None)
        self.maxinclusive = Integer(xsFacet.maxinclusive) if xsFacet else Integer(None)
        self.maxexclusive = Integer(xsFacet.maxexclusive) if xsFacet else Integer(None)
        self.totaldigits = Integer(xsFacet.totaldigits) if xsFacet else Integer(None)
        self.fractiondigits = Integer(xsFacet.fractiondigits) if xsFacet else Integer(None)
        super().__init__(self._context, **_kwargs)


_CONTEXT.NAMESPACE = locals()

# Auto generated from jsg/NodeConstraint.jsg by PyJSG version 0.3.1
# Generation date: 2017-12-17 21:17
#
from typing import Optional, Dict, List, Union, _ForwardRef

from pyjsg.jsglib import jsg
from pyjsg.jsglib import typing_patch

# .TYPE and .IGNORE settings
_CONTEXT = jsg.JSGContext()
_CONTEXT.TYPE_EXCEPTIONS.append("stringFacet_1_")
_CONTEXT.TYPE_EXCEPTIONS.append("stringFacet_2_")
_CONTEXT.TYPE_EXCEPTIONS.append("numericFacet")
_CONTEXT.TYPE_EXCEPTIONS.append("xsFacet_2_")
_CONTEXT.TYPE_EXCEPTIONS.append("stringFacet")
_CONTEXT.TYPE_EXCEPTIONS.append("xsFacet_1_")
_CONTEXT.TYPE_EXCEPTIONS.append("xsFacet")
_CONTEXT.TYPE_EXCEPTIONS.append("NodeConstraint")




class _Anon1(jsg.JSGString):
    pattern = jsg.JSGPattern(r'(iri)|(bnode)|(nonliteral)|(literal)')


class IRI(jsg.JSGString):
    pattern = jsg.JSGPattern(r'[0-9]')

class stringFacet_1_(jsg.JSGObject):
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
        self.length = jsg.Integer(length)
        self.minlength = jsg.Integer(minlength)
        self.maxlength = jsg.Integer(maxlength)
        super().__init__(self._context, **_kwargs)


class stringFacet_2_(jsg.JSGObject):
    _reference_types = []
    _members = {'pattern': str,
                'flags': Optional[str]}
    _strict = True
    
    def __init__(self,
                 pattern: str = None,
                 flags: Optional[str] = None,
                 **_kwargs: Dict[str, object]):
        self._context = _CONTEXT
        self.pattern = jsg.String(pattern)
        self.flags = jsg.String(flags)
        super().__init__(self._context, **_kwargs)


class numericFacet(jsg.JSGObject):
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
        self.mininclusive = jsg.Integer(mininclusive)
        self.minexclusive = jsg.Integer(minexclusive)
        self.maxinclusive = jsg.Integer(maxinclusive)
        self.maxexclusive = jsg.Integer(maxexclusive)
        self.totaldigits = jsg.Integer(totaldigits)
        self.fractiondigits = jsg.Integer(fractiondigits)
        super().__init__(self._context, **_kwargs)


class xsFacet_2_(jsg.JSGObject):
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
        self.mininclusive = jsg.Integer(numericFacet.mininclusive)
        self.minexclusive = jsg.Integer(numericFacet.minexclusive)
        self.maxinclusive = jsg.Integer(numericFacet.maxinclusive)
        self.maxexclusive = jsg.Integer(numericFacet.maxexclusive)
        self.totaldigits = jsg.Integer(numericFacet.totaldigits)
        self.fractiondigits = jsg.Integer(numericFacet.fractiondigits)
        super().__init__(self._context, **_kwargs)


class stringFacet(jsg.JSGObject):
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
        self.length = jsg.Integer(opt_.length) if isinstance(opt_, stringFacet_1_) else jsg.Integer(None)
        self.minlength = jsg.Integer(opt_.minlength) if isinstance(opt_, stringFacet_1_) else jsg.Integer(None)
        self.maxlength = jsg.Integer(opt_.maxlength) if isinstance(opt_, stringFacet_1_) else jsg.Integer(None)
        self.pattern = jsg.String(opt_.pattern) if isinstance(opt_, stringFacet_2_) else jsg.String(None)
        self.flags = jsg.String(opt_.flags) if opt_ else jsg.String(None) if isinstance(opt_, stringFacet_2_) else jsg.String(None)
        super().__init__(self._context, **_kwargs)


class xsFacet_1_(jsg.JSGObject):
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
        self.length = jsg.Integer(stringFacet.length)
        self.minlength = jsg.Integer(stringFacet.minlength)
        self.maxlength = jsg.Integer(stringFacet.maxlength)
        self.pattern = jsg.String(stringFacet.pattern)
        self.flags = jsg.String(stringFacet.flags) if stringFacet else jsg.String(None)
        super().__init__(self._context, **_kwargs)


class xsFacet(jsg.JSGObject):
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
        self.length = jsg.Integer(opt_.length) if isinstance(opt_, xsFacet_1_) else jsg.Integer(None)
        self.minlength = jsg.Integer(opt_.minlength) if isinstance(opt_, xsFacet_1_) else jsg.Integer(None)
        self.maxlength = jsg.Integer(opt_.maxlength) if isinstance(opt_, xsFacet_1_) else jsg.Integer(None)
        self.pattern = jsg.String(opt_.pattern) if isinstance(opt_, xsFacet_1_) else jsg.String(None)
        self.flags = jsg.String(opt_.flags) if opt_ else jsg.String(None) if isinstance(opt_, xsFacet_1_) else jsg.String(None)
        self.mininclusive = jsg.Integer(opt_.mininclusive) if isinstance(opt_, xsFacet_2_) else jsg.Integer(None)
        self.minexclusive = jsg.Integer(opt_.minexclusive) if isinstance(opt_, xsFacet_2_) else jsg.Integer(None)
        self.maxinclusive = jsg.Integer(opt_.maxinclusive) if isinstance(opt_, xsFacet_2_) else jsg.Integer(None)
        self.maxexclusive = jsg.Integer(opt_.maxexclusive) if isinstance(opt_, xsFacet_2_) else jsg.Integer(None)
        self.totaldigits = jsg.Integer(opt_.totaldigits) if isinstance(opt_, xsFacet_2_) else jsg.Integer(None)
        self.fractiondigits = jsg.Integer(opt_.fractiondigits) if isinstance(opt_, xsFacet_2_) else jsg.Integer(None)
        super().__init__(self._context, **_kwargs)


class NodeConstraint(jsg.JSGObject):
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
        self.length = jsg.Integer(xsFacet.length) if xsFacet else jsg.Integer(None)
        self.minlength = jsg.Integer(xsFacet.minlength) if xsFacet else jsg.Integer(None)
        self.maxlength = jsg.Integer(xsFacet.maxlength) if xsFacet else jsg.Integer(None)
        self.pattern = jsg.String(xsFacet.pattern) if xsFacet else jsg.String(None)
        self.flags = jsg.String(xsFacet.flags) if xsFacet else jsg.String(None)
        self.mininclusive = jsg.Integer(xsFacet.mininclusive) if xsFacet else jsg.Integer(None)
        self.minexclusive = jsg.Integer(xsFacet.minexclusive) if xsFacet else jsg.Integer(None)
        self.maxinclusive = jsg.Integer(xsFacet.maxinclusive) if xsFacet else jsg.Integer(None)
        self.maxexclusive = jsg.Integer(xsFacet.maxexclusive) if xsFacet else jsg.Integer(None)
        self.totaldigits = jsg.Integer(xsFacet.totaldigits) if xsFacet else jsg.Integer(None)
        self.fractiondigits = jsg.Integer(xsFacet.fractiondigits) if xsFacet else jsg.Integer(None)
        super().__init__(self._context, **_kwargs)


_CONTEXT.NAMESPACE = locals()

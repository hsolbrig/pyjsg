# Auto generated from tests/test_basics/jsg/NodeConstraint.jsg by PyJSG version 0.7.0
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
    _members = {'length': Integer,
                'minlength': Integer,
                'maxlength': Integer}
    _strict = True

    def __init__(self,
                 length: int = None,
                 minlength: int = None,
                 maxlength: int = None,
                 **_kwargs: Dict[str, object]):
        super().__init__(_CONTEXT, **_kwargs)
        self.length = length
        self.minlength = minlength
        self.maxlength = maxlength


class stringFacet_2_(JSGObject):
    _reference_types = []
    _members = {'pattern': String,
                'flags': Optional[String]}
    _strict = True

    def __init__(self,
                 pattern: str = None,
                 flags: Optional[str] = None,
                 **_kwargs: Dict[str, object]):
        super().__init__(_CONTEXT, **_kwargs)
        self.pattern = pattern
        self.flags = flags


class numericFacet(JSGObject):
    _reference_types = []
    _members = {'mininclusive': Integer,
                'minexclusive': Integer,
                'maxinclusive': Integer,
                'maxexclusive': Integer,
                'totaldigits': Integer,
                'fractiondigits': Integer}
    _strict = True

    def __init__(self,
                 mininclusive: int = None,
                 minexclusive: int = None,
                 maxinclusive: int = None,
                 maxexclusive: int = None,
                 totaldigits: int = None,
                 fractiondigits: int = None,
                 **_kwargs: Dict[str, object]):
        super().__init__(_CONTEXT, **_kwargs)
        self.mininclusive = mininclusive
        self.minexclusive = minexclusive
        self.maxinclusive = maxinclusive
        self.maxexclusive = maxexclusive
        self.totaldigits = totaldigits
        self.fractiondigits = fractiondigits


class xsFacet_2_(JSGObject):
    _reference_types = [numericFacet]
    _members = {'mininclusive': Integer,
                'minexclusive': Integer,
                'maxinclusive': Integer,
                'maxexclusive': Integer,
                'totaldigits': Integer,
                'fractiondigits': Integer}
    _strict = True

    def __init__(self,
                 mininclusive: int = None,
                 minexclusive: int = None,
                 maxinclusive: int = None,
                 maxexclusive: int = None,
                 totaldigits: int = None,
                 fractiondigits: int = None,
                 **_kwargs: Dict[str, object]):
        super().__init__(_CONTEXT, **_kwargs)
        self.mininclusive = mininclusive
        self.minexclusive = minexclusive
        self.maxinclusive = maxinclusive
        self.maxexclusive = maxexclusive
        self.totaldigits = totaldigits
        self.fractiondigits = fractiondigits


class stringFacet(JSGObject):
    _reference_types = [stringFacet_1_, stringFacet_2_]
    _members = {'length': Optional[Integer],
                'minlength': Optional[Integer],
                'maxlength': Optional[Integer],
                'pattern': Optional[String],
                'flags': Optional[String]}
    _strict = True

    def __init__(self,
                 opts_: Union[stringFacet_1_, stringFacet_2_] = None,
                 **_kwargs: Dict[str, object]):
        super().__init__(_CONTEXT, **_kwargs)
        if opts_ is not None:
            if isinstance(opts_, stringFacet_1_):
                self.length = opts_.length
                self.minlength = opts_.minlength
                self.maxlength = opts_.maxlength
            elif isinstance(opts_, stringFacet_2_):
                self.pattern = opts_.pattern
                self.flags = opts_.flags
            else:
                raise ValueError(f"Unrecognized value type: {opts_}")


class xsFacet_1_(JSGObject):
    _reference_types = [stringFacet]
    _members = {'length': Optional[Integer],
                'minlength': Optional[Integer],
                'maxlength': Optional[Integer],
                'pattern': Optional[String],
                'flags': Optional[String]}
    _strict = True

    def __init__(self,
                 opts_: Union[stringFacet_1_, stringFacet_2_] = None,
                 **_kwargs: Dict[str, object]):
        super().__init__(_CONTEXT, **_kwargs)
        if opts_ is not None:
            if isinstance(opts_, stringFacet_1_):
                self.length = opts_.length
                self.minlength = opts_.minlength
                self.maxlength = opts_.maxlength
            elif isinstance(opts_, stringFacet_2_):
                self.pattern = opts_.pattern
                self.flags = opts_.flags
            else:
                raise ValueError(f"Unrecognized value type: {opts_}")


class xsFacet(JSGObject):
    _reference_types = [xsFacet_1_, xsFacet_2_]
    _members = {'length': Optional[Optional[Integer]],
                'minlength': Optional[Optional[Integer]],
                'maxlength': Optional[Optional[Integer]],
                'pattern': Optional[Optional[String]],
                'flags': Optional[Optional[String]],
                'mininclusive': Optional[Optional[Integer]],
                'minexclusive': Optional[Optional[Integer]],
                'maxinclusive': Optional[Optional[Integer]],
                'maxexclusive': Optional[Optional[Integer]],
                'totaldigits': Optional[Optional[Integer]],
                'fractiondigits': Optional[Optional[Integer]]}
    _strict = True

    def __init__(self,
                 opts_: Union[xsFacet_1_, xsFacet_2_] = None,
                 **_kwargs: Dict[str, object]):
        super().__init__(_CONTEXT, **_kwargs)
        if opts_ is not None:
            if isinstance(opts_, xsFacet_1_):
                if opts_ is not None:
                    if isinstance(opts_, stringFacet_1_):
                        self.length = opts_.length
                        self.minlength = opts_.minlength
                        self.maxlength = opts_.maxlength
                    elif isinstance(opts_, stringFacet_2_):
                        self.pattern = opts_.pattern
                        self.flags = opts_.flags
                    else:
                        raise ValueError(f"Unrecognized value type: {opts_}")
            elif isinstance(opts_, xsFacet_2_):
                self.mininclusive = opts_.mininclusive
                self.minexclusive = opts_.minexclusive
                self.maxinclusive = opts_.maxinclusive
                self.maxexclusive = opts_.maxexclusive
                self.totaldigits = opts_.totaldigits
                self.fractiondigits = opts_.fractiondigits
            else:
                raise ValueError(f"Unrecognized value type: {opts_}")


class NodeConstraint(JSGObject):
    _reference_types = [xsFacet]
    _members = {'nodeKind': Optional[_Anon1],
                'datatype': Optional[IRI],
                'length': Optional[Optional[Integer]],
                'minlength': Optional[Optional[Integer]],
                'maxlength': Optional[Optional[Integer]],
                'pattern': Optional[Optional[String]],
                'flags': Optional[Optional[String]],
                'mininclusive': Optional[Optional[Integer]],
                'minexclusive': Optional[Optional[Integer]],
                'maxinclusive': Optional[Optional[Integer]],
                'maxexclusive': Optional[Optional[Integer]],
                'totaldigits': Optional[Optional[Integer]],
                'fractiondigits': Optional[Optional[Integer]]}
    _strict = True

    def __init__(self,
                 nodeKind: Optional[str] = None,
                 datatype: Optional[str] = None,
                 opts_: Union[xsFacet_1_, xsFacet_2_] = None,
                 **_kwargs: Dict[str, object]):
        super().__init__(_CONTEXT, **_kwargs)
        self.nodeKind = nodeKind
        self.datatype = datatype
        if opts_ is not None:
            if isinstance(opts_, xsFacet_1_):
                if opts_ is not None:
                    if isinstance(opts_, stringFacet_1_):
                        self.length = opts_.length
                        self.minlength = opts_.minlength
                        self.maxlength = opts_.maxlength
                    elif isinstance(opts_, stringFacet_2_):
                        self.pattern = opts_.pattern
                        self.flags = opts_.flags
                    else:
                        raise ValueError(f"Unrecognized value type: {opts_}")
            elif isinstance(opts_, xsFacet_2_):
                self.mininclusive = opts_.mininclusive
                self.minexclusive = opts_.minexclusive
                self.maxinclusive = opts_.maxinclusive
                self.maxexclusive = opts_.maxexclusive
                self.totaldigits = opts_.totaldigits
                self.fractiondigits = opts_.fractiondigits
            else:
                raise ValueError(f"Unrecognized value type: {opts_}")


_CONTEXT.NAMESPACE = locals()

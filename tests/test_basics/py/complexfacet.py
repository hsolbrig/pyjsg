# Auto generated from tests/test_basics/jsg/complexfacet.jsg by PyJSG version 0.7.0
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
_CONTEXT.TYPE_EXCEPTIONS.append("optFacet")
_CONTEXT.TYPE_EXCEPTIONS.append("reqFacet")
_CONTEXT.TYPE_EXCEPTIONS.append("listFacet")
_CONTEXT.TYPE_EXCEPTIONS.append("optOpt")
_CONTEXT.TYPE_EXCEPTIONS.append("optReq")
_CONTEXT.TYPE_EXCEPTIONS.append("optList")
_CONTEXT.TYPE_EXCEPTIONS.append("reqOpt")
_CONTEXT.TYPE_EXCEPTIONS.append("reqReq")
_CONTEXT.TYPE_EXCEPTIONS.append("reqList")
_CONTEXT.TYPE_EXCEPTIONS.append("listOpt")
_CONTEXT.TYPE_EXCEPTIONS.append("listReq")
_CONTEXT.TYPE_EXCEPTIONS.append("listList")


class INTEGER(JSGString):
    pattern = JSGPattern(r'[0-9]*')


class DECIMAL(JSGString):
    pattern = JSGPattern(r'[0-9]*')


class DOUBLE(JSGString):
    pattern = JSGPattern(r'[0-9]*')


class STRING(JSGString):
    pattern = JSGPattern(r'[a-z]*')



numericLiteral = Union[INTEGER, DECIMAL, DOUBLE]
class optFacet(JSGObject):
    _reference_types = []
    _members = {'mininclusive': Optional[Union[INTEGER, DECIMAL, DOUBLE]],
                'minexclusive': Optional[Union[INTEGER, DECIMAL, DOUBLE]],
                'maxinclusive': Optional[Union[INTEGER, DECIMAL, DOUBLE]],
                'maxexclusive': Optional[Union[INTEGER, DECIMAL, DOUBLE]]}
    _strict = True

    def __init__(self,
                 mininclusive: Optional[Union[str, str, str]] = None,
                 minexclusive: Optional[Union[str, str, str]] = None,
                 maxinclusive: Optional[Union[str, str, str]] = None,
                 maxexclusive: Optional[Union[str, str, str]] = None,
                 **_kwargs: Dict[str, object]):
        super().__init__(_CONTEXT, **_kwargs)
        self.mininclusive = mininclusive
        self.minexclusive = minexclusive
        self.maxinclusive = maxinclusive
        self.maxexclusive = maxexclusive


class reqFacet(JSGObject):
    _reference_types = []
    _members = {'mininclusive': Union[INTEGER, DECIMAL, DOUBLE],
                'minexclusive': Union[INTEGER, DECIMAL, DOUBLE],
                'maxinclusive': Union[INTEGER, DECIMAL, DOUBLE],
                'maxexclusive': Union[INTEGER, DECIMAL, DOUBLE]}
    _strict = True

    def __init__(self,
                 mininclusive: Union[str, str, str] = None,
                 minexclusive: Union[str, str, str] = None,
                 maxinclusive: Union[str, str, str] = None,
                 maxexclusive: Union[str, str, str] = None,
                 **_kwargs: Dict[str, object]):
        super().__init__(_CONTEXT, **_kwargs)
        self.mininclusive = mininclusive
        self.minexclusive = minexclusive
        self.maxinclusive = maxinclusive
        self.maxexclusive = maxexclusive


class listFacet(JSGObject):
    _reference_types = []
    _members = {'mininclusive': ArrayFactory('mininclusive', _CONTEXT, Union[INTEGER, DECIMAL, DOUBLE], 0, None),
                'minexclusive': ArrayFactory('minexclusive', _CONTEXT, Union[INTEGER, DECIMAL, DOUBLE], 0, None),
                'maxinclusive': ArrayFactory('maxinclusive', _CONTEXT, Union[INTEGER, DECIMAL, DOUBLE], 0, None),
                'maxexclusive': ArrayFactory('maxexclusive', _CONTEXT, Union[INTEGER, DECIMAL, DOUBLE], 0, None)}
    _strict = True

    def __init__(self,
                 mininclusive: List[Union[str, str, str]] = None,
                 minexclusive: List[Union[str, str, str]] = None,
                 maxinclusive: List[Union[str, str, str]] = None,
                 maxexclusive: List[Union[str, str, str]] = None,
                 **_kwargs: Dict[str, object]):
        super().__init__(_CONTEXT, **_kwargs)
        self.mininclusive = mininclusive
        self.minexclusive = minexclusive
        self.maxinclusive = maxinclusive
        self.maxexclusive = maxexclusive


class optOpt(JSGObject):
    _reference_types = [optFacet]
    _members = {'first': Optional[INTEGER],
                'mininclusive': Optional[Union[INTEGER, DECIMAL, DOUBLE]],
                'minexclusive': Optional[Union[INTEGER, DECIMAL, DOUBLE]],
                'maxinclusive': Optional[Union[INTEGER, DECIMAL, DOUBLE]],
                'maxexclusive': Optional[Union[INTEGER, DECIMAL, DOUBLE]],
                'last': ArrayFactory('last', _CONTEXT, STRING, 1, None)}
    _strict = True

    def __init__(self,
                 first: Optional[str] = None,
                 mininclusive: Optional[Union[str, str, str]] = None,
                 minexclusive: Optional[Union[str, str, str]] = None,
                 maxinclusive: Optional[Union[str, str, str]] = None,
                 maxexclusive: Optional[Union[str, str, str]] = None,
                 last: List[str] = None,
                 **_kwargs: Dict[str, object]):
        super().__init__(_CONTEXT, **_kwargs)
        self.first = first
        self.mininclusive = mininclusive
        self.minexclusive = minexclusive
        self.maxinclusive = maxinclusive
        self.maxexclusive = maxexclusive
        self.last = last


class optReq(JSGObject):
    _reference_types = [optFacet]
    _members = {'first': Integer,
                'mininclusive': Optional[Union[INTEGER, DECIMAL, DOUBLE]],
                'minexclusive': Optional[Union[INTEGER, DECIMAL, DOUBLE]],
                'maxinclusive': Optional[Union[INTEGER, DECIMAL, DOUBLE]],
                'maxexclusive': Optional[Union[INTEGER, DECIMAL, DOUBLE]],
                'last': String}
    _strict = True

    def __init__(self,
                 first: int = None,
                 mininclusive: Optional[Union[str, str, str]] = None,
                 minexclusive: Optional[Union[str, str, str]] = None,
                 maxinclusive: Optional[Union[str, str, str]] = None,
                 maxexclusive: Optional[Union[str, str, str]] = None,
                 last: str = None,
                 **_kwargs: Dict[str, object]):
        super().__init__(_CONTEXT, **_kwargs)
        self.first = first
        self.mininclusive = mininclusive
        self.minexclusive = minexclusive
        self.maxinclusive = maxinclusive
        self.maxexclusive = maxexclusive
        self.last = last


class optList(JSGObject):
    _reference_types = [optFacet]
    _members = {'first': ArrayFactory('first', _CONTEXT, INTEGER, 0, None),
                'mininclusive': ArrayFactory('{name}', _CONTEXT, Optional[Union[INTEGER, DECIMAL, DOUBLE]], 0, None),
                'minexclusive': ArrayFactory('{name}', _CONTEXT, Optional[Union[INTEGER, DECIMAL, DOUBLE]], 0, None),
                'maxinclusive': ArrayFactory('{name}', _CONTEXT, Optional[Union[INTEGER, DECIMAL, DOUBLE]], 0, None),
                'maxexclusive': ArrayFactory('{name}', _CONTEXT, Optional[Union[INTEGER, DECIMAL, DOUBLE]], 0, None),
                'last': ArrayFactory('last', _CONTEXT, STRING, 0, None)}
    _strict = True

    def __init__(self,
                 first: List[str] = None,
                 mininclusive: Optional[Union[str, str, str]] = None,
                 minexclusive: Optional[Union[str, str, str]] = None,
                 maxinclusive: Optional[Union[str, str, str]] = None,
                 maxexclusive: Optional[Union[str, str, str]] = None,
                 last: List[str] = None,
                 **_kwargs: Dict[str, object]):
        super().__init__(_CONTEXT, **_kwargs)
        self.first = first
        self.mininclusive = mininclusive
        self.minexclusive = minexclusive
        self.maxinclusive = maxinclusive
        self.maxexclusive = maxexclusive
        self.last = last


class reqOpt(JSGObject):
    _reference_types = [reqFacet]
    _members = {'first': Optional[INTEGER],
                'mininclusive': Optional[Union[INTEGER, DECIMAL, DOUBLE]],
                'minexclusive': Optional[Union[INTEGER, DECIMAL, DOUBLE]],
                'maxinclusive': Optional[Union[INTEGER, DECIMAL, DOUBLE]],
                'maxexclusive': Optional[Union[INTEGER, DECIMAL, DOUBLE]],
                'last': ArrayFactory('last', _CONTEXT, STRING, 1, None)}
    _strict = True

    def __init__(self,
                 first: Optional[str] = None,
                 mininclusive: Union[str, str, str] = None,
                 minexclusive: Union[str, str, str] = None,
                 maxinclusive: Union[str, str, str] = None,
                 maxexclusive: Union[str, str, str] = None,
                 last: List[str] = None,
                 **_kwargs: Dict[str, object]):
        super().__init__(_CONTEXT, **_kwargs)
        self.first = first
        self.mininclusive = mininclusive
        self.minexclusive = minexclusive
        self.maxinclusive = maxinclusive
        self.maxexclusive = maxexclusive
        self.last = last


class reqReq(JSGObject):
    _reference_types = [reqFacet]
    _members = {'first': Integer,
                'mininclusive': Union[INTEGER, DECIMAL, DOUBLE],
                'minexclusive': Union[INTEGER, DECIMAL, DOUBLE],
                'maxinclusive': Union[INTEGER, DECIMAL, DOUBLE],
                'maxexclusive': Union[INTEGER, DECIMAL, DOUBLE],
                'last': String}
    _strict = True

    def __init__(self,
                 first: int = None,
                 mininclusive: Union[str, str, str] = None,
                 minexclusive: Union[str, str, str] = None,
                 maxinclusive: Union[str, str, str] = None,
                 maxexclusive: Union[str, str, str] = None,
                 last: str = None,
                 **_kwargs: Dict[str, object]):
        super().__init__(_CONTEXT, **_kwargs)
        self.first = first
        self.mininclusive = mininclusive
        self.minexclusive = minexclusive
        self.maxinclusive = maxinclusive
        self.maxexclusive = maxexclusive
        self.last = last


class reqList(JSGObject):
    _reference_types = [reqFacet]
    _members = {'first': ArrayFactory('first', _CONTEXT, INTEGER, 0, None),
                'mininclusive': ArrayFactory('{name}', _CONTEXT, Union[INTEGER, DECIMAL, DOUBLE], 0, None),
                'minexclusive': ArrayFactory('{name}', _CONTEXT, Union[INTEGER, DECIMAL, DOUBLE], 0, None),
                'maxinclusive': ArrayFactory('{name}', _CONTEXT, Union[INTEGER, DECIMAL, DOUBLE], 0, None),
                'maxexclusive': ArrayFactory('{name}', _CONTEXT, Union[INTEGER, DECIMAL, DOUBLE], 0, None),
                'last': ArrayFactory('last', _CONTEXT, STRING, 0, None)}
    _strict = True

    def __init__(self,
                 first: List[str] = None,
                 mininclusive: Union[str, str, str] = None,
                 minexclusive: Union[str, str, str] = None,
                 maxinclusive: Union[str, str, str] = None,
                 maxexclusive: Union[str, str, str] = None,
                 last: List[str] = None,
                 **_kwargs: Dict[str, object]):
        super().__init__(_CONTEXT, **_kwargs)
        self.first = first
        self.mininclusive = mininclusive
        self.minexclusive = minexclusive
        self.maxinclusive = maxinclusive
        self.maxexclusive = maxexclusive
        self.last = last


class listOpt(JSGObject):
    _reference_types = [listFacet]
    _members = {'first': Optional[INTEGER],
                'mininclusive': Optional[ArrayFactory('mininclusive', _CONTEXT, Union[INTEGER, DECIMAL, DOUBLE], 0, None)],
                'minexclusive': Optional[ArrayFactory('minexclusive', _CONTEXT, Union[INTEGER, DECIMAL, DOUBLE], 0, None)],
                'maxinclusive': Optional[ArrayFactory('maxinclusive', _CONTEXT, Union[INTEGER, DECIMAL, DOUBLE], 0, None)],
                'maxexclusive': Optional[ArrayFactory('maxexclusive', _CONTEXT, Union[INTEGER, DECIMAL, DOUBLE], 0, None)],
                'last': ArrayFactory('last', _CONTEXT, STRING, 1, None)}
    _strict = True

    def __init__(self,
                 first: Optional[str] = None,
                 mininclusive: List[Union[str, str, str]] = None,
                 minexclusive: List[Union[str, str, str]] = None,
                 maxinclusive: List[Union[str, str, str]] = None,
                 maxexclusive: List[Union[str, str, str]] = None,
                 last: List[str] = None,
                 **_kwargs: Dict[str, object]):
        super().__init__(_CONTEXT, **_kwargs)
        self.first = first
        self.mininclusive = mininclusive
        self.minexclusive = minexclusive
        self.maxinclusive = maxinclusive
        self.maxexclusive = maxexclusive
        self.last = last


class listReq(JSGObject):
    _reference_types = [listFacet]
    _members = {'first': Integer,
                'mininclusive': ArrayFactory('mininclusive', _CONTEXT, Union[INTEGER, DECIMAL, DOUBLE], 0, None),
                'minexclusive': ArrayFactory('minexclusive', _CONTEXT, Union[INTEGER, DECIMAL, DOUBLE], 0, None),
                'maxinclusive': ArrayFactory('maxinclusive', _CONTEXT, Union[INTEGER, DECIMAL, DOUBLE], 0, None),
                'maxexclusive': ArrayFactory('maxexclusive', _CONTEXT, Union[INTEGER, DECIMAL, DOUBLE], 0, None),
                'last': String}
    _strict = True

    def __init__(self,
                 first: int = None,
                 mininclusive: List[Union[str, str, str]] = None,
                 minexclusive: List[Union[str, str, str]] = None,
                 maxinclusive: List[Union[str, str, str]] = None,
                 maxexclusive: List[Union[str, str, str]] = None,
                 last: str = None,
                 **_kwargs: Dict[str, object]):
        super().__init__(_CONTEXT, **_kwargs)
        self.first = first
        self.mininclusive = mininclusive
        self.minexclusive = minexclusive
        self.maxinclusive = maxinclusive
        self.maxexclusive = maxexclusive
        self.last = last


class listList(JSGObject):
    _reference_types = [listFacet]
    _members = {'first': ArrayFactory('first', _CONTEXT, INTEGER, 0, None),
                'mininclusive': ArrayFactory('{name}', _CONTEXT, ArrayFactory('mininclusive', _CONTEXT, Union[INTEGER, DECIMAL, DOUBLE], 0, None), 0, None),
                'minexclusive': ArrayFactory('{name}', _CONTEXT, ArrayFactory('minexclusive', _CONTEXT, Union[INTEGER, DECIMAL, DOUBLE], 0, None), 0, None),
                'maxinclusive': ArrayFactory('{name}', _CONTEXT, ArrayFactory('maxinclusive', _CONTEXT, Union[INTEGER, DECIMAL, DOUBLE], 0, None), 0, None),
                'maxexclusive': ArrayFactory('{name}', _CONTEXT, ArrayFactory('maxexclusive', _CONTEXT, Union[INTEGER, DECIMAL, DOUBLE], 0, None), 0, None),
                'last': ArrayFactory('last', _CONTEXT, STRING, 0, None)}
    _strict = True

    def __init__(self,
                 first: List[str] = None,
                 mininclusive: List[Union[str, str, str]] = None,
                 minexclusive: List[Union[str, str, str]] = None,
                 maxinclusive: List[Union[str, str, str]] = None,
                 maxexclusive: List[Union[str, str, str]] = None,
                 last: List[str] = None,
                 **_kwargs: Dict[str, object]):
        super().__init__(_CONTEXT, **_kwargs)
        self.first = first
        self.mininclusive = mininclusive
        self.minexclusive = minexclusive
        self.maxinclusive = maxinclusive
        self.maxexclusive = maxexclusive
        self.last = last


_CONTEXT.NAMESPACE = locals()

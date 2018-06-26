# Auto generated from tests/test_basics/jsg/complexfacet.jsg by PyJSG version 0.6.0
# Generation date: 2018-06-26 12:40
#
import sys
from typing import Optional, Dict, List, Union
if sys.version_info < (3, 7):
    from typing import _ForwardRef as ForwardRef
    from pyjsg.jsglib import typing_patch_36
else:
    from typing import ForwardRef
    from pyjsg.jsglib import typing_patch_37

from pyjsg.jsglib import jsg, jsg_array
from pyjsg.jsglib.jsg import isinstance_

# .TYPE and .IGNORE settings
_CONTEXT = jsg.JSGContext()
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




class INTEGER(jsg.JSGString):
    pattern = jsg.JSGPattern(r'[0-9]*')


class DECIMAL(jsg.JSGString):
    pattern = jsg.JSGPattern(r'[0-9]*')


class DOUBLE(jsg.JSGString):
    pattern = jsg.JSGPattern(r'[0-9]*')


class STRING(jsg.JSGString):
    pattern = jsg.JSGPattern(r'[a-z]*')

numericLiteral = Union[INTEGER, DECIMAL, DOUBLE]

class optFacet(jsg.JSGObject):
    _reference_types = []
    _members = {'mininclusive': Optional[numericLiteral],
                'minexclusive': Optional[numericLiteral],
                'maxinclusive': Optional[numericLiteral],
                'maxexclusive': Optional[numericLiteral]}
    _strict = True
    
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


class reqFacet(jsg.JSGObject):
    _reference_types = []
    _members = {'mininclusive': numericLiteral,
                'minexclusive': numericLiteral,
                'maxinclusive': numericLiteral,
                'maxexclusive': numericLiteral}
    _strict = True
    
    def __init__(self,
                 mininclusive: numericLiteral = None,
                 minexclusive: numericLiteral = None,
                 maxinclusive: numericLiteral = None,
                 maxexclusive: numericLiteral = None,
                 **_kwargs: Dict[str, object]):
        self._context = _CONTEXT
        self.mininclusive = mininclusive
        self.minexclusive = minexclusive
        self.maxinclusive = maxinclusive
        self.maxexclusive = maxexclusive
        super().__init__(self._context, **_kwargs)


class listFacet(jsg.JSGObject):
    _reference_types = []
    _members = {'mininclusive': List[numericLiteral],
                'minexclusive': List[numericLiteral],
                'maxinclusive': List[numericLiteral],
                'maxexclusive': List[numericLiteral]}
    _strict = True
    
    def __init__(self,
                 mininclusive: List[numericLiteral] = None,
                 minexclusive: List[numericLiteral] = None,
                 maxinclusive: List[numericLiteral] = None,
                 maxexclusive: List[numericLiteral] = None,
                 **_kwargs: Dict[str, object]):
        self._context = _CONTEXT
        self.mininclusive = jsg_array.JSGArray(_CONTEXT, numericLiteral, 0, None, mininclusive)
        self.minexclusive = jsg_array.JSGArray(_CONTEXT, numericLiteral, 0, None, minexclusive)
        self.maxinclusive = jsg_array.JSGArray(_CONTEXT, numericLiteral, 0, None, maxinclusive)
        self.maxexclusive = jsg_array.JSGArray(_CONTEXT, numericLiteral, 0, None, maxexclusive)
        super().__init__(self._context, **_kwargs)


class optOpt(jsg.JSGObject):
    _reference_types = [optFacet]
    _members = {'first': Optional[INTEGER],
                'mininclusive': Optional[numericLiteral],
                'minexclusive': Optional[numericLiteral],
                'maxinclusive': Optional[numericLiteral],
                'maxexclusive': Optional[numericLiteral],
                'last': List[STRING]}
    _strict = True
    
    def __init__(self,
                 first: Optional[INTEGER] = None,
                 optFacet: Optional[optFacet] = None,
                 last: List[STRING] = None,
                 **_kwargs: Dict[str, object]):
        self._context = _CONTEXT
        self.first = first
        self.mininclusive = optFacet.mininclusive if optFacet else None
        self.minexclusive = optFacet.minexclusive if optFacet else None
        self.maxinclusive = optFacet.maxinclusive if optFacet else None
        self.maxexclusive = optFacet.maxexclusive if optFacet else None
        self.last = jsg_array.JSGArray(_CONTEXT, STRING, 1, None, last)
        super().__init__(self._context, **_kwargs)


class optReq(jsg.JSGObject):
    _reference_types = [optFacet]
    _members = {'first': int,
                'mininclusive': Optional[numericLiteral],
                'minexclusive': Optional[numericLiteral],
                'maxinclusive': Optional[numericLiteral],
                'maxexclusive': Optional[numericLiteral],
                'last': str}
    _strict = True
    
    def __init__(self,
                 first: int = None,
                 optFacet: optFacet = None,
                 last: str = None,
                 **_kwargs: Dict[str, object]):
        self._context = _CONTEXT
        self.first = jsg.Integer(first)
        self.mininclusive = optFacet.mininclusive if optFacet else None
        self.minexclusive = optFacet.minexclusive if optFacet else None
        self.maxinclusive = optFacet.maxinclusive if optFacet else None
        self.maxexclusive = optFacet.maxexclusive if optFacet else None
        self.last = jsg.String(last)
        super().__init__(self._context, **_kwargs)


class optList(jsg.JSGObject):
    _reference_types = [optFacet]
    _members = {'first': List[INTEGER],
                'optFacet': List[optFacet],
                'last': List[STRING]}
    _strict = True
    
    def __init__(self,
                 first: List[INTEGER] = None,
                 optFacet: List[optFacet] = None,
                 last: List[STRING] = None,
                 **_kwargs: Dict[str, object]):
        self._context = _CONTEXT
        self.first = jsg_array.JSGArray(_CONTEXT, INTEGER, 0, None, first)
        self.optFacet = optFacet
        self.last = jsg_array.JSGArray(_CONTEXT, STRING, 0, None, last)
        super().__init__(self._context, **_kwargs)


class reqOpt(jsg.JSGObject):
    _reference_types = [reqFacet]
    _members = {'first': Optional[INTEGER],
                'mininclusive': Optional[numericLiteral],
                'minexclusive': Optional[numericLiteral],
                'maxinclusive': Optional[numericLiteral],
                'maxexclusive': Optional[numericLiteral],
                'last': List[STRING]}
    _strict = True
    
    def __init__(self,
                 first: Optional[INTEGER] = None,
                 reqFacet: Optional[reqFacet] = None,
                 last: List[STRING] = None,
                 **_kwargs: Dict[str, object]):
        self._context = _CONTEXT
        self.first = first
        self.mininclusive = reqFacet.mininclusive if reqFacet else None
        self.minexclusive = reqFacet.minexclusive if reqFacet else None
        self.maxinclusive = reqFacet.maxinclusive if reqFacet else None
        self.maxexclusive = reqFacet.maxexclusive if reqFacet else None
        self.last = jsg_array.JSGArray(_CONTEXT, STRING, 1, None, last)
        super().__init__(self._context, **_kwargs)


class reqReq(jsg.JSGObject):
    _reference_types = [reqFacet]
    _members = {'first': int,
                'mininclusive': numericLiteral,
                'minexclusive': numericLiteral,
                'maxinclusive': numericLiteral,
                'maxexclusive': numericLiteral,
                'last': str}
    _strict = True
    
    def __init__(self,
                 first: int = None,
                 reqFacet: reqFacet = None,
                 last: str = None,
                 **_kwargs: Dict[str, object]):
        self._context = _CONTEXT
        self.first = jsg.Integer(first)
        self.mininclusive = reqFacet.mininclusive
        self.minexclusive = reqFacet.minexclusive
        self.maxinclusive = reqFacet.maxinclusive
        self.maxexclusive = reqFacet.maxexclusive
        self.last = jsg.String(last)
        super().__init__(self._context, **_kwargs)


class reqList(jsg.JSGObject):
    _reference_types = [reqFacet]
    _members = {'first': List[INTEGER],
                'reqFacet': List[reqFacet],
                'last': List[STRING]}
    _strict = True
    
    def __init__(self,
                 first: List[INTEGER] = None,
                 reqFacet: List[reqFacet] = None,
                 last: List[STRING] = None,
                 **_kwargs: Dict[str, object]):
        self._context = _CONTEXT
        self.first = jsg_array.JSGArray(_CONTEXT, INTEGER, 0, None, first)
        self.reqFacet = reqFacet
        self.last = jsg_array.JSGArray(_CONTEXT, STRING, 0, None, last)
        super().__init__(self._context, **_kwargs)


class listOpt(jsg.JSGObject):
    _reference_types = [listFacet]
    _members = {'first': Optional[INTEGER],
                'mininclusive': Optional[List[numericLiteral]],
                'minexclusive': Optional[List[numericLiteral]],
                'maxinclusive': Optional[List[numericLiteral]],
                'maxexclusive': Optional[List[numericLiteral]],
                'last': List[STRING]}
    _strict = True
    
    def __init__(self,
                 first: Optional[INTEGER] = None,
                 listFacet: Optional[listFacet] = None,
                 last: List[STRING] = None,
                 **_kwargs: Dict[str, object]):
        self._context = _CONTEXT
        self.first = first
        self.mininclusive = jsg_array.JSGArray(_CONTEXT, numericLiteral, 0, None, mininclusive)
        self.minexclusive = jsg_array.JSGArray(_CONTEXT, numericLiteral, 0, None, minexclusive)
        self.maxinclusive = jsg_array.JSGArray(_CONTEXT, numericLiteral, 0, None, maxinclusive)
        self.maxexclusive = jsg_array.JSGArray(_CONTEXT, numericLiteral, 0, None, maxexclusive)
        self.last = jsg_array.JSGArray(_CONTEXT, STRING, 1, None, last)
        super().__init__(self._context, **_kwargs)


class listReq(jsg.JSGObject):
    _reference_types = [listFacet]
    _members = {'first': int,
                'mininclusive': List[numericLiteral],
                'minexclusive': List[numericLiteral],
                'maxinclusive': List[numericLiteral],
                'maxexclusive': List[numericLiteral],
                'last': str}
    _strict = True
    
    def __init__(self,
                 first: int = None,
                 listFacet: listFacet = None,
                 last: str = None,
                 **_kwargs: Dict[str, object]):
        self._context = _CONTEXT
        self.first = jsg.Integer(first)
        self.mininclusive = jsg_array.JSGArray(_CONTEXT, numericLiteral, 0, None, mininclusive)
        self.minexclusive = jsg_array.JSGArray(_CONTEXT, numericLiteral, 0, None, minexclusive)
        self.maxinclusive = jsg_array.JSGArray(_CONTEXT, numericLiteral, 0, None, maxinclusive)
        self.maxexclusive = jsg_array.JSGArray(_CONTEXT, numericLiteral, 0, None, maxexclusive)
        self.last = jsg.String(last)
        super().__init__(self._context, **_kwargs)


class listList(jsg.JSGObject):
    _reference_types = [listFacet]
    _members = {'first': List[INTEGER],
                'listFacet': List[listFacet],
                'last': List[STRING]}
    _strict = True
    
    def __init__(self,
                 first: List[INTEGER] = None,
                 listFacet: List[listFacet] = None,
                 last: List[STRING] = None,
                 **_kwargs: Dict[str, object]):
        self._context = _CONTEXT
        self.first = jsg_array.JSGArray(_CONTEXT, INTEGER, 0, None, first)
        self.listFacet = listFacet
        self.last = jsg_array.JSGArray(_CONTEXT, STRING, 0, None, last)
        super().__init__(self._context, **_kwargs)


_CONTEXT.NAMESPACE = locals()

# Auto generated from JSGPython by PyJSG version 0.7.0
# Generation date: 2018-07-17 11:12
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
_CONTEXT.TYPE_EXCEPTIONS.append("doc")
_CONTEXT.TYPE_EXCEPTIONS.append("another_object")


class doc(JSGObject):
    _reference_types = []
    _members = {'v 1': String,
                'v 2': Number,
                'v 3': Integer,
                'v 4': Boolean,
                'v 5': JSGNull,
                'v 6': ArrayFactory('v 6', _CONTEXT, AnyType, 0, None),
                'v 7': ObjectFactory('v 7', _CONTEXT, Object)}
    _strict = True

    def __init__(self,
                 **_kwargs: Dict[str, object]):
        super().__init__(_CONTEXT, **_kwargs)
        setattr(self, 'v 1', _kwargs.get('v 1', None))
        setattr(self, 'v 2', _kwargs.get('v 2', None))
        setattr(self, 'v 3', _kwargs.get('v 3', None))
        setattr(self, 'v 4', _kwargs.get('v 4', None))
        setattr(self, 'v 5', _kwargs.get('v 5', EmptyAny))
        setattr(self, 'v 6', _kwargs.get('v 6', None))
        setattr(self, 'v 7', _kwargs.get('v 7', None))


class another_object(JSGObject):
    _reference_types = []
    _members = {}
    _strict = False

    def __init__(self,
                 **_kwargs: Dict[str, object]):
        super().__init__(_CONTEXT, **_kwargs)


_CONTEXT.NAMESPACE = locals()

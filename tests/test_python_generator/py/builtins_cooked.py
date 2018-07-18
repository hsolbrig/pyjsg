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
    _members = {'v1': String,
                'v2': Number,
                'v3': Integer,
                'v4': Boolean,
                'v5': JSGNull,
                'v6': ArrayFactory('v6', _CONTEXT, AnyType, 0, None),
                'v7': ObjectFactory('v7', _CONTEXT, Object)}
    _strict = True

    def __init__(self,
                 v1: str = None,
                 v2: float = None,
                 v3: int = None,
                 v4: bool = None,
                 v5: type(None) = EmptyAny,
                 v6: list = None,
                 v7: object = None,
                 **_kwargs: Dict[str, object]):
        super().__init__(_CONTEXT, **_kwargs)
        self.v1 = v1
        self.v2 = v2
        self.v3 = v3
        self.v4 = v4
        self.v5 = v5
        self.v6 = v6
        self.v7 = v7


class another_object(JSGObject):
    _reference_types = []
    _members = {}
    _strict = False

    def __init__(self,
                 **_kwargs: Dict[str, object]):
        super().__init__(_CONTEXT, **_kwargs)


_CONTEXT.NAMESPACE = locals()

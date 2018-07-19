# Auto generated from JSGPython by PyJSG version 0.7.0
# Generation date: 2018-06-28 17:34
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
from pyjsg.jsglib.jsg_base import isinstance_

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
                'v6': Array,
                'v7': JsonObj}
    _strict = True

    def __init__(self,
                 v1: str = None,
                 v2: float = None,
                 v3: int = None,
                 v4: bool = None,
                 v5: type(None) = EmptyAny,
                 v6: list = None,
                 v7: Object = None,
                 **_kwargs: Dict[str, object]):
        super().__init__(_CONTEXT, **_kwargs)
        self.v1 = String(v1) if v1 is not None else v1
        self.v2 = Number(v2) if v2 is not None else v2
        self.v3 = Integer(v3) if v3 is not None else v3
        self.v4 = Boolean(v4) if v4 is not None else v4
        self.v5 = JSGNull(v5) if v5 is not EmptyAny else v5
        self.v6 = Array('v6', self._context, AnyType, 0, None, v6) if v6 is not None else v6
        self.v7 = JsonObj(**v7.__dict__) if v7 is not None else v7


class another_object(JSGObject):
    _reference_types = []
    _members = {}
    _strict = False

    def __init__(self,
                 **_kwargs: Dict[str, object]):
        super().__init__(_CONTEXT, **_kwargs)


_CONTEXT.NAMESPACE = locals()

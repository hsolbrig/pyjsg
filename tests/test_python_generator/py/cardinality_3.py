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


class doc(JSGObject):
    _reference_types = []
    _members = {'l0nl0n': ArrayFactory('l0nl0n', _CONTEXT, ArrayFactory('l0nl0n', _CONTEXT, AnyType, 0, None), 0, None)}
    _strict = True

    def __init__(self,
                 l0nl0n: List[List[object]] = None,
                 **_kwargs: Dict[str, object]):
        super().__init__(_CONTEXT, **_kwargs)
        self.l0nl0n = l0nl0n


_CONTEXT.NAMESPACE = locals()

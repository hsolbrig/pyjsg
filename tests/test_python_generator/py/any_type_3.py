# Auto generated from JSGPython by PyJSG version 0.7.0
# Generation date: 2018-07-17 11:13
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
    _members = {'A 1': AnyType}
    _strict = True

    def __init__(self,
                 **_kwargs: Dict[str, object]):
        super().__init__(_CONTEXT, **_kwargs)
        setattr(self, 'A 1', _kwargs.get('A 1', EmptyAny))


_CONTEXT.NAMESPACE = locals()

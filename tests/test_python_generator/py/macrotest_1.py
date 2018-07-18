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
_CONTEXT.TYPE_EXCEPTIONS.append("Shape")


class Shape(JSGObject):
    _reference_types = []
    _members = {'id': Optional[Union[Integer, String]]}
    _strict = True

    def __init__(self,
                 id: Optional[Union[int, str]] = None,
                 **_kwargs: Dict[str, object]):
        super().__init__(_CONTEXT, **_kwargs)
        self.id = id


_CONTEXT.NAMESPACE = locals()

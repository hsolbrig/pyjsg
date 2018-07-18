# Auto generated from test_jsg_readme/jsg/type_directive_1.jsg by PyJSG version 0.7.0
# Generation date: 2018-07-01 17:04
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



class doc(JSGObject):
    _reference_types = []
    _members = {'a': AnyType}
    _strict = True

    def __init__(self,
                 a: object = EmptyAny,
                 **_kwargs: Dict[str, object]):
        super().__init__(_CONTEXT, **_kwargs)
        self.a = AnyType(a)


_CONTEXT.NAMESPACE = locals()

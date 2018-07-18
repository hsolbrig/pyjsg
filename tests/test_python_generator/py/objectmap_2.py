# Auto generated from JSGPython by PyJSG version 0.7.0
# Generation date: 2018-07-18 08:46
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
_CONTEXT.TYPE_EXCEPTIONS.append("Person")
_CONTEXT.TYPE_EXCEPTIONS.append("Directory")


class PNAME(JSGString):
    pattern = JSGPattern(r'[A-Z][0-9]+')


class Person(JSGObject):
    _reference_types = []
    _members = {'name': String,
                'age': Optional[Integer]}
    _strict = True

    def __init__(self,
                 name: str = None,
                 age: Optional[int] = None,
                 **_kwargs: Dict[str, object]):
        super().__init__(_CONTEXT, **_kwargs)
        self.name = name
        self.age = age


class Directory(JSGObjectMap):
    _name_filter = PNAME
    _value_type = Person

    def __init__(self,
                 **_kwargs):
        super().__init__(_CONTEXT, **_kwargs)


_CONTEXT.NAMESPACE = locals()

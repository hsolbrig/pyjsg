# Auto generated from test_jsg_readme/jsg/pd1.jsg by PyJSG version 0.7.0
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
_CONTEXT.TYPE = "id"



class person(JSGObject):
    _reference_types = []
    _members = {'name': String,
                'age': Integer}
    _strict = True

    def __init__(self,
                 name: str = None,
                 age: int = None,
                 **_kwargs: Dict[str, object]):
        super().__init__(_CONTEXT, **_kwargs)
        self.name = String(name) if name is not None else None
        self.age = Integer(age) if age is not None else None


class membership(JSGObject):
    _reference_types = []
    _members = {'list_name': String,
                'members': List[person]}
    _strict = True

    def __init__(self,
                 list_name: str = None,
                 members: List[person] = None,
                 **_kwargs: Dict[str, object]):
        super().__init__(_CONTEXT, **_kwargs)
        self.list_name = String(list_name) if list_name is not None else None
        self.members = JSGArray('members', self._context, person, 0, None, members)


_CONTEXT.NAMESPACE = locals()

# Auto generated from jsg/pd1.jsg by PyJSG version 1.0.0
# Generation date: 2017-05-15 12:03
#
from typing import Optional, Dict, List, Union, _ForwardRef

from pyjsg.jsglib.jsg import *
from pyjsg.jsglib.typing_patch import fix_forwards

# .TYPE and .IGNORE settings
_CONTEXT = JSGContext()
_CONTEXT.TYPE = "id"



class person(JSGObject):
    _reference_types = []
    
    def __init__(self,
                 name: str = None,
                 age: int = None,
                 **_kwargs: Dict[str, object]):
        self._context = _CONTEXT
        self.name = String(name)
        self.age = Integer(age)
        super().__init__(self._context, **_kwargs)


class membership(JSGObject):
    _reference_types = []
    
    def __init__(self,
                 list_name: str = None,
                 members: List[person] = None,
                 **_kwargs: Dict[str, object]):
        self._context = _CONTEXT
        self.list_name = String(list_name)
        self.members = members
        super().__init__(self._context, **_kwargs)


fix_forwards(locals())

# Auto generated from test_jsg_readme/jsg/pd3.jsg by PyJSG version 0.4.1
# Generation date: 2018-01-05 13:51
#
from typing import Optional, Dict, List, Union, _ForwardRef

from pyjsg.jsglib import jsg
from pyjsg.jsglib.jsg import isinstance_

# .TYPE and .IGNORE settings
_CONTEXT = jsg.JSGContext()
_CONTEXT.TYPE = "id"
_CONTEXT.TYPE_EXCEPTIONS.append("person")
_CONTEXT.IGNORE.append("height")
_CONTEXT.IGNORE.append("weight")
_CONTEXT.IGNORE.append("location")



class person(jsg.JSGObject):
    _reference_types = []
    _members = {'name': str,
                'age': int}
    _strict = True
    
    def __init__(self,
                 name: str = None,
                 age: int = None,
                 **_kwargs: Dict[str, object]):
        self._context = _CONTEXT
        self.name = jsg.String(name)
        self.age = jsg.Integer(age)
        super().__init__(self._context, **_kwargs)


class membership(jsg.JSGObject):
    _reference_types = []
    _members = {'list_name': str,
                'members': List[person]}
    _strict = True
    
    def __init__(self,
                 list_name: str = None,
                 members: List[person] = None,
                 **_kwargs: Dict[str, object]):
        self._context = _CONTEXT
        self.list_name = jsg.String(list_name)
        self.members = members
        super().__init__(self._context, **_kwargs)


_CONTEXT.NAMESPACE = locals()

# Auto generated from test_jsg_readme/jsg/ge1.jsg by PyJSG version 0.7.0
# Generation date: 2018-07-17 10:58
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
from pyjsg.jsglib.jsg_array import ArrayFactory
from pyjsg.jsglib.jsg_object import ObjectFactory

# .TYPE and .IGNORE settings
_CONTEXT = JSGContext()
_CONTEXT.TYPE = "type"
_CONTEXT.TYPE_EXCEPTIONS.append("person")




class _Anon1(JSGString):
    pattern = JSGPattern(r'(m)|(f)')
class details(JSGObject):
    _reference_types = []
    _members = {'id': String}
    _strict = False

    def __init__(self,
                 id: str = None,
                 **_kwargs: Dict[str, object]):
        super().__init__(_CONTEXT, **_kwargs)
        self.id = id


class person(JSGObject):
    _reference_types = [details]
    _members = {'name': String,
                'gender': _Anon1,
                'active': Boolean,
                'id': ArrayFactory('{name}', _CONTEXT, String, 0, None)}
    _strict = True

    def __init__(self,
                 name: str = None,
                 gender: str = None,
                 active: bool = None,
                 id: str = None,
                 **_kwargs: Dict[str, object]):
        super().__init__(_CONTEXT, **_kwargs)
        self.name = name
        self.gender = gender
        self.active = active
        self.id = id


class company(JSGObject):
    _reference_types = []
    _members = {'name': String,
                'year founded': Optional[Integer],
                'employees': ArrayFactory('employees', _CONTEXT, person, 2, None)}
    _strict = True

    def __init__(self,
                 name: str = None,
                 employees: List[person] = None,
                 **_kwargs: Dict[str, object]):
        super().__init__(_CONTEXT, **_kwargs)
        self.name = name
        setattr(self, 'year founded', _kwargs.get('year founded', None))
        self.employees = employees


_CONTEXT.NAMESPACE = locals()

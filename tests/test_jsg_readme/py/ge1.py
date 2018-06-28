# Auto generated from test_jsg_readme/jsg/ge1.jsg by PyJSG version 0.7.0
# Generation date: 2018-06-28 11:40
#
import sys
from typing import Optional, Dict, List, Union
if sys.version_info < (3, 7):
    from typing import _ForwardRef as ForwardRef
    from pyjsg.jsglib import typing_patch_36
else:
    from typing import ForwardRef
    from pyjsg.jsglib import typing_patch_37

from pyjsg.jsglib import *
from pyjsg.jsglib.jsg import isinstance_

# .TYPE and .IGNORE settings
_CONTEXT = JSGContext()
_CONTEXT.TYPE = "type"
_CONTEXT.TYPE_EXCEPTIONS.append("person")




class _Anon1(JSGString):
    pattern = JSGPattern(r'(m)|(f)')

class details(JSGObject):
    _reference_types = []
    _members = {'id': str}
    _strict = False
    
    def __init__(self,
                 id: str = None,
                 **_kwargs: Dict[str, object]):
        self._context = _CONTEXT
        self.id = String(id)
        super().__init__(self._context, **_kwargs)


class person(JSGObject):
    _reference_types = [details]
    _members = {'name': str,
                'gender': _Anon1,
                'active': bool,
                'details': List[details]}
    _strict = True
    
    def __init__(self,
                 name: str = None,
                 gender: _Anon1 = None,
                 active: bool = None,
                 details: List[details] = None,
                 **_kwargs: Dict[str, object]):
        self._context = _CONTEXT
        self.name = String(name)
        self.gender = gender
        self.active = Boolean(active)
        self.details = details
        super().__init__(self._context, **_kwargs)


class company(JSGObject):
    _reference_types = []
    _members = {'name': str,
                'year founded': Optional[int],
                'employees': List[person]}
    _strict = True
    
    def __init__(self,
                 name: str = None,
                 employees: List[person] = None,
                 **_kwargs: Dict[str, object]):
        self._context = _CONTEXT
        self.name = String(name)
        setattr(self, 'year founded', Integer(_kwargs.pop('year founded', None)))
        self.employees = JSGArray('employees', _CONTEXT, person, 2, None, employees)
        super().__init__(self._context, **_kwargs)


_CONTEXT.NAMESPACE = locals()

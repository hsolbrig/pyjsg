# Auto generated from jsg/ge1.jsg by PyJSG version 1.0.0
# Generation date: 2017-05-15 12:43
#
from typing import Optional, Dict, List, Union, _ForwardRef

from pyjsg.jsglib.jsg import *
from pyjsg.jsglib.typing_patch import fix_forwards

# .TYPE and .IGNORE settings
_CONTEXT = JSGContext()
_CONTEXT.TYPE = "type"
_CONTEXT.TYPE_EXCEPTIONS.append("person")




class _Anon1(JSGString):
    pattern = JSGPattern(r'(m)|(f)')

class details(JSGObject):
    _reference_types = []
    
    def __init__(self,
                 type: str = None,
                 **_kwargs: Dict[str, object]):
        self._context = _CONTEXT
        self.type = String(type)
        super().__init__(self._context, **_kwargs)


class person(JSGObject):
    _reference_types = []
    
    def __init__(self,
                 name: str = None,
                 gender: _Anon1 = None,
                 active: bool = None,
                 **_kwargs: Dict[str, object]):
        self._context = _CONTEXT
        self.name = String(name)
        self.gender = gender
        self.active = Boolean(active)
        super().__init__(self._context, **_kwargs)


class company(JSGObject):
    _reference_types = []
    
    def __init__(self,
                 name: str = None,
                 employees: List[person] = None,
                 **_kwargs: Dict[str, object]):
        self._context = _CONTEXT
        self.name = String(name)
        setattr(self, 'year founded', Integer(_kwargs.pop('year founded')))
        self.employees = employees
        super().__init__(self._context, **_kwargs)


fix_forwards(locals())

# Auto generated from test_jsg_readme/jsg/ge1.jsg by PyJSG version 0.4.2
# Generation date: 2018-01-05 13:56
#
from typing import Optional, Dict, List, Union, _ForwardRef

from pyjsg.jsglib import jsg
from pyjsg.jsglib.jsg import isinstance_

# .TYPE and .IGNORE settings
_CONTEXT = jsg.JSGContext()
_CONTEXT.TYPE = "type"
_CONTEXT.TYPE_EXCEPTIONS.append("person")




class _Anon1(jsg.JSGString):
    pattern = jsg.JSGPattern(r'(m)|(f)')

class details(jsg.JSGObject):
    _reference_types = []
    _members = {'id': str}
    _strict = False
    
    def __init__(self,
                 id: str = None,
                 **_kwargs: Dict[str, object]):
        self._context = _CONTEXT
        self.id = jsg.String(id)
        super().__init__(self._context, **_kwargs)


class person(jsg.JSGObject):
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
        self.name = jsg.String(name)
        self.gender = gender
        self.active = jsg.Boolean(active)
        self.details = details
        super().__init__(self._context, **_kwargs)


class company(jsg.JSGObject):
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
        self.name = jsg.String(name)
        setattr(self, 'year founded', jsg.Integer(_kwargs.pop('year founded', None)))
        self.employees = employees
        super().__init__(self._context, **_kwargs)


_CONTEXT.NAMESPACE = locals()

# Auto generated from jsg/example_3.jsg by PyJSG version 0.5.0
# Generation date: 2018-01-27 10:29
#
from typing import Optional, Dict, List, Union, _ForwardRef

from pyjsg.jsglib import jsg
from pyjsg.jsglib.jsg import isinstance_

# .TYPE and .IGNORE settings
_CONTEXT = jsg.JSGContext()
_CONTEXT.TYPE_EXCEPTIONS.append("doc")




class _Anon1(jsg.JSGString):
    pattern = jsg.JSGPattern(r'\*')


class NAME(jsg.JSGString):
    pattern = jsg.JSGPattern(r'[A-Za-z].*')


class TEMPLATE(jsg.JSGString):
    pattern = jsg.JSGPattern(r'\{.*\}')

class doc(jsg.JSGObject):
    _reference_types = []
    _members = {'street': Union[_Anon1, NAME, TEMPLATE]}
    _strict = True
    
    def __init__(self,
                 street: Union[_Anon1, NAME, TEMPLATE] = None,
                 **_kwargs: Dict[str, object]):
        self._context = _CONTEXT
        self.street = street
        super().__init__(self._context, **_kwargs)


_CONTEXT.NAMESPACE = locals()

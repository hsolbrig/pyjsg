# Auto generated from tests/jsg/example_5.jsg by PyJSG version 0.5.3
# Generation date: 2018-04-19 11:35
#
import sys
from typing import Optional, Dict, List, Union
if sys.version_info < (3, 7):
    from typing import _ForwardRef as ForwardRef
else:
    from typing import ForwardRef

from pyjsg.jsglib import jsg
from pyjsg.jsglib.jsg import isinstance_

# .TYPE and .IGNORE settings
_CONTEXT = jsg.JSGContext()
_CONTEXT.TYPE_EXCEPTIONS.append("doc")




class _Anon1(jsg.JSGString):
    pattern = jsg.JSGPattern(r'\*')


class NAME(jsg.JSGString):
    pattern = jsg.JSGPattern(r'.*')


class TEMPLATE(jsg.JSGString):
    pattern = jsg.JSGPattern(r'\{.*\}')

class doc(jsg.JSGObject):
    _reference_types = []
    _members = {'street': List[Union[_Anon1, NAME, TEMPLATE]]}
    _strict = True
    
    def __init__(self,
                 street: List[Union[_Anon1, NAME, TEMPLATE]] = None,
                 **_kwargs: Dict[str, object]):
        self._context = _CONTEXT
        self.street = street
        super().__init__(self._context, **_kwargs)


_CONTEXT.NAMESPACE = locals()

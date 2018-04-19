# Auto generated from tests/jsg/example_2.jsg by PyJSG version 0.5.3
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



class doc(jsg.JSGObject):
    _reference_types = []
    _members = {'street': str,
                'no': int}
    _strict = True
    
    def __init__(self,
                 street: str = None,
                 no: int = None,
                 **_kwargs: Dict[str, object]):
        self._context = _CONTEXT
        self.street = jsg.String(street)
        self.no = jsg.Integer(no)
        super().__init__(self._context, **_kwargs)


_CONTEXT.NAMESPACE = locals()

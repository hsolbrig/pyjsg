# Auto generated from jsg/example_2.jsg by PyJSG version 1.0.0
# Generation date: 2017-05-15 11:10
#
from typing import Optional, Dict, List, Union, _ForwardRef

from pyjsg.jsglib.jsg import *
from pyjsg.jsglib.typing_patch import fix_forwards

# .TYPE and .IGNORE settings
_CONTEXT = JSGContext()

class doc(JSGObject):
    _reference_types = []
    
    def __init__(self,
                 street: str = None,
                 no: int = None,
                 **_kwargs: Dict[str, object]):
        self._context = _CONTEXT
        self.street = String(street)
        self.no = Integer(no)
        super().__init__(self._context, **_kwargs)


fix_forwards(locals())

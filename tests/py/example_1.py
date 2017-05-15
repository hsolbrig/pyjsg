# Auto generated from jsg/example_1.jsg by PyJSG version 1.0.0
# Generation date: 2017-05-15 11:10
#
from typing import Optional, Dict, List, Union, _ForwardRef

from pyjsg.jsglib.jsg import *
from pyjsg.jsglib.typing_patch import fix_forwards

# .TYPE and .IGNORE settings
_CONTEXT = JSGContext()


class _Anon1(JSGString):
    pattern = JSGPattern(r'ready')

class doc(JSGObject):
    _reference_types = []
    
    def __init__(self,
                 status: _Anon1 = None,
                 **_kwargs: Dict[str, object]):
        self._context = _CONTEXT
        self.status = status
        super().__init__(self._context, **_kwargs)


fix_forwards(locals())

# Auto generated from test_basics/jsg/example_2.jsg by PyJSG version 0.7.0
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
_CONTEXT.TYPE_EXCEPTIONS.append("doc")



class doc(JSGObject):
    _reference_types = []
    _members = {'street': str,
                'no': int}
    _strict = True
    
    def __init__(self,
                 street: str = None,
                 no: int = None,
                 **_kwargs: Dict[str, object]):
        self._context = _CONTEXT
        self.street = String(street)
        self.no = Integer(no)
        super().__init__(self._context, **_kwargs)


_CONTEXT.NAMESPACE = locals()

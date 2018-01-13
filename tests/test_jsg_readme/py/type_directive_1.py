# Auto generated from test_jsg_readme/jsg/type_directive_1.jsg by PyJSG version 0.4.2
# Generation date: 2018-01-13 16:20
#
from typing import Optional, Dict, List, Union, _ForwardRef

from pyjsg.jsglib import jsg
from pyjsg.jsglib.jsg import isinstance_

# .TYPE and .IGNORE settings
_CONTEXT = jsg.JSGContext()
_CONTEXT.TYPE_EXCEPTIONS.append("doc")



class doc(jsg.JSGObject):
    _reference_types = []
    _members = {'a': object}
    _strict = True
    
    def __init__(self,
                 a: object = None,
                 **_kwargs: Dict[str, object]):
        self._context = _CONTEXT
        self.a = jsg.AnyType(a)
        super().__init__(self._context, **_kwargs)


_CONTEXT.NAMESPACE = locals()

# Auto generated from tests/test_basics/jsg/example_5.jsg by PyJSG version 0.7.0
# Generation date: 2018-07-18 09:39
#
import sys
from typing import Optional, Dict, List, Union, Any
from jsonasobj import JsonObj

if sys.version_info < (3, 7):
    from typing import _ForwardRef as ForwardRef
    from pyjsg.jsglib import typing_patch_36
else:
    from typing import ForwardRef
    from pyjsg.jsglib import typing_patch_37

from pyjsg.jsglib import *

# .TYPE and .IGNORE settings
_CONTEXT = JSGContext()
_CONTEXT.TYPE_EXCEPTIONS.append("doc")


class _Anon1(JSGString):
    pattern = JSGPattern(r'\*')


class NAME(JSGString):
    pattern = JSGPattern(r'.*')


class TEMPLATE(JSGString):
    pattern = JSGPattern(r'\{.*\}')


class doc(JSGObject):
    _reference_types = []
    _members = {'street': ArrayFactory('street', _CONTEXT, Union[_Anon1, NAME, TEMPLATE], 2, None)}
    _strict = True

    def __init__(self,
                 street: List[Union[str, str, str]] = None,
                 **_kwargs: Dict[str, object]):
        super().__init__(_CONTEXT, **_kwargs)
        self.street = street


_CONTEXT.NAMESPACE = locals()

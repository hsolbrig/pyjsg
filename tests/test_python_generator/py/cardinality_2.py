# Auto generated from JSGPython by PyJSG version 0.7.0
# Generation date: 2018-07-17 11:12
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


class doc(JSGObject):
    _reference_types = []
    _members = {'opt': Optional[String],
                'req': String,
                'l0n': ArrayFactory('l0n', _CONTEXT, String, 0, None),
                'l1n': ArrayFactory('l1n', _CONTEXT, String, 1, None),
                'l01': ArrayFactory('l01', _CONTEXT, String, 0, 1),
                'l11': ArrayFactory('l11', _CONTEXT, String, 0, None),
                'l0na': ArrayFactory('l0na', _CONTEXT, String, 0, None),
                'l1na': ArrayFactory('l1na', _CONTEXT, String, 1, None),
                'optl0n': Optional[ArrayFactory('optl0n', _CONTEXT, String, 0, None)],
                'optl1n': Optional[ArrayFactory('optl1n', _CONTEXT, String, 1, None)]}
    _strict = True

    def __init__(self,
                 opt: Optional[str] = None,
                 req: str = None,
                 l0n: List[str] = None,
                 l1n: List[str] = None,
                 l01: List[str] = None,
                 l11: List[str] = None,
                 l0na: List[str] = None,
                 l1na: List[str] = None,
                 optl0n: Optional[List[str]] = None,
                 optl1n: Optional[List[str]] = None,
                 **_kwargs: Dict[str, object]):
        super().__init__(_CONTEXT, **_kwargs)
        self.opt = opt
        self.req = req
        self.l0n = l0n
        self.l1n = l1n
        self.l01 = l01
        self.l11 = l11
        self.l0na = l0na
        self.l1na = l1na
        self.optl0n = optl0n
        self.optl1n = optl1n


_CONTEXT.NAMESPACE = locals()

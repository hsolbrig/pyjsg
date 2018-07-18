# Auto generated from tests/test_basics/jsg/list_options.jsg by PyJSG version 0.7.0
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
_CONTEXT.TYPE_EXCEPTIONS.append("list_eval")


class INT(JSGString):
    pattern = JSGPattern(r'[0-9]')


class list_eval(JSGObject):
    _reference_types = []
    _members = {'req': INT,
                'opt': Optional[INT],
                'zero_or_more': ArrayFactory('zero_or_more', _CONTEXT, INT, 0, None),
                'one_or_more': ArrayFactory('one_or_more', _CONTEXT, INT, 1, None),
                'two_or_more': ArrayFactory('two_or_more', _CONTEXT, INT, 2, None),
                'three_or_four': ArrayFactory('three_or_four', _CONTEXT, INT, 3, 4),
                'one_or_more_v2': ArrayFactory('one_or_more_v2', _CONTEXT, INT, 1, None)}
    _strict = True

    def __init__(self,
                 req: str = None,
                 opt: Optional[str] = None,
                 zero_or_more: List[str] = None,
                 one_or_more: List[str] = None,
                 two_or_more: List[str] = None,
                 three_or_four: List[str] = None,
                 one_or_more_v2: List[str] = None,
                 **_kwargs: Dict[str, object]):
        super().__init__(_CONTEXT, **_kwargs)
        self.req = req
        self.opt = opt
        self.zero_or_more = zero_or_more
        self.one_or_more = one_or_more
        self.two_or_more = two_or_more
        self.three_or_four = three_or_four
        self.one_or_more_v2 = one_or_more_v2


_CONTEXT.NAMESPACE = locals()

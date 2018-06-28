# Auto generated from test_basics/jsg/list_options.jsg by PyJSG version 0.7.0
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
_CONTEXT.TYPE_EXCEPTIONS.append("list_eval")




class INT(JSGString):
    pattern = JSGPattern(r'[0-9]')

class list_eval(JSGObject):
    _reference_types = []
    _members = {'req': INT,
                'opt': Optional[INT],
                'zero_or_more': List[INT],
                'one_or_more': List[INT],
                'two_or_more': List[INT],
                'three_or_four': List[INT],
                'one_or_more_v2': List[INT]}
    _strict = True
    
    def __init__(self,
                 req: INT = None,
                 opt: Optional[INT] = None,
                 zero_or_more: List[INT] = None,
                 one_or_more: List[INT] = None,
                 two_or_more: List[INT] = None,
                 three_or_four: List[INT] = None,
                 one_or_more_v2: List[INT] = None,
                 **_kwargs: Dict[str, object]):
        self._context = _CONTEXT
        self.req = req
        self.opt = opt
        self.zero_or_more = JSGArray('zero_or_more', _CONTEXT, INT, 0, None, zero_or_more)
        self.one_or_more = JSGArray('one_or_more', _CONTEXT, INT, 1, None, one_or_more)
        self.two_or_more = JSGArray('two_or_more', _CONTEXT, INT, 2, None, two_or_more)
        self.three_or_four = JSGArray('three_or_four', _CONTEXT, INT, 3, 4, three_or_four)
        self.one_or_more_v2 = JSGArray('one_or_more_v2', _CONTEXT, INT, 1, None, one_or_more_v2)
        super().__init__(self._context, **_kwargs)


_CONTEXT.NAMESPACE = locals()

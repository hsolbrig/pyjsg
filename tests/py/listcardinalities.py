# Auto generated from jsg/listcardinalities.jsg by PyJSG version 0.5.2
# Generation date: 2018-01-28 17:28
#
from typing import Optional, Dict, List, Union, _ForwardRef

from pyjsg.jsglib import jsg
from pyjsg.jsglib.jsg import isinstance_

# .TYPE and .IGNORE settings
_CONTEXT = jsg.JSGContext()
_CONTEXT.TYPE_EXCEPTIONS.append("list_eval")




class INT(jsg.JSGString):
    pattern = jsg.JSGPattern(r'[0-9]')

class list_eval(jsg.JSGObject):
    _reference_types = []
    _members = {'req': INT,
                'opt': Optional[INT],
                'none': None,
                'zero_or_more': List[INT],
                'one_or_more': List[INT],
                'two_or_more': List[INT],
                'three_or_four': List[INT],
                'one_or_more_v2': List[INT]}
    _strict = True
    
    def __init__(self,
                 req: INT = None,
                 opt: Optional[INT] = None,
                 none: None = None,
                 zero_or_more: List[INT] = None,
                 one_or_more: List[INT] = None,
                 two_or_more: List[INT] = None,
                 three_or_four: List[INT] = None,
                 one_or_more_v2: List[INT] = None,
                 **_kwargs: Dict[str, object]):
        self._context = _CONTEXT
        self.req = req
        self.opt = opt
        self.none = none
        self.zero_or_more = zero_or_more
        self.one_or_more = one_or_more
        self.two_or_more = two_or_more
        self.three_or_four = three_or_four
        self.one_or_more_v2 = one_or_more_v2
        super().__init__(self._context, **_kwargs)


_CONTEXT.NAMESPACE = locals()

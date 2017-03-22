# Auto generated from jsg/list_options.jsg by PyJSG version 0.1.0-DEV
# Generation date: 2017-03-22 13:51
#
from typing import Optional, Dict, List, Union, _ForwardRef

from jsglib.jsg import JSGString, JSGPattern, JSGObject, JSGContext
from jsglib.typing_patch import fix_forwards

# .TYPE and .IGNORE settings
_CONTEXT = JSGContext()






class INT(JSGString):
    pattern = JSGPattern(r'[0-9]')

class list_eval(JSGObject):
    def __init__(self,
                 req: INT = None,
                 opt: Optional[INT] = None,
                 zero_or_more: List[INT] = None,
                 one_or_more: List[INT] = None,
                 two_or_more: List[INT] = None,
                 three_or_four: List[INT] = None,
                 one_or_more_v2: List[INT] = None,
                 **_: Dict[str, object]):
        JSGObject.__init__(self, _CONTEXT)
        self.req = req
        self.opt = opt
        self.zero_or_more = zero_or_more
        self.one_or_more = one_or_more
        self.two_or_more = two_or_more
        self.three_or_four = three_or_four
        self.one_or_more_v2 = one_or_more_v2


fix_forwards(globals())

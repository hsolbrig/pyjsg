# Auto generated from jsg/example_5.jsg by PyJSG version 0.1.0-DEV
# Generation date: 2017-03-22 18:52
#
from typing import Optional, Dict, List, Union, _ForwardRef

from jsglib.jsg import JSGString, JSGPattern, JSGObject, JSGContext
from jsglib.typing_patch import fix_forwards

# .TYPE and .IGNORE settings
_CONTEXT = JSGContext()






class _A1(JSGString):
    pattern = JSGPattern(r'\*')


class NAME(JSGString):
    pattern = JSGPattern(r'.*')


class TEMPLATE(JSGString):
    pattern = JSGPattern(r'\{.*\}')

class doc(JSGObject):
    def __init__(self,
                 street: List[Union[_A1, NAME, TEMPLATE]] = None,
                 **_extra: Dict[str, object]):
        JSGObject.__init__(self, _CONTEXT, **_extra)
        self.street = street


fix_forwards(globals())

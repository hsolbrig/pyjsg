# Auto generated from jsg/example_2.jsg by PyJSG version 0.1.0-DEV
# Generation date: 2017-03-22 13:51
#
from typing import Optional, Dict, List, Union, _ForwardRef

from jsglib.jsg import JSGString, JSGPattern, JSGObject, JSGContext
from jsglib.typing_patch import fix_forwards

# .TYPE and .IGNORE settings
_CONTEXT = JSGContext()






class NAME(JSGString):
    pattern = JSGPattern(r'.*')


class NUM(JSGString):
    pattern = JSGPattern(r'[0-9]+[a-e]?')

class doc(JSGObject):
    def __init__(self,
                 street: NAME = None,
                 no: NUM = None,
                 **_: Dict[str, object]):
        JSGObject.__init__(self, _CONTEXT)
        self.street = street
        self.no = no


fix_forwards(globals())

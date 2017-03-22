# Auto generated from jsg/example_1.jsg by PyJSG version 0.1.0-DEV
# Generation date: 2017-03-22 18:52
#
from typing import Optional, Dict, List, Union, _ForwardRef

from jsglib.jsg import JSGString, JSGPattern, JSGObject, JSGContext
from jsglib.typing_patch import fix_forwards

# .TYPE and .IGNORE settings
_CONTEXT = JSGContext()





class doc(JSGObject):
    def __init__(self,
                 status: str = None,
                 **_extra: Dict[str, object]):
        JSGObject.__init__(self, _CONTEXT, **_extra)
        self.status = "ready"


fix_forwards(globals())

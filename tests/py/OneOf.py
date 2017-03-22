# Auto generated from jsg/OneOf.jsg by PyJSG version 0.1.0-DEV
# Generation date: 2017-03-22 13:51
#
from typing import Optional, Dict, List, Union, _ForwardRef

from jsglib.jsg import JSGString, JSGPattern, JSGObject, JSGContext
from jsglib.typing_patch import fix_forwards

# .TYPE and .IGNORE settings
_CONTEXT = JSGContext()




OneOft_ = _ForwardRef('OneOf')


class IRI(JSGString):
    pattern = JSGPattern(r'[0-9]')


class BNODE(JSGString):
    pattern = JSGPattern(r'[0-9]')


class INTEGER(JSGString):
    pattern = JSGPattern(r'[0-9]')


class _A1(JSGString):
    pattern = JSGPattern(r'unbounded')

class EachOf(JSGObject):
    def __init__(self,
                 **_: Dict[str, object]):
        JSGObject.__init__(self, _CONTEXT)
        


class TripleConstraint(JSGObject):
    def __init__(self,
                 **_: Dict[str, object]):
        JSGObject.__init__(self, _CONTEXT)
        


class OneOf(JSGObject):
    def __init__(self,
                 id: Optional[Union[IRI, BNODE]] = None,
                 expressions: List[Union[EachOf, OneOft_, IRI, BNODE]] = None,
                 min: Optional[INTEGER] = None,
                 max: Optional[Union[_A1, INTEGER]] = None,
                 **_: Dict[str, object]):
        JSGObject.__init__(self, _CONTEXT)
        self.id = id
        self.expressions = expressions
        self.min = min
        self.max = max


fix_forwards(globals())
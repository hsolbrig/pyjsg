# Auto generated from jsg/StemRange.jsg by PyJSG version 0.1.0-DEV
# Generation date: 2017-03-22 13:51
#
from typing import Optional, Dict, List, Union, _ForwardRef

from jsglib.jsg import JSGString, JSGPattern, JSGObject, JSGContext
from jsglib.typing_patch import fix_forwards

# .TYPE and .IGNORE settings
_CONTEXT = JSGContext()






class IRI(JSGString):
    pattern = JSGPattern(r'[a-z]')


class STRING(JSGString):
    pattern = JSGPattern(r'[a-z]')

class Wildcard(JSGObject):
    def __init__(self,
                 **_: Dict[str, object]):
        JSGObject.__init__(self, _CONTEXT)
        


class ObjectLiteral(JSGObject):
    def __init__(self,
                 value: STRING = None,
                 language: Optional[STRING] = None,
                 type: Optional[STRING] = None,
                 **_: Dict[str, object]):
        JSGObject.__init__(self, _CONTEXT)
        self.value = value
        self.language = language
        self.type = type


class Stem(JSGObject):
    def __init__(self,
                 stem: IRI = None,
                 **_: Dict[str, object]):
        JSGObject.__init__(self, _CONTEXT)
        self.stem = stem


class StemRange(JSGObject):
    def __init__(self,
                 stem: Union[IRI, Wildcard] = None,
                 exclusions: Optional[List[Union[IRI, ObjectLiteral, Stem]]] = None,
                 **_: Dict[str, object]):
        JSGObject.__init__(self, _CONTEXT)
        self.stem = stem
        self.exclusions = exclusions


fix_forwards(globals())

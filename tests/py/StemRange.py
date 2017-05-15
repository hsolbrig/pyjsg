# Auto generated from jsg/StemRange.jsg by PyJSG version 1.0.0
# Generation date: 2017-05-15 11:10
#
from typing import Optional, Dict, List, Union, _ForwardRef

from pyjsg.jsglib.jsg import *
from pyjsg.jsglib.typing_patch import fix_forwards

# .TYPE and .IGNORE settings
_CONTEXT = JSGContext()


class IRI(String):
    pattern = JSGPattern(r'')

class Wildcard(JSGObject):
    _reference_types = []
    
    def __init__(self,
                 **_kwargs: Dict[str, object]):
        self._context = _CONTEXT
        super().__init__(self._context, **_kwargs)


class ObjectLiteral(JSGObject):
    _reference_types = []
    
    def __init__(self,
                 value: str = None,
                 language: Optional[str] = None,
                 type: Optional[str] = None,
                 **_kwargs: Dict[str, object]):
        self._context = _CONTEXT
        self.value = String(value)
        self.language = String(language)
        self.type = String(type)
        super().__init__(self._context, **_kwargs)


objectValue = Union[IRI, ObjectLiteral]

class Stem(JSGObject):
    _reference_types = []
    
    def __init__(self,
                 stem: IRI = None,
                 **_kwargs: Dict[str, object]):
        self._context = _CONTEXT
        self.stem = stem
        super().__init__(self._context, **_kwargs)


class StemRange(JSGObject):
    _reference_types = []
    
    def __init__(self,
                 stem: Union[IRI, Wildcard] = None,
                 exclusions: Optional[List[Union[objectValue, Stem]]] = None,
                 **_kwargs: Dict[str, object]):
        self._context = _CONTEXT
        self.stem = stem
        self.exclusions = exclusions
        super().__init__(self._context, **_kwargs)


fix_forwards(locals())

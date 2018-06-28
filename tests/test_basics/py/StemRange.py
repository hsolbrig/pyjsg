# Auto generated from test_basics/jsg/StemRange.jsg by PyJSG version 0.7.0
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
_CONTEXT.TYPE_EXCEPTIONS.append("Wildcard")
_CONTEXT.TYPE_EXCEPTIONS.append("ObjectLiteral")
_CONTEXT.TYPE_EXCEPTIONS.append("Stem")
_CONTEXT.TYPE_EXCEPTIONS.append("StemRange")




class IRI(String):
    pattern = JSGPattern(r'')

class Wildcard(JSGObject):
    _reference_types = []
    _members = {}
    _strict = True
    
    def __init__(self,
                 **_kwargs: Dict[str, object]):
        self._context = _CONTEXT
        super().__init__(self._context, **_kwargs)


class ObjectLiteral(JSGObject):
    _reference_types = []
    _members = {'value': str,
                'language': Optional[str],
                'type': Optional[str]}
    _strict = True
    
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
    _members = {'stem': IRI}
    _strict = True
    
    def __init__(self,
                 stem: IRI = None,
                 **_kwargs: Dict[str, object]):
        self._context = _CONTEXT
        self.stem = stem
        super().__init__(self._context, **_kwargs)


class StemRange(JSGObject):
    _reference_types = []
    _members = {'stem': Union[IRI, Wildcard],
                'exclusions': Optional[List[Union[objectValue, Stem]]]}
    _strict = True
    
    def __init__(self,
                 stem: Union[IRI, Wildcard] = None,
                 exclusions: Optional[List[Union[objectValue, Stem]]] = None,
                 **_kwargs: Dict[str, object]):
        self._context = _CONTEXT
        self.stem = stem
        self.exclusions = exclusions
        super().__init__(self._context, **_kwargs)


_CONTEXT.NAMESPACE = locals()

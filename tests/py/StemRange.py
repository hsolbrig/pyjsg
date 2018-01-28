# Auto generated from jsg/StemRange.jsg by PyJSG version 0.5.2
# Generation date: 2018-01-28 17:28
#
from typing import Optional, Dict, List, Union, _ForwardRef

from pyjsg.jsglib import jsg
from pyjsg.jsglib.jsg import isinstance_

# .TYPE and .IGNORE settings
_CONTEXT = jsg.JSGContext()
_CONTEXT.TYPE_EXCEPTIONS.append("Wildcard")
_CONTEXT.TYPE_EXCEPTIONS.append("ObjectLiteral")
_CONTEXT.TYPE_EXCEPTIONS.append("Stem")
_CONTEXT.TYPE_EXCEPTIONS.append("StemRange")




class IRI(jsg.String):
    pattern = jsg.JSGPattern(r'')

class Wildcard(jsg.JSGObject):
    _reference_types = []
    _members = {}
    _strict = True
    
    def __init__(self,
                 **_kwargs: Dict[str, object]):
        self._context = _CONTEXT
        super().__init__(self._context, **_kwargs)


class ObjectLiteral(jsg.JSGObject):
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
        self.value = jsg.String(value)
        self.language = jsg.String(language)
        self.type = jsg.String(type)
        super().__init__(self._context, **_kwargs)


objectValue = Union[IRI, ObjectLiteral]

class Stem(jsg.JSGObject):
    _reference_types = []
    _members = {'stem': IRI}
    _strict = True
    
    def __init__(self,
                 stem: IRI = None,
                 **_kwargs: Dict[str, object]):
        self._context = _CONTEXT
        self.stem = stem
        super().__init__(self._context, **_kwargs)


class StemRange(jsg.JSGObject):
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

# Auto generated from tests/test_basics/jsg/StemRange.jsg by PyJSG version 0.7.0
# Generation date: 2018-07-18 09:39
#
import sys
from typing import Optional, Dict, List, Union, Any
from jsonasobj import JsonObj

if sys.version_info < (3, 7):
    from typing import _ForwardRef as ForwardRef
    from pyjsg.jsglib import typing_patch_36
else:
    from typing import ForwardRef
    from pyjsg.jsglib import typing_patch_37

from pyjsg.jsglib import *

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
        super().__init__(_CONTEXT, **_kwargs)


class ObjectLiteral(JSGObject):
    _reference_types = []
    _members = {'value': String,
                'language': Optional[String],
                'type': Optional[String]}
    _strict = True

    def __init__(self,
                 value: str = None,
                 language: Optional[str] = None,
                 type: Optional[str] = None,
                 **_kwargs: Dict[str, object]):
        super().__init__(_CONTEXT, **_kwargs)
        self.value = value
        self.language = language
        self.type = type



objectValue = Union[IRI, ObjectLiteral]
class Stem(JSGObject):
    _reference_types = []
    _members = {'stem': IRI}
    _strict = True

    def __init__(self,
                 stem: str = None,
                 **_kwargs: Dict[str, object]):
        super().__init__(_CONTEXT, **_kwargs)
        self.stem = stem


class StemRange(JSGObject):
    _reference_types = []
    _members = {'stem': Union[IRI, Wildcard],
                'exclusions': Optional[ArrayFactory('exclusions', _CONTEXT, Union[Union[IRI, ObjectLiteral], Stem], 1, None)]}
    _strict = True

    def __init__(self,
                 stem: Union[str, Wildcard] = None,
                 exclusions: Optional[List[Union[Union[str, ObjectLiteral], Stem]]] = None,
                 **_kwargs: Dict[str, object]):
        super().__init__(_CONTEXT, **_kwargs)
        self.stem = stem
        self.exclusions = exclusions


_CONTEXT.NAMESPACE = locals()

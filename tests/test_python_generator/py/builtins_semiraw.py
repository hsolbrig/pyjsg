# Auto generated from JSGPython by PyJSG version 0.7.0
# Generation date: 2018-07-17 11:12
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
_CONTEXT.TYPE_EXCEPTIONS.append("doc")
_CONTEXT.TYPE_EXCEPTIONS.append("another_object")


class doc(JSGObject):
    _reference_types = []
    _members = {'class': String,
                'def': Number,
                'import': Integer,
                'with': Boolean,
                'if': JSGNull,
                'else': ArrayFactory('else', _CONTEXT, AnyType, 0, None),
                'raise': ObjectFactory('raise', _CONTEXT, Object)}
    _strict = True

    def __init__(self,
                 class_: str = None,
                 def_: float = None,
                 import_: int = None,
                 with_: bool = None,
                 if_: type(None) = EmptyAny,
                 else_: list = None,
                 raise_: object = None,
                 **_kwargs: Dict[str, object]):
        super().__init__(_CONTEXT, **_kwargs)
        setattr(self, 'class', class_ if class_ is not None else _kwargs.get('class', None))
        setattr(self, 'def', def_ if def_ is not None else _kwargs.get('def', None))
        setattr(self, 'import', import_ if import_ is not None else _kwargs.get('import', None))
        setattr(self, 'with', with_ if with_ is not None else _kwargs.get('with', None))
        setattr(self, 'if', if_ if if_ is not EmptyAny else _kwargs.get('if', EmptyAny))
        setattr(self, 'else', else_ if else_ is not None else _kwargs.get('else', None))
        setattr(self, 'raise', raise_ if raise_ is not None else _kwargs.get('raise', None))


class another_object(JSGObject):
    _reference_types = []
    _members = {}
    _strict = False

    def __init__(self,
                 **_kwargs: Dict[str, object]):
        super().__init__(_CONTEXT, **_kwargs)


_CONTEXT.NAMESPACE = locals()

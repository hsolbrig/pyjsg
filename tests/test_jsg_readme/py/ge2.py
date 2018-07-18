# Auto generated from test_jsg_readme/jsg/ge2.jsg by PyJSG version 0.7.0
# Generation date: 2018-07-01 17:04
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
from pyjsg.jsglib.jsg_base import isinstance_

# .TYPE and .IGNORE settings
_CONTEXT = JSGContext()
_CONTEXT.TYPE = "id"



class empty_object(JSGObject):
    _reference_types = []
    _members = {}
    _strict = True

    def __init__(self,
                 **_kwargs: Dict[str, object]):
        super().__init__(_CONTEXT, **_kwargs)


class wild_card_object(JSGObject):
    _reference_types = []
    _members = {}
    _strict = False

    def __init__(self,
                 **_kwargs: Dict[str, object]):
        super().__init__(_CONTEXT, **_kwargs)


class closed_object(JSGObject):
    _reference_types = []
    _members = {'a': String,
                'b': Optional[Integer]}
    _strict = True

    def __init__(self,
                 a: str = None,
                 b: Optional[int] = None,
                 **_kwargs: Dict[str, object]):
        super().__init__(_CONTEXT, **_kwargs)
        self.a = String(a) if a is not None else None
        self.b = Integer(b) if b is not None else None


class open_object(JSGObject):
    _reference_types = []
    _members = {'a': String,
                'b': Optional[Integer]}
    _strict = False

    def __init__(self,
                 a: str = None,
                 b: Optional[int] = None,
                 **_kwargs: Dict[str, object]):
        super().__init__(_CONTEXT, **_kwargs)
        self.a = String(a) if a is not None else None
        self.b = Integer(b) if b is not None else None


class object_options_1_(JSGObject):
    _reference_types = []
    _members = {'a': String,
                'b': Optional[Integer]}
    _strict = True

    def __init__(self,
                 a: str = None,
                 b: Optional[int] = None,
                 **_kwargs: Dict[str, object]):
        super().__init__(_CONTEXT, **_kwargs)
        self.a = String(a) if a is not None else None
        self.b = Integer(b) if b is not None else None


class object_options_2_(JSGObject):
    _reference_types = []
    _members = {'k': JSGNull}
    _strict = False

    def __init__(self,
                 k: type(None) = EmptyAny,
                 **_kwargs: Dict[str, object]):
        super().__init__(_CONTEXT, **_kwargs)
        self.k = JSGNull(k) if k is not EmptyAny else EmptyAny


class object_options_3_(JSGObject):
    _reference_types = []
    _members = {}
    _strict = True

    def __init__(self,
                 **_kwargs: Dict[str, object]):
        super().__init__(_CONTEXT, **_kwargs)


class object_options_2_1_(JSGObject):
    _reference_types = []
    _members = {'a': String}
    _strict = True

    def __init__(self,
                 a: str = None,
                 **_kwargs: Dict[str, object]):
        super().__init__(_CONTEXT, **_kwargs)
        self.a = String(a) if a is not None else None


class object_options_2_2_(JSGObject):
    _reference_types = []
    _members = {}
    _strict = True

    def __init__(self,
                 **_kwargs: Dict[str, object]):
        super().__init__(_CONTEXT, **_kwargs)


class object_options(JSGObject):
    _reference_types = [object_options_1_, object_options_2_, object_options_3_]
    _members = {'a': String,
                'b': Optional[Integer],
                'k': JSGNull}
    _strict = True

    def __init__(self,
                 opt_: Union[object_options_1_, object_options_2_, object_options_3_] = None,
                 **_kwargs: Dict[str, object]):
        super().__init__(_CONTEXT, **_kwargs)
        self.a = String(opt_.a) if isinstance(opt_, object_options_1_) else String(None)
        self.b = Integer(opt_.b) if isinstance(opt_, object_options_1_) else Integer(None)
        self.k = JSGNull(opt_.k) if isinstance(opt_, object_options_2_) else JSGNull(None)


class object_options_2(JSGObject):
    _reference_types = [object_options_2_1_, object_options_2_2_]
    _members = {'a': String}
    _strict = True

    def __init__(self,
                 opt_: Union[object_options_2_1_, object_options_2_2_] = None,
                 **_kwargs: Dict[str, object]):
        super().__init__(_CONTEXT, **_kwargs)
        self.a = String(opt_.a) if isinstance(opt_, object_options_2_1_) else String(None)


class doc(JSGObject):
    _reference_types = []
    _members = {'e': Union[empty_object, wild_card_object, closed_object, open_object, object_options, object_options_2]}
    _strict = True

    def __init__(self,
                 e: Union[empty_object, wild_card_object, closed_object, open_object, object_options, object_options_2] = None,
                 **_kwargs: Dict[str, object]):
        super().__init__(_CONTEXT, **_kwargs)
        self.e = e


_CONTEXT.NAMESPACE = locals()

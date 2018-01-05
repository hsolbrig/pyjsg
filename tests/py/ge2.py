# Auto generated from /Users/mrf7578/Development/git/hsolbrig/pyjsg/tests/test_jsg_readme/jsg/ge2.jsg by PyJSG version 0.3.1
# Generation date: 2017-12-17 20:23
#
from typing import Optional, Dict, List, Union, _ForwardRef

from pyjsg.jsglib import jsg
from pyjsg.jsglib import typing_patch

# .TYPE and .IGNORE settings
_CONTEXT = jsg.JSGContext()
_CONTEXT.TYPE = "id"



class empty_object(jsg.JSGObject):
    _reference_types = []
    _members = {}
    _strict = True
    
    def __init__(self,
                 **_kwargs: Dict[str, object]):
        self._context = _CONTEXT
        super().__init__(self._context, **_kwargs)


class wild_card_object(jsg.JSGObject):
    _reference_types = []
    _members = {}
    _strict = False
    
    def __init__(self,
                 **_kwargs: Dict[str, object]):
        self._context = _CONTEXT
        super().__init__(self._context, **_kwargs)


class closed_object(jsg.JSGObject):
    _reference_types = []
    _members = {'a': str,
                'b': Optional[int]}
    _strict = True
    
    def __init__(self,
                 a: str = None,
                 b: Optional[int] = None,
                 **_kwargs: Dict[str, object]):
        self._context = _CONTEXT
        self.a = jsg.String(a)
        self.b = jsg.Integer(b)
        super().__init__(self._context, **_kwargs)


class open_object(jsg.JSGObject):
    _reference_types = []
    _members = {'a': str,
                'b': Optional[int]}
    _strict = False
    
    def __init__(self,
                 a: str = None,
                 b: Optional[int] = None,
                 **_kwargs: Dict[str, object]):
        self._context = _CONTEXT
        self.a = jsg.String(a)
        self.b = jsg.Integer(b)
        super().__init__(self._context, **_kwargs)


class object_options_1_(jsg.JSGObject):
    _reference_types = []
    _members = {'a': str,
                'b': Optional[int]}
    _strict = True
    
    def __init__(self,
                 a: str = None,
                 b: Optional[int] = None,
                 **_kwargs: Dict[str, object]):
        self._context = _CONTEXT
        self.a = jsg.String(a)
        self.b = jsg.Integer(b)
        super().__init__(self._context, **_kwargs)


class object_options_2_(jsg.JSGObject):
    _reference_types = []
    _members = {'k': jsg.JSGNull}
    _strict = False
    
    def __init__(self,
                 k: jsg.JSGNull = None,
                 **_kwargs: Dict[str, object]):
        self._context = _CONTEXT
        self.k = jsg.JSGNull(k)
        super().__init__(self._context, **_kwargs)


class object_options_3_(jsg.JSGObject):
    _reference_types = []
    _members = {}
    _strict = True
    
    def __init__(self,
                 **_kwargs: Dict[str, object]):
        self._context = _CONTEXT
        super().__init__(self._context, **_kwargs)


class object_options_2_1_(jsg.JSGObject):
    _reference_types = []
    _members = {'a': str}
    _strict = True
    
    def __init__(self,
                 a: str = None,
                 **_kwargs: Dict[str, object]):
        self._context = _CONTEXT
        self.a = jsg.String(a)
        super().__init__(self._context, **_kwargs)


class object_options_2_2_(jsg.JSGObject):
    _reference_types = []
    _members = {}
    _strict = True
    
    def __init__(self,
                 **_kwargs: Dict[str, object]):
        self._context = _CONTEXT
        super().__init__(self._context, **_kwargs)


class object_options(jsg.JSGObject):
    _reference_types = [object_options_1_, object_options_2_, object_options_3_]
    _members = {'a': str,
                'b': Optional[int],
                'k': jsg.JSGNull}
    _strict = True
    
    def __init__(self,
                 opt_: Union[object_options_1_, object_options_2_, object_options_3_] = None,
                 **_kwargs: Dict[str, object]):
        self._context = _CONTEXT
        self.a = jsg.String(opt_.a) if isinstance(opt_, object_options_1_) else jsg.String(None)
        self.b = jsg.Integer(opt_.b) if opt_ else jsg.Integer(None) if isinstance(opt_, object_options_1_) else jsg.Integer(None)
        self.k = jsg.JSGNull(opt_.k) if isinstance(opt_, object_options_2_) else jsg.JSGNull(None)
        super().__init__(self._context, **_kwargs)


class object_options_2(jsg.JSGObject):
    _reference_types = [object_options_2_1_, object_options_2_2_]
    _members = {'a': str}
    _strict = True
    
    def __init__(self,
                 opt_: Union[object_options_2_1_, object_options_2_2_] = None,
                 **_kwargs: Dict[str, object]):
        self._context = _CONTEXT
        self.a = jsg.String(opt_.a) if isinstance(opt_, object_options_2_1_) else jsg.String(None)
        super().__init__(self._context, **_kwargs)


class doc(jsg.JSGObject):
    _reference_types = []
    _members = {'e': Union[empty_object, wild_card_object, closed_object, open_object, object_options, object_options_2]}
    _strict = True
    
    def __init__(self,
                 e: Union[empty_object, wild_card_object, closed_object, open_object, object_options, object_options_2] = None,
                 **_kwargs: Dict[str, object]):
        self._context = _CONTEXT
        self.e = e
        super().__init__(self._context, **_kwargs)


_CONTEXT.NAMESPACE = locals()

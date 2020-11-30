import typing
import pyjsg.jsglib as jsg

# .TYPE and .IGNORE settings
_CONTEXT = jsg.JSGContext()
_CONTEXT.TYPE = "id"


class empty_object(jsg.JSGObject):
    _reference_types = []
    _members = {}
    _strict = True

    def __init__(self,
                 **_kwargs: typing.Dict[str, object]):
        super().__init__(_CONTEXT, **_kwargs)



class wild_card_object(jsg.JSGObject):
    _reference_types = []
    _members = {}
    _strict = False

    def __init__(self,
                 **_kwargs: typing.Dict[str, object]):
        super().__init__(_CONTEXT, **_kwargs)



class closed_object(jsg.JSGObject):
    _reference_types = []
    _members = {'a': jsg.String,
                'b': typing.Optional[jsg.Integer]}
    _strict = True

    def __init__(self,
                 a: str = None,
                 b: typing.Optional[int] = None,
                 **_kwargs: typing.Dict[str, object]):
        super().__init__(_CONTEXT, **_kwargs)
        self.a = a
        self.b = b



class open_object(jsg.JSGObject):
    _reference_types = []
    _members = {'a': jsg.String,
                'b': typing.Optional[jsg.Integer]}
    _strict = False

    def __init__(self,
                 a: str = None,
                 b: typing.Optional[int] = None,
                 **_kwargs: typing.Dict[str, object]):
        super().__init__(_CONTEXT, **_kwargs)
        self.a = a
        self.b = b



class object_options_1_(jsg.JSGObject):
    _reference_types = []
    _members = {'a': jsg.String,
                'b': typing.Optional[jsg.Integer]}
    _strict = True

    def __init__(self,
                 a: str = None,
                 b: typing.Optional[int] = None,
                 **_kwargs: typing.Dict[str, object]):
        super().__init__(_CONTEXT, **_kwargs)
        self.a = a
        self.b = b



class object_options_2_(jsg.JSGObject):
    _reference_types = []
    _members = {'k': jsg.JSGNull}
    _strict = False

    def __init__(self,
                 k: type(None) = jsg.Empty,
                 **_kwargs: typing.Dict[str, object]):
        super().__init__(_CONTEXT, **_kwargs)
        self.k = k



class object_options_3_(jsg.JSGObject):
    _reference_types = []
    _members = {}
    _strict = True

    def __init__(self,
                 **_kwargs: typing.Dict[str, object]):
        super().__init__(_CONTEXT, **_kwargs)



class object_options_2_1_(jsg.JSGObject):
    _reference_types = []
    _members = {'a': jsg.String}
    _strict = True

    def __init__(self,
                 a: str = None,
                 **_kwargs: typing.Dict[str, object]):
        super().__init__(_CONTEXT, **_kwargs)
        self.a = a



class object_options_2_2_(jsg.JSGObject):
    _reference_types = []
    _members = {}
    _strict = True

    def __init__(self,
                 **_kwargs: typing.Dict[str, object]):
        super().__init__(_CONTEXT, **_kwargs)



class object_options(jsg.JSGObject):
    _reference_types = [object_options_1_, object_options_2_, object_options_3_]
    _members = {'a': typing.Optional[jsg.String],
                'b': typing.Optional[jsg.Integer],
                'k': typing.Optional[jsg.JSGNull]}
    _strict = True

    def __init__(self,
                 opts_: typing.Union[object_options_1_, object_options_2_, object_options_3_] = None,
                 **_kwargs: typing.Dict[str, object]):
        super().__init__(_CONTEXT, **_kwargs)
        if opts_ is not None:
            if isinstance(opts_, object_options_1_):
                self.a = opts_.a
                self.b = opts_.b
            elif isinstance(opts_, object_options_2_):
                self.k = opts_.k
            elif isinstance(opts_, object_options_3_):
                pass
            else:
                raise ValueError(f"Unrecognized value type: {opts_}")



class object_options_2(jsg.JSGObject):
    _reference_types = [object_options_2_1_, object_options_2_2_]
    _members = {'a': typing.Optional[jsg.String]}
    _strict = True

    def __init__(self,
                 opts_: typing.Union[object_options_2_1_, object_options_2_2_] = None,
                 **_kwargs: typing.Dict[str, object]):
        super().__init__(_CONTEXT, **_kwargs)
        if opts_ is not None:
            if isinstance(opts_, object_options_2_1_):
                self.a = opts_.a
            elif isinstance(opts_, object_options_2_2_):
                pass
            else:
                raise ValueError(f"Unrecognized value type: {opts_}")



class doc(jsg.JSGObject):
    _reference_types = []
    _members = {'e': typing.Union[empty_object, wild_card_object, closed_object, open_object, object_options, object_options_2]}
    _strict = True

    def __init__(self,
                 e: typing.Union[empty_object, wild_card_object, closed_object, open_object, object_options, object_options_2] = None,
                 **_kwargs: typing.Dict[str, object]):
        super().__init__(_CONTEXT, **_kwargs)
        self.e = e


_CONTEXT.NAMESPACE = locals()

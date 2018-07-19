# Auto generated from JSGPython by PyJSG version 0.7b2
# Generation date: 2018-07-18 18:06
#
import typing
import pyjsg.jsglib as jsg

# .TYPE and .IGNORE settings
_CONTEXT = jsg.JSGContext()
_CONTEXT.TYPE_EXCEPTIONS.append("l")


class l(jsg.JSGObject):
    _reference_types = []
    _members = {'e': jsg.ArrayFactory('e', _CONTEXT, jsg.String, 1, None)}
    _strict = True

    def __init__(self,
                 e: typing.List[str] = None,
                 **_kwargs: typing.Dict[str, object]):
        super().__init__(_CONTEXT, **_kwargs)
        self.e = e


_CONTEXT.NAMESPACE = locals()

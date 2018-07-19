# Auto generated from JSGPython by PyJSG version 0.7b2
# Generation date: 2018-07-18 18:06
#
import typing
import pyjsg.jsglib as jsg

# .TYPE and .IGNORE settings
_CONTEXT = jsg.JSGContext()
_CONTEXT.TYPE_EXCEPTIONS.append("doc")


class doc(jsg.JSGObject):
    _reference_types = []
    _members = {'status': jsg.AnyType}
    _strict = True

    def __init__(self,
                 status: object = jsg.EmptyAny,
                 **_kwargs: typing.Dict[str, object]):
        super().__init__(_CONTEXT, **_kwargs)
        self.status = status


_CONTEXT.NAMESPACE = locals()

# Auto generated from test_basics/jsg/example_2.jsg by PyJSG version 0.8b1
# Generation date: 2018-08-01 15:41
#
import typing
import pyjsg.jsglib as jsg

# .TYPE and .IGNORE settings
_CONTEXT = jsg.JSGContext()
_CONTEXT.TYPE_EXCEPTIONS.append("doc")


class doc(jsg.JSGObject):
    _reference_types = []
    _members = {'street': jsg.String,
                'no': jsg.Integer}
    _strict = True

    def __init__(self,
                 street: str = None,
                 no: int = None,
                 **_kwargs: typing.Dict[str, object]):
        super().__init__(_CONTEXT, **_kwargs)
        self.street = street
        self.no = no


_CONTEXT.NAMESPACE = locals()

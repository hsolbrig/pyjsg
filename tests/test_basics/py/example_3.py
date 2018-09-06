# Auto generated from test_basics/jsg/example_3.jsg by PyJSG version 0.8b3
# Generation date: 2018-09-06 13:05
#
import typing
import pyjsg.jsglib as jsg

# .TYPE and .IGNORE settings
_CONTEXT = jsg.JSGContext()
_CONTEXT.TYPE_EXCEPTIONS.append("doc")


class _Anon1(jsg.JSGString):
    pattern = jsg.JSGPattern(r'\*')


class NAME(jsg.JSGString):
    pattern = jsg.JSGPattern(r'[A-Za-z].*')


class TEMPLATE(jsg.JSGString):
    pattern = jsg.JSGPattern(r'\{.*\}')


class doc(jsg.JSGObject):
    _reference_types = []
    _members = {'street': typing.Union[_Anon1, NAME, TEMPLATE]}
    _strict = True

    def __init__(self,
                 street: typing.Union[str, str, str] = None,
                 **_kwargs: typing.Dict[str, object]):
        super().__init__(_CONTEXT, **_kwargs)
        self.street = street


_CONTEXT.NAMESPACE = locals()

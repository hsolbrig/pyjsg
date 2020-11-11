# Auto generated from tests/test_basics/jsg/example_5.jsg by PyJSG version 0.10.0
# Generation date: 2020-11-11 10:23
#
import typing
import pyjsg.jsglib as jsg

# .TYPE and .IGNORE settings
_CONTEXT = jsg.JSGContext()
_CONTEXT.TYPE_EXCEPTIONS.append("doc")


class _Anon1(jsg.JSGString):
    pattern = jsg.JSGPattern(r'\*')


class NAME(jsg.JSGString):
    pattern = jsg.JSGPattern(r'.*')


class TEMPLATE(jsg.JSGString):
    pattern = jsg.JSGPattern(r'\{.*\}')


class doc(jsg.JSGObject):
    _reference_types = []
    _members = {'street': jsg.ArrayFactory('street', _CONTEXT, typing.Union[_Anon1, NAME, TEMPLATE], 2, None)}
    _strict = True

    def __init__(self,
                 street: typing.List[typing.Union[str, str, str]] = None,
                 **_kwargs: typing.Dict[str, object]):
        super().__init__(_CONTEXT, **_kwargs)
        self.street = street


_CONTEXT.NAMESPACE = locals()

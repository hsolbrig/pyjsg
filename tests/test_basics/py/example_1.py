# Auto generated from test_basics/jsg/example_1.jsg by PyJSG version 0.7b2
# Generation date: 2018-07-23 12:17
#
import typing
import pyjsg.jsglib as jsg

# .TYPE and .IGNORE settings
_CONTEXT = jsg.JSGContext()
_CONTEXT.TYPE_EXCEPTIONS.append("doc")


class _Anon1(jsg.JSGString):
    pattern = jsg.JSGPattern(r'ready')


class doc(jsg.JSGObject):
    _reference_types = []
    _members = {'status': _Anon1}
    _strict = True

    def __init__(self,
                 status: str = None,
                 **_kwargs: typing.Dict[str, object]):
        super().__init__(_CONTEXT, **_kwargs)
        self.status = status


_CONTEXT.NAMESPACE = locals()

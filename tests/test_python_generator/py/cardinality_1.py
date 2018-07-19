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
    _members = {'opt': typing.Optional[jsg.AnyType],
                'req': jsg.AnyType,
                'l0n': jsg.ArrayFactory('l0n', _CONTEXT, jsg.AnyType, 0, None),
                'l1n': jsg.ArrayFactory('l1n', _CONTEXT, jsg.AnyType, 1, None),
                'l01': jsg.ArrayFactory('l01', _CONTEXT, jsg.AnyType, 0, 1),
                'l11': jsg.ArrayFactory('l11', _CONTEXT, jsg.AnyType, 1, 1),
                'l0na': jsg.ArrayFactory('l0na', _CONTEXT, jsg.AnyType, 0, None),
                'l1na': jsg.ArrayFactory('l1na', _CONTEXT, jsg.AnyType, 1, None),
                'optl0n': typing.Optional[jsg.ArrayFactory('optl0n', _CONTEXT, jsg.AnyType, 0, None)],
                'optl1n': typing.Optional[jsg.ArrayFactory('optl1n', _CONTEXT, jsg.AnyType, 1, None)]}
    _strict = True

    def __init__(self,
                 opt: typing.Optional[object] = jsg.EmptyAny,
                 req: object = jsg.EmptyAny,
                 l0n: typing.List[object] = None,
                 l1n: typing.List[object] = None,
                 l01: typing.List[object] = None,
                 l11: typing.List[object] = None,
                 l0na: typing.List[object] = None,
                 l1na: typing.List[object] = None,
                 optl0n: typing.Optional[typing.List[object]] = None,
                 optl1n: typing.Optional[typing.List[object]] = None,
                 **_kwargs: typing.Dict[str, object]):
        super().__init__(_CONTEXT, **_kwargs)
        self.opt = opt
        self.req = req
        self.l0n = l0n
        self.l1n = l1n
        self.l01 = l01
        self.l11 = l11
        self.l0na = l0na
        self.l1na = l1na
        self.optl0n = optl0n
        self.optl1n = optl1n


_CONTEXT.NAMESPACE = locals()

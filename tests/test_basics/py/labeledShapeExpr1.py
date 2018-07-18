# Auto generated from tests/test_basics/jsg/labeledShapeExpr1.jsg by PyJSG version 0.7.0
# Generation date: 2018-07-18 09:39
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

# .TYPE and .IGNORE settings
_CONTEXT = JSGContext()
_CONTEXT.TYPE_EXCEPTIONS.append("labeledShapeOr")
_CONTEXT.TYPE_EXCEPTIONS.append("labeledShapeAnd")
_CONTEXT.TYPE_EXCEPTIONS.append("labeledShapeNot")
_CONTEXT.TYPE_EXCEPTIONS.append("labeledNodeConstraint")
_CONTEXT.TYPE_EXCEPTIONS.append("labeledShape")
_CONTEXT.TYPE_EXCEPTIONS.append("shapeExprLabel")
_CONTEXT.TYPE_EXCEPTIONS.append("labeledShapeExternal")
_CONTEXT.TYPE_EXCEPTIONS.append("bar")
_CONTEXT.TYPE_EXCEPTIONS.append("expr_1_")
_CONTEXT.TYPE_EXCEPTIONS.append("expr_2_")
_CONTEXT.TYPE_EXCEPTIONS.append("expr_3_")
_CONTEXT.TYPE_EXCEPTIONS.append("expr_4_")
_CONTEXT.TYPE_EXCEPTIONS.append("expr_5_")
_CONTEXT.TYPE_EXCEPTIONS.append("expr_6_")
_CONTEXT.TYPE_EXCEPTIONS.append("expr_7_")
_CONTEXT.TYPE_EXCEPTIONS.append("foo")
_CONTEXT.TYPE_EXCEPTIONS.append("expr")
_CONTEXT.TYPE_EXCEPTIONS.append("single")


class XX(JSGString):
    pattern = JSGPattern(r'[0-9]')


class YY(JSGString):
    pattern = JSGPattern(r'[0-9]')


class labeledShapeOr(JSGObject):
    _reference_types = []
    _members = {}
    _strict = True

    def __init__(self,
                 **_kwargs: Dict[str, object]):
        super().__init__(_CONTEXT, **_kwargs)


class labeledShapeAnd(JSGObject):
    _reference_types = []
    _members = {}
    _strict = True

    def __init__(self,
                 **_kwargs: Dict[str, object]):
        super().__init__(_CONTEXT, **_kwargs)


class labeledShapeNot(JSGObject):
    _reference_types = []
    _members = {}
    _strict = True

    def __init__(self,
                 **_kwargs: Dict[str, object]):
        super().__init__(_CONTEXT, **_kwargs)


class labeledNodeConstraint(JSGObject):
    _reference_types = []
    _members = {}
    _strict = True

    def __init__(self,
                 **_kwargs: Dict[str, object]):
        super().__init__(_CONTEXT, **_kwargs)


class labeledShape(JSGObject):
    _reference_types = []
    _members = {}
    _strict = True

    def __init__(self,
                 **_kwargs: Dict[str, object]):
        super().__init__(_CONTEXT, **_kwargs)


class shapeExprLabel(JSGObject):
    _reference_types = []
    _members = {}
    _strict = True

    def __init__(self,
                 **_kwargs: Dict[str, object]):
        super().__init__(_CONTEXT, **_kwargs)


class labeledShapeExternal(JSGObject):
    _reference_types = []
    _members = {}
    _strict = True

    def __init__(self,
                 **_kwargs: Dict[str, object]):
        super().__init__(_CONTEXT, **_kwargs)


class bar(JSGObject):
    _reference_types = []
    _members = {}
    _strict = True

    def __init__(self,
                 **_kwargs: Dict[str, object]):
        super().__init__(_CONTEXT, **_kwargs)


class expr_1_(JSGObject):
    _reference_types = [labeledShapeOr]
    _members = {}
    _strict = True

    def __init__(self,
                 **_kwargs: Dict[str, object]):
        super().__init__(_CONTEXT, **_kwargs)


class expr_2_(JSGObject):
    _reference_types = [labeledShapeAnd]
    _members = {}
    _strict = True

    def __init__(self,
                 **_kwargs: Dict[str, object]):
        super().__init__(_CONTEXT, **_kwargs)


class expr_3_(JSGObject):
    _reference_types = [labeledShapeNot]
    _members = {}
    _strict = True

    def __init__(self,
                 **_kwargs: Dict[str, object]):
        super().__init__(_CONTEXT, **_kwargs)


class expr_4_(JSGObject):
    _reference_types = [labeledNodeConstraint]
    _members = {}
    _strict = True

    def __init__(self,
                 **_kwargs: Dict[str, object]):
        super().__init__(_CONTEXT, **_kwargs)


class expr_5_(JSGObject):
    _reference_types = [labeledShape]
    _members = {}
    _strict = True

    def __init__(self,
                 **_kwargs: Dict[str, object]):
        super().__init__(_CONTEXT, **_kwargs)


class expr_6_(JSGObject):
    _reference_types = [shapeExprLabel]
    _members = {}
    _strict = True

    def __init__(self,
                 **_kwargs: Dict[str, object]):
        super().__init__(_CONTEXT, **_kwargs)


class expr_7_(JSGObject):
    _reference_types = [labeledShapeExternal]
    _members = {}
    _strict = True

    def __init__(self,
                 **_kwargs: Dict[str, object]):
        super().__init__(_CONTEXT, **_kwargs)


class foo(JSGObject):
    _reference_types = []
    _members = {'a': XX,
                'b': YY}
    _strict = True

    def __init__(self,
                 a: str = None,
                 b: str = None,
                 **_kwargs: Dict[str, object]):
        super().__init__(_CONTEXT, **_kwargs)
        self.a = a
        self.b = b


class expr(JSGObject):
    _reference_types = [expr_1_, expr_2_, expr_3_, expr_4_, expr_5_, expr_6_, expr_7_]
    _members = {}
    _strict = True

    def __init__(self,
                 opts_: Union[expr_1_, expr_2_, expr_3_, expr_4_, expr_5_, expr_6_, expr_7_] = None,
                 **_kwargs: Dict[str, object]):
        super().__init__(_CONTEXT, **_kwargs)
        if opts_ is not None:
            if isinstance(opts_, expr_1_):
                pass
            elif isinstance(opts_, expr_2_):
                pass
            elif isinstance(opts_, expr_3_):
                pass
            elif isinstance(opts_, expr_4_):
                pass
            elif isinstance(opts_, expr_5_):
                pass
            elif isinstance(opts_, expr_6_):
                pass
            elif isinstance(opts_, expr_7_):
                pass
            else:
                raise ValueError(f"Unrecognized value type: {opts_}")


class single(JSGObject):
    _reference_types = [expr]
    _members = {}
    _strict = True

    def __init__(self,
                 opts_: Union[expr_1_, expr_2_, expr_3_, expr_4_, expr_5_, expr_6_, expr_7_] = None,
                 **_kwargs: Dict[str, object]):
        super().__init__(_CONTEXT, **_kwargs)
        if opts_ is not None:
            if isinstance(opts_, expr_1_):
                pass
            elif isinstance(opts_, expr_2_):
                pass
            elif isinstance(opts_, expr_3_):
                pass
            elif isinstance(opts_, expr_4_):
                pass
            elif isinstance(opts_, expr_5_):
                pass
            elif isinstance(opts_, expr_6_):
                pass
            elif isinstance(opts_, expr_7_):
                pass
            else:
                raise ValueError(f"Unrecognized value type: {opts_}")


_CONTEXT.NAMESPACE = locals()

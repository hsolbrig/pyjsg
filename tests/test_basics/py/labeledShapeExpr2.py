# Auto generated from tests/test_basics/jsg/labeledShapeExpr2.jsg by PyJSG version 0.7.0
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
_CONTEXT.TYPE_EXCEPTIONS.append("labeledShapeExternal_1_")
_CONTEXT.TYPE_EXCEPTIONS.append("labeledShapeExternal_2_")
_CONTEXT.TYPE_EXCEPTIONS.append("expr_1_")
_CONTEXT.TYPE_EXCEPTIONS.append("expr_2_")
_CONTEXT.TYPE_EXCEPTIONS.append("expr_3_")
_CONTEXT.TYPE_EXCEPTIONS.append("expr_4_")
_CONTEXT.TYPE_EXCEPTIONS.append("expr_5_")
_CONTEXT.TYPE_EXCEPTIONS.append("expr_6_")
_CONTEXT.TYPE_EXCEPTIONS.append("labeledShapeExternal")
_CONTEXT.TYPE_EXCEPTIONS.append("expr_7_")
_CONTEXT.TYPE_EXCEPTIONS.append("expr")


class labeledShapeOr(JSGObject):
    _reference_types = []
    _members = {'id': String}
    _strict = True

    def __init__(self,
                 id: str = None,
                 **_kwargs: Dict[str, object]):
        super().__init__(_CONTEXT, **_kwargs)
        self.id = id


class labeledShapeAnd(JSGObject):
    _reference_types = []
    _members = {'id': String}
    _strict = True

    def __init__(self,
                 id: str = None,
                 **_kwargs: Dict[str, object]):
        super().__init__(_CONTEXT, **_kwargs)
        self.id = id


class labeledShapeNot(JSGObject):
    _reference_types = []
    _members = {'id': String}
    _strict = True

    def __init__(self,
                 id: str = None,
                 **_kwargs: Dict[str, object]):
        super().__init__(_CONTEXT, **_kwargs)
        self.id = id


class labeledNodeConstraint(JSGObject):
    _reference_types = []
    _members = {'id': String}
    _strict = True

    def __init__(self,
                 id: str = None,
                 **_kwargs: Dict[str, object]):
        super().__init__(_CONTEXT, **_kwargs)
        self.id = id


class labeledShape(JSGObject):
    _reference_types = []
    _members = {'id': String}
    _strict = True

    def __init__(self,
                 id: str = None,
                 **_kwargs: Dict[str, object]):
        super().__init__(_CONTEXT, **_kwargs)
        self.id = id


class shapeExprLabel(JSGObject):
    _reference_types = []
    _members = {'id': String}
    _strict = True

    def __init__(self,
                 id: str = None,
                 **_kwargs: Dict[str, object]):
        super().__init__(_CONTEXT, **_kwargs)
        self.id = id


class labeledShapeExternal_1_(JSGObject):
    _reference_types = []
    _members = {'id': String}
    _strict = True

    def __init__(self,
                 id: str = None,
                 **_kwargs: Dict[str, object]):
        super().__init__(_CONTEXT, **_kwargs)
        self.id = id


class labeledShapeExternal_2_(JSGObject):
    _reference_types = []
    _members = {}
    _strict = True

    def __init__(self,
                 **_kwargs: Dict[str, object]):
        super().__init__(_CONTEXT, **_kwargs)


class expr_1_(JSGObject):
    _reference_types = [labeledShapeOr]
    _members = {'id': String}
    _strict = True

    def __init__(self,
                 id: str = None,
                 **_kwargs: Dict[str, object]):
        super().__init__(_CONTEXT, **_kwargs)
        self.id = id


class expr_2_(JSGObject):
    _reference_types = [labeledShapeAnd]
    _members = {'id': String}
    _strict = True

    def __init__(self,
                 id: str = None,
                 **_kwargs: Dict[str, object]):
        super().__init__(_CONTEXT, **_kwargs)
        self.id = id


class expr_3_(JSGObject):
    _reference_types = [labeledShapeNot]
    _members = {'id': String}
    _strict = True

    def __init__(self,
                 id: str = None,
                 **_kwargs: Dict[str, object]):
        super().__init__(_CONTEXT, **_kwargs)
        self.id = id


class expr_4_(JSGObject):
    _reference_types = [labeledNodeConstraint]
    _members = {'id': String}
    _strict = True

    def __init__(self,
                 id: str = None,
                 **_kwargs: Dict[str, object]):
        super().__init__(_CONTEXT, **_kwargs)
        self.id = id


class expr_5_(JSGObject):
    _reference_types = [labeledShape]
    _members = {'id': String}
    _strict = True

    def __init__(self,
                 id: str = None,
                 **_kwargs: Dict[str, object]):
        super().__init__(_CONTEXT, **_kwargs)
        self.id = id


class expr_6_(JSGObject):
    _reference_types = [shapeExprLabel]
    _members = {'id': String}
    _strict = True

    def __init__(self,
                 id: str = None,
                 **_kwargs: Dict[str, object]):
        super().__init__(_CONTEXT, **_kwargs)
        self.id = id


class labeledShapeExternal(JSGObject):
    _reference_types = [labeledShapeExternal_1_, labeledShapeExternal_2_]
    _members = {'id': Optional[String]}
    _strict = True

    def __init__(self,
                 opts_: Union[labeledShapeExternal_1_, labeledShapeExternal_2_] = None,
                 **_kwargs: Dict[str, object]):
        super().__init__(_CONTEXT, **_kwargs)
        if opts_ is not None:
            if isinstance(opts_, labeledShapeExternal_1_):
                self.id = opts_.id
            elif isinstance(opts_, labeledShapeExternal_2_):
                pass
            else:
                raise ValueError(f"Unrecognized value type: {opts_}")


class expr_7_(JSGObject):
    _reference_types = [labeledShapeExternal]
    _members = {'id': Optional[String]}
    _strict = True

    def __init__(self,
                 opts_: Union[labeledShapeExternal_1_, labeledShapeExternal_2_] = None,
                 **_kwargs: Dict[str, object]):
        super().__init__(_CONTEXT, **_kwargs)
        if opts_ is not None:
            if isinstance(opts_, labeledShapeExternal_1_):
                self.id = opts_.id
            elif isinstance(opts_, labeledShapeExternal_2_):
                pass
            else:
                raise ValueError(f"Unrecognized value type: {opts_}")


class expr(JSGObject):
    _reference_types = [expr_1_, expr_2_, expr_3_, expr_4_, expr_5_, expr_6_, expr_7_]
    _members = {'id': Optional[Optional[String]],
                'id': Optional[Optional[String]],
                'id': Optional[Optional[String]],
                'id': Optional[Optional[String]],
                'id': Optional[Optional[String]],
                'id': Optional[Optional[String]],
                'id': Optional[Optional[String]]}
    _strict = True

    def __init__(self,
                 opts_: Union[expr_1_, expr_2_, expr_3_, expr_4_, expr_5_, expr_6_, expr_7_] = None,
                 **_kwargs: Dict[str, object]):
        super().__init__(_CONTEXT, **_kwargs)
        if opts_ is not None:
            if isinstance(opts_, expr_1_):
                self.id = opts_.id
            elif isinstance(opts_, expr_2_):
                self.id = opts_.id
            elif isinstance(opts_, expr_3_):
                self.id = opts_.id
            elif isinstance(opts_, expr_4_):
                self.id = opts_.id
            elif isinstance(opts_, expr_5_):
                self.id = opts_.id
            elif isinstance(opts_, expr_6_):
                self.id = opts_.id
            elif isinstance(opts_, expr_7_):
                if opts_ is not None:
                    if isinstance(opts_, labeledShapeExternal_1_):
                        self.id = opts_.id
                    elif isinstance(opts_, labeledShapeExternal_2_):
                        pass
                    else:
                        raise ValueError(f"Unrecognized value type: {opts_}")
            else:
                raise ValueError(f"Unrecognized value type: {opts_}")


_CONTEXT.NAMESPACE = locals()

# Auto generated from test_basics/jsg/labeledShapeExpr.jsg by PyJSG version 0.7.0
# Generation date: 2018-06-28 11:40
#
import sys
from typing import Optional, Dict, List, Union
if sys.version_info < (3, 7):
    from typing import _ForwardRef as ForwardRef
    from pyjsg.jsglib import typing_patch_36
else:
    from typing import ForwardRef
    from pyjsg.jsglib import typing_patch_37

from pyjsg.jsglib import *
from pyjsg.jsglib.jsg import isinstance_

# .TYPE and .IGNORE settings
_CONTEXT = JSGContext()
_CONTEXT.TYPE_EXCEPTIONS.append("labeledShapeOr")
_CONTEXT.TYPE_EXCEPTIONS.append("labeledShapeAnd")
_CONTEXT.TYPE_EXCEPTIONS.append("labeledShapeNot")
_CONTEXT.TYPE_EXCEPTIONS.append("labeledNodeConstraint")
_CONTEXT.TYPE_EXCEPTIONS.append("labeledShape")
_CONTEXT.TYPE_EXCEPTIONS.append("shapeExprLabel")
_CONTEXT.TYPE_EXCEPTIONS.append("labeledShapeExternal")
_CONTEXT.TYPE_EXCEPTIONS.append("expr_1_")
_CONTEXT.TYPE_EXCEPTIONS.append("expr_2_")
_CONTEXT.TYPE_EXCEPTIONS.append("expr_3_")
_CONTEXT.TYPE_EXCEPTIONS.append("expr_4_")
_CONTEXT.TYPE_EXCEPTIONS.append("expr_5_")
_CONTEXT.TYPE_EXCEPTIONS.append("expr_6_")
_CONTEXT.TYPE_EXCEPTIONS.append("expr_7_")
_CONTEXT.TYPE_EXCEPTIONS.append("expr")



class labeledShapeOr(JSGObject):
    _reference_types = []
    _members = {}
    _strict = True
    
    def __init__(self,
                 **_kwargs: Dict[str, object]):
        self._context = _CONTEXT
        super().__init__(self._context, **_kwargs)


class labeledShapeAnd(JSGObject):
    _reference_types = []
    _members = {}
    _strict = True
    
    def __init__(self,
                 **_kwargs: Dict[str, object]):
        self._context = _CONTEXT
        super().__init__(self._context, **_kwargs)


class labeledShapeNot(JSGObject):
    _reference_types = []
    _members = {}
    _strict = True
    
    def __init__(self,
                 **_kwargs: Dict[str, object]):
        self._context = _CONTEXT
        super().__init__(self._context, **_kwargs)


class labeledNodeConstraint(JSGObject):
    _reference_types = []
    _members = {}
    _strict = True
    
    def __init__(self,
                 **_kwargs: Dict[str, object]):
        self._context = _CONTEXT
        super().__init__(self._context, **_kwargs)


class labeledShape(JSGObject):
    _reference_types = []
    _members = {}
    _strict = True
    
    def __init__(self,
                 **_kwargs: Dict[str, object]):
        self._context = _CONTEXT
        super().__init__(self._context, **_kwargs)


class shapeExprLabel(JSGObject):
    _reference_types = []
    _members = {}
    _strict = True
    
    def __init__(self,
                 **_kwargs: Dict[str, object]):
        self._context = _CONTEXT
        super().__init__(self._context, **_kwargs)


class labeledShapeExternal(JSGObject):
    _reference_types = []
    _members = {}
    _strict = True
    
    def __init__(self,
                 **_kwargs: Dict[str, object]):
        self._context = _CONTEXT
        super().__init__(self._context, **_kwargs)


class expr_1_(JSGObject):
    _reference_types = [labeledShapeOr]
    _members = {}
    _strict = True
    
    def __init__(self,
                 labeledShapeOr: labeledShapeOr = None,
                 **_kwargs: Dict[str, object]):
        self._context = _CONTEXT
        super().__init__(self._context, **_kwargs)


class expr_2_(JSGObject):
    _reference_types = [labeledShapeAnd]
    _members = {}
    _strict = True
    
    def __init__(self,
                 labeledShapeAnd: labeledShapeAnd = None,
                 **_kwargs: Dict[str, object]):
        self._context = _CONTEXT
        super().__init__(self._context, **_kwargs)


class expr_3_(JSGObject):
    _reference_types = [labeledShapeNot]
    _members = {}
    _strict = True
    
    def __init__(self,
                 labeledShapeNot: labeledShapeNot = None,
                 **_kwargs: Dict[str, object]):
        self._context = _CONTEXT
        super().__init__(self._context, **_kwargs)


class expr_4_(JSGObject):
    _reference_types = [labeledNodeConstraint]
    _members = {}
    _strict = True
    
    def __init__(self,
                 labeledNodeConstraint: labeledNodeConstraint = None,
                 **_kwargs: Dict[str, object]):
        self._context = _CONTEXT
        super().__init__(self._context, **_kwargs)


class expr_5_(JSGObject):
    _reference_types = [labeledShape]
    _members = {}
    _strict = True
    
    def __init__(self,
                 labeledShape: labeledShape = None,
                 **_kwargs: Dict[str, object]):
        self._context = _CONTEXT
        super().__init__(self._context, **_kwargs)


class expr_6_(JSGObject):
    _reference_types = [shapeExprLabel]
    _members = {}
    _strict = True
    
    def __init__(self,
                 shapeExprLabel: shapeExprLabel = None,
                 **_kwargs: Dict[str, object]):
        self._context = _CONTEXT
        super().__init__(self._context, **_kwargs)


class expr_7_(JSGObject):
    _reference_types = [labeledShapeExternal]
    _members = {}
    _strict = True
    
    def __init__(self,
                 labeledShapeExternal: labeledShapeExternal = None,
                 **_kwargs: Dict[str, object]):
        self._context = _CONTEXT
        super().__init__(self._context, **_kwargs)


class expr(JSGObject):
    _reference_types = [expr_1_, expr_2_, expr_3_, expr_4_, expr_5_, expr_6_, expr_7_]
    _members = {}
    _strict = True
    
    def __init__(self,
                 opt_: Union[expr_1_, expr_2_, expr_3_, expr_4_, expr_5_, expr_6_, expr_7_] = None,
                 **_kwargs: Dict[str, object]):
        self._context = _CONTEXT
        
        super().__init__(self._context, **_kwargs)


_CONTEXT.NAMESPACE = locals()

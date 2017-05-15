# Auto generated from jsg/labeledShapeExpr.jsg by PyJSG version 1.0.0
# Generation date: 2017-05-15 11:10
#
from typing import Optional, Dict, List, Union, _ForwardRef

from pyjsg.jsglib.jsg import *
from pyjsg.jsglib.typing_patch import fix_forwards

# .TYPE and .IGNORE settings
_CONTEXT = JSGContext()

class labeledShapeOr(JSGObject):
    _reference_types = []
    
    def __init__(self,
                 **_kwargs: Dict[str, object]):
        self._context = _CONTEXT
        super().__init__(self._context, **_kwargs)


class labeledShapeAnd(JSGObject):
    _reference_types = []
    
    def __init__(self,
                 **_kwargs: Dict[str, object]):
        self._context = _CONTEXT
        super().__init__(self._context, **_kwargs)


class labeledShapeNot(JSGObject):
    _reference_types = []
    
    def __init__(self,
                 **_kwargs: Dict[str, object]):
        self._context = _CONTEXT
        super().__init__(self._context, **_kwargs)


class labeledNodeConstraint(JSGObject):
    _reference_types = []
    
    def __init__(self,
                 **_kwargs: Dict[str, object]):
        self._context = _CONTEXT
        super().__init__(self._context, **_kwargs)


class labeledShape(JSGObject):
    _reference_types = []
    
    def __init__(self,
                 **_kwargs: Dict[str, object]):
        self._context = _CONTEXT
        super().__init__(self._context, **_kwargs)


class shapeExprLabel(JSGObject):
    _reference_types = []
    
    def __init__(self,
                 **_kwargs: Dict[str, object]):
        self._context = _CONTEXT
        super().__init__(self._context, **_kwargs)


class labeledShapeExternal(JSGObject):
    _reference_types = []
    
    def __init__(self,
                 **_kwargs: Dict[str, object]):
        self._context = _CONTEXT
        super().__init__(self._context, **_kwargs)


class expr_1_(JSGObject):
    _reference_types = [labeledShapeOr]
    
    def __init__(self,
                 labeledShapeOr: labeledShapeOr = None,
                 **_kwargs: Dict[str, object]):
        self._context = _CONTEXT
        super().__init__(self._context, **_kwargs)


class expr_2_(JSGObject):
    _reference_types = [labeledShapeAnd]
    
    def __init__(self,
                 labeledShapeAnd: labeledShapeAnd = None,
                 **_kwargs: Dict[str, object]):
        self._context = _CONTEXT
        super().__init__(self._context, **_kwargs)


class expr_3_(JSGObject):
    _reference_types = [labeledShapeNot]
    
    def __init__(self,
                 labeledShapeNot: labeledShapeNot = None,
                 **_kwargs: Dict[str, object]):
        self._context = _CONTEXT
        super().__init__(self._context, **_kwargs)


class expr_4_(JSGObject):
    _reference_types = [labeledNodeConstraint]
    
    def __init__(self,
                 labeledNodeConstraint: labeledNodeConstraint = None,
                 **_kwargs: Dict[str, object]):
        self._context = _CONTEXT
        super().__init__(self._context, **_kwargs)


class expr_5_(JSGObject):
    _reference_types = [labeledShape]
    
    def __init__(self,
                 labeledShape: labeledShape = None,
                 **_kwargs: Dict[str, object]):
        self._context = _CONTEXT
        super().__init__(self._context, **_kwargs)


class expr_6_(JSGObject):
    _reference_types = [shapeExprLabel]
    
    def __init__(self,
                 shapeExprLabel: shapeExprLabel = None,
                 **_kwargs: Dict[str, object]):
        self._context = _CONTEXT
        super().__init__(self._context, **_kwargs)


class expr_7_(JSGObject):
    _reference_types = [labeledShapeExternal]
    
    def __init__(self,
                 labeledShapeExternal: labeledShapeExternal = None,
                 **_kwargs: Dict[str, object]):
        self._context = _CONTEXT
        super().__init__(self._context, **_kwargs)


class expr(JSGObject):
    _reference_types = [expr_1_, expr_2_, expr_3_, expr_4_, expr_5_, expr_6_, expr_7_]
    
    def __init__(self,
                 opt_: Union[expr_1_, expr_2_, expr_3_, expr_4_, expr_5_, expr_6_, expr_7_] = None,
                 **_kwargs: Dict[str, object]):
        self._context = _CONTEXT
        
        super().__init__(self._context, **_kwargs)


fix_forwards(locals())

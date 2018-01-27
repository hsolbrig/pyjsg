# Auto generated from jsg/labeledShapeExpr1.jsg by PyJSG version 0.5.0
# Generation date: 2018-01-27 10:29
#
from typing import Optional, Dict, List, Union, _ForwardRef

from pyjsg.jsglib import jsg
from pyjsg.jsglib.jsg import isinstance_

# .TYPE and .IGNORE settings
_CONTEXT = jsg.JSGContext()
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




class XX(jsg.JSGString):
    pattern = jsg.JSGPattern(r'[0-9]')


class YY(jsg.JSGString):
    pattern = jsg.JSGPattern(r'[0-9]')

class labeledShapeOr(jsg.JSGObject):
    _reference_types = []
    _members = {}
    _strict = True
    
    def __init__(self,
                 **_kwargs: Dict[str, object]):
        self._context = _CONTEXT
        super().__init__(self._context, **_kwargs)


class labeledShapeAnd(jsg.JSGObject):
    _reference_types = []
    _members = {}
    _strict = True
    
    def __init__(self,
                 **_kwargs: Dict[str, object]):
        self._context = _CONTEXT
        super().__init__(self._context, **_kwargs)


class labeledShapeNot(jsg.JSGObject):
    _reference_types = []
    _members = {}
    _strict = True
    
    def __init__(self,
                 **_kwargs: Dict[str, object]):
        self._context = _CONTEXT
        super().__init__(self._context, **_kwargs)


class labeledNodeConstraint(jsg.JSGObject):
    _reference_types = []
    _members = {}
    _strict = True
    
    def __init__(self,
                 **_kwargs: Dict[str, object]):
        self._context = _CONTEXT
        super().__init__(self._context, **_kwargs)


class labeledShape(jsg.JSGObject):
    _reference_types = []
    _members = {}
    _strict = True
    
    def __init__(self,
                 **_kwargs: Dict[str, object]):
        self._context = _CONTEXT
        super().__init__(self._context, **_kwargs)


class shapeExprLabel(jsg.JSGObject):
    _reference_types = []
    _members = {}
    _strict = True
    
    def __init__(self,
                 **_kwargs: Dict[str, object]):
        self._context = _CONTEXT
        super().__init__(self._context, **_kwargs)


class labeledShapeExternal(jsg.JSGObject):
    _reference_types = []
    _members = {}
    _strict = True
    
    def __init__(self,
                 **_kwargs: Dict[str, object]):
        self._context = _CONTEXT
        super().__init__(self._context, **_kwargs)


class bar(jsg.JSGObject):
    _reference_types = []
    _members = {}
    _strict = True
    
    def __init__(self,
                 **_kwargs: Dict[str, object]):
        self._context = _CONTEXT
        super().__init__(self._context, **_kwargs)


class expr_1_(jsg.JSGObject):
    _reference_types = [labeledShapeOr]
    _members = {}
    _strict = True
    
    def __init__(self,
                 labeledShapeOr: labeledShapeOr = None,
                 **_kwargs: Dict[str, object]):
        self._context = _CONTEXT
        super().__init__(self._context, **_kwargs)


class expr_2_(jsg.JSGObject):
    _reference_types = [labeledShapeAnd]
    _members = {}
    _strict = True
    
    def __init__(self,
                 labeledShapeAnd: labeledShapeAnd = None,
                 **_kwargs: Dict[str, object]):
        self._context = _CONTEXT
        super().__init__(self._context, **_kwargs)


class expr_3_(jsg.JSGObject):
    _reference_types = [labeledShapeNot]
    _members = {}
    _strict = True
    
    def __init__(self,
                 labeledShapeNot: labeledShapeNot = None,
                 **_kwargs: Dict[str, object]):
        self._context = _CONTEXT
        super().__init__(self._context, **_kwargs)


class expr_4_(jsg.JSGObject):
    _reference_types = [labeledNodeConstraint]
    _members = {}
    _strict = True
    
    def __init__(self,
                 labeledNodeConstraint: labeledNodeConstraint = None,
                 **_kwargs: Dict[str, object]):
        self._context = _CONTEXT
        super().__init__(self._context, **_kwargs)


class expr_5_(jsg.JSGObject):
    _reference_types = [labeledShape]
    _members = {}
    _strict = True
    
    def __init__(self,
                 labeledShape: labeledShape = None,
                 **_kwargs: Dict[str, object]):
        self._context = _CONTEXT
        super().__init__(self._context, **_kwargs)


class expr_6_(jsg.JSGObject):
    _reference_types = [shapeExprLabel]
    _members = {}
    _strict = True
    
    def __init__(self,
                 shapeExprLabel: shapeExprLabel = None,
                 **_kwargs: Dict[str, object]):
        self._context = _CONTEXT
        super().__init__(self._context, **_kwargs)


class expr_7_(jsg.JSGObject):
    _reference_types = [labeledShapeExternal]
    _members = {}
    _strict = True
    
    def __init__(self,
                 labeledShapeExternal: labeledShapeExternal = None,
                 **_kwargs: Dict[str, object]):
        self._context = _CONTEXT
        super().__init__(self._context, **_kwargs)


class foo(jsg.JSGObject):
    _reference_types = []
    _members = {'a': XX,
                'b': YY}
    _strict = True
    
    def __init__(self,
                 a: XX = None,
                 b: YY = None,
                 **_kwargs: Dict[str, object]):
        self._context = _CONTEXT
        self.a = a
        self.b = b
        super().__init__(self._context, **_kwargs)


class expr(jsg.JSGObject):
    _reference_types = [expr_1_, expr_2_, expr_3_, expr_4_, expr_5_, expr_6_, expr_7_]
    _members = {}
    _strict = True
    
    def __init__(self,
                 opt_: Union[expr_1_, expr_2_, expr_3_, expr_4_, expr_5_, expr_6_, expr_7_] = None,
                 **_kwargs: Dict[str, object]):
        self._context = _CONTEXT
        
        super().__init__(self._context, **_kwargs)


class single(jsg.JSGObject):
    _reference_types = [expr]
    _members = {}
    _strict = True
    
    def __init__(self,
                 expr: expr = None,
                 **_kwargs: Dict[str, object]):
        self._context = _CONTEXT
        super().__init__(self._context, **_kwargs)


_CONTEXT.NAMESPACE = locals()

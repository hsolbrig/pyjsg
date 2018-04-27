# Auto generated from jsg/labeledShapeExpr2.jsg by PyJSG version 0.6.0
# Generation date: 2018-04-27 13:34
#
import sys
from typing import Optional, Dict, List, Union
if sys.version_info < (3, 7):
    from typing import _ForwardRef as ForwardRef
    from pyjsg.jsglib import typing_patch_36
else:
    from typing import ForwardRef
    from pyjsg.jsglib import typing_patch_37

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



class labeledShapeOr(jsg.JSGObject):
    _reference_types = []
    _members = {'id': str}
    _strict = True
    
    def __init__(self,
                 id: str = None,
                 **_kwargs: Dict[str, object]):
        self._context = _CONTEXT
        self.id = jsg.String(id)
        super().__init__(self._context, **_kwargs)


class labeledShapeAnd(jsg.JSGObject):
    _reference_types = []
    _members = {'id': str}
    _strict = True
    
    def __init__(self,
                 id: str = None,
                 **_kwargs: Dict[str, object]):
        self._context = _CONTEXT
        self.id = jsg.String(id)
        super().__init__(self._context, **_kwargs)


class labeledShapeNot(jsg.JSGObject):
    _reference_types = []
    _members = {'id': str}
    _strict = True
    
    def __init__(self,
                 id: str = None,
                 **_kwargs: Dict[str, object]):
        self._context = _CONTEXT
        self.id = jsg.String(id)
        super().__init__(self._context, **_kwargs)


class labeledNodeConstraint(jsg.JSGObject):
    _reference_types = []
    _members = {'id': str}
    _strict = True
    
    def __init__(self,
                 id: str = None,
                 **_kwargs: Dict[str, object]):
        self._context = _CONTEXT
        self.id = jsg.String(id)
        super().__init__(self._context, **_kwargs)


class labeledShape(jsg.JSGObject):
    _reference_types = []
    _members = {'id': str}
    _strict = True
    
    def __init__(self,
                 id: str = None,
                 **_kwargs: Dict[str, object]):
        self._context = _CONTEXT
        self.id = jsg.String(id)
        super().__init__(self._context, **_kwargs)


class shapeExprLabel(jsg.JSGObject):
    _reference_types = []
    _members = {'id': str}
    _strict = True
    
    def __init__(self,
                 id: str = None,
                 **_kwargs: Dict[str, object]):
        self._context = _CONTEXT
        self.id = jsg.String(id)
        super().__init__(self._context, **_kwargs)


class labeledShapeExternal_1_(jsg.JSGObject):
    _reference_types = []
    _members = {'id': str}
    _strict = True
    
    def __init__(self,
                 id: str = None,
                 **_kwargs: Dict[str, object]):
        self._context = _CONTEXT
        self.id = jsg.String(id)
        super().__init__(self._context, **_kwargs)


class labeledShapeExternal_2_(jsg.JSGObject):
    _reference_types = []
    _members = {}
    _strict = True
    
    def __init__(self,
                 **_kwargs: Dict[str, object]):
        self._context = _CONTEXT
        super().__init__(self._context, **_kwargs)


class expr_1_(jsg.JSGObject):
    _reference_types = [labeledShapeOr]
    _members = {'id': str}
    _strict = True
    
    def __init__(self,
                 labeledShapeOr: labeledShapeOr = None,
                 **_kwargs: Dict[str, object]):
        self._context = _CONTEXT
        self.id = jsg.String(labeledShapeOr.id)
        super().__init__(self._context, **_kwargs)


class expr_2_(jsg.JSGObject):
    _reference_types = [labeledShapeAnd]
    _members = {'id': str}
    _strict = True
    
    def __init__(self,
                 labeledShapeAnd: labeledShapeAnd = None,
                 **_kwargs: Dict[str, object]):
        self._context = _CONTEXT
        self.id = jsg.String(labeledShapeAnd.id)
        super().__init__(self._context, **_kwargs)


class expr_3_(jsg.JSGObject):
    _reference_types = [labeledShapeNot]
    _members = {'id': str}
    _strict = True
    
    def __init__(self,
                 labeledShapeNot: labeledShapeNot = None,
                 **_kwargs: Dict[str, object]):
        self._context = _CONTEXT
        self.id = jsg.String(labeledShapeNot.id)
        super().__init__(self._context, **_kwargs)


class expr_4_(jsg.JSGObject):
    _reference_types = [labeledNodeConstraint]
    _members = {'id': str}
    _strict = True
    
    def __init__(self,
                 labeledNodeConstraint: labeledNodeConstraint = None,
                 **_kwargs: Dict[str, object]):
        self._context = _CONTEXT
        self.id = jsg.String(labeledNodeConstraint.id)
        super().__init__(self._context, **_kwargs)


class expr_5_(jsg.JSGObject):
    _reference_types = [labeledShape]
    _members = {'id': str}
    _strict = True
    
    def __init__(self,
                 labeledShape: labeledShape = None,
                 **_kwargs: Dict[str, object]):
        self._context = _CONTEXT
        self.id = jsg.String(labeledShape.id)
        super().__init__(self._context, **_kwargs)


class expr_6_(jsg.JSGObject):
    _reference_types = [shapeExprLabel]
    _members = {'id': str}
    _strict = True
    
    def __init__(self,
                 shapeExprLabel: shapeExprLabel = None,
                 **_kwargs: Dict[str, object]):
        self._context = _CONTEXT
        self.id = jsg.String(shapeExprLabel.id)
        super().__init__(self._context, **_kwargs)


class labeledShapeExternal(jsg.JSGObject):
    _reference_types = [labeledShapeExternal_1_, labeledShapeExternal_2_]
    _members = {'id': str}
    _strict = True
    
    def __init__(self,
                 opt_: Union[labeledShapeExternal_1_, labeledShapeExternal_2_] = None,
                 **_kwargs: Dict[str, object]):
        self._context = _CONTEXT
        self.id = jsg.String(opt_.id) if isinstance(opt_, labeledShapeExternal_1_) else jsg.String(None)
        super().__init__(self._context, **_kwargs)


class expr_7_(jsg.JSGObject):
    _reference_types = [labeledShapeExternal]
    _members = {'id': str}
    _strict = True
    
    def __init__(self,
                 labeledShapeExternal: labeledShapeExternal = None,
                 **_kwargs: Dict[str, object]):
        self._context = _CONTEXT
        self.id = jsg.String(labeledShapeExternal.id)
        super().__init__(self._context, **_kwargs)


class expr(jsg.JSGObject):
    _reference_types = [expr_1_, expr_2_, expr_3_, expr_4_, expr_5_, expr_6_, expr_7_]
    _members = {'id': str}
    _strict = True
    
    def __init__(self,
                 opt_: Union[expr_1_, expr_2_, expr_3_, expr_4_, expr_5_, expr_6_, expr_7_] = None,
                 **_kwargs: Dict[str, object]):
        self._context = _CONTEXT
        self.id = jsg.String(opt_.id) if isinstance(opt_, expr_1_) else jsg.String(None)
        self.id = jsg.String(opt_.id) if isinstance(opt_, expr_2_) else jsg.String(None)
        self.id = jsg.String(opt_.id) if isinstance(opt_, expr_3_) else jsg.String(None)
        self.id = jsg.String(opt_.id) if isinstance(opt_, expr_4_) else jsg.String(None)
        self.id = jsg.String(opt_.id) if isinstance(opt_, expr_5_) else jsg.String(None)
        self.id = jsg.String(opt_.id) if isinstance(opt_, expr_6_) else jsg.String(None)
        self.id = jsg.String(opt_.id) if isinstance(opt_, expr_7_) else jsg.String(None)
        super().__init__(self._context, **_kwargs)


_CONTEXT.NAMESPACE = locals()

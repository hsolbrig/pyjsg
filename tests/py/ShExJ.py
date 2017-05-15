# Auto generated from jsg/ShExJ.jsg by PyJSG version 1.0.0
# Generation date: 2017-05-15 11:10
#
from typing import Optional, Dict, List, Union, _ForwardRef

from pyjsg.jsglib.jsg import *
from pyjsg.jsglib.typing_patch import fix_forwards

# .TYPE and .IGNORE settings
_CONTEXT = JSGContext()
_CONTEXT.TYPE = "type"
_CONTEXT.TYPE_EXCEPTIONS.append("ObjectLiteral")


EachOft_ = _ForwardRef('EachOf')
OneOft_ = _ForwardRef('OneOf')
ShapeAndt_ = _ForwardRef('ShapeAnd')
ShapeNott_ = _ForwardRef('ShapeNot')
ShapeOrt_ = _ForwardRef('ShapeOr')
Shapet_ = _ForwardRef('Shape')
TripleConstraintt_ = _ForwardRef('TripleConstraint')
shapeExprt_ = _ForwardRef('shapeExpr')
tripleExprt_ = _ForwardRef('tripleExpr')


class _Anon1(JSGString):
    pattern = JSGPattern(r'http\:\/\/www\.w3\.org\/ns\/shex\.jsonld')


class _Anon2(JSGString):
    pattern = JSGPattern(r'(iri)|(bnode)|(nonliteral)|(literal)')


class LANGTAG(JSGString):
    pattern = JSGPattern(r'[a-zA-Z]+(\-([a-zA-Z0-9])+)*')


class PN_CHARS_BASE(JSGString):
    pattern = JSGPattern(r'[A-Z]|[a-z]|[\u00C0-\u00D6]|[\u00D8-\u00F6]|[\u00F8-\u02FF]|[\u0370-\u037D]|[\u037F-\u1FFF]|[\u200C-\u200D]|[\u2070-\u218F]|[\u2C00-\u2FEF]|[\u3001-\uD7FF]|[\uF900-\uFDCF]|[\uFDF0-\uFFFD]|[\u10000-\uEFFFF]')


class HEX(JSGString):
    pattern = JSGPattern(r'[0-9]|[A-F]|[a-f]')


class PN_CHARS_U(JSGString):
    pattern = JSGPattern(r'({PN_CHARS_BASE})|_'.format(PN_CHARS_BASE=PN_CHARS_BASE.pattern))


class UCHAR(JSGString):
    pattern = JSGPattern(r'\\\\u({HEX})({HEX})({HEX})({HEX})|\\\\U({HEX})({HEX})({HEX})({HEX})({HEX})({HEX})({HEX})({HEX})'.format(HEX=HEX.pattern))


class PN_CHARS(JSGString):
    pattern = JSGPattern(r'({PN_CHARS_U})|\-|[0-9]|\\u00B7|[\u0300-\u036F]|[\u203F-\u2040]'.format(PN_CHARS_U=PN_CHARS_U.pattern))


class IRI(JSGString):
    pattern = JSGPattern(r'(({PN_CHARS})|\.|\:|\/|\\\\|\#|\@|\%|\&|({UCHAR}))*'.format(PN_CHARS=PN_CHARS.pattern, UCHAR=UCHAR.pattern))


class BNODE(JSGString):
    pattern = JSGPattern(r'_\:(({PN_CHARS_U})|[0-9])((({PN_CHARS})|\.)*({PN_CHARS}))?'.format(PN_CHARS=PN_CHARS.pattern, PN_CHARS_U=PN_CHARS_U.pattern))


class PN_PREFIX(JSGString):
    pattern = JSGPattern(r'({PN_CHARS_BASE})((({PN_CHARS})|\.)*({PN_CHARS}))?'.format(PN_CHARS=PN_CHARS.pattern, PN_CHARS_BASE=PN_CHARS_BASE.pattern))

class stringFacet_1_(JSGObject):
    _reference_types = []
    
    def __init__(self,
                 length: int = None,
                 minlength: int = None,
                 maxlength: int = None,
                 **_kwargs: Dict[str, object]):
        self._context = _CONTEXT
        self.length = Integer(length)
        self.minlength = Integer(minlength)
        self.maxlength = Integer(maxlength)
        super().__init__(self._context, **_kwargs)


class stringFacet_2_(JSGObject):
    _reference_types = []
    
    def __init__(self,
                 pattern: str = None,
                 flags: Optional[str] = None,
                 **_kwargs: Dict[str, object]):
        self._context = _CONTEXT
        self.pattern = String(pattern)
        self.flags = String(flags)
        super().__init__(self._context, **_kwargs)


class numericFacet(JSGObject):
    _reference_types = []
    
    def __init__(self,
                 mininclusive: float = None,
                 minexclusive: float = None,
                 maxinclusive: float = None,
                 maxexclusive: float = None,
                 totaldigits: int = None,
                 fractiondigits: int = None,
                 **_kwargs: Dict[str, object]):
        self._context = _CONTEXT
        self.mininclusive = Number(mininclusive)
        self.minexclusive = Number(minexclusive)
        self.maxinclusive = Number(maxinclusive)
        self.maxexclusive = Number(maxexclusive)
        self.totaldigits = Integer(totaldigits)
        self.fractiondigits = Integer(fractiondigits)
        super().__init__(self._context, **_kwargs)


class LiteralStem(JSGObject):
    _reference_types = []
    
    def __init__(self,
                 stem: str = None,
                 **_kwargs: Dict[str, object]):
        self._context = _CONTEXT
        self.stem = String(stem)
        super().__init__(self._context, **_kwargs)


class Wildcard(JSGObject):
    _reference_types = []
    
    def __init__(self,
                 **_kwargs: Dict[str, object]):
        self._context = _CONTEXT
        super().__init__(self._context, **_kwargs)


class xsFacet_2_(JSGObject):
    _reference_types = [numericFacet]
    
    def __init__(self,
                 numericFacet: numericFacet = None,
                 **_kwargs: Dict[str, object]):
        self._context = _CONTEXT
        self.mininclusive = Number(numericFacet.mininclusive)
        self.minexclusive = Number(numericFacet.minexclusive)
        self.maxinclusive = Number(numericFacet.maxinclusive)
        self.maxexclusive = Number(numericFacet.maxexclusive)
        self.totaldigits = Integer(numericFacet.totaldigits)
        self.fractiondigits = Integer(numericFacet.fractiondigits)
        super().__init__(self._context, **_kwargs)


class stringFacet(JSGObject):
    _reference_types = [stringFacet_1_, stringFacet_2_]
    
    def __init__(self,
                 opt_: Union[stringFacet_1_, stringFacet_2_] = None,
                 **_kwargs: Dict[str, object]):
        self._context = _CONTEXT
        self.length = Integer(opt_.length) if isinstance(opt_, stringFacet_1_) else Integer(None)
        self.minlength = Integer(opt_.minlength) if isinstance(opt_, stringFacet_1_) else Integer(None)
        self.maxlength = Integer(opt_.maxlength) if isinstance(opt_, stringFacet_1_) else Integer(None)
        self.pattern = String(opt_.pattern) if isinstance(opt_, stringFacet_2_) else String(None)
        self.flags = String(opt_.flags) if opt_ else String(None) if isinstance(opt_, stringFacet_2_) else String(None)
        super().__init__(self._context, **_kwargs)


class LiteralStemRange(JSGObject):
    _reference_types = []
    
    def __init__(self,
                 stem: Union[str, Wildcard] = None,
                 exclusions: List[Union[str, LiteralStem]] = None,
                 **_kwargs: Dict[str, object]):
        self._context = _CONTEXT
        self.stem = stem
        self.exclusions = exclusions
        super().__init__(self._context, **_kwargs)


class LanguageStem(JSGObject):
    _reference_types = []
    
    def __init__(self,
                 stem: LANGTAG = None,
                 **_kwargs: Dict[str, object]):
        self._context = _CONTEXT
        self.stem = stem
        super().__init__(self._context, **_kwargs)


class xsFacet_1_(JSGObject):
    _reference_types = [stringFacet]
    
    def __init__(self,
                 stringFacet: stringFacet = None,
                 **_kwargs: Dict[str, object]):
        self._context = _CONTEXT
        self.length = Integer(stringFacet.length)
        self.minlength = Integer(stringFacet.minlength)
        self.maxlength = Integer(stringFacet.maxlength)
        self.pattern = String(stringFacet.pattern)
        self.flags = String(stringFacet.flags) if stringFacet else String(None)
        super().__init__(self._context, **_kwargs)


class LanguageStemRange(JSGObject):
    _reference_types = []
    
    def __init__(self,
                 stem: Union[LANGTAG, Wildcard] = None,
                 exclusions: List[Union[LANGTAG, LanguageStem]] = None,
                 **_kwargs: Dict[str, object]):
        self._context = _CONTEXT
        self.stem = stem
        self.exclusions = exclusions
        super().__init__(self._context, **_kwargs)


class xsFacet(JSGObject):
    _reference_types = [xsFacet_1_, xsFacet_2_]
    
    def __init__(self,
                 opt_: Union[xsFacet_1_, xsFacet_2_] = None,
                 **_kwargs: Dict[str, object]):
        self._context = _CONTEXT
        self.length = Integer(opt_.length) if isinstance(opt_, xsFacet_1_) else Integer(None)
        self.minlength = Integer(opt_.minlength) if isinstance(opt_, xsFacet_1_) else Integer(None)
        self.maxlength = Integer(opt_.maxlength) if isinstance(opt_, xsFacet_1_) else Integer(None)
        self.pattern = String(opt_.pattern) if isinstance(opt_, xsFacet_1_) else String(None)
        self.flags = String(opt_.flags) if opt_ else String(None) if isinstance(opt_, xsFacet_1_) else String(None)
        self.mininclusive = Number(opt_.mininclusive) if isinstance(opt_, xsFacet_2_) else Number(None)
        self.minexclusive = Number(opt_.minexclusive) if isinstance(opt_, xsFacet_2_) else Number(None)
        self.maxinclusive = Number(opt_.maxinclusive) if isinstance(opt_, xsFacet_2_) else Number(None)
        self.maxexclusive = Number(opt_.maxexclusive) if isinstance(opt_, xsFacet_2_) else Number(None)
        self.totaldigits = Integer(opt_.totaldigits) if isinstance(opt_, xsFacet_2_) else Integer(None)
        self.fractiondigits = Integer(opt_.fractiondigits) if isinstance(opt_, xsFacet_2_) else Integer(None)
        super().__init__(self._context, **_kwargs)


class IriStem(JSGObject):
    _reference_types = []
    
    def __init__(self,
                 stem: IRI = None,
                 **_kwargs: Dict[str, object]):
        self._context = _CONTEXT
        self.stem = stem
        super().__init__(self._context, **_kwargs)


class SemAct(JSGObject):
    _reference_types = []
    
    def __init__(self,
                 name: IRI = None,
                 code: Optional[str] = None,
                 **_kwargs: Dict[str, object]):
        self._context = _CONTEXT
        self.name = name
        self.code = String(code)
        super().__init__(self._context, **_kwargs)


shapeExprLabel = Union[IRI, BNODE]

tripleExprLabel = Union[IRI, BNODE]

class ObjectLiteral(JSGObject):
    _reference_types = []
    
    def __init__(self,
                 value: str = None,
                 language: Optional[LANGTAG] = None,
                 type: Optional[IRI] = None,
                 **_kwargs: Dict[str, object]):
        self._context = _CONTEXT
        self.value = String(value)
        self.language = language
        self.type = type
        super().__init__(self._context, **_kwargs)


class ShapeOr(JSGObject):
    _reference_types = []
    
    def __init__(self,
                 id: Optional[shapeExprLabel] = None,
                 shapeExprs: List[shapeExprt_] = None,
                 **_kwargs: Dict[str, object]):
        self._context = _CONTEXT
        self.id = id
        self.shapeExprs = shapeExprs
        super().__init__(self._context, **_kwargs)


class ShapeAnd(JSGObject):
    _reference_types = []
    
    def __init__(self,
                 id: Optional[shapeExprLabel] = None,
                 shapeExprs: List[shapeExprt_] = None,
                 **_kwargs: Dict[str, object]):
        self._context = _CONTEXT
        self.id = id
        self.shapeExprs = shapeExprs
        super().__init__(self._context, **_kwargs)


class ShapeNot(JSGObject):
    _reference_types = []
    
    def __init__(self,
                 id: Optional[shapeExprLabel] = None,
                 shapeExpr: shapeExprt_ = None,
                 **_kwargs: Dict[str, object]):
        self._context = _CONTEXT
        self.id = id
        self.shapeExpr = shapeExpr
        super().__init__(self._context, **_kwargs)


class ShapeExternal(JSGObject):
    _reference_types = []
    
    def __init__(self,
                 id: Optional[shapeExprLabel] = None,
                 **_kwargs: Dict[str, object]):
        self._context = _CONTEXT
        self.id = id
        super().__init__(self._context, **_kwargs)


objectValue = Union[IRI, ObjectLiteral]

class IriStemRange(JSGObject):
    _reference_types = []
    
    def __init__(self,
                 stem: Union[IRI, Wildcard] = None,
                 exclusions: List[Union[IRI, IriStem]] = None,
                 **_kwargs: Dict[str, object]):
        self._context = _CONTEXT
        self.stem = stem
        self.exclusions = exclusions
        super().__init__(self._context, **_kwargs)


valueSetValue = Union[objectValue, IriStem, IriStemRange, LiteralStem, LiteralStemRange, LanguageStem, LanguageStemRange]

class Annotation(JSGObject):
    _reference_types = []
    
    def __init__(self,
                 predicate: IRI = None,
                 object: objectValue = None,
                 **_kwargs: Dict[str, object]):
        self._context = _CONTEXT
        self.predicate = predicate
        self.object = object
        super().__init__(self._context, **_kwargs)


class NodeConstraint(JSGObject):
    _reference_types = [xsFacet]
    
    def __init__(self,
                 id: Optional[shapeExprLabel] = None,
                 nodeKind: Optional[_Anon2] = None,
                 datatype: Optional[IRI] = None,
                 xsFacet: Optional[xsFacet] = None,
                 values: Optional[List[valueSetValue]] = None,
                 **_kwargs: Dict[str, object]):
        self._context = _CONTEXT
        self.id = id
        self.nodeKind = nodeKind
        self.datatype = datatype
        self.length = Integer(xsFacet.length) if xsFacet else Integer(None)
        self.minlength = Integer(xsFacet.minlength) if xsFacet else Integer(None)
        self.maxlength = Integer(xsFacet.maxlength) if xsFacet else Integer(None)
        self.pattern = String(xsFacet.pattern) if xsFacet else String(None)
        self.flags = String(xsFacet.flags) if xsFacet else String(None)
        self.mininclusive = Number(xsFacet.mininclusive) if xsFacet else Number(None)
        self.minexclusive = Number(xsFacet.minexclusive) if xsFacet else Number(None)
        self.maxinclusive = Number(xsFacet.maxinclusive) if xsFacet else Number(None)
        self.maxexclusive = Number(xsFacet.maxexclusive) if xsFacet else Number(None)
        self.totaldigits = Integer(xsFacet.totaldigits) if xsFacet else Integer(None)
        self.fractiondigits = Integer(xsFacet.fractiondigits) if xsFacet else Integer(None)
        self.values = values
        super().__init__(self._context, **_kwargs)


class Shape(JSGObject):
    _reference_types = []
    
    def __init__(self,
                 id: Optional[shapeExprLabel] = None,
                 virtual: Optional[bool] = None,
                 closed: Optional[bool] = None,
                 extra: Optional[List[IRI]] = None,
                 expression: Optional[tripleExprt_] = None,
                 inherit: Optional[List[shapeExprLabel]] = None,
                 semActs: Optional[List[SemAct]] = None,
                 annotations: Optional[List[Annotation]] = None,
                 **_kwargs: Dict[str, object]):
        self._context = _CONTEXT
        self.id = id
        self.virtual = Boolean(virtual)
        self.closed = Boolean(closed)
        self.extra = extra
        self.expression = expression
        self.inherit = inherit
        self.semActs = semActs
        self.annotations = annotations
        super().__init__(self._context, **_kwargs)


tripleExpr = Union[EachOft_, OneOft_, TripleConstraintt_, tripleExprLabel]

class EachOf(JSGObject):
    _reference_types = []
    
    def __init__(self,
                 id: Optional[tripleExprLabel] = None,
                 expressions: List[tripleExprt_] = None,
                 min: Optional[int] = None,
                 max: Optional[int] = None,
                 semActs: Optional[List[SemAct]] = None,
                 annotations: Optional[List[Annotation]] = None,
                 **_kwargs: Dict[str, object]):
        self._context = _CONTEXT
        self.id = id
        self.expressions = expressions
        self.min = Integer(min)
        self.max = Integer(max)
        self.semActs = semActs
        self.annotations = annotations
        super().__init__(self._context, **_kwargs)


class OneOf(JSGObject):
    _reference_types = []
    
    def __init__(self,
                 id: Optional[tripleExprLabel] = None,
                 expressions: List[tripleExprt_] = None,
                 min: Optional[int] = None,
                 max: Optional[int] = None,
                 semActs: Optional[List[SemAct]] = None,
                 annotations: Optional[List[Annotation]] = None,
                 **_kwargs: Dict[str, object]):
        self._context = _CONTEXT
        self.id = id
        self.expressions = expressions
        self.min = Integer(min)
        self.max = Integer(max)
        self.semActs = semActs
        self.annotations = annotations
        super().__init__(self._context, **_kwargs)


class TripleConstraint(JSGObject):
    _reference_types = []
    
    def __init__(self,
                 id: Optional[tripleExprLabel] = None,
                 inverse: Optional[bool] = None,
                 negated: Optional[bool] = None,
                 predicate: IRI = None,
                 valueExpr: Optional[shapeExprt_] = None,
                 min: Optional[int] = None,
                 max: Optional[int] = None,
                 semActs: Optional[List[SemAct]] = None,
                 annotations: Optional[List[Annotation]] = None,
                 **_kwargs: Dict[str, object]):
        self._context = _CONTEXT
        self.id = id
        self.inverse = Boolean(inverse)
        self.negated = Boolean(negated)
        self.predicate = predicate
        self.valueExpr = valueExpr
        self.min = Integer(min)
        self.max = Integer(max)
        self.semActs = semActs
        self.annotations = annotations
        super().__init__(self._context, **_kwargs)


class Schema(JSGObject):
    _reference_types = []
    
    def __init__(self,
                 startActs: Optional[List[SemAct]] = None,
                 start: Optional[shapeExprt_] = None,
                 shapes: Optional[List[shapeExprt_]] = None,
                 **_kwargs: Dict[str, object]):
        self._context = _CONTEXT
        setattr(self, '@context', _kwargs.pop('@context'))
        self.startActs = startActs
        self.start = start
        self.shapes = shapes
        super().__init__(self._context, **_kwargs)


shapeExpr = Union[ShapeOrt_, ShapeAndt_, ShapeNott_, NodeConstraint, Shapet_, shapeExprLabel, ShapeExternal]

fix_forwards(locals())

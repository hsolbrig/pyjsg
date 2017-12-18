# Auto generated from jsg/ShExJ.jsg by PyJSG version 0.3.1
# Generation date: 2017-12-17 21:15
#
from typing import Optional, Dict, List, Union, _ForwardRef

from pyjsg.jsglib import jsg
from pyjsg.jsglib import typing_patch

# .TYPE and .IGNORE settings
_CONTEXT = jsg.JSGContext()
_CONTEXT.TYPE = "type"
_CONTEXT.TYPE_EXCEPTIONS.append("ObjectLiteral")




class _Anon1(jsg.JSGString):
    pattern = jsg.JSGPattern(r'http\:\/\/www\.w3\.org\/ns\/shex\.jsonld')


class _Anon2(jsg.JSGString):
    pattern = jsg.JSGPattern(r'(iri)|(bnode)|(nonliteral)|(literal)')


class LANGTAG(jsg.JSGString):
    pattern = jsg.JSGPattern(r'[a-zA-Z]+(\-([a-zA-Z0-9])+)*')


class PN_CHARS_BASE(jsg.JSGString):
    pattern = jsg.JSGPattern(r'[A-Z]|[a-z]|[\u00C0-\u00D6]|[\u00D8-\u00F6]|[\u00F8-\u02FF]|[\u0370-\u037D]|[\u037F-\u1FFF]|[\u200C-\u200D]|[\u2070-\u218F]|[\u2C00-\u2FEF]|[\u3001-\uD7FF]|[\uF900-\uFDCF]|[\uFDF0-\uFFFD]|[\u10000-\uEFFFF]')


class HEX(jsg.JSGString):
    pattern = jsg.JSGPattern(r'[0-9]|[A-F]|[a-f]')


class PN_CHARS_U(jsg.JSGString):
    pattern = jsg.JSGPattern(r'({PN_CHARS_BASE})|_'.format(PN_CHARS_BASE=PN_CHARS_BASE.pattern))


class UCHAR(jsg.JSGString):
    pattern = jsg.JSGPattern(r'\\\\u({HEX})({HEX})({HEX})({HEX})|\\\\U({HEX})({HEX})({HEX})({HEX})({HEX})({HEX})({HEX})({HEX})'.format(HEX=HEX.pattern))


class IRIREF(jsg.JSGString):
    pattern = jsg.JSGPattern(r'([^\u0000-\u0020\u005C\u007B\u007D<>"|^`]|({UCHAR}))*'.format(UCHAR=UCHAR.pattern))


class PN_CHARS(jsg.JSGString):
    pattern = jsg.JSGPattern(r'({PN_CHARS_U})|\-|[0-9]|\\u00B7|[\u0300-\u036F]|[\u203F-\u2040]'.format(PN_CHARS_U=PN_CHARS_U.pattern))


class BNODE(jsg.JSGString):
    pattern = jsg.JSGPattern(r'_\:(({PN_CHARS_U})|[0-9])((({PN_CHARS})|\.)*({PN_CHARS}))?'.format(PN_CHARS=PN_CHARS.pattern, PN_CHARS_U=PN_CHARS_U.pattern))


class PN_PREFIX(jsg.JSGString):
    pattern = jsg.JSGPattern(r'({PN_CHARS_BASE})((({PN_CHARS})|\.)*({PN_CHARS}))?'.format(PN_CHARS=PN_CHARS.pattern, PN_CHARS_BASE=PN_CHARS_BASE.pattern))

class stringFacet_1_(jsg.JSGObject):
    _reference_types = []
    _members = {'length': int,
                'minlength': int,
                'maxlength': int}
    _strict = True
    
    def __init__(self,
                 length: int = None,
                 minlength: int = None,
                 maxlength: int = None,
                 **_kwargs: Dict[str, object]):
        self._context = _CONTEXT
        self.length = jsg.Integer(length)
        self.minlength = jsg.Integer(minlength)
        self.maxlength = jsg.Integer(maxlength)
        super().__init__(self._context, **_kwargs)


class stringFacet_2_(jsg.JSGObject):
    _reference_types = []
    _members = {'pattern': str,
                'flags': Optional[str]}
    _strict = True
    
    def __init__(self,
                 pattern: str = None,
                 flags: Optional[str] = None,
                 **_kwargs: Dict[str, object]):
        self._context = _CONTEXT
        self.pattern = jsg.String(pattern)
        self.flags = jsg.String(flags)
        super().__init__(self._context, **_kwargs)


class numericFacet(jsg.JSGObject):
    _reference_types = []
    _members = {'mininclusive': float,
                'minexclusive': float,
                'maxinclusive': float,
                'maxexclusive': float,
                'totaldigits': int,
                'fractiondigits': int}
    _strict = True
    
    def __init__(self,
                 mininclusive: float = None,
                 minexclusive: float = None,
                 maxinclusive: float = None,
                 maxexclusive: float = None,
                 totaldigits: int = None,
                 fractiondigits: int = None,
                 **_kwargs: Dict[str, object]):
        self._context = _CONTEXT
        self.mininclusive = jsg.Number(mininclusive)
        self.minexclusive = jsg.Number(minexclusive)
        self.maxinclusive = jsg.Number(maxinclusive)
        self.maxexclusive = jsg.Number(maxexclusive)
        self.totaldigits = jsg.Integer(totaldigits)
        self.fractiondigits = jsg.Integer(fractiondigits)
        super().__init__(self._context, **_kwargs)


class LiteralStem(jsg.JSGObject):
    _reference_types = []
    _members = {'stem': str}
    _strict = True
    
    def __init__(self,
                 stem: str = None,
                 **_kwargs: Dict[str, object]):
        self._context = _CONTEXT
        self.stem = jsg.String(stem)
        super().__init__(self._context, **_kwargs)


class Wildcard(jsg.JSGObject):
    _reference_types = []
    _members = {}
    _strict = True
    
    def __init__(self,
                 **_kwargs: Dict[str, object]):
        self._context = _CONTEXT
        super().__init__(self._context, **_kwargs)


class xsFacet_2_(jsg.JSGObject):
    _reference_types = [numericFacet]
    _members = {'mininclusive': float,
                'minexclusive': float,
                'maxinclusive': float,
                'maxexclusive': float,
                'totaldigits': int,
                'fractiondigits': int}
    _strict = True
    
    def __init__(self,
                 numericFacet: numericFacet = None,
                 **_kwargs: Dict[str, object]):
        self._context = _CONTEXT
        self.mininclusive = jsg.Number(numericFacet.mininclusive)
        self.minexclusive = jsg.Number(numericFacet.minexclusive)
        self.maxinclusive = jsg.Number(numericFacet.maxinclusive)
        self.maxexclusive = jsg.Number(numericFacet.maxexclusive)
        self.totaldigits = jsg.Integer(numericFacet.totaldigits)
        self.fractiondigits = jsg.Integer(numericFacet.fractiondigits)
        super().__init__(self._context, **_kwargs)


class stringFacet(jsg.JSGObject):
    _reference_types = [stringFacet_1_, stringFacet_2_]
    _members = {'length': int,
                'minlength': int,
                'maxlength': int,
                'pattern': str,
                'flags': Optional[str]}
    _strict = True
    
    def __init__(self,
                 opt_: Union[stringFacet_1_, stringFacet_2_] = None,
                 **_kwargs: Dict[str, object]):
        self._context = _CONTEXT
        self.length = jsg.Integer(opt_.length) if isinstance(opt_, stringFacet_1_) else jsg.Integer(None)
        self.minlength = jsg.Integer(opt_.minlength) if isinstance(opt_, stringFacet_1_) else jsg.Integer(None)
        self.maxlength = jsg.Integer(opt_.maxlength) if isinstance(opt_, stringFacet_1_) else jsg.Integer(None)
        self.pattern = jsg.String(opt_.pattern) if isinstance(opt_, stringFacet_2_) else jsg.String(None)
        self.flags = jsg.String(opt_.flags) if opt_ else jsg.String(None) if isinstance(opt_, stringFacet_2_) else jsg.String(None)
        super().__init__(self._context, **_kwargs)


class LiteralStemRange(jsg.JSGObject):
    _reference_types = []
    _members = {'stem': Union[str, Wildcard],
                'exclusions': List[Union[str, LiteralStem]]}
    _strict = True
    
    def __init__(self,
                 stem: Union[str, Wildcard] = None,
                 exclusions: List[Union[str, LiteralStem]] = None,
                 **_kwargs: Dict[str, object]):
        self._context = _CONTEXT
        self.stem = stem
        self.exclusions = exclusions
        super().__init__(self._context, **_kwargs)


class Language(jsg.JSGObject):
    _reference_types = []
    _members = {'languageTag': LANGTAG}
    _strict = True
    
    def __init__(self,
                 languageTag: LANGTAG = None,
                 **_kwargs: Dict[str, object]):
        self._context = _CONTEXT
        self.languageTag = languageTag
        super().__init__(self._context, **_kwargs)


class LanguageStem(jsg.JSGObject):
    _reference_types = []
    _members = {'stem': LANGTAG}
    _strict = True
    
    def __init__(self,
                 stem: LANGTAG = None,
                 **_kwargs: Dict[str, object]):
        self._context = _CONTEXT
        self.stem = stem
        super().__init__(self._context, **_kwargs)


class xsFacet_1_(jsg.JSGObject):
    _reference_types = [stringFacet]
    _members = {'length': int,
                'minlength': int,
                'maxlength': int,
                'pattern': str,
                'flags': Optional[str]}
    _strict = True
    
    def __init__(self,
                 stringFacet: stringFacet = None,
                 **_kwargs: Dict[str, object]):
        self._context = _CONTEXT
        self.length = jsg.Integer(stringFacet.length)
        self.minlength = jsg.Integer(stringFacet.minlength)
        self.maxlength = jsg.Integer(stringFacet.maxlength)
        self.pattern = jsg.String(stringFacet.pattern)
        self.flags = jsg.String(stringFacet.flags) if stringFacet else jsg.String(None)
        super().__init__(self._context, **_kwargs)


class LanguageStemRange(jsg.JSGObject):
    _reference_types = []
    _members = {'stem': Union[LANGTAG, Wildcard],
                'exclusions': List[Union[LANGTAG, LanguageStem]]}
    _strict = True
    
    def __init__(self,
                 stem: Union[LANGTAG, Wildcard] = None,
                 exclusions: List[Union[LANGTAG, LanguageStem]] = None,
                 **_kwargs: Dict[str, object]):
        self._context = _CONTEXT
        self.stem = stem
        self.exclusions = exclusions
        super().__init__(self._context, **_kwargs)


class xsFacet(jsg.JSGObject):
    _reference_types = [xsFacet_1_, xsFacet_2_]
    _members = {'length': int,
                'minlength': int,
                'maxlength': int,
                'pattern': str,
                'flags': Optional[str],
                'mininclusive': float,
                'minexclusive': float,
                'maxinclusive': float,
                'maxexclusive': float,
                'totaldigits': int,
                'fractiondigits': int}
    _strict = True
    
    def __init__(self,
                 opt_: Union[xsFacet_1_, xsFacet_2_] = None,
                 **_kwargs: Dict[str, object]):
        self._context = _CONTEXT
        self.length = jsg.Integer(opt_.length) if isinstance(opt_, xsFacet_1_) else jsg.Integer(None)
        self.minlength = jsg.Integer(opt_.minlength) if isinstance(opt_, xsFacet_1_) else jsg.Integer(None)
        self.maxlength = jsg.Integer(opt_.maxlength) if isinstance(opt_, xsFacet_1_) else jsg.Integer(None)
        self.pattern = jsg.String(opt_.pattern) if isinstance(opt_, xsFacet_1_) else jsg.String(None)
        self.flags = jsg.String(opt_.flags) if opt_ else jsg.String(None) if isinstance(opt_, xsFacet_1_) else jsg.String(None)
        self.mininclusive = jsg.Number(opt_.mininclusive) if isinstance(opt_, xsFacet_2_) else jsg.Number(None)
        self.minexclusive = jsg.Number(opt_.minexclusive) if isinstance(opt_, xsFacet_2_) else jsg.Number(None)
        self.maxinclusive = jsg.Number(opt_.maxinclusive) if isinstance(opt_, xsFacet_2_) else jsg.Number(None)
        self.maxexclusive = jsg.Number(opt_.maxexclusive) if isinstance(opt_, xsFacet_2_) else jsg.Number(None)
        self.totaldigits = jsg.Integer(opt_.totaldigits) if isinstance(opt_, xsFacet_2_) else jsg.Integer(None)
        self.fractiondigits = jsg.Integer(opt_.fractiondigits) if isinstance(opt_, xsFacet_2_) else jsg.Integer(None)
        super().__init__(self._context, **_kwargs)


class ObjectLiteral(jsg.JSGObject):
    _reference_types = []
    _members = {'value': str,
                'language': Optional[LANGTAG],
                'type': Optional[IRIREF]}
    _strict = True
    
    def __init__(self,
                 value: str = None,
                 language: Optional[LANGTAG] = None,
                 type: Optional[IRIREF] = None,
                 **_kwargs: Dict[str, object]):
        self._context = _CONTEXT
        self.value = jsg.String(value)
        self.language = language
        self.type = type
        super().__init__(self._context, **_kwargs)


class IriStem(jsg.JSGObject):
    _reference_types = []
    _members = {'stem': IRIREF}
    _strict = True
    
    def __init__(self,
                 stem: IRIREF = None,
                 **_kwargs: Dict[str, object]):
        self._context = _CONTEXT
        self.stem = stem
        super().__init__(self._context, **_kwargs)


class SemAct(jsg.JSGObject):
    _reference_types = []
    _members = {'name': IRIREF,
                'code': Optional[str]}
    _strict = True
    
    def __init__(self,
                 name: IRIREF = None,
                 code: Optional[str] = None,
                 **_kwargs: Dict[str, object]):
        self._context = _CONTEXT
        self.name = name
        self.code = jsg.String(code)
        super().__init__(self._context, **_kwargs)


shapeExprLabel = Union[IRIREF, BNODE]

objectValue = Union[IRIREF, ObjectLiteral]

class IriStemRange(jsg.JSGObject):
    _reference_types = []
    _members = {'stem': Union[IRIREF, Wildcard],
                'exclusions': List[Union[IRIREF, IriStem]]}
    _strict = True
    
    def __init__(self,
                 stem: Union[IRIREF, Wildcard] = None,
                 exclusions: List[Union[IRIREF, IriStem]] = None,
                 **_kwargs: Dict[str, object]):
        self._context = _CONTEXT
        self.stem = stem
        self.exclusions = exclusions
        super().__init__(self._context, **_kwargs)


tripleExprLabel = Union[IRIREF, BNODE]

class ShapeOr(jsg.JSGObject):
    _reference_types = []
    _members = {'id': Optional[shapeExprLabel],
                'shapeExprs': List["shapeExpr"]}
    _strict = True
    
    def __init__(self,
                 id: Optional[shapeExprLabel] = None,
                 shapeExprs: List["shapeExpr"] = None,
                 **_kwargs: Dict[str, object]):
        self._context = _CONTEXT
        self.id = id
        self.shapeExprs = shapeExprs
        super().__init__(self._context, **_kwargs)


class ShapeAnd(jsg.JSGObject):
    _reference_types = []
    _members = {'id': Optional[shapeExprLabel],
                'shapeExprs': List["shapeExpr"]}
    _strict = True
    
    def __init__(self,
                 id: Optional[shapeExprLabel] = None,
                 shapeExprs: List["shapeExpr"] = None,
                 **_kwargs: Dict[str, object]):
        self._context = _CONTEXT
        self.id = id
        self.shapeExprs = shapeExprs
        super().__init__(self._context, **_kwargs)


class ShapeNot(jsg.JSGObject):
    _reference_types = []
    _members = {'id': Optional[shapeExprLabel],
                'shapeExpr': "shapeExpr"}
    _strict = True
    
    def __init__(self,
                 id: Optional[shapeExprLabel] = None,
                 shapeExpr: "shapeExpr" = None,
                 **_kwargs: Dict[str, object]):
        self._context = _CONTEXT
        self.id = id
        self.shapeExpr = shapeExpr
        super().__init__(self._context, **_kwargs)


class ShapeExternal(jsg.JSGObject):
    _reference_types = []
    _members = {'id': Optional[shapeExprLabel]}
    _strict = True
    
    def __init__(self,
                 id: Optional[shapeExprLabel] = None,
                 **_kwargs: Dict[str, object]):
        self._context = _CONTEXT
        self.id = id
        super().__init__(self._context, **_kwargs)


valueSetValue = Union[objectValue, IriStem, IriStemRange, LiteralStem, LiteralStemRange, Language, LanguageStem, LanguageStemRange]

class Annotation(jsg.JSGObject):
    _reference_types = []
    _members = {'predicate': IRIREF,
                'object': objectValue}
    _strict = True
    
    def __init__(self,
                 predicate: IRIREF = None,
                 object: objectValue = None,
                 **_kwargs: Dict[str, object]):
        self._context = _CONTEXT
        self.predicate = predicate
        self.object = object
        super().__init__(self._context, **_kwargs)


class NodeConstraint(jsg.JSGObject):
    _reference_types = [xsFacet]
    _members = {'id': Optional[shapeExprLabel],
                'nodeKind': Optional[_Anon2],
                'datatype': Optional[IRIREF],
                'length': Optional[int],
                'minlength': Optional[int],
                'maxlength': Optional[int],
                'pattern': Optional[str],
                'flags': Optional[str],
                'mininclusive': Optional[float],
                'minexclusive': Optional[float],
                'maxinclusive': Optional[float],
                'maxexclusive': Optional[float],
                'totaldigits': Optional[int],
                'fractiondigits': Optional[int],
                'values': Optional[List[valueSetValue]]}
    _strict = True
    
    def __init__(self,
                 id: Optional[shapeExprLabel] = None,
                 nodeKind: Optional[_Anon2] = None,
                 datatype: Optional[IRIREF] = None,
                 xsFacet: Optional[xsFacet] = None,
                 values: Optional[List[valueSetValue]] = None,
                 **_kwargs: Dict[str, object]):
        self._context = _CONTEXT
        self.id = id
        self.nodeKind = nodeKind
        self.datatype = datatype
        self.length = jsg.Integer(xsFacet.length) if xsFacet else jsg.Integer(None)
        self.minlength = jsg.Integer(xsFacet.minlength) if xsFacet else jsg.Integer(None)
        self.maxlength = jsg.Integer(xsFacet.maxlength) if xsFacet else jsg.Integer(None)
        self.pattern = jsg.String(xsFacet.pattern) if xsFacet else jsg.String(None)
        self.flags = jsg.String(xsFacet.flags) if xsFacet else jsg.String(None)
        self.mininclusive = jsg.Number(xsFacet.mininclusive) if xsFacet else jsg.Number(None)
        self.minexclusive = jsg.Number(xsFacet.minexclusive) if xsFacet else jsg.Number(None)
        self.maxinclusive = jsg.Number(xsFacet.maxinclusive) if xsFacet else jsg.Number(None)
        self.maxexclusive = jsg.Number(xsFacet.maxexclusive) if xsFacet else jsg.Number(None)
        self.totaldigits = jsg.Integer(xsFacet.totaldigits) if xsFacet else jsg.Integer(None)
        self.fractiondigits = jsg.Integer(xsFacet.fractiondigits) if xsFacet else jsg.Integer(None)
        self.values = values
        super().__init__(self._context, **_kwargs)


class Shape(jsg.JSGObject):
    _reference_types = []
    _members = {'id': Optional[shapeExprLabel],
                'closed': Optional[bool],
                'extra': Optional[List[IRIREF]],
                'expression': Optional["tripleExpr"],
                'semActs': Optional[List[SemAct]],
                'annotations': Optional[List[Annotation]]}
    _strict = True
    
    def __init__(self,
                 id: Optional[shapeExprLabel] = None,
                 closed: Optional[bool] = None,
                 extra: Optional[List[IRIREF]] = None,
                 expression: Optional["tripleExpr"] = None,
                 semActs: Optional[List[SemAct]] = None,
                 annotations: Optional[List[Annotation]] = None,
                 **_kwargs: Dict[str, object]):
        self._context = _CONTEXT
        self.id = id
        self.closed = jsg.Boolean(closed)
        self.extra = extra
        self.expression = expression
        self.semActs = semActs
        self.annotations = annotations
        super().__init__(self._context, **_kwargs)


tripleExpr = Union["EachOf", "OneOf", "TripleConstraint", tripleExprLabel]

class EachOf(jsg.JSGObject):
    _reference_types = []
    _members = {'id': Optional[tripleExprLabel],
                'expressions': List["tripleExpr"],
                'min': Optional[int],
                'max': Optional[int],
                'semActs': Optional[List[SemAct]],
                'annotations': Optional[List[Annotation]]}
    _strict = True
    
    def __init__(self,
                 id: Optional[tripleExprLabel] = None,
                 expressions: List["tripleExpr"] = None,
                 min: Optional[int] = None,
                 max: Optional[int] = None,
                 semActs: Optional[List[SemAct]] = None,
                 annotations: Optional[List[Annotation]] = None,
                 **_kwargs: Dict[str, object]):
        self._context = _CONTEXT
        self.id = id
        self.expressions = expressions
        self.min = jsg.Integer(min)
        self.max = jsg.Integer(max)
        self.semActs = semActs
        self.annotations = annotations
        super().__init__(self._context, **_kwargs)


class OneOf(jsg.JSGObject):
    _reference_types = []
    _members = {'id': Optional[tripleExprLabel],
                'expressions': List["tripleExpr"],
                'min': Optional[int],
                'max': Optional[int],
                'semActs': Optional[List[SemAct]],
                'annotations': Optional[List[Annotation]]}
    _strict = True
    
    def __init__(self,
                 id: Optional[tripleExprLabel] = None,
                 expressions: List["tripleExpr"] = None,
                 min: Optional[int] = None,
                 max: Optional[int] = None,
                 semActs: Optional[List[SemAct]] = None,
                 annotations: Optional[List[Annotation]] = None,
                 **_kwargs: Dict[str, object]):
        self._context = _CONTEXT
        self.id = id
        self.expressions = expressions
        self.min = jsg.Integer(min)
        self.max = jsg.Integer(max)
        self.semActs = semActs
        self.annotations = annotations
        super().__init__(self._context, **_kwargs)


class TripleConstraint(jsg.JSGObject):
    _reference_types = []
    _members = {'id': Optional[tripleExprLabel],
                'inverse': Optional[bool],
                'predicate': IRIREF,
                'valueExpr': Optional["shapeExpr"],
                'min': Optional[int],
                'max': Optional[int],
                'semActs': Optional[List[SemAct]],
                'annotations': Optional[List[Annotation]]}
    _strict = True
    
    def __init__(self,
                 id: Optional[tripleExprLabel] = None,
                 inverse: Optional[bool] = None,
                 predicate: IRIREF = None,
                 valueExpr: Optional["shapeExpr"] = None,
                 min: Optional[int] = None,
                 max: Optional[int] = None,
                 semActs: Optional[List[SemAct]] = None,
                 annotations: Optional[List[Annotation]] = None,
                 **_kwargs: Dict[str, object]):
        self._context = _CONTEXT
        self.id = id
        self.inverse = jsg.Boolean(inverse)
        self.predicate = predicate
        self.valueExpr = valueExpr
        self.min = jsg.Integer(min)
        self.max = jsg.Integer(max)
        self.semActs = semActs
        self.annotations = annotations
        super().__init__(self._context, **_kwargs)


class Schema(jsg.JSGObject):
    _reference_types = []
    _members = {'@context': _Anon1,
                'imports': Optional[List[IRIREF]],
                'startActs': Optional[List[SemAct]],
                'start': Optional["shapeExpr"],
                'shapes': Optional[List["shapeExpr"]]}
    _strict = True
    
    def __init__(self,
                 imports: Optional[List[IRIREF]] = None,
                 startActs: Optional[List[SemAct]] = None,
                 start: Optional["shapeExpr"] = None,
                 shapes: Optional[List["shapeExpr"]] = None,
                 **_kwargs: Dict[str, object]):
        self._context = _CONTEXT
        setattr(self, '@context', _kwargs.pop('@context', None))
        self.imports = imports
        self.startActs = startActs
        self.start = start
        self.shapes = shapes
        super().__init__(self._context, **_kwargs)


shapeExpr = Union["ShapeOr", "ShapeAnd", "ShapeNot", NodeConstraint, "Shape", shapeExprLabel, ShapeExternal]

_CONTEXT.NAMESPACE = locals()

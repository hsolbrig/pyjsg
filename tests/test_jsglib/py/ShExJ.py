# Auto generated from tests/test_basics/jsg/ShExJ.jsg by PyJSG version 0.7.0
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
_CONTEXT.TYPE = "type"
_CONTEXT.TYPE_EXCEPTIONS.append("ObjectLiteral")


class _Anon1(JSGString):
    pattern = JSGPattern(r'http://www\.w3\.org/ns/shex\.jsonld')


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


class IRIREF(JSGString):
    pattern = JSGPattern(r'([^\u0000-\u0020\u005C\u007B\u007D<>"|^`]|({UCHAR}))*'.format(UCHAR=UCHAR.pattern))


class PN_CHARS(JSGString):
    pattern = JSGPattern(r'({PN_CHARS_U})|\-|[0-9]|\\u00B7|[\u0300-\u036F]|[\u203F-\u2040]'.format(PN_CHARS_U=PN_CHARS_U.pattern))


class BNODE(JSGString):
    pattern = JSGPattern(r'_:(({PN_CHARS_U})|[0-9])((({PN_CHARS})|\.)*({PN_CHARS}))?'.format(PN_CHARS=PN_CHARS.pattern, PN_CHARS_U=PN_CHARS_U.pattern))


class PN_PREFIX(JSGString):
    pattern = JSGPattern(r'({PN_CHARS_BASE})((({PN_CHARS})|\.)*({PN_CHARS}))?'.format(PN_CHARS=PN_CHARS.pattern, PN_CHARS_BASE=PN_CHARS_BASE.pattern))


class stringFacet_1_(JSGObject):
    _reference_types = []
    _members = {'length': Integer,
                'minlength': Integer,
                'maxlength': Integer}
    _strict = True

    def __init__(self,
                 length: int = None,
                 minlength: int = None,
                 maxlength: int = None,
                 **_kwargs: Dict[str, object]):
        super().__init__(_CONTEXT, **_kwargs)
        self.length = length
        self.minlength = minlength
        self.maxlength = maxlength


class stringFacet_2_(JSGObject):
    _reference_types = []
    _members = {'pattern': String,
                'flags': Optional[String]}
    _strict = True

    def __init__(self,
                 pattern: str = None,
                 flags: Optional[str] = None,
                 **_kwargs: Dict[str, object]):
        super().__init__(_CONTEXT, **_kwargs)
        self.pattern = pattern
        self.flags = flags


class numericFacet(JSGObject):
    _reference_types = []
    _members = {'mininclusive': Number,
                'minexclusive': Number,
                'maxinclusive': Number,
                'maxexclusive': Number,
                'totaldigits': Integer,
                'fractiondigits': Integer}
    _strict = True

    def __init__(self,
                 mininclusive: float = None,
                 minexclusive: float = None,
                 maxinclusive: float = None,
                 maxexclusive: float = None,
                 totaldigits: int = None,
                 fractiondigits: int = None,
                 **_kwargs: Dict[str, object]):
        super().__init__(_CONTEXT, **_kwargs)
        self.mininclusive = mininclusive
        self.minexclusive = minexclusive
        self.maxinclusive = maxinclusive
        self.maxexclusive = maxexclusive
        self.totaldigits = totaldigits
        self.fractiondigits = fractiondigits


class LiteralStem(JSGObject):
    _reference_types = []
    _members = {'stem': String}
    _strict = True

    def __init__(self,
                 stem: str = None,
                 **_kwargs: Dict[str, object]):
        super().__init__(_CONTEXT, **_kwargs)
        self.stem = stem


class Wildcard(JSGObject):
    _reference_types = []
    _members = {}
    _strict = True

    def __init__(self,
                 **_kwargs: Dict[str, object]):
        super().__init__(_CONTEXT, **_kwargs)


class xsFacet_2_(JSGObject):
    _reference_types = [numericFacet]
    _members = {'mininclusive': Number,
                'minexclusive': Number,
                'maxinclusive': Number,
                'maxexclusive': Number,
                'totaldigits': Integer,
                'fractiondigits': Integer}
    _strict = True

    def __init__(self,
                 mininclusive: float = None,
                 minexclusive: float = None,
                 maxinclusive: float = None,
                 maxexclusive: float = None,
                 totaldigits: int = None,
                 fractiondigits: int = None,
                 **_kwargs: Dict[str, object]):
        super().__init__(_CONTEXT, **_kwargs)
        self.mininclusive = mininclusive
        self.minexclusive = minexclusive
        self.maxinclusive = maxinclusive
        self.maxexclusive = maxexclusive
        self.totaldigits = totaldigits
        self.fractiondigits = fractiondigits


class stringFacet(JSGObject):
    _reference_types = [stringFacet_1_, stringFacet_2_]
    _members = {'length': Optional[Integer],
                'minlength': Optional[Integer],
                'maxlength': Optional[Integer],
                'pattern': Optional[String],
                'flags': Optional[String]}
    _strict = True

    def __init__(self,
                 opts_: Union[stringFacet_1_, stringFacet_2_] = None,
                 **_kwargs: Dict[str, object]):
        super().__init__(_CONTEXT, **_kwargs)
        if opts_ is not None:
            if isinstance(opts_, stringFacet_1_):
                self.length = opts_.length
                self.minlength = opts_.minlength
                self.maxlength = opts_.maxlength
            elif isinstance(opts_, stringFacet_2_):
                self.pattern = opts_.pattern
                self.flags = opts_.flags
            else:
                raise ValueError(f"Unrecognized value type: {opts_}")


class LiteralStemRange(JSGObject):
    _reference_types = []
    _members = {'stem': Union[String, Wildcard],
                'exclusions': ArrayFactory('exclusions', _CONTEXT, Union[String, LiteralStem], 1, None)}
    _strict = True

    def __init__(self,
                 stem: Union[str, Wildcard] = None,
                 exclusions: List[Union[str, LiteralStem]] = None,
                 **_kwargs: Dict[str, object]):
        super().__init__(_CONTEXT, **_kwargs)
        self.stem = stem
        self.exclusions = exclusions


class Language(JSGObject):
    _reference_types = []
    _members = {'languageTag': LANGTAG}
    _strict = True

    def __init__(self,
                 languageTag: str = None,
                 **_kwargs: Dict[str, object]):
        super().__init__(_CONTEXT, **_kwargs)
        self.languageTag = languageTag


class LanguageStem(JSGObject):
    _reference_types = []
    _members = {'stem': LANGTAG}
    _strict = True

    def __init__(self,
                 stem: str = None,
                 **_kwargs: Dict[str, object]):
        super().__init__(_CONTEXT, **_kwargs)
        self.stem = stem


class xsFacet_1_(JSGObject):
    _reference_types = [stringFacet]
    _members = {'length': Optional[Integer],
                'minlength': Optional[Integer],
                'maxlength': Optional[Integer],
                'pattern': Optional[String],
                'flags': Optional[String]}
    _strict = True

    def __init__(self,
                 opts_: Union[stringFacet_1_, stringFacet_2_] = None,
                 **_kwargs: Dict[str, object]):
        super().__init__(_CONTEXT, **_kwargs)
        if opts_ is not None:
            if isinstance(opts_, stringFacet_1_):
                self.length = opts_.length
                self.minlength = opts_.minlength
                self.maxlength = opts_.maxlength
            elif isinstance(opts_, stringFacet_2_):
                self.pattern = opts_.pattern
                self.flags = opts_.flags
            else:
                raise ValueError(f"Unrecognized value type: {opts_}")


class LanguageStemRange(JSGObject):
    _reference_types = []
    _members = {'stem': Union[LANGTAG, Wildcard],
                'exclusions': ArrayFactory('exclusions', _CONTEXT, Union[LANGTAG, LanguageStem], 1, None)}
    _strict = True

    def __init__(self,
                 stem: Union[str, Wildcard] = None,
                 exclusions: List[Union[str, LanguageStem]] = None,
                 **_kwargs: Dict[str, object]):
        super().__init__(_CONTEXT, **_kwargs)
        self.stem = stem
        self.exclusions = exclusions


class xsFacet(JSGObject):
    _reference_types = [xsFacet_1_, xsFacet_2_]
    _members = {'length': Optional[Optional[Integer]],
                'minlength': Optional[Optional[Integer]],
                'maxlength': Optional[Optional[Integer]],
                'pattern': Optional[Optional[String]],
                'flags': Optional[Optional[String]],
                'mininclusive': Optional[Optional[Number]],
                'minexclusive': Optional[Optional[Number]],
                'maxinclusive': Optional[Optional[Number]],
                'maxexclusive': Optional[Optional[Number]],
                'totaldigits': Optional[Optional[Integer]],
                'fractiondigits': Optional[Optional[Integer]]}
    _strict = True

    def __init__(self,
                 opts_: Union[xsFacet_1_, xsFacet_2_] = None,
                 **_kwargs: Dict[str, object]):
        super().__init__(_CONTEXT, **_kwargs)
        if opts_ is not None:
            if isinstance(opts_, xsFacet_1_):
                if opts_ is not None:
                    if isinstance(opts_, stringFacet_1_):
                        self.length = opts_.length
                        self.minlength = opts_.minlength
                        self.maxlength = opts_.maxlength
                    elif isinstance(opts_, stringFacet_2_):
                        self.pattern = opts_.pattern
                        self.flags = opts_.flags
                    else:
                        raise ValueError(f"Unrecognized value type: {opts_}")
            elif isinstance(opts_, xsFacet_2_):
                self.mininclusive = opts_.mininclusive
                self.minexclusive = opts_.minexclusive
                self.maxinclusive = opts_.maxinclusive
                self.maxexclusive = opts_.maxexclusive
                self.totaldigits = opts_.totaldigits
                self.fractiondigits = opts_.fractiondigits
            else:
                raise ValueError(f"Unrecognized value type: {opts_}")


class ObjectLiteral(JSGObject):
    _reference_types = []
    _members = {'value': String,
                'language': Optional[LANGTAG],
                'type': Optional[IRIREF]}
    _strict = True

    def __init__(self,
                 value: str = None,
                 language: Optional[str] = None,
                 type: Optional[str] = None,
                 **_kwargs: Dict[str, object]):
        super().__init__(_CONTEXT, **_kwargs)
        self.value = value
        self.language = language
        self.type = type


class IriStem(JSGObject):
    _reference_types = []
    _members = {'stem': IRIREF}
    _strict = True

    def __init__(self,
                 stem: str = None,
                 **_kwargs: Dict[str, object]):
        super().__init__(_CONTEXT, **_kwargs)
        self.stem = stem


class SemAct(JSGObject):
    _reference_types = []
    _members = {'name': IRIREF,
                'code': Optional[String]}
    _strict = True

    def __init__(self,
                 name: str = None,
                 code: Optional[str] = None,
                 **_kwargs: Dict[str, object]):
        super().__init__(_CONTEXT, **_kwargs)
        self.name = name
        self.code = code



shapeExprLabel = Union[IRIREF, BNODE]

objectValue = Union[IRIREF, ObjectLiteral]
class IriStemRange(JSGObject):
    _reference_types = []
    _members = {'stem': Union[IRIREF, Wildcard],
                'exclusions': ArrayFactory('exclusions', _CONTEXT, Union[IRIREF, IriStem], 1, None)}
    _strict = True

    def __init__(self,
                 stem: Union[str, Wildcard] = None,
                 exclusions: List[Union[str, IriStem]] = None,
                 **_kwargs: Dict[str, object]):
        super().__init__(_CONTEXT, **_kwargs)
        self.stem = stem
        self.exclusions = exclusions



tripleExprLabel = Union[IRIREF, BNODE]
class ShapeExternal(JSGObject):
    _reference_types = []
    _members = {'id': Optional[Union[IRIREF, BNODE]]}
    _strict = True

    def __init__(self,
                 id: Optional[Union[str, str]] = None,
                 **_kwargs: Dict[str, object]):
        super().__init__(_CONTEXT, **_kwargs)
        self.id = id



valueSetValue = Union[Union[IRIREF, ObjectLiteral], IriStem, IriStemRange, LiteralStem, LiteralStemRange, Language, LanguageStem, LanguageStemRange]
class Annotation(JSGObject):
    _reference_types = []
    _members = {'predicate': IRIREF,
                'object': Union[IRIREF, ObjectLiteral]}
    _strict = True

    def __init__(self,
                 predicate: str = None,
                 object: Union[str, ObjectLiteral] = None,
                 **_kwargs: Dict[str, object]):
        super().__init__(_CONTEXT, **_kwargs)
        self.predicate = predicate
        self.object = object


class NodeConstraint(JSGObject):
    _reference_types = [xsFacet]
    _members = {'id': Optional[Union[IRIREF, BNODE]],
                'nodeKind': Optional[_Anon2],
                'datatype': Optional[IRIREF],
                'length': Optional[Optional[Integer]],
                'minlength': Optional[Optional[Integer]],
                'maxlength': Optional[Optional[Integer]],
                'pattern': Optional[Optional[String]],
                'flags': Optional[Optional[String]],
                'mininclusive': Optional[Optional[Number]],
                'minexclusive': Optional[Optional[Number]],
                'maxinclusive': Optional[Optional[Number]],
                'maxexclusive': Optional[Optional[Number]],
                'totaldigits': Optional[Optional[Integer]],
                'fractiondigits': Optional[Optional[Integer]],
                'values': Optional[ArrayFactory('values', _CONTEXT, Union[Union[IRIREF, ObjectLiteral], IriStem, IriStemRange, LiteralStem, LiteralStemRange, Language, LanguageStem, LanguageStemRange], 1, None)]}
    _strict = True

    def __init__(self,
                 id: Optional[Union[str, str]] = None,
                 nodeKind: Optional[str] = None,
                 datatype: Optional[str] = None,
                 opts_: Union[xsFacet_1_, xsFacet_2_] = None,
                 values: Optional[List[Union[Union[str, ObjectLiteral], IriStem, IriStemRange, LiteralStem, LiteralStemRange, Language, LanguageStem, LanguageStemRange]]] = None,
                 **_kwargs: Dict[str, object]):
        super().__init__(_CONTEXT, **_kwargs)
        self.id = id
        self.nodeKind = nodeKind
        self.datatype = datatype
        if opts_ is not None:
            if isinstance(opts_, xsFacet_1_):
                if opts_ is not None:
                    if isinstance(opts_, stringFacet_1_):
                        self.length = opts_.length
                        self.minlength = opts_.minlength
                        self.maxlength = opts_.maxlength
                    elif isinstance(opts_, stringFacet_2_):
                        self.pattern = opts_.pattern
                        self.flags = opts_.flags
                    else:
                        raise ValueError(f"Unrecognized value type: {opts_}")
            elif isinstance(opts_, xsFacet_2_):
                self.mininclusive = opts_.mininclusive
                self.minexclusive = opts_.minexclusive
                self.maxinclusive = opts_.maxinclusive
                self.maxexclusive = opts_.maxexclusive
                self.totaldigits = opts_.totaldigits
                self.fractiondigits = opts_.fractiondigits
            else:
                raise ValueError(f"Unrecognized value type: {opts_}")
        self.values = values


class Schema(JSGObject):
    _reference_types = []
    _members = {'@context': _Anon1,
                'imports': Optional[ArrayFactory('imports', _CONTEXT, IRIREF, 1, None)],
                'startActs': Optional[ArrayFactory('startActs', _CONTEXT, SemAct, 1, None)],
                'start': Optional[Union["ShapeOr", "ShapeAnd", "ShapeNot", NodeConstraint, "Shape", Union[IRIREF, BNODE], ShapeExternal]],
                'shapes': Optional[ArrayFactory('shapes', _CONTEXT, Union["ShapeOr", "ShapeAnd", "ShapeNot", NodeConstraint, "Shape", Union[IRIREF, BNODE], ShapeExternal], 1, None)]}
    _strict = True

    def __init__(self,
                 imports: Optional[List[str]] = None,
                 startActs: Optional[List[SemAct]] = None,
                 start: Optional[Union["ShapeOr", "ShapeAnd", "ShapeNot", NodeConstraint, "Shape", Union[str, str], ShapeExternal]] = None,
                 shapes: Optional[List[Union["ShapeOr", "ShapeAnd", "ShapeNot", NodeConstraint, "Shape", Union[str, str], ShapeExternal]]] = None,
                 **_kwargs: Dict[str, object]):
        super().__init__(_CONTEXT, **_kwargs)
        setattr(self, '@context', _kwargs.get('@context', None))
        self.imports = imports
        self.startActs = startActs
        self.start = start
        self.shapes = shapes


class ShapeOr(JSGObject):
    _reference_types = []
    _members = {'id': Optional[Union[IRIREF, BNODE]],
                'shapeExprs': ArrayFactory('shapeExprs', _CONTEXT, Union["ShapeOr", "ShapeAnd", "ShapeNot", NodeConstraint, "Shape", Union[IRIREF, BNODE], ShapeExternal], 2, None)}
    _strict = True

    def __init__(self,
                 id: Optional[Union[str, str]] = None,
                 shapeExprs: List[Union["ShapeOr", "ShapeAnd", "ShapeNot", NodeConstraint, "Shape", Union[str, str], ShapeExternal]] = None,
                 **_kwargs: Dict[str, object]):
        super().__init__(_CONTEXT, **_kwargs)
        self.id = id
        self.shapeExprs = shapeExprs


class ShapeAnd(JSGObject):
    _reference_types = []
    _members = {'id': Optional[Union[IRIREF, BNODE]],
                'shapeExprs': ArrayFactory('shapeExprs', _CONTEXT, Union[ShapeOr, "ShapeAnd", "ShapeNot", NodeConstraint, "Shape", Union[IRIREF, BNODE], ShapeExternal], 2, None)}
    _strict = True

    def __init__(self,
                 id: Optional[Union[str, str]] = None,
                 shapeExprs: List[Union[ShapeOr, "ShapeAnd", "ShapeNot", NodeConstraint, "Shape", Union[str, str], ShapeExternal]] = None,
                 **_kwargs: Dict[str, object]):
        super().__init__(_CONTEXT, **_kwargs)
        self.id = id
        self.shapeExprs = shapeExprs


class ShapeNot(JSGObject):
    _reference_types = []
    _members = {'id': Optional[Union[IRIREF, BNODE]],
                'shapeExpr': Union[ShapeOr, ShapeAnd, "ShapeNot", NodeConstraint, "Shape", Union[IRIREF, BNODE], ShapeExternal]}
    _strict = True

    def __init__(self,
                 id: Optional[Union[str, str]] = None,
                 shapeExpr: Union[ShapeOr, ShapeAnd, "ShapeNot", NodeConstraint, "Shape", Union[str, str], ShapeExternal] = None,
                 **_kwargs: Dict[str, object]):
        super().__init__(_CONTEXT, **_kwargs)
        self.id = id
        self.shapeExpr = shapeExpr


class Shape(JSGObject):
    _reference_types = []
    _members = {'id': Optional[Union[IRIREF, BNODE]],
                'closed': Optional[Boolean],
                'extra': Optional[ArrayFactory('extra', _CONTEXT, IRIREF, 1, None)],
                'expression': Optional[Union["EachOf", "OneOf", "TripleConstraint", Union[IRIREF, BNODE]]],
                'semActs': Optional[ArrayFactory('semActs', _CONTEXT, SemAct, 1, None)],
                'annotations': Optional[ArrayFactory('annotations', _CONTEXT, Annotation, 1, None)]}
    _strict = True

    def __init__(self,
                 id: Optional[Union[str, str]] = None,
                 closed: Optional[bool] = None,
                 extra: Optional[List[str]] = None,
                 expression: Optional[Union["EachOf", "OneOf", "TripleConstraint", Union[str, str]]] = None,
                 semActs: Optional[List[SemAct]] = None,
                 annotations: Optional[List[Annotation]] = None,
                 **_kwargs: Dict[str, object]):
        super().__init__(_CONTEXT, **_kwargs)
        self.id = id
        self.closed = closed
        self.extra = extra
        self.expression = expression
        self.semActs = semActs
        self.annotations = annotations



tripleExpr = Union["EachOf", "OneOf", "TripleConstraint", Union[IRIREF, BNODE]]
class EachOf(JSGObject):
    _reference_types = []
    _members = {'id': Optional[Union[IRIREF, BNODE]],
                'expressions': ArrayFactory('expressions', _CONTEXT, Union["EachOf", "OneOf", "TripleConstraint", Union[IRIREF, BNODE]], 2, None),
                'min': Optional[Integer],
                'max': Optional[Integer],
                'semActs': Optional[ArrayFactory('semActs', _CONTEXT, SemAct, 1, None)],
                'annotations': Optional[ArrayFactory('annotations', _CONTEXT, Annotation, 1, None)]}
    _strict = True

    def __init__(self,
                 id: Optional[Union[str, str]] = None,
                 expressions: List[Union["EachOf", "OneOf", "TripleConstraint", Union[str, str]]] = None,
                 min: Optional[int] = None,
                 max: Optional[int] = None,
                 semActs: Optional[List[SemAct]] = None,
                 annotations: Optional[List[Annotation]] = None,
                 **_kwargs: Dict[str, object]):
        super().__init__(_CONTEXT, **_kwargs)
        self.id = id
        self.expressions = expressions
        self.min = min
        self.max = max
        self.semActs = semActs
        self.annotations = annotations


class OneOf(JSGObject):
    _reference_types = []
    _members = {'id': Optional[Union[IRIREF, BNODE]],
                'expressions': ArrayFactory('expressions', _CONTEXT, Union[EachOf, "OneOf", "TripleConstraint", Union[IRIREF, BNODE]], 2, None),
                'min': Optional[Integer],
                'max': Optional[Integer],
                'semActs': Optional[ArrayFactory('semActs', _CONTEXT, SemAct, 1, None)],
                'annotations': Optional[ArrayFactory('annotations', _CONTEXT, Annotation, 1, None)]}
    _strict = True

    def __init__(self,
                 id: Optional[Union[str, str]] = None,
                 expressions: List[Union[EachOf, "OneOf", "TripleConstraint", Union[str, str]]] = None,
                 min: Optional[int] = None,
                 max: Optional[int] = None,
                 semActs: Optional[List[SemAct]] = None,
                 annotations: Optional[List[Annotation]] = None,
                 **_kwargs: Dict[str, object]):
        super().__init__(_CONTEXT, **_kwargs)
        self.id = id
        self.expressions = expressions
        self.min = min
        self.max = max
        self.semActs = semActs
        self.annotations = annotations


class TripleConstraint(JSGObject):
    _reference_types = []
    _members = {'id': Optional[Union[IRIREF, BNODE]],
                'inverse': Optional[Boolean],
                'predicate': IRIREF,
                'valueExpr': Optional[Union[ShapeOr, ShapeAnd, ShapeNot, NodeConstraint, Shape, Union[IRIREF, BNODE], ShapeExternal]],
                'min': Optional[Integer],
                'max': Optional[Integer],
                'semActs': Optional[ArrayFactory('semActs', _CONTEXT, SemAct, 1, None)],
                'annotations': Optional[ArrayFactory('annotations', _CONTEXT, Annotation, 1, None)]}
    _strict = True

    def __init__(self,
                 id: Optional[Union[str, str]] = None,
                 inverse: Optional[bool] = None,
                 predicate: str = None,
                 valueExpr: Optional[Union[ShapeOr, ShapeAnd, ShapeNot, NodeConstraint, Shape, Union[str, str], ShapeExternal]] = None,
                 min: Optional[int] = None,
                 max: Optional[int] = None,
                 semActs: Optional[List[SemAct]] = None,
                 annotations: Optional[List[Annotation]] = None,
                 **_kwargs: Dict[str, object]):
        super().__init__(_CONTEXT, **_kwargs)
        self.id = id
        self.inverse = inverse
        self.predicate = predicate
        self.valueExpr = valueExpr
        self.min = min
        self.max = max
        self.semActs = semActs
        self.annotations = annotations



shapeExpr = Union[ShapeOr, ShapeAnd, ShapeNot, NodeConstraint, Shape, Union[IRIREF, BNODE], ShapeExternal]
_CONTEXT.NAMESPACE = locals()

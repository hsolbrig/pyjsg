# Auto generated from jsg/ShExJ.jsg by PyJSG version 0.1.2
# Generation date: 2017-03-29 14:02
#
from typing import Optional, Dict, List, Union, _ForwardRef

from pyjsg.jsglib.jsg import JSGString, JSGPattern, JSGObject, JSGContext
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


class _A1(JSGString):
    pattern = JSGPattern(r'iri|bnode|nonliteral|literal')


class BOOL(JSGString):
    pattern = JSGPattern(r'true|false')


class INTEGER(JSGString):
    pattern = JSGPattern(r'[+-]?[0-9]+')


class DECIMAL(JSGString):
    pattern = JSGPattern(r'[+-]?[0-9]*\.[0-9]+')


class STRING(JSGString):
    pattern = JSGPattern(r'.*')


class PN_CHARS_BASE(JSGString):
    pattern = JSGPattern(r'[A-Z]|[a-z]|[\u00C0-\u00D6]|[\u00D8-\u00F6]|[\u00F8-\u02FF]|[\u0370-\u037D]|[\u037F-\u1FFF]|[\u200C-\u200D]|[\u2070-\u218F]|[\u2C00-\u2FEF]|[\u3001-\uD7FF]|[\uF900-\uFDCF]|[\uFDF0-\uFFFD]|[\u10000-\uEFFFF]')


class HEX(JSGString):
    pattern = JSGPattern(r'[0-9]|[A-F]|[a-f]')


class EXPONENT(JSGString):
    pattern = JSGPattern(r'[eE][+-]?[0-9]+')


class LANGTAG(JSGString):
    pattern = JSGPattern(r'\@[a-zA-Z]+(\-[a-zA-Z0-9]+)*')


class DOUBLE(JSGString):
    pattern = JSGPattern(r'[+-]?([0-9]+\.[0-9]*{EXPONENT}|\.[0-9]+{EXPONENT}|[0-9]+{EXPONENT})'.format(EXPONENT=EXPONENT.pattern))


class PN_CHARS_U(JSGString):
    pattern = JSGPattern(r'{PN_CHARS_BASE}|_'.format(PN_CHARS_BASE=PN_CHARS_BASE.pattern))


class UCHAR(JSGString):
    pattern = JSGPattern(r'\\\\u{HEX}{HEX}{HEX}{HEX}|\\\\U{HEX}{HEX}{HEX}{HEX}{HEX}{HEX}{HEX}{HEX}'.format(HEX=HEX.pattern))


class PN_CHARS(JSGString):
    pattern = JSGPattern(r'{PN_CHARS_U}|\-|[0-9]|\\u00B7|[\u0300-\u036F]|[\u203F-\u2040]'.format(PN_CHARS_U=PN_CHARS_U.pattern))


class IRI(JSGString):
    pattern = JSGPattern(r'({PN_CHARS}|\.|\:|\/|\\\\|\#|\@|\%|\&|{UCHAR})*'.format(UCHAR=UCHAR.pattern, PN_CHARS=PN_CHARS.pattern))


class BNODE(JSGString):
    pattern = JSGPattern(r'_\:({PN_CHARS_U}|[0-9])(({PN_CHARS}|\.)*{PN_CHARS})?'.format(PN_CHARS=PN_CHARS.pattern, PN_CHARS_U=PN_CHARS_U.pattern))


class PN_PREFIX(JSGString):
    pattern = JSGPattern(r'{PN_CHARS_BASE}(({PN_CHARS}|\.)*{PN_CHARS})?'.format(PN_CHARS=PN_CHARS.pattern, PN_CHARS_BASE=PN_CHARS_BASE.pattern))

class Wildcard(JSGObject):
    def __init__(self,
                 **_extra: Dict[str, object]):
        JSGObject.__init__(self, _CONTEXT, **_extra)
        


class ObjectLiteral(JSGObject):
    def __init__(self,
                 value: STRING = None,
                 language: Optional[STRING] = None,
                 type: Optional[STRING] = None,
                 **_extra: Dict[str, object]):
        JSGObject.__init__(self, _CONTEXT, **_extra)
        self.value = value
        self.language = language
        self.type = type


class LiteralStem(JSGObject):
    def __init__(self,
                 stem: ObjectLiteral = None,
                 **_extra: Dict[str, object]):
        JSGObject.__init__(self, _CONTEXT, **_extra)
        self.stem = stem


class LanguageStem(JSGObject):
    def __init__(self,
                 stem: ObjectLiteral = None,
                 **_extra: Dict[str, object]):
        JSGObject.__init__(self, _CONTEXT, **_extra)
        self.stem = stem


class ShapeExternal(JSGObject):
    def __init__(self,
                 id: Optional[Union[IRI, BNODE]] = None,
                 **_extra: Dict[str, object]):
        JSGObject.__init__(self, _CONTEXT, **_extra)
        self.id = id


class IriStem(JSGObject):
    def __init__(self,
                 stem: IRI = None,
                 **_extra: Dict[str, object]):
        JSGObject.__init__(self, _CONTEXT, **_extra)
        self.stem = stem


class LiteralStemRange(JSGObject):
    def __init__(self,
                 stem: Union[ObjectLiteral, Wildcard] = None,
                 exclusions: Optional[List[Union[IRI, ObjectLiteral, LiteralStem]]] = None,
                 **_extra: Dict[str, object]):
        JSGObject.__init__(self, _CONTEXT, **_extra)
        self.stem = stem
        self.exclusions = exclusions


class LanguageStemRange(JSGObject):
    def __init__(self,
                 stem: Union[ObjectLiteral, Wildcard] = None,
                 exclusions: Optional[List[Union[IRI, ObjectLiteral, LanguageStem]]] = None,
                 **_extra: Dict[str, object]):
        JSGObject.__init__(self, _CONTEXT, **_extra)
        self.stem = stem
        self.exclusions = exclusions


class SemAct(JSGObject):
    def __init__(self,
                 name: IRI = None,
                 code: Optional[STRING] = None,
                 **_extra: Dict[str, object]):
        JSGObject.__init__(self, _CONTEXT, **_extra)
        self.name = name
        self.code = code


class Annotation(JSGObject):
    def __init__(self,
                 predicate: IRI = None,
                 object: Union[IRI, ObjectLiteral] = None,
                 **_extra: Dict[str, object]):
        JSGObject.__init__(self, _CONTEXT, **_extra)
        self.predicate = predicate
        self.object = object


class Shape(JSGObject):
    def __init__(self,
                 id: Optional[Union[IRI, BNODE]] = None,
                 virtual: Optional[BOOL] = None,
                 closed: Optional[BOOL] = None,
                 extra: Optional[List[IRI]] = None,
                 expression: Optional[Union[EachOft_, OneOft_, TripleConstraintt_, IRI, BNODE]] = None,
                 inherit: Optional[List[Union[IRI, BNODE]]] = None,
                 semActs: Optional[List[SemAct]] = None,
                 **_extra: Dict[str, object]):
        JSGObject.__init__(self, _CONTEXT, **_extra)
        self.id = id
        self.virtual = virtual
        self.closed = closed
        self.extra = extra
        self.expression = expression
        self.inherit = inherit
        self.semActs = semActs


class EachOf(JSGObject):
    def __init__(self,
                 id: Optional[Union[IRI, BNODE]] = None,
                 expressions: List[Union[EachOft_, OneOft_, TripleConstraintt_, IRI, BNODE]] = None,
                 min: Optional[INTEGER] = None,
                 max: Optional[INTEGER] = None,
                 semActs: Optional[List[SemAct]] = None,
                 annotations: Optional[List[Annotation]] = None,
                 **_extra: Dict[str, object]):
        JSGObject.__init__(self, _CONTEXT, **_extra)
        self.id = id
        self.expressions = expressions
        self.min = min
        self.max = max
        self.semActs = semActs
        self.annotations = annotations


class OneOf(JSGObject):
    def __init__(self,
                 id: Optional[Union[IRI, BNODE]] = None,
                 expressions: List[Union[EachOft_, OneOft_, TripleConstraintt_, IRI, BNODE]] = None,
                 min: Optional[INTEGER] = None,
                 max: Optional[INTEGER] = None,
                 semActs: Optional[List[SemAct]] = None,
                 annotations: Optional[List[Annotation]] = None,
                 **_extra: Dict[str, object]):
        JSGObject.__init__(self, _CONTEXT, **_extra)
        self.id = id
        self.expressions = expressions
        self.min = min
        self.max = max
        self.semActs = semActs
        self.annotations = annotations


class IriStemRange(JSGObject):
    def __init__(self,
                 stem: Union[IRI, Wildcard] = None,
                 exclusions: Optional[List[Union[IRI, ObjectLiteral, IriStem]]] = None,
                 **_extra: Dict[str, object]):
        JSGObject.__init__(self, _CONTEXT, **_extra)
        self.stem = stem
        self.exclusions = exclusions


class NodeConstraint(JSGObject):
    def __init__(self,
                 id: Optional[Union[IRI, BNODE]] = None,
                 nodeKind: Optional[_A1] = None,
                 datatype: Optional[IRI] = None,
                 length: Optional[INTEGER] = None,
                 minlength: Optional[INTEGER] = None,
                 maxlength: Optional[INTEGER] = None,
                 pattern: Optional[STRING] = None,
                 flags: Optional[STRING] = None,
                 mininclusive: Optional[Union[INTEGER, DECIMAL, DOUBLE]] = None,
                 minexclusive: Optional[Union[INTEGER, DECIMAL, DOUBLE]] = None,
                 maxinclusive: Optional[Union[INTEGER, DECIMAL, DOUBLE]] = None,
                 maxexclusive: Optional[Union[INTEGER, DECIMAL, DOUBLE]] = None,
                 totaldigits: Optional[INTEGER] = None,
                 fractiondigits: Optional[INTEGER] = None,
                 values: Optional[List[Union[IRI, ObjectLiteral, IriStem, IriStemRange, LiteralStem, LiteralStemRange, LanguageStem, LanguageStemRange]]] = None,
                 **_extra: Dict[str, object]):
        JSGObject.__init__(self, _CONTEXT, **_extra)
        self.id = id
        self.nodeKind = nodeKind
        self.datatype = datatype
        self.length = length
        self.minlength = minlength
        self.maxlength = maxlength
        self.pattern = pattern
        self.flags = flags
        self.mininclusive = mininclusive
        self.minexclusive = minexclusive
        self.maxinclusive = maxinclusive
        self.maxexclusive = maxexclusive
        self.totaldigits = totaldigits
        self.fractiondigits = fractiondigits
        self.values = values


class Schema(JSGObject):
    def __init__(self,
                 startActs: Optional[List[SemAct]] = None,
                 start: Optional[Union[ShapeOrt_, ShapeAndt_, ShapeNott_, NodeConstraint, Shapet_, IRI, BNODE, ShapeExternal]] = None,
                 shapes: Optional[List[Union[ShapeOrt_, ShapeAndt_, ShapeNott_, NodeConstraint, Shapet_, IRI, BNODE, ShapeExternal]]] = None,
                 **_extra: Dict[str, object]):
        JSGObject.__init__(self, _CONTEXT, **_extra)
        setattr(self, '@context', "http://www.w3.org/ns/shex.jsonld")
        self.startActs = startActs
        self.start = start
        self.shapes = shapes


class ShapeOr(JSGObject):
    def __init__(self,
                 id: Optional[Union[IRI, BNODE]] = None,
                 shapeExprs: List[Union[ShapeOrt_, ShapeAndt_, ShapeNott_, NodeConstraint, Shapet_, IRI, BNODE, ShapeExternal]] = None,
                 **_extra: Dict[str, object]):
        JSGObject.__init__(self, _CONTEXT, **_extra)
        self.id = id
        self.shapeExprs = shapeExprs


class ShapeAnd(JSGObject):
    def __init__(self,
                 id: Optional[Union[IRI, BNODE]] = None,
                 shapeExprs: List[Union[ShapeOrt_, ShapeAndt_, ShapeNott_, NodeConstraint, Shapet_, IRI, BNODE, ShapeExternal]] = None,
                 **_extra: Dict[str, object]):
        JSGObject.__init__(self, _CONTEXT, **_extra)
        self.id = id
        self.shapeExprs = shapeExprs


class ShapeNot(JSGObject):
    def __init__(self,
                 id: Optional[Union[IRI, BNODE]] = None,
                 shapeExpr: Union[ShapeOrt_, ShapeAndt_, ShapeNott_, NodeConstraint, Shapet_, IRI, BNODE, ShapeExternal] = None,
                 **_extra: Dict[str, object]):
        JSGObject.__init__(self, _CONTEXT, **_extra)
        self.id = id
        self.shapeExpr = shapeExpr


class TripleConstraint(JSGObject):
    def __init__(self,
                 id: Optional[Union[IRI, BNODE]] = None,
                 inverse: Optional[BOOL] = None,
                 negated: Optional[BOOL] = None,
                 predicate: IRI = None,
                 valueExpr: Optional[Union[ShapeOrt_, ShapeAndt_, ShapeNott_, NodeConstraint, Shapet_, IRI, BNODE, ShapeExternal]] = None,
                 min: Optional[INTEGER] = None,
                 max: Optional[INTEGER] = None,
                 semActs: Optional[List[SemAct]] = None,
                 annotations: Optional[List[Annotation]] = None,
                 **_extra: Dict[str, object]):
        JSGObject.__init__(self, _CONTEXT, **_extra)
        self.id = id
        self.inverse = inverse
        self.negated = negated
        self.predicate = predicate
        self.valueExpr = valueExpr
        self.min = min
        self.max = max
        self.semActs = semActs
        self.annotations = annotations


fix_forwards(globals())

from typing import Optional, Tuple, Dict

from pyjsg.jsglib import String, Object, Integer, Number, JSGNull, Boolean, AnyType, Array
from pyjsg.jsglib.jsg_strings import JSGStringMeta
from pyjsg.parser.jsgParser import *
from pyjsg.parser.jsgParserVisitor import jsgParserVisitor
from pyjsg.parser_impl.jsg_doc_context import JSGDocContext


class JSGBuiltinValueType(jsgParserVisitor):
    parserTypeToImplClass: Dict[str, Tuple[JSGStringMeta, object]] = \
        {"@string": (String, str),
         "@object": (Object, object),
         "@int": (Integer, int),
         "@number": (Number, float),
         "@null": (JSGNull, JSGNull),
         "@array": (Array, list),
         "@bool": (Boolean, bool),
         ".": (AnyType, object)}

    def __init__(self, context: JSGDocContext, ctx: Optional[jsgParser.BuiltinValueTypeContext] = None):
        self._context = context

        self._value_type_text = ""             # type: Optional[str]
        if ctx:
            self.visit(ctx)

    def __str__(self):
        return "builtinValueType: {}".format(self.basetypename)

    @property
    def typeid(self) -> str:
        id_ = self.parserTypeToImplClass[self._value_type_text][1]
        return "JSGNull" if id_ == JSGNull else id_.__name__

    @property
    def basetype(self) -> JSGStringMeta:
        return self.parserTypeToImplClass[self._value_type_text][0]

    @property
    def basetypename(self) -> str:
        obj = self.basetype
        # return obj.__module__.rsplit('.', 1)[1] + '.' + obj.__name__
        return obj.__name__

    def set_anytype(self) -> jsgParserVisitor:
        self._value_type_text = "."
        return self

    # ***************
    #   Visitors
    # ***************
    def visitBuiltinValueType(self, ctx: jsgParser.BuiltinValueTypeContext):
        """ valueTypeExpr: JSON_STRING | JSON_NUMBER | JSON_INT | JSON_BOOL | JSON_NULL | JSON_ARRAY | JSON_OBJECT """
        self._value_type_text = ctx.getText()

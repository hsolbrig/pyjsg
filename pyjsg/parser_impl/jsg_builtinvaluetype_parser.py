from typing import Optional, Tuple, Dict

from pyjsg.jsglib.jsg import JSGStringMeta, String, Object, Integer, Number, JSGNull, Array, Boolean, AnyType
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
        return "builtinValueType: {}".format(self.basetype)

    @property
    def typeid(self):
        id = self.parserTypeToImplClass[self._value_type_text][1]
        return "jsg.JSGNull" if id == JSGNull else id.__name__

    @property
    def basetype(self):
        return "jsg." + self.parserTypeToImplClass[self._value_type_text][0].__name__

    def set_anytype(self) -> jsgParserVisitor:
        self._value_type_text = "."
        return self

    # ***************
    #   Visitors
    # ***************
    def visitBuiltinValueType(self, ctx: jsgParser.BuiltinValueTypeContext):
        """ valueTypeExpr: JSON_STRING | JSON_NUMBER | JSON_INT | JSON_BOOL | JSON_NULL | JSON_ARRAY | JSON_OBJECT """
        self._value_type_text = ctx.getText()

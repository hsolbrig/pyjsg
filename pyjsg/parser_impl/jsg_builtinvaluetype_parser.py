from typing import Optional, Tuple, Dict, List

from jsonasobj import JsonObj

from pyjsg.jsglib import String, Integer, Number, JSGNull, Boolean, AnyType, Array
from pyjsg.jsglib.jsg_strings import JSGPatternedValMeta
from pyjsg.parser.jsgParser import *
from pyjsg.parser.jsgParserVisitor import jsgParserVisitor
from pyjsg.parser_impl.jsg_doc_context import JSGDocContext, PythonGeneratorElement


class JSGBuiltinValueType(jsgParserVisitor, PythonGeneratorElement):
    # builtin name, signature type, python type, mt value
    parserTypeToImplClass: Dict[str, Tuple[str, object, str]] = \
        {"@string": ("String", str, "None"),
         "@object": ("ObjectFactory('{name}', _CONTEXT, Object)", object, "None"),
         "@int": ("Integer", int, "None"),
         "@number": ("Number", float, "None"),
         "@null": ("JSGNull", None, "EmptyAny"),
         "@array": ("ArrayFactory('{name}', _CONTEXT, AnyType, 0, None)", list, "None"),
         "@bool": ("Boolean", bool, "None"),
         ".": ("AnyType", object, "EmptyAny")}

    def __init__(self, context: JSGDocContext, ctx: Optional[jsgParser.BuiltinValueTypeContext] = None):
        self._context = context
        self._value_type_text: Optional[str] = None
        self.text = ""
        if ctx:
            self.text = ctx.getText()
            self.visit(ctx)

    def __str__(self):
        return f"builtinValueType: {self._value_type_text if self._value_type_text != '.' else 'AnyType'}"

    def python_type(self) -> str:
        id_ = self.parserTypeToImplClass[self._value_type_text][1]
        return "type(None)" if id_ is None else id_.__name__

    def signature_type(self) -> str:
        return self.parserTypeToImplClass[self._value_type_text][0]

    def mt_value(self) -> str:
        return self.parserTypeToImplClass[self._value_type_text][2]

    def members_entries(self, all_are_optional: Optional[bool] = False) -> List[Tuple[str, str]]:
        return []

    def dependency_list(self) -> List[str]:
        return []

    def constructor(self, raw_name: str, getter: str) -> str:
        return ""

    # ***************
    #   Visitors
    # ***************
    def visitBuiltinValueType(self, ctx: jsgParser.BuiltinValueTypeContext):
        """ valueTypeExpr: JSON_STRING | JSON_NUMBER | JSON_INT | JSON_BOOL | JSON_NULL | JSON_ARRAY | JSON_OBJECT """
        self._value_type_text = ctx.getText()

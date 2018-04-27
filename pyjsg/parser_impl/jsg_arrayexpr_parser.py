from typing import Optional, List, Set, Dict, Tuple

from pyjsg.parser_impl.jsg_ebnf_parser import JSGEbnf
from pyjsg.parser_impl.jsg_valuetype_parser import JSGValueType
from pyjsg.parser.jsgParser import *


from pyjsg.parser.jsgParserVisitor import jsgParserVisitor
from pyjsg.parser_impl.jsg_doc_context import JSGDocContext


_array_template = """

{} = {}
"""


class JSGArrayExpr(jsgParserVisitor):
    def __init__(self, context: JSGDocContext, ctx: Optional[jsgParser.ArrayExprContext] = None):
        self._context = context

        self._typ = None                     # type: JSGValueType
        self._ebnf = None                    # type: Optional[JSGEbnf]

        if ctx:
            self.visit(ctx)

    def __str__(self):
        return "arrayExpr: [{}{}]".format(self._typ, self._ebnf if self._ebnf else "")

    def as_python(self, name: str) -> str:
        return _array_template.format(name, self.signature())

    def signature(self, all_are_optional: Optional[bool]=False) -> str:
        fstr = "List[{}]" if not all_are_optional else "Optional[List[{}]]"
        return fstr.format(self._context.reference_for(self._typ.typeid))

    def members(self, all_are_optional: Optional[bool] = False) -> List[Tuple[str, str]]:
        return []

    def dependency_list(self) -> List[str]:
        return self._typ.dependency_list()

    def dependencies(self) -> Set[str]:
        return set(self.dependency_list())

    def visitArrayExpr(self, ctx: jsgParser.ArrayExprContext):
        """ arrayExpr: OBRACKET valueType (BAR valueType)* ebnfSuffix? CBRACKET; """
        self._typ = JSGValueType(self._context, ctx.valueType())
        if ctx.ebnfSuffix():
            self._ebnf = JSGEbnf(self._context, ctx.ebnfSuffix())

# Copyright (c) 2017, Mayo Clinic
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without modification,
# are permitted provided that the following conditions are met:
#
# Redistributions of source code must retain the above copyright notice, this
#     list of conditions and the following disclaimer.
#
#     Redistributions in binary form must reproduce the above copyright notice,
#     this list of conditions and the following disclaimer in the documentation
#     and/or other materials provided with the distribution.
#
#     Neither the name of the Mayo Clinic nor the names of its contributors
#     may be used to endorse or promote products derived from this software
#     without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED.
# IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT,
# INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, 
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
# LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE
# OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED
# OF THE POSSIBILITY OF SUCH DAMAGE.
from typing import Optional, List, Set, Union, cast

from pyjsg.parser.jsgParser import *
from pyjsg.parser.jsgParserVisitor import jsgParserVisitor

from pyjsg.parser_impl.jsg_doc_context import JSGDocContext
from pyjsg.parser_impl.jsg_builtinvaluetype_parser import JSGBuiltinValueType

from .parser_utils import as_token, flatten

_valuetype_template = """

{} = {}"""


class JSGValueType(jsgParserVisitor):
    def __init__(self, context: JSGDocContext,
                 ctx: Optional[Union[jsgParser.ValueTypeContext, jsgParser.ValueTypeMacroContext,
                                     jsgParser.NonRefValueTypeContext]] = None):
        self._context = context

        # Note: both lexeridref and alttypelist can co-occur
        self._typeid = None             # type: Optional[str]
        self._arrayDef = None           # type: Optional[JSGArrayExpr]
        self._lexeridref = None         # type: Optional[str]
        self._builtintype = None        # type: Optional[JSGBuiltinValueType]
        self._alttypelist = []          # type: List[JSGValueType]

        if ctx:
            self.visit(ctx)

    def __str__(self):
        if self._typeid:
            if self._context.is_anon(self._typeid):
                typ = "(inner): {}".format(self._context.grammarelts[self._typeid])
            else:
                typ = "ID: {}".format(self._typeid)
        elif self._builtintype:
            typ = "builtinValueType: {}".format(self._builtintype.basetype)
        elif self._alttypelist:
            lid_str = "({}) | ".format(self._lexerid_str()) if self._lexeridref else ""
            typ = "({}{})".format(lid_str, ' | '.join(ta.typeid for ta in self._alttypelist))
        elif self._lexeridref:
            typ = self._lexerid_str()
        elif self._arrayDef:
            typ = str(self._arrayDef)
        else:
            typ = "NONE"
        return "valueType: {}".format(typ)

    def _lexerid_str(self) -> str:
        if not self._context.is_anon(self._lexeridref):
            return "LEXER_ID_REF: {}".format(self._lexeridref)
        else:
            return "STRING: {}".format(self._context.grammarelts[self._lexeridref])

    def as_python(self, name: str) -> str:
        return _valuetype_template.format(name, self.basetype if self._builtintype else self.typeid)

    @property
    def typeid(self) -> str:
        types = []
        if self._lexeridref:
            types.append(self._lexeridref)
        if self._typeid:
            types.append(self._context.reference_for(self._typeid))
        if self._builtintype:
            types.append(self._builtintype.typeid)
        if self._alttypelist:
            types += [self._context.reference_for(e.typeid) for e in self._alttypelist]
        if self._arrayDef:
            types.append(self._arrayDef.signature())
        return "JSGAnyType" if len(types) == 0 else \
            types[0] if len(types) == 1 else "Union[{}]".format(', '.join(types))

    @property
    def basetype(self) -> Optional[str]:
        return self._builtintype.basetype if self._builtintype else None

    def dependencies(self) -> Set[str]:
        return set(self.dependency_list())

    def dependency_list(self) -> List[str]:
        rval = []
        if self._typeid:
            rval.append(self._typeid)
            rval += self._context.dependency_list(self._typeid)
        if self._lexeridref:
            rval.append(self._lexeridref)
        if self._arrayDef:
            rval.append(self._arrayDef.dependency_list())
        if self._alttypelist:
            rval += flatten([e.dependency_list() for e in self._alttypelist])
        return rval

    # ***************
    #   Visitors
    # ***************
    def visitValueType(self, ctx: jsgParser.ValueTypeContext):
        """ valueTYpe: idref | nonRefValueType """
        if ctx.idref():
            self._typeid = as_token(ctx)
        else:
            self.visitChildren(ctx)

    def visitNonRefValueType(self, ctx: jsgParser.NonRefValueTypeContext):
        """ nonRefValueType: LEXER_ID_REF | STRING | builtinValueType | objectExpr | arrayExpr  
                             | OPREN typeAlternatives CPREN | ANY """
        if ctx.LEXER_ID_REF():                # Reference to a lexer token
            self._lexeridref = as_token(ctx)
        elif ctx.STRING():                      # Anonymous lexer token
            from pyjsg.parser_impl.jsg_lexerruleblock_parser import JSGLexerRuleBlock
            lrb = JSGLexerRuleBlock(self._context)
            lrb.add_string(ctx.getText()[1:-1], False)
            self._lexeridref = self._context.anon_id()
            self._context.grammarelts[self._lexeridref] = lrb
        elif ctx.ANY():
            self._builtintype = JSGBuiltinValueType(self._context).set_anytype()
        else:
            self.visitChildren(ctx)

    def visitBuiltinValueType(self, ctx: jsgParser.BuiltinValueTypeContext):
        from pyjsg.parser_impl.jsg_builtinvaluetype_parser import JSGBuiltinValueType
        self._builtintype = JSGBuiltinValueType(self._context, ctx)

    def visitObjectExpr(self, ctx: jsgParser.ObjectExprContext):
        from pyjsg.parser_impl.jsg_objectexpr_parser import JSGObjectExpr
        oe = JSGObjectExpr(self._context, ctx)
        self._typeid = self._context.anon_id()
        self._context.grammarelts[self._typeid] = oe

    def visitArrayExpr(self, ctx: jsgParser.ArrayExprContext):
        from pyjsg.parser_impl.jsg_arrayexpr_parser import JSGArrayExpr
        self._arrayDef = JSGArrayExpr(self._context, ctx)

    def visitValueTypeMacro(self, ctx: jsgParser.ValueTypeMacroContext):
        if len(ctx.nonRefValueType()) > 1:
            self._proc_value_types(ctx.nonRefValueType())
        else:
            self.visit(ctx.nonRefValueType(0))

    def visitTypeAlternatives(self, ctx: jsgParser.TypeAlternativesContext):
        self._proc_value_types(ctx.valueType())

    def _proc_value_types(self, ctx: Union[List[jsgParser.ValueTypeContext], List[jsgParser.NonRefValueTypeContext]]):
        from pyjsg.parser_impl.jsg_lexerruleblock_parser import JSGLexerRuleBlock

        stringalts = []                 # Aggregate multiple strings into a single type
        for vt in ctx:
            nrvt = vt.nonRefValueType() if isinstance(vt, jsgParser.ValueTypeContext) \
                else cast(jsgParser.NonRefValueTypeContext, vt)
            stringval = nrvt.STRING() if nrvt else None
            if stringval:
                stringalts.append(stringval.getText()[1:-1])
            else:
                self._alttypelist.append(JSGValueType(self._context, vt))

        if stringalts:
            lrb = JSGLexerRuleBlock(self._context)
            lrb.add_strings(stringalts)
            self._lexeridref = self._context.anon_id()
            self._context.grammarelts[self._lexeridref] = lrb

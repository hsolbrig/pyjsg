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
import re
from typing import Optional, Union, List, Set

from pyjsg.parser.jsgParser import *
from pyjsg.parser_impl.jsg_lexerrule_parser import JSGLexerRule

from pyjsg.parser.jsgParserVisitor import jsgParserVisitor
from pyjsg.parser_impl.jsg_doc_context import JSGDocContext
from .parser_utils import as_tokens, as_token, flatten


class JSGPropertyType(jsgParserVisitor):
    def __init__(self, context: JSGDocContext,
                 ctx: Optional[Union[jsgParser.PropertyTypeIDContext,
                                     jsgParser.PropertyTypeSTRINGContext,
                                     jsgParser.PropertyTypeObjectExprContext,
                                     jsgParser.PropertyTypeChoiceContext,
                                     jsgParser.PropertyTypeAnyContext]] = None):
        self._context = context

        self._arraytypeid = None        # JSGArrayExpr      Type is Array
        self._fixedvalue = None         # str               type is STRING
        self._typeidlist = []           # List[str]         Single entry is simple type - multi is union

        if ctx:
            self.visit(ctx)

    def __str__(self):
        return "Property: {}".format(self._typeidlist[0] if len(self._typeidlist) == 1
                                     else "({})".format(', '.join(self._typeidlist)))

    @property
    def typeid(self):
        if self._arraytypeid:
            return repr(self._arraytypeid)
        else:
            flattened_types = self.dependency_list()
            if len(flattened_types) > 1:
                return "Union[{}]".format(", ".join(flattened_types))
            else:
                return flattened_types[0]

    @property
    def fixedvalue(self):
        return self._fixedvalue

    def dependencies(self) -> Set[str]:
        return set(self.dependency_list())

    def dependency_list(self) -> List[str]:
        if self._arraytypeid:
            return self._arraytypeid.dependency_list()
        else:
            return flatten([self._context.signature_for(t) for t in self._typeidlist])

    def visitPropertyTypeID(self, ctx: jsgParser.PropertyTypeIDContext):
        """ propertyType: ID  -- a reference to another named property """
        self._typeidlist = [as_token(ctx)]

    def visitPropertyTypeSTRING(self, ctx: jsgParser.PropertyTypeSTRINGContext):
        """ propertyType: STRING  -- a string literal """
        self._fixedvalue = ctx.getText()
        self._typeidlist = ["str"]

    def visitPropertyTypeObjectExpr(self, ctx: jsgParser.PropertyTypeObjectExprContext):
        """ propertyType: objectExpr -- an anonymous object """
        from pyjsg.parser_impl.jsg_objectexpr_parser import JSGObjectExpr
        self._context.grammarelts[self._context.anon_id()] = JSGObjectExpr(self._context, ctx.objectExpr())

    def visitPropertyTypeArrayExpr(self, ctx: jsgParser.PropertyTypeArrayExprContext):
        """ propertyType: objectExpr -- an array """
        from pyjsg.parser_impl.jsg_arrayexpr_parser import JSGArrayExpr
        self._arraytypeid = JSGArrayExpr(self._context, ctx.arrayExpr())

    def visitPropertyTypeChoice(self, ctx: jsgParser.PropertyTypeChoiceContext):
        """ propertype: OPREN typeAlternatives CPREN -- a reference to an anonymous choice """
        alts = ctx.typeAlternatives()

        # Generate one regex for all of the strings
        if alts.STRING():
            string_id = self._context.anon_id()
            lexer = JSGLexerRule(self._context, '|'.join([re.escape(s.getText()[1:-1]) for s in alts.STRING()]))
            self._context.grammarelts[string_id] = lexer
            self._typeidlist = [string_id]

        # Generate a union for all the non-strings
        if len(alts.ID()):
            self._typeidlist += as_tokens(alts)


    def visitPropertyTypeAny(self, ctx: jsgParser.PropertyTypeAnyContext):
        """ propertytype: . -- type wild card.  Anything goes """
        self._typeidlist = ["JSGObject"]



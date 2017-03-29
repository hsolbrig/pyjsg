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
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES LOSS OF USE, 
# DATA, OR PROFITS OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
# LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE
# OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED
# OF THE POSSIBILITY OF SUCH DAMAGE.
import datetime
from typing import List

from pyjsg.parser.jsgParser import *
from pyjsg.parser_impl import __version__
from pyjsg.parser_impl.jsg_arrayexpr_parser import JSGArrayExpr
from pyjsg.parser_impl.jsg_lexerrule_parser import JSGLexerRule
from pyjsg.parser_impl.jsg_nonobjectexprdef_parser import JSGNonObjectExprDef
from pyjsg.parser_impl.jsg_objectexpr_parser import JSGObjectExpr

from pyjsg.parser.jsgParserVisitor import jsgParserVisitor
from pyjsg.parser_impl.jsg_doc_context import JSGDocContext
from .parser_utils import as_token, as_tokens

# Outermost python template
#
_jsg_python_template = '''# Auto generated from {infile} by PyJSG version {version}
# Generation date: {gendate}
#
from typing import Optional, Dict, List, Union, _ForwardRef

from pyjsg.jsglib.jsg import JSGString, JSGPattern, JSGObject, JSGContext
from pyjsg.jsglib.typing_patch import fix_forwards

# .TYPE and .IGNORE settings
_CONTEXT = JSGContext()

{body}

fix_forwards(globals())
'''

_class_template = """

class {}(JSGObject):
{}"""

_pattern_template = """


class {}(JSGString):
    pattern = {}"""

_array_template = """


class {}(JSGArray):
{}"""

_union_template = """
{} = {}"""

_forward_template = """
{} = {}"""


class JSGDocParser(jsgParserVisitor):
    def __init__(self):
        jsgParserVisitor.__init__(self)
        self._context = JSGDocContext()

    def __str__(self):
        return "JSGDocParser"

    def python(self, infile):
        self._context.resolve_circular_references()            # add forwards for any circular entries
        body = '\n'.join(self._context.directives) + '\n\n'
        for k in self._context.ordered_elements():
            v = self._context.grammarelts[k]
            if isinstance(v, JSGLexerRule):
                body += _pattern_template.format(k, repr(v))
            elif isinstance(v, JSGObjectExpr):
                if v.is_object():
                    body += _class_template.format(k, repr(v))
                else:
                    body += _union_template.format(k, repr(v))
            elif isinstance(v, JSGArrayExpr):
                body += _array_template.format(k, repr(v))
            elif isinstance(v, JSGDocContext.JSGForwardRef):
                body += _forward_template.format(k, repr(v))
            elif isinstance(v, str):
                body += _pattern_template.format(k, v)

        return _jsg_python_template.format(infile=infile,
                                           version=__version__,
                                           gendate=datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),
                                           body=body)

    def undefined_tokens(self) -> List[str]:
        """
        Return a list of undefined tokens
        :return:
        """
        return sorted(self._context.undefined_entries())

    # ****************************
    # Directives
    # ****************************
    def visitTypeDirective(self, ctx: jsgParser.TypeDirectiveContext):
        """ directive: '.TYPE' ID (DASH typeExceptions)? SEMI """
        self._context.directives.append('_CONTEXT.TYPE = "{}"'.format(as_token(ctx)))
        self.visitChildren(ctx)

    def visitTypeExceptions(self, ctx: jsgParser.TypeExceptionsContext):
        """ typeExceptions: ID+"""
        for tkn in as_tokens(ctx):
            self._context.directives.append('_CONTEXT.TYPE_EXCEPTIONS.append("{}")'.format(tkn))

    def visitIgnoreDirective(self, ctx: jsgParser.IgnoreDirectiveContext):
        """ directive: '.IGNORE' ID* SEMI """
        for tkn in as_tokens(ctx):
            self._context.directives.append('_CONTEXT.IGNORE.append("{}")'.format(tkn))

    # ****************************
    # Top Level
    # ****************************
    def visitGrammarElt(self, ctx: jsgParser.GrammarEltContext):
        """ grammarElt: objectDef | arrayDef | nonObject | lexerRuleSpec"""
        # First visit all lexical definitions in reverse order
        if ctx.lexerRuleSpec():
            self.visit(ctx.lexerRuleSpec())

        # Second visit all of the non-object definitions so they are available
        if ctx.nonObject():
            self.visit(ctx.nonObject())

        # Finally visit all the object and array definitions
        if ctx.arrayDef():
            self.visit(ctx.arrayDef())
        if ctx.objectDef():
            self.visit(ctx.objectDef())

    # ****************************
    # Object Definition
    # ****************************
    def visitObjectDef(self, ctx: jsgParser.ObjectDefContext):
        """ objectDef: ID objectExpr """
        objexpr = JSGObjectExpr(self._context)
        objexpr.visit(ctx.objectExpr())
        self._context.grammarelts[as_token(ctx)] = objexpr

    # ****************************
    # Array Definition
    # ****************************
    def visitArrayDef(self, ctx: jsgParser.ArrayDefContext):
        """ arrayDef : ID arrayExpr """
        arrayexpr = JSGArrayExpr(self._context)
        arrayexpr.visit(ctx.arrayExpr())
        self._context.grammarelts[as_token(ctx)] = arrayexpr

    # ************************
    # Non Object Definition -- assigns a shorthand identifier to an arbitrary building block
    # ************************
    def visitNonObject(self, ctx: jsgParser.NonObjectContext):
        """ nonObject: ID EQUALS objectExprDef SEMI """
        nonobj = JSGNonObjectExprDef(self._context, ctx.objectExprDef())
        obj = JSGObjectExpr(self._context)
        obj.set_object_def(nonobj)
        self._context.nonobjects[as_token(ctx)] = obj

    # ************************
    # Lexer Rule Spec
    # ************************
    def visitLexerRuleSpec(self, ctx: jsgParser.LexerRuleSpecContext):
        """ lexerRuleSpec: ID COLON lexerRuleBlock LSEMI """
        rule = JSGLexerRule(self._context)
        rule.visit(ctx.lexerRuleBlock())
        self._context.grammarelts[as_token(ctx)] = rule

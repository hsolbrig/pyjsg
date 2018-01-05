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
from typing import List, Optional

from pyjsg.parser_impl.jsg_forwardref import JSGForwardRef
from pyjsg.parser.jsgParser import *
from pyjsg.parser_impl import __version__
from pyjsg.parser_impl.jsg_arrayexpr_parser import JSGArrayExpr
from pyjsg.parser_impl.jsg_lexerruleblock_parser import JSGLexerRuleBlock
from pyjsg.parser_impl.jsg_objectexpr_parser import JSGObjectExpr
from pyjsg.parser_impl.jsg_valuetype_parser import JSGValueType

from pyjsg.parser.jsgParserVisitor import jsgParserVisitor
from pyjsg.parser_impl.jsg_doc_context import JSGDocContext
from .parser_utils import as_token, as_tokens

# Outermost python template
#
_jsg_python_template = '''# Auto generated from {infile} by PyJSG version {version}
# Generation date: {gendate}
#
from typing import Optional, Dict, List, Union, _ForwardRef

from pyjsg.jsglib import jsg
from pyjsg.jsglib.jsg import isinstance_

# .TYPE and .IGNORE settings
_CONTEXT = jsg.JSGContext(){body}

_CONTEXT.NAMESPACE = locals()
'''


class JSGDocParser(jsgParserVisitor):
    def __init__(self, context: Optional[JSGDocContext] = None):
        jsgParserVisitor.__init__(self)
        self._context = JSGDocContext() if context is None else context

    def as_python(self, infile):
        self._context.resolve_circular_references()            # add forwards for any circular entries
        body = ''
        for k in self._context.ordered_elements():
            v = self._context.grammarelts[k]
            if isinstance(v, JSGLexerRuleBlock):
                body += v.as_python(k)
            elif isinstance(v, JSGObjectExpr):
                body += v.as_python(k)
                # TODO: See whether this needs to be escaped
                # If there is no context type, add all objects to the list of exceptions
                if not any(e.startswith('_CONTEXT.TYPE = ') for e in self._context.directives):
                    self._context.directives.append('_CONTEXT.TYPE_EXCEPTIONS.append("{}")'.format(str(k)))
            elif isinstance(v, JSGValueType):
                body += v.as_python(k)
            elif isinstance(v, JSGArrayExpr):
                body += v.as_python(k)
            elif isinstance(v, JSGForwardRef):
                body += v.as_python()
            else:
                raise NotImplementedError("Unknown grammar elt for {}".format(k))

        body = '\n' + '\n'.join(self._context.directives) + '\n\n' + body
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
        """ directive: '.TYPE' name typeExceptions? SEMI """
        self._context.directives.append('_CONTEXT.TYPE = "{}"'.format(as_token(ctx.name())))
        self.visitChildren(ctx)

    def visitTypeExceptions(self, ctx: jsgParser.TypeExceptionsContext):
        """ typeExceptions: DASH idref+ """
        for tkn in as_tokens(ctx.idref()):
            self._context.directives.append('_CONTEXT.TYPE_EXCEPTIONS.append("{}")'.format(tkn))

    def visitIgnoreDirective(self, ctx: jsgParser.IgnoreDirectiveContext):
        """ directive: '.IGNORE' name* SEMI """
        for name in as_tokens(ctx.name()):
            self._context.directives.append('_CONTEXT.IGNORE.append("{}")'.format(name))

    # ****************************
    # JSON object definition
    # ****************************
    def visitObjectDef(self, ctx: jsgParser.ObjectDefContext):
        """ objectDef: ID objectExpr """
        name = as_token(ctx)
        self._context.grammarelts[name] = JSGObjectExpr(self._context, ctx.objectExpr(), name)

    # ****************************
    # JSON array definition
    # ****************************
    def visitArrayDef(self, ctx: jsgParser.ArrayDefContext):
        """ arrayDef : ID arrayExpr """
        self._context.grammarelts[as_token(ctx)] = JSGArrayExpr(self._context, ctx.arrayExpr())

    # ************************
    # Macro that represents an abstract object
    # ************************
    def visitObjectMacro(self, ctx: jsgParser.ObjectExprContext):
        """ objectMacro : ID EQUALS membersDef SEMI """
        name = as_token(ctx)
        self._context.grammarelts[name] = JSGObjectExpr(self._context, ctx.membersDef(), name)

    # ************************
    # Macro that represents an abstract value type
    # ************************
    def visitValueTypeMacro(self, ctx: jsgParser.ValueTypeMacroContext):
        """ valueTypeMacro : ID EQUALS nonRefValueType (BAR nonRefValueType)* SEMI """
        self._context.grammarelts[as_token(ctx)] = JSGValueType(self._context, ctx)

    # ************************
    # Lexer Rule
    # ************************
    def visitLexerRuleSpec(self, ctx: jsgParser.LexerRuleSpecContext):
        """ lexerRuleSpec: LEXER_ID COLON lexerRuleBlock SEMI """
        self._context.grammarelts[as_token(ctx)] = JSGLexerRuleBlock(self._context, ctx.lexerRuleBlock())

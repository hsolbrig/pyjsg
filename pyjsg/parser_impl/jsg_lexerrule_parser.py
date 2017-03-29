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
from typing import List, Set, Optional

from pyjsg.parser.jsgParser import *

from pyjsg.parser.jsgParserVisitor import jsgParserVisitor
from pyjsg.parser_impl.jsg_doc_context import JSGDocContext


class JSGLexerRule(jsgParserVisitor):

    def __init__(self, _: JSGDocContext, pattern: Optional[str] = ""):
        self._rulePattern = pattern
        self._ruleTokens = set()

    def __str__(self):
        return repr(self)

    def __repr__(self):
        if self._ruleTokens:
            return "JSGPattern(r'{}'.format({}))".\
                format(self._rulePattern, ', '.join(['{v}={v}.pattern'.format(v=v) for v in self._ruleTokens]))
        else:
            return "JSGPattern(r'{}')".format(self._rulePattern)

    # Note: the following two methods cannot be static
    def dependencies(self) -> Set[str]:
        return self._ruleTokens

    def dependency_list(self) -> List[str]:
        return list(self._ruleTokens)

    def visitLexerAltList(self, ctx: jsgParser.LexerAltListContext):
        """ lexerAltList: lexerAlt (LBAR lexerAlt)* """
        altlist = ctx.lexerAlt()
        self.visit(altlist[0])
        for alt in altlist[1:]:
            self._rulePattern += '|'
            self.visit(alt)

    def visitLexerElement(self, ctx: jsgParser.LexerElementContext):
        """ lexerElement: lexerAtom lexerebnf? | lexerBlock lexerebnf? """
        self.visitChildren(ctx)
        if ctx.lexerebnf():
            self._rulePattern += ctx.lexerebnf().getText()

    def visitLexerBlock(self, ctx: jsgParser.LexerBlockContext):
        """ lexerBlock: OPREN lexeraltList CPREN """
        self._rulePattern += '('
        self.visitChildren(ctx)
        self._rulePattern += ')'

    def visitLexerAtomCharSet(self, ctx: jsgParser.LexerAtomCharSetContext):
        """ lexerAtom : LEXER_CHAR_SET  """
        self._rulePattern += str(ctx.getText())

    def visitLexerAtomDot(self, ctx: jsgParser.LexerAtomDotContext):
        """ lexerAtom: LDOT """
        self._rulePattern += ctx.getText()

    def visitLexerTerminalID(self, ctx: jsgParser.LexerTerminalIDContext):
        """ terminal: LEXER_ID """
        # Substitute LEXER_ID with its string equivalent - "{LEXER_ID}".format(LEXER_ID=LEXER_ID.pattern)
        idtoken = ctx.getText()
        self._rulePattern += '{' + idtoken + '}'
        self._ruleTokens.add(idtoken)

    def visitLexerTerminalString(self, ctx: jsgParser.LexerTerminalStringContext):
        """ terminal: LEXER_STRING """
        self._rulePattern += re.escape(ctx.getText()[1:-1])

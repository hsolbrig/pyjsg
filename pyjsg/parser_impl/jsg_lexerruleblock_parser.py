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

from pyjsg.parser_impl.jsg_builtinvaluetype_parser import JSGBuiltinValueType
from pyjsg.parser_impl.parser_utils import as_token
from pyjsg.parser.jsgParser import *

from pyjsg.parser.jsgParserVisitor import jsgParserVisitor
from pyjsg.parser_impl.jsg_doc_context import JSGDocContext

python_template = """


class {}({}):
    pattern = {}"""

json_class_template = """
    typ = {}"""


class JSGLexerRuleBlock(jsgParserVisitor):

    def __init__(self, context, ctx: Optional[jsgParser.lexerRuleBlock] = None):
        self._context = context                 # type: JSGDocContext

        self._rulePattern = ""                  # type: str
        self._ruleTokens = set()                # type: Set[str]
        self._jsontype = None                   # type: Optional[JSGBuiltinValueType]

        if ctx:
            self.visit(ctx)

    def __str__(self):
        return "pattern: r'{}'".format(self._rulePattern)

    def as_python(self, name: str) -> str:
        """ Return the python constructor """
        base_type = self._jsontype.basetype if self._jsontype else "jsg.JSGString"
        if self._ruleTokens:
            pattern = "jsg.JSGPattern(r'{}'.format({}))".\
                format(self._rulePattern, ', '.join(['{v}={v}.pattern'.format(v=v) for v in sorted(self._ruleTokens)]))
        else:
            pattern = "jsg.JSGPattern(r'{}')".format(self._rulePattern)
        return python_template.format(name, base_type, pattern)

    # Note: the following two methods cannot be static
    def dependencies(self) -> Set[str]:
        return self._ruleTokens

    def dependency_list(self) -> List[str]:
        return list(self._ruleTokens)

    # ***************
    #   Visitors
    # ***************
    def visitBuiltinValueType(self, ctx: jsgParser.BuiltinValueTypeContext):
        self._jsontype = JSGBuiltinValueType(self._context, ctx)

    def visitLexerAltList(self, ctx: jsgParser.LexerAltListContext):
        """ lexerAltList: lexerAlt (LBAR lexerAlt)* """
        altlist = ctx.lexerAlt()
        self.visit(altlist[0])
        for alt in altlist[1:]:
            self._rulePattern += '|'
            self.visit(alt)

    def visitLexerElement(self, ctx: jsgParser.LexerElementContext):
        """ lexerElement: lexerAtom ebnfSuffix? | lexerBlock ebnfSuffix? """
        self.visitChildren(ctx)
        if ctx.ebnfSuffix():
            self._rulePattern += ctx.ebnfSuffix().getText()

    def visitLexerBlock(self, ctx: jsgParser.LexerBlockContext):
        """ lexerBlock: OPREN lexeraltList CPREN """
        self._rulePattern += '('
        self.visitChildren(ctx)
        self._rulePattern += ')'

    def visitLexerAtom(self, ctx: jsgParser.LexerAtomContext):
        """ lexerAtom : lexerTerminal | LEXER_CHAR_SET | ANY """
        if ctx.LEXER_CHAR_SET() or ctx.ANY():
            self._rulePattern += str(ctx.getText())
        else:
            self.visitChildren(ctx)

    def visitLexerTerminal(self, ctx: jsgParser.LexerTerminalContext):
        """ terminal: LEXER_ID | STRING  """
        if ctx.LEXER_ID():
            # Substitute LEXER_ID with its string equivalent - "{LEXER_ID}".format(LEXER_ID=LEXER_ID.pattern)
            idtoken = as_token(ctx)
            self._rulePattern += '({' + idtoken + '})'
            self._ruleTokens.add(idtoken)
        else:
            self.add_string(ctx.getText()[1:-1], False)

    def add_string(self, pattern: str, parens: bool) -> None:
        self._rulePattern += ('(' if parens else '') + re.escape(pattern) + (')' if parens else '')

    def add_strings(self, patterns: List[str]):
        self.add_string(patterns[0], len(patterns) > 1)
        for p in patterns[1:]:
            self._rulePattern += "|"
            self.add_string(p, True)

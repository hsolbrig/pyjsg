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
from typing import Optional, List, Set

from pyjsg.parser.jsgParser import *
from pyjsg.parser_impl.jsg_lexerrule_parser import JSGLexerRule
from pyjsg.parser_impl.jsg_propertyOrGroup_parser import JSGPropertyOrGroup

from pyjsg.parser.jsgParserVisitor import jsgParserVisitor
from pyjsg.parser_impl.jsg_doc_context import JSGDocContext
from .parser_utils import as_token


class JSGParticle(jsgParserVisitor):
    def __init__(self, context: JSGDocContext, ctx: Optional[jsgParser.ParticleContext] = None):
        self._context = context

        # ID ebnSuffix COMMA?
        self._reference = None                      # Optional[str] -- identifier or a non object
        self._ebnf = None                           # Optional[str] -- ebnfSuffix for a non-object

        # propertyOrGroup COMMA?
        self._property = None                       # Optional[JSGPropertyOrGroup]

        if ctx:
            self.visitParticle(ctx)

    def __str__(self):
        return "Particle: {}".format(self._reference if self._reference else str(self._property))

    def is_object(self):
        return self._reference is None

    def signature(self, all_are_optional: bool=False) -> List[str]:
        if self._reference:
            return self._context.signature_for(self._reference)
        else:
            return self._property.signature(allopt=all_are_optional)

    def initializer(self) -> List[str]:
        if self._reference:
            if self._reference in self._context.grammarelts:
                if isinstance(self._context.grammarelts[self._reference], JSGLexerRule):
                    raise NotImplementedError("ID {}: Lexer Tokens are not legal in non object productions"
                                              .format(self._reference))
                return self._context.grammarelts[self._reference].inner_initializer()
            elif self._reference in self._context.nonobjects:
                if isinstance(self._context.nonobjects[self._reference], JSGLexerRule):
                    raise NotImplementedError("ID {}: Lexer Tokens are not legal in non object productions"
                                              .format(self._reference))
                return self._context.nonobjects[self._reference].inner_initializer()
            else:
                return []
        else:
            return self._property.initializer()

    def dependency_list(self) -> List[str]:
        if self._reference:
            return self._context.dependency_list(self._reference)
        else:
            return self._property.dependency_list()

    def dependencies(self) -> Set[str]:
        return set(self.dependency_list())

    def visitParticle(self, ctx: jsgParser.ParticleContext):
        """ particle: ID ebnfSuffix? COMMA? | propertyOrGroup COMMA? """
        if ctx.ID():
            self._reference = as_token(ctx)
            self._ebnf = ctx.ebnfSuffix().getText() if ctx.ebnfSuffix() else ""
        else:
            self._property = JSGPropertyOrGroup(self._context, ctx.propertyOrGroup())

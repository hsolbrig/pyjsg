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
from pyjsg.parser_impl.jsg_particle_parser import JSGParticle

from pyjsg.parser.jsgParserVisitor import jsgParserVisitor
from pyjsg.parser_impl.jsg_doc_context import JSGDocContext
from .parser_utils import flatten


class JSGObjectExprDef(jsgParserVisitor):
    def __init__(self, context: JSGDocContext, ctx: Optional[jsgParser.ObjectExprDefContext] = None):
        self._context = context
        self._choices = []                  # List[List[JSGParticle]]
        if ctx:
            self.visit(ctx)

    def __str__(self):
        return "objectExprDef({})".format(id(self))

    def is_object(self):
        """ Return true if this expression needs to be represented as an object. False as a simple type def """
        return any([any([e.is_object for e in elist]) for elist in self._choices])

    def signature(self) -> List[str]:
        """ Return a list of __init__ signatures in the form of id = type"""
        return flatten([[c.signature() for c in clist] for clist in self._choices])

    def initializer(self) -> List[str]:
        return flatten([[c.initializer() for c in clist] for clist in self._choices])

    def dependency_list(self) -> List[str]:
        return flatten([[c.dependency_list() for c in clist] for clist in self._choices])

    def dependencies(self) -> Set[str]:
        return set(self.dependency_list())

    def visitObjectExprDef(self, ctx: jsgParser.ObjectExprDefContext):
        """ objectExprDef: particle+ (BAR particleOpt)* """
        self._choices.append([JSGParticle(self._context, p) for p in ctx.particle()])
        for opt in ctx.particleOpt():
            self._choices.append([JSGParticle(self._context, p) for p in opt.particle()])

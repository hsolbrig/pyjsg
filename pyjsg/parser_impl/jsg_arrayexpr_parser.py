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
from pyjsg.parser_impl.jsg_propertytype_parser import JSGPropertyType

from pyjsg.parser.jsgParserVisitor import jsgParserVisitor
from pyjsg.parser_impl.jsg_doc_context import JSGDocContext
from .parser_utils import flatten


# TODO: Implement array cardinality


class JSGArrayExpr(jsgParserVisitor):
    def __init__(self, context: JSGDocContext, ctx: Optional[jsgParser.ArrayExprContext] = None):
        self._context = context
        self._ebnfsuffix = ""
        self._proptypes = []            # JSGPropertyType

        if ctx:
            self.visit(ctx)

    def __str__(self):
        return "arrayExpr[{}]".format('|'.join([str(p) for p in self._proptypes]))

    def __repr__(self):
        types = self.dependency_list()
        if len(types) > 1:
            inner_type = "Union[{}]".format(', '.join(types))
        elif len(types):
            inner_type = self._proptypes[0].typeid
        else:
            inner_type = ""
        return "List[{}]".format(inner_type)

    def dependency_list(self) -> List[str]:
        return flatten([e.dependency_list() for e in self._proptypes])

    def dependencies(self) -> Set[str]:
        return set(self.dependency_list())

    def visitArrayExpr(self, ctx: jsgParser.ArrayExprContext):
        """ arrayExpr: '[' propertyType (BAR propertType)* ebnSuffix? ']'"""
        for pt in ctx.propertyType():
            ptparser = JSGPropertyType(self._context)
            ptparser.visit(pt)
            self._proptypes.append(ptparser)
        if ctx.ebnfSuffix():
            self._ebnfsuffix = ctx.ebnfSuffix().getText()

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

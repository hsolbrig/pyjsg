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
from typing import Optional, List, Union, Set

from pyjsg.parser.jsgParser import *
from pyjsg.parser_impl.jsg_propertytype_parser import JSGPropertyType

from pyjsg.parser.jsgParserVisitor import jsgParserVisitor
from pyjsg.parser_impl.jsg_doc_context import JSGDocContext
from .parser_utils import is_valid_python, map_ebnf, flatten


class JSGPropertyOrGroup(jsgParserVisitor):
    def __init__(self, context: JSGDocContext,
                 ctx: Optional[Union[jsgParser.PropertyOrGroupSimpleContext,
                                     jsgParser.PropertyOrGroupShorthandContext,
                                     jsgParser.PropertyOrGroupChoiceContext]] = None):
        self._context = context

        # Simple
        self._property_id = None                # str
        self._property_type = None              # JSGPropertyType
        self._ebnf = None                       # EbnfSuffixContext

        # Shorthand or choice
        self._groups = []                       # List[List[JSGPropertyOrGroup]]

        if ctx:
            self.visit(ctx)

    def __str__(self):
        return "propertyOrGroup({})".format(self.signature())

    def signature(self, allopt: bool = False) -> List[str]:
        ebnf = "?" if allopt else self._ebnf
        if self._property_id:
            if is_valid_python(self._property_id):
                return ["{}: {} = None".format(self._property_id, map_ebnf(self._property_type.typeid, ebnf))]
            else:
                return []
        else:
            return flatten([[e.signature(True) for e in glist] for glist in self._groups])

    def initializer(self) -> List[str]:
        if self._property_id:
            val = self._property_type.fixedvalue if self._property_type.fixedvalue else self._property_id
            if is_valid_python(self._property_id):
                return ["self.{} = {}".format(self._property_id, val)]
            else:
                return ["setattr(self, '{}', {})".format(self._property_id, val)]
        else:
            return flatten([[e.initializer() for e in glist] for glist in self._groups])

    def dependency_list(self) -> List[str]:
        if self._property_type:
            return self._property_type.dependency_list()
        else:
            return flatten([[e.dependency_list() for e in glist] for glist in self._groups])

    def dependencies(self) -> Set[str]:
        return set(self.dependency_list())

    def as_property(self, id_: str, proptype: JSGPropertyType, ebnf: str):
        porg = JSGPropertyOrGroup(self._context)
        porg._property_id = id_
        porg._property_type = proptype
        porg._ebnf = ebnf
        return porg

    def visitPropertyOrGroupSimple(self, ctx: jsgParser.PropertyOrGroupSimpleContext):
        """ propertyOrGroup: (ID|STRING) COLON propertyType ebnfSuffix? """
        self._property_id = ctx.ID().getText() if ctx.ID() else ctx.STRING().getText()[1:-1]
        self._property_type = JSGPropertyType(self._context, ctx.propertyType())
        self._ebnf = ctx.ebnfSuffix() if ctx.ebnfSuffix() else ""

    def visitPropertyOrGroupShorthand(self, ctx: jsgParser.PropertyOrGroupShorthandContext):
        """ propertyOrGroup: OPREN ID (BAR ID)+ CPREN COLON propertype ebnfSuffix? """
        proptype = JSGPropertyType(self._context, ctx.propertyType())
        ebnf = ctx.ebnfSuffix().getText() if ctx.ebnfSuffix() else ''
        self._groups.append([self.as_property(str(id_), proptype, ebnf) for id_ in ctx.ID()])

    def visitPropertyOrGroupChoice(self, ctx: jsgParser.PropertyOrGroupChoiceContext):
        """ propertyOrGroup: OPREN propertyOrGroupList (BAR propertyOrGroupList)+ """
        for property_or_group_list in ctx.propertyOrGroupList():
            self._groups.append([JSGPropertyOrGroup(self._context, porg)
                                 for porg in property_or_group_list.propertyOrGroup()])

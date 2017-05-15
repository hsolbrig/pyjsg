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
from typing import Optional, Union, List, Set

from pyjsg.parser_impl.jsg_ebnf_parser import JSGEbnf
from pyjsg.parser_impl.jsg_valuetype_parser import JSGValueType
from pyjsg.parser.jsgParser import *
from pyjsg.parser_impl.jsg_pairdef_parser import JSGPairDef
from pyjsg.parser_impl.jsg_builtinvaluetype_parser import JSGBuiltinValueType

from pyjsg.parser.jsgParserVisitor import jsgParserVisitor
from pyjsg.parser_impl.jsg_doc_context import JSGDocContext
from .parser_utils import as_token, flatten

_class_template = """

class {name}(JSGObject):
    _reference_types = [{reference_types}]
    
{init_fctn}"""


_init_template = """    def __init__(self{},
                 **_kwargs: Dict[str, object]):
        self._context = _CONTEXT{}
        super().__init__(self._context, **_kwargs)
"""
indent1 = ",\n                 "
indent2 = "\n        "
indent3 = "\n            "

_choice_template = "opt_: Union[{}] = None"
_choice_initializer = """{initializer} if isinstance(opt_, {choice}) else {none}"""
_none_initializer = "{}(None)"


class JSGObjectExpr(jsgParserVisitor):
    """ objectExpr: OBRACE membersDef? CBRACE | OBRACE ID MAPSTO valueType CBRACE """
    def __init__(self, context: JSGDocContext,
                 ctx: Optional[Union[jsgParser.ObjectExprContext, jsgParser.MembersDefContext]] = None,
                 name: Optional[str] = None):
        self._context = context
        self._name = name

        # _members is if there is a single set of pairs
        self._members = []                  # type: List[JSGPairDef]

        # _choices are if there are alternative members
        self._choices = []                  # type: List[str]

        # _map is for a map style definition
        self._map_name_type = None          # type: Optional[Union[str, JSGBuiltinValueType]]
        self._map_valuetype = None          # type: Optional[JSGValueType]
        self._map_ebnf = None               # type: Optional[JSGEbnf]

        if ctx:
            self.visit(ctx)

    def __str__(self):
        return "objectExpr: {}"\
            .format("simple object" if self._members else "object choices" if self._choices else "object map")

    def as_python(self, name: str) -> str:
        # TODO: Complete map implementation
        if self._map_valuetype:
            reference_types = ""
            init_fctn = _init_template.format("", "")
            return _class_template.format(**locals())
        elif self._choices:
            pair_signatures = indent1 + _choice_template.format(', '.join(self._choices))
            pair_initializers = []
            for c in self._choices:
                c_initializers = self._context.initializer(c, 'opt_')
                c_none_initializers = self._context.none_initializer(c)
                if len(c_initializers) != len(c_none_initializers):
                    raise Exception("HELP")
                for c_initializer, c_none in zip(c_initializers, c_none_initializers):
                    pair_initializers.append(_choice_initializer
                                             .format(choice=c, initializer=c_initializer, none=c_none))
            init_fctn = _init_template.format(pair_signatures, indent2 + indent2.join(pair_initializers))
            reference_types = ", ".join(self._choices)
            return _class_template.format(**locals())
        else:
            return self._create_classdef(name, self._members)

    def _create_classdef(self, name: str, pairs: List[JSGPairDef]) -> str:
        pair_signatures = []
        pair_refs = flatten(pair.signature() for pair in pairs if pair.is_reference_type())
        for pair in pairs:
            if not pair.is_reference_type():
                pair_signatures += pair.signature()
            elif len(pair_refs) == 1:
                pair_signatures.append("{name}: {typ} = None".format(name=pair.typeid, typ=pair_refs[0]))
        if len(pair_refs) > 1:
            pair_signatures.append("choice: Union[{}] = None".format(', '.join(pair_refs)))
        signatures = indent1 + indent1.join(flatten(pair_signatures)) if pair_signatures else ""

        pair_initializers = []
        for pair in pairs:
            if not pair.is_reference_type():
                pair_initializers += pair.initializer()
            elif len(pair_refs) == 1 and not pair.is_list:
                pair_initializers += pair.initializer(pair.typeid)
            else:
                pair_initializers += ["self.{} = {}".format(pair.typeid, pair.typeid)]
        if len(pair_refs) > 1:
            for pair_ref in pair_refs:
                pair_initializers.append(self._gen_choice_initializer(pair_ref))

        initializers = indent2 + indent2.join(flatten(pair_initializers)) if pair_initializers else ""
        init_fctn = _init_template.format(signatures, initializers)
        reference_types = ', '.join(pair.typeid for pair in pairs if pair.is_reference_type())
        return _class_template.format(**locals())

    def _gen_choice_initializer(self, pair_ref: str) -> str:
        ref_initializers = self._context.initializer(pair_ref, "choice")
        rval = ""
        for ref_initializer in ref_initializers:
            rval += indent2 + ref_initializer + " if isinstance(choice, {}) else None".format(pair_ref)
        return rval

    def dependency_list(self) -> List[str]:
        if self._members:
            return flatten(member.dependency_list() for member in self._members)
        elif self._map_valuetype:
            raise NotImplementedError("Map is not implemented")
        else:
            return flatten(self._context.dependency_list(c) + [c] for c in self._choices)

    def dependencies(self) -> Set[str]:
        return set(self.dependency_list())

    def signature(self, all_are_optional: bool=False) -> List[str]:
        """
        Return a list of __init__ type declarations (format: name: type) for the components
        :param all_are_optional: If true, type must be Optional
        :return: list of signatures
        """
        if self._map_valuetype:
            return[_init_template.format("", "")]
        elif self._choices:
            return flatten(self._context.signature(c, True) for c in self._choices)
        else:
            return flatten(pair.signature(all_are_optional) for pair in self._members)

    def initializer(self, prefix: Optional[str] = None, add_exists_clause: bool=False) -> List[str]:
        if self._map_valuetype:
            return []
        elif self._choices:
            return flatten(self._context.initializer(c, prefix, add_exists_clause) for c in self._choices)
        else:
            return flatten(pair.initializer(prefix, add_exists_clause) for pair in self._members)

    def none_initializer(self) -> List[str]:
        if self._map_valuetype:
            return []
        elif self._choices:
            return flatten(self._context.none_initializer(c) for c in self._choices)
        else:
            return flatten(pair.none_initializer() for pair in self._members)

    def _add_choice(self, branch: int, ctx) -> None:
        choice_name = "{}_{}_".format(self._name, branch)
        choice_obj = JSGObjectExpr(self._context, name=choice_name)
        for pairdef in ctx.pairDef():
            choice_obj.visit(pairdef)
        self._choices.append(choice_name)
        self._context.grammarelts[choice_name] = choice_obj

    # ***************
    #   Visitors
    # ***************
    def visitObjectExpr(self, ctx: jsgParser.ObjectExprContext):
        """ objectExpr: OBRACE membersDef? CBRACE 
                        |OBRACE (LEXER_ID_REF | JSON_STRING | ANY) MAPSTO valueType ebnfSuffix?"""
        if ctx.membersDef():
            self.visitChildren(ctx)
        elif ctx.MAPSTO():
            if ctx.LEXER_ID_REF():                  # JSON_STRING and ANY are equivalent in this context
                self._map_name_type = as_token(ctx)
            self._map_valuetype = JSGValueType(self._context, ctx.valueType())
            if ctx.ebnfSuffix():
                self._map_ebnf = JSGEbnf(self._context, ctx.ebnfSuffix())

    def visitMembersDef(self, ctx: jsgParser.MembersDefContext):
        """ membersDef: pairDef+ (BAR altMembersDef)* ;
            altMembersDef: pairDef* 
        """
        if not ctx.altMembersDef():
            self.visitChildren(ctx)
        else:
            if not self._name:
                self._name = self._context.anon_id()
            entry = 1
            self._add_choice(entry, ctx)
            for alt in ctx.altMembersDef():
                entry += 1
                self._add_choice(entry, alt)

    def visitPairDef(self, ctx: jsgParser.PairDefContext):
        self._members.append(JSGPairDef(self._context, ctx))

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
from typing import Optional, List, Set, Tuple, Dict

from pyjsg.parser_impl.jsg_ebnf_parser import JSGEbnf
from pyjsg.parser_impl.jsg_valuetype_parser import JSGValueType
from pyjsg.parser.jsgParser import *

from pyjsg.parser.jsgParserVisitor import jsgParserVisitor
from pyjsg.parser_impl.jsg_doc_context import JSGDocContext
from .parser_utils import as_token, is_valid_python, optional

_val_template_simple = "{prefix}{cooked_name}"
_val_template_simple_raw = "_kwargs.pop('{raw_name}', None)"

_val_template_builtin = "{basetype}({prefix}{cooked_name})"
_val_template_builtin_raw = "{basetype}(_kwargs.pop('{raw_name}', None))"

_initializer_template_cooked = "self.{raw_name} = {val}{opt_clause}"
_initializer_template_raw = "setattr(self, '{raw_name}', {val}){opt_clause}"


class JSGPairDef(jsgParserVisitor):
    def __init__(self, context: JSGDocContext, ctx: Optional[jsgParser.PairDefContext] = None):
        self._context = context

        # Names is raw name / tokenized name tuple
        self._names = []             # type: List[Tuple[str, str]]
        self._typ = None             # type: Optional[JSGValueType]

        self._type_reference = None  # type: Optional[str]

        self._ebnf = None            # type: Optional[JSGEbnf]

        if ctx:
            self.visit(ctx)

    def __str__(self):
        if self._names:
            namelist = ' | '.join(name[0] for name in self._names)
            return "pairDef: {} : {}{}".format('({})'.format(namelist) if len(self._names) > 1 else namelist,
                                               self._typ,
                                               self._ebnf if self._ebnf else "")
        else:
            return "pairDef: typeReference: {}{}".format(self._type_reference, self._ebnf if self._ebnf else "")

    def _card(self, e: str, all_are_optional: bool) -> str:
        if self._ebnf and self._ebnf.is_optional:
            return optional(e, True)
        return optional(self._ebnf.python_type(e) if self._ebnf else e, all_are_optional)

    def is_reference_type(self) -> bool:
        return self._type_reference is not None

    def signature(self, all_are_optional: Optional[bool] = False) -> List[str]:
        """ Return the __init__ signature element(s) """
        if self._type_reference:
            return [self._card(self._context.reference_for(self.typeid), all_are_optional)]
        else:
            return ["{}: {} = None".format(n, self._card(self.typeid, all_are_optional))
                    for _, n in self._names if is_valid_python(n)]

    def members(self, all_are_optional: Optional[bool] = False) -> List[Tuple[str, str]]:
        """
        Return the name/type tuples represented by this pairdef
        :param all_are_optional: If true, all types must be optional
        :return: 
        """
        if self._type_reference:
            if self._ebnf and self._ebnf.is_list:
                return [(self.typeid, optional("List[{}]".format(self.typeid), all_are_optional))]
            else:
                return self._context.members(self.typeid, all_are_optional or (self._ebnf and self._ebnf.is_optional))
        else:
            member_type = self._card(self.typeid, all_are_optional)
            return [(raw_name, member_type) for raw_name, _ in self._names]

    @property
    def typeid(self) -> str:
        return self._typ.typeid if self._typ else self._type_reference

    @property
    def is_optional(self) -> bool:
        return self._ebnf and self._ebnf.is_optional

    @property
    def is_list(self) -> bool:
        return self._ebnf and self._ebnf.is_list

    def _optional_clause(self, prefix: Optional[str], basetype: Optional[str], add_exists_clause: bool) -> str:
        if prefix and self._context.is_optional(self._ebnf, add_exists_clause):
            elsepart = "{}(None)".format(basetype) if basetype else "None"
            return " if {} else {}".format(prefix, elsepart)
        else:
            return ""

    def _initializer_for(self, raw_name: str, cooked_name: str, prefix: Optional[str], basetype: Optional[str], add_exists_clause: bool) -> str:
        """
        Create an initializer entry for the entry
        :param raw_name: name unadjusted for python compatibility.
        :param cooked_name: name tweaked to be compatible with python
        :param prefix: owner of the element
        :param basetype: JSON type to use as wrapper if it exists
        :param add_exists_clause: if True, add on an existence test
        :return: 
        """
        opt_clause = self._optional_clause(prefix, basetype, add_exists_clause)
        prefix = "" if prefix is None else prefix + "."
        if is_valid_python(raw_name + '_'):
            val = _val_template_builtin.format(**locals()) if basetype else _val_template_simple.format(**locals())
            rval = _initializer_template_cooked.format(**locals())
        else:
            val = _val_template_builtin_raw.format(**locals()) if basetype else _val_template_simple_raw.format(**locals())
            rval = _initializer_template_raw.format(**locals())
        return rval

    def initializer(self, prefix: Optional[str] = None, add_exists_clause: bool=False) -> List[str]:
        """ Return the __init__ initializer assignment block """
        add_exists_clause = self._context.is_optional(self._ebnf, add_exists_clause)
        if self._type_reference:
            return self._context.initializer(self._type_reference, prefix, add_exists_clause)
        else:
            return [self._initializer_for(rn, cn, prefix, self._typ.basetype, add_exists_clause) for rn, cn in self._names]

    def none_initializer(self) -> List[str]:
        if self._type_reference:
            return self._context.none_initializer(self._type_reference)
        else:
            return ["{}(None)".format(self._typ.basetype) if self._typ.basetype else "None" for _ in self._names]

    def dependency_list(self) -> List[str]:
        return self._typ.dependency_list() if self._typ else [self._type_reference]

    def dependencies(self) -> Set[str]:
        return set(self.dependency_list())

    # ***************
    #   Visitors
    # ***************
    def visitPairDef(self, ctx: jsgParser.PairDefContext):
        """ pairDef: name COLON valueType ebnfSuffix? 
                     | idref ebnfSuffix?
                     | OPREN name (BAR? name)+ CPREN COLON valueType ebnfSuffix?
        """
        if ctx.name():
            self.visitChildren(ctx)
        else:
            self._type_reference = as_token(ctx)
            if ctx.ebnfSuffix():
                self.visit(ctx.ebnfSuffix())

    def visitName(self, ctx: jsgParser.NameContext):
        """ name: ID | STRING """
        self._names.append((ctx.ID().getText() if ctx.ID() else ctx.STRING().getText()[1:-1], as_token(ctx)))

    def visitValueType(self, ctx: jsgParser.ValueTypeContext):
        self._typ = JSGValueType(self._context, ctx)

    def visitEbnfSuffix(self, ctx: jsgParser.EbnfSuffixContext):
        self._ebnf = JSGEbnf(self._context, ctx)

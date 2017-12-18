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
from collections import OrderedDict
from typing import List, Set, Optional, Dict, Union, Tuple

from .parser_utils import as_set
from pyjsg.parser_impl.anonymousidentifierfactory import AnonymousIdentifierFactory


BUILTIN_TYPES = ["String, Number, Int, Bool, Null, Object, AnyType"]


class JSGDocContext:
    """
    Context for JSG to Python conversion
    """
    def __init__(self):
        from pyjsg.parser_impl.jsg_lexerruleblock_parser import JSGLexerRuleBlock
        from pyjsg.parser_impl.jsg_objectexpr_parser import JSGObjectExpr
        from pyjsg.parser_impl.jsg_arrayexpr_parser import JSGArrayExpr
        from pyjsg.parser_impl.jsg_builtinvaluetype_parser import JSGBuiltinValueType
        from pyjsg.parser_impl.jsg_forwardref import JSGForwardRef

        self.directives = []                # type: List[str]
        self.grammarelts = OrderedDict()    # type: Dict[str, Union[JSGLexerRuleBlock, JSGObjectExpr,  JSGArrayExpr, JSGForwardRef, JSGBuiltinValueType]]
        self.dependency_map = {}            # type: Dict[str, List[str]]
        self.forward_refs = {}              # type: Dict[str, str]
        self.depths = {}                    # type: Dict[str, int]

        self._id_factory = AnonymousIdentifierFactory()

    def anon_id(self):
        return self._id_factory.next_id()

    def is_anon(self, tkn: str) -> bool:
        return self._id_factory.is_anon(tkn)

    def is_optional(self, ebnf, flag: bool ) -> bool:
        """
        Pass through optional setting for initialization
        :param ebnf: ebnf of current state (type Optional[JSGEbnf])
        :param flag: current flag pass through -- once true, always true
        :return: new setting
        """
        return flag or (ebnf is not None and ebnf.is_optional)

    def initializer(self, tkn: str, prefix: Optional[str], add_exists_clause=False) -> List[str]:
        tkn = self.reference_for(tkn)
        if tkn in self.grammarelts:
            initializer = getattr(self.grammarelts[tkn], "initializer", None)
            if not initializer:
                # TODO: Report this error properly
                raise NotImplementedError("Token {} doesn't have an initializer".format(tkn))
            return self.grammarelts[tkn].initializer(prefix, add_exists_clause)
        else:
            return []

    def none_initializer(self, tkn: str) -> List[str]:
        tkn = self.reference_for(tkn)
        if tkn in self.grammarelts:
            none_initializer = getattr(self.grammarelts[tkn], "none_initializer", None)
            if not none_initializer:
                raise NotImplementedError("Token {} doesn't have a none_initializer".format(tkn))
            return self.grammarelts[tkn].none_initializer()
        else:
            raise NotImplementedError("Token {} is not in grammarelts".format(tkn))

    def reference_for(self, tkn: str) -> str:
        return self.forward_refs.get(tkn, tkn)

    def signature(self, tkn: str, all_are_optional: Optional[bool]=False) -> List[str]:
        """
        Return the __init__ signature for tkn
        :param tkn: Token to retrieve signature for
        :param all_are_optional: If True, all parameters are forced optional
        :return: 
        """
        tkn = self.reference_for(tkn)
        if tkn in self.grammarelts:
            return self.grammarelts[tkn].signature(all_are_optional)
        else:
            return []

    def members(self, tkn: str, all_are_optional: Optional[bool] = False) -> List[Tuple[str, str]]:
        tkn = self.reference_for(tkn)
        if tkn in self.grammarelts:
            return self.grammarelts[tkn].members(all_are_optional)
        else:
            raise NotImplementedError("Token {} is not in grammarelts".format(tkn))

    def dependency_list(self, tkn: str) -> List[str]:
        """
        Return a list all of the grammarelts that depend on tkn
        :param tkn: 
        :return:
        """
        if tkn not in self.dependency_map:
            self.dependency_map[tkn] = [tkn]        # Force a circular reference
            if tkn in self.grammarelts:
                self.dependency_map[tkn] = self.grammarelts[tkn].dependency_list()
            else:
                self.dependency_map[tkn] = []
        return self.dependency_map[tkn]

    def dependencies(self, tkn: str) -> Set[str]:
        """
        Return all the items that tkn depends on as a set
        :param tkn:
        :return:
        """
        return set(self.dependency_list(tkn))

    def undefined_entries(self) -> Set[str]:
        """ Return the set of tokens that are referenced but not defined. """
        return as_set([[d for d in self.dependencies(k) if d not in self.grammarelts and d not in BUILTIN_TYPES]
                       for k in self.grammarelts.keys()])

    def dependency_closure(self, tkn: str, seen: Optional[Set[str]]=None) -> Set[str]:
        """
        Determine the transitive closure of tkn's dependencies
        :param tkn: root token
        :param seen: list of tokens already visited in closure process
        :return: dependents, dependents of dependents, etc.
        """
        if seen is None:
            seen = set()
        for k in self.dependencies(tkn):
            if k not in seen:
                seen.add(k)
                self.dependency_closure(k, seen)
        return seen

    def circular_references(self) -> Set[str]:
        """
        Return the set of recursive (circular) references
        :return:
        """
        rval = set()
        for k in self.grammarelts.keys():
            if k in self.dependency_closure(k):
                rval.add(k)
        return rval

    def resolve_circular_references(self) -> None:
        """
        Create forward references for all circular references
        :return:
        """
        from pyjsg.parser_impl.jsg_forwardref import JSGForwardRef

        circulars = self.circular_references()
        for c in circulars:
            fwdref = JSGForwardRef(c)
            self.grammarelts[fwdref.label] = fwdref
            self.forward_refs[c] = fwdref.label

    def ordered_elements(self) -> str:
        """ Generator that returns items in ther order needed for the actual python
            1) All forward references
            2) All lexer items
            3) Object / Array definitions in order of increasing dependency depth

            Within each category, items are returned alphabetically
        """
        from pyjsg.parser_impl.jsg_lexerruleblock_parser import JSGLexerRuleBlock
        from pyjsg.parser_impl.jsg_arrayexpr_parser import JSGArrayExpr
        from pyjsg.parser_impl.jsg_forwardref import JSGForwardRef
        from pyjsg.parser_impl.jsg_objectexpr_parser import JSGObjectExpr
        from pyjsg.parser_impl.jsg_builtinvaluetype_parser import JSGBuiltinValueType
        from pyjsg.parser_impl.jsg_valuetype_parser import JSGValueType

        state = 0
        self.depths = {}
        for k in self.dependency_map.keys():
            self.calc_depths(k)
        # NOTE that depth is not in the closure -- if you create an iterator and then bump depth
        #      the iterator will work against the bumped depth
        depth = -1
        max_depth = max(self.depths.values()) if self.depths else 0
        while state >= 0:
            iter_ = iter([])
            if state == 0:          # Forward references
                iter_ = (k for k, v in sorted(self.grammarelts.items()) if isinstance(v, JSGForwardRef))
                state += 1
            elif state == 1:
                depth += 1
                if depth <= max_depth:
                    iter_ = (k for k, v in self.grammarelts.items()
                             if isinstance(v, (JSGLexerRuleBlock, JSGBuiltinValueType)) and self.depths[k] == depth)
                else:
                    depth = -1
                    state += 1
            elif state == 2:
                depth += 1
                if depth <= max_depth:
                    iter_ = (k for k, v in self.grammarelts.items()
                             if isinstance(v, (JSGObjectExpr, JSGArrayExpr, JSGValueType)) and self.depths[k] == depth)
                else:
                    state = -1
            while state >= 0:
                rval = next(iter_, None)
                if rval is None:
                    break
                yield rval

    def calc_depths(self, k: str) -> int:

        if k in self.depths:
            return self.depths[k]
        if k in self.forward_refs:
            self.depths[self.forward_refs[k]] = 1
        max_depth = 0
        for v in self.dependency_map[k]:
            if v in self.forward_refs:
                max_depth = max(max_depth, 1)
            else:
                max_depth = max(max_depth, self.calc_depths(v) + 1)
        self.depths[k] = max_depth
        return max_depth

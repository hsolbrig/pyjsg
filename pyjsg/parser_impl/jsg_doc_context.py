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
from collections import OrderedDict
from typing import List, Set, Optional, Dict

from .parser_utils import as_set, AnonymousIdentifierFactory

SPECIAL_TYPES = ["str"]                     # Types that can remain unreferenced
forward_ref_tmplt = "{}t_"                  # template for forward references

class JSGDocContext:
    """
    Context for JSG to Python conversion
    """

    def __init__(self):
        self.directives = []                # List[str]
        self.grammarelts = OrderedDict()    # Dict[str, Union[JSGObjectExpr, JSGArrayExpr,  str]]
        self.nonobjects = {}                # Dict[str, List[JSGParticleDef]]
        self.dependency_map = {}            # Dict[str, List[str]]
        self.forward_refs = []              # List[str]

        self._id_factory = AnonymousIdentifierFactory()

    def anon_id(self):
        return self._id_factory.next_id()

    def signature_for(self, tkn: str) -> List[str]:
        """
        Return the __init__ signature for tkn
        :param tkn: token to generate signature for
        :return: list of name: type strings
        """
        if tkn in self.nonobjects:
            return self.nonobjects[tkn].inner_signature()
        elif tkn in self.forward_refs:
            return [forward_ref_tmplt.format(tkn)]
        return [tkn]

    def dependency_list(self, tkn: str) -> List[str]:
        """
        Return all of the items that tkn depends on in list format
        :param tkn:
        :return:
        """
        if tkn not in self.dependency_map:
            if tkn in self.nonobjects:
                self.dependency_map[tkn] = self.raw_dependencies(self.nonobjects[tkn].dependency_list())
            elif tkn in self.grammarelts:
                self.dependency_map[tkn] = self.raw_dependencies(self.grammarelts[tkn].dependency_list())
            else:
                self.dependency_map[tkn] = set()
        return self.dependency_map[tkn]

    def dependencies(self, tkn: str) -> Set[str]:
        """
        Return all the items that tkn depends on as a set
        :param tkn:
        :return:
        """
        return set(self.dependency_list(tkn))

    @staticmethod
    def raw_dependencies(tkns: List[str]) -> List[str]:
        return [re.sub(r".*\[(.*?)\]+", r'\1', tkn) for tkn in tkns]

    def undefined_entries(self) -> Set[str]:
        """ Return the set of tokens that are referenced but not defined. """
        return as_set([[d for d in self.dependencies(k)
                        if d not in self.grammarelts and d not in self.nonobjects and d not in SPECIAL_TYPES]
                       for k in self.grammarelts.keys()])

    def dependency_closure(self, tkn: str, seen:Optional[Set[str]]=None) -> Set[str]:
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
        circulars = self.circular_references()
        for c in circulars:
            self.grammarelts[forward_ref_tmplt.format(c)] = self.JSGForwardRef(c)
            self.forward_refs.append(c)


    def ordered_elements(self) -> str:
        """ Generator that returns items in ther order needed for the actual python
            1) All forward references
            2) All lexer items
            3) Object / Array definitions in order of increasing dependency depth

            Within each category, items are returned alphabetically
        """
        from pyjsg.parser_impl.jsg_lexerrule_parser import JSGLexerRule
        from pyjsg.parser_impl.jsg_objectexpr_parser import JSGObjectExpr
        from pyjsg.parser_impl.jsg_arrayexpr_parser import JSGArrayExpr

        state = 0
        depth_map = {}
        for k in self.dependency_map.keys():
            self.depth(k, self.dependency_map, depth_map, self.forward_refs)
        # NOTE that depth is not in the closure -- if you create an iterator and then bump depth
        #      the iterator will work against the bumped depth
        depth = -1
        max_depth = max(depth_map.values()) if depth_map else 0
        while state >= 0:
            if state == 0:          # Forward references
                iter_ = (k for k, v in sorted(self.grammarelts.items()) if isinstance(v, self.JSGForwardRef))
                state += 1
            elif state == 1:
                depth += 1
                if depth <= max_depth:
                    iter_ = (k for k, v in self.grammarelts.items()
                             if isinstance(v, JSGLexerRule) and depth_map[k] == depth)
                else:
                    depth = -1
                    state += 1
            elif state == 2:
                depth += 1
                if depth <= max_depth:
                    iter_ = (k for k, v in self.grammarelts.items()
                                    if isinstance(v, (JSGObjectExpr, JSGArrayExpr)) and depth_map[k] == depth)
                else:
                    state = -1
            while state >= 0:
                rval = next(iter_, None)
                if rval is None:
                    break
                yield rval

    class JSGForwardRef:
        def __init__(self, ref: str):
            self._ref = ref

        def __repr__(self):
            return "_ForwardRef('{ref}')".format(ref=self._ref)

        def dependencies(self) -> Set[str]:
            # Forwards don't show dependencies
            return set(self.dependency_list)

        def dependency_list(self):
            return []

    @staticmethod
    def depth(k: str,
              dependency_map: Dict[str, List[str]],
              known_depths: Dict[str, int],
              forwards: List[str]) -> int:
        if k in known_depths:
            return known_depths[k]
        if k in forwards:
            known_depths[forward_ref_tmplt.format(k)] = 1
        max_depth = 0
        for v in dependency_map[k]:
            if v in forwards:
                max_depth = max(max_depth, 1)
            else:
                max_depth = max(max_depth, JSGDocContext.depth(v, dependency_map, known_depths, forwards) + 1)
        known_depths[k] = max_depth
        return max_depth
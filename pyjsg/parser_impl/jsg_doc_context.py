import sys
from abc import ABCMeta, abstractmethod
from collections import OrderedDict
from typing import List, Set, Optional, Dict, Union, Tuple

from .parser_utils import as_set
from pyjsg.parser_impl.anonymousidentifierfactory import AnonymousIdentifierFactory


class PythonGeneratorElement(metaclass=ABCMeta):
    @abstractmethod
    def python_type(self) -> str:
        """ Return the native python type of this element """
        ...

    @abstractmethod
    def signature_type(self) -> str:
        """ Return the formal JSG type of this element """
        ...

    @abstractmethod
    def reference_type(self) -> str:
        """ Return how this type should be referenced from other types """
        ...

    @abstractmethod
    def mt_value(self) -> str:
        """ Return the empty (missing) value token fo rthis element """

    @abstractmethod
    def members_entries(self, all_are_optional: Optional[bool] = False) -> List[Tuple[str, str]]:
        """ Return the name / type initializers for the _members section of the generated python """
        ...

    @abstractmethod
    def dependency_list(self) -> List[str]:
        """ Return an ordered list of element names that this is dependent on """
        ...


class UndefinedElement(PythonGeneratorElement):
    def __init__(self, name) -> None:
        self.name = f"Undefined({name})"

    def __str__(self):
        return self.name

    def python_type(self) -> str:
        return self.name

    def signature_type(self) -> str:
        return self.name

    def reference_type(self) -> str:
        return self.signature_type()

    def mt_value(self) -> str:
        return "None"

    def members_entries(self, all_are_optional: Optional[bool] = False) -> List[Tuple[str, str]]:
        return []

    def dependency_list(self) -> List[str]:
        return []

    def signatures(self, all_are_optional: bool=False) -> List[str]:
        return []

    def initializers(self, prefix: Optional[str] = None) -> List[str]:
        return []


class JSGForwardRef:
    def __init__(self, ref: str):
        self._ref = ref

    @property
    def label(self) -> str:
        return f'"{self._ref}"'


class JSGDocContext:
    """
    Context for JSG to Python conversion
    """
    def __init__(self):
        from pyjsg.parser_impl.jsg_lexerruleblock_parser import JSGLexerRuleBlock
        from pyjsg.parser_impl.jsg_objectexpr_parser import JSGObjectExpr
        from pyjsg.parser_impl.jsg_arrayexpr_parser import JSGArrayExpr
        from pyjsg.parser_impl.jsg_builtinvaluetype_parser import JSGBuiltinValueType

        self.directives: List[str] = []
        self.grammarelts: Dict[str, Union[JSGLexerRuleBlock, JSGObjectExpr,  JSGArrayExpr,
                                          JSGForwardRef, JSGBuiltinValueType]] = OrderedDict()
        self.dependency_map: Dict[str, List[str]] = {}
        self.forward_refs: Dict[str, str] = {}
        self.depths: Dict[str, int] = {}
        self.has_typeid: bool = False

        self._id_factory = AnonymousIdentifierFactory()

    def anon_id(self) -> str:
        """ Generate a new anonymous identifier
        """
        return self._id_factory.next_id()

    def is_anon(self, tkn: str) -> bool:
        """ Determine whther tkn represents an anonymous identifier """
        return self._id_factory.is_anon(tkn)

    def reference(self, tkn: str):
        """ Return the element that tkn represents"""
        return self.grammarelts[tkn] if tkn in self.grammarelts else UndefinedElement(tkn)

    def python_type(self, tkn: str) -> str:
        from pyjsg.parser_impl.jsg_objectexpr_parser import JSGObjectExpr

        typ = self.reference(tkn)
        if tkn in self.forward_refs and isinstance(typ, JSGObjectExpr):
            return self.forward_refs[tkn]
        return typ.python_type()

    def signature_type(self, tkn: str) -> str:
        from pyjsg.parser_impl.jsg_objectexpr_parser import JSGObjectExpr

        typ = self.reference(tkn)
        if tkn in self.forward_refs and isinstance(typ, JSGObjectExpr):
            return self.forward_refs[tkn]
        return typ.signature_type()

    def reference_type(self, tkn: str) -> str:
        if tkn in self.forward_refs:
            return self.forward_refs[tkn]
        typ = self.reference(tkn)
        if isinstance(typ, UndefinedElement):
            return typ.reference_type()
        return tkn

    def dependency_list(self, tkn: str) -> List[str]:
        """Return a list all of the grammarelts that depend on tkn

        :param tkn: 
        :return:
        """
        if tkn not in self.dependency_map:
            self.dependency_map[tkn] = [tkn]        # Force a circular reference
            self.dependency_map[tkn] = self.reference(tkn).dependency_list()
        return self.dependency_map[tkn]

    def dependencies(self, tkn: str) -> Set[str]:
        """Return all the items that tkn depends on as a set

        :param tkn:
        :return:
        """
        return set(self.dependency_list(tkn))

    def undefined_entries(self) -> Set[str]:
        """ Return the set of tokens that are referenced but not defined. """
        return as_set([[d for d in self.dependencies(k) if d not in self.grammarelts]
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
            if state == 0:
                depth += 1
                if depth <= max_depth:
                    iter_ = (k for k, v in self.grammarelts.items()
                             if isinstance(v, (JSGLexerRuleBlock, JSGBuiltinValueType)) and self.depths[k] == depth)
                else:
                    depth = -1
                    state += 1
            elif state == 1:
                depth += 1
                if depth <= max_depth:
                    iter_ = (k for k, v in self.grammarelts.items()
                             if isinstance(v, (JSGObjectExpr, JSGArrayExpr, JSGValueType)) and
                             self.depths[k] == depth and k not in self.forward_refs)
                else:
                    depth = -1
                    state += 1
            elif state == 2:          # Forward references
                depth += 1
                if depth <= max_depth:
                    iter_ = (k for k, v in self.grammarelts.items()
                             if isinstance(v, (JSGObjectExpr, JSGArrayExpr, JSGValueType)) and
                             self.depths[k] == depth and k in self.forward_refs)
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

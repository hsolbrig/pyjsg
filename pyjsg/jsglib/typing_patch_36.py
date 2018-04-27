import sys

# Typing_patch module for Python 3.6

# Note: ModuleType and _ForwardRef and _Union IDE errors are expected
from types import ModuleType
if sys.version_info < (3, 7):
    from typing import GenericMeta, Dict, Any, List, Union, _ForwardRef
from collections import Iterable


# TODO: Pay attention to the goings on at the python development (http://bugs.python.org/issue29262) and #377

def conforms(element, etype, namespace: Dict[str, Any]) -> bool:
    if isinstance(element, str) and element == '_context':
        return True
    elif is_forward(etype):
        etype = etype._eval_type(namespace, namespace)      # Everything should have been resolved
    if is_union(etype):
        return union_conforms(element, etype, namespace)
    elif is_dict(etype):
        return dict_conforms(element, etype, namespace)
    elif is_iterable(etype):
        return iterable_conforms(element, etype, namespace)
    else:
        return element_conforms(element, etype)


def is_typing_type(etype) -> bool:
    return is_union(etype) or is_dict(etype) or is_iterable(etype)


def is_forward(etype) -> bool:
    return type(etype) is _ForwardRef


def is_union(etype) -> bool:
    return type(etype) == type(Union)


def is_dict(etype) -> bool:
    return type(etype) is GenericMeta and etype.__extra__ is dict


def is_iterable(etype) -> bool:
    return type(etype) is GenericMeta and issubclass(etype.__extra__, Iterable)


def union_conforms(element, etype, namespace: Dict[str, Any]) -> bool:
    if is_union(etype):
        union_vals = etype.__union_params__ if sys.version_info < (3, 6) else etype.__args__
        return any(conforms(element, t, namespace) for t in union_vals)
    return False


def dict_conforms(element, etype, namespace: Dict[str, Any]) -> bool:
    if is_dict(etype) and isinstance(element, dict):
        kt, vt = etype.__args__
        return all(conforms(k, kt, namespace) and
                   conforms(v, vt, namespace) for k, v in element.items())
    return False


def iterable_conforms(element, etype, namespace: Dict[str, Any]) -> bool:
    if element is None and issubclass(etype, List):
        element = []
    if is_iterable(etype) and isinstance(element, Iterable):
        vt = etype.__args__[0]
        return all(conforms(e, vt, namespace) for e in element)
    return False


def element_conforms(element, etype) -> bool:
    if element is None and etype == object:
        return False
    elif isinstance(etype, type(type)) and (issubclass(etype, type(None))):
        return element is None
    elif element is None:
        return False
    return isinstance(element, etype)

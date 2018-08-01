import sys

# Typing_patch module for Python 3.6

# Note: ModuleType and _ForwardRef and _Union IDE errors are expected
from types import ModuleType
from collections import Iterable


if sys.version_info < (3, 7):
    from typing import GenericMeta, Dict, Any, List, Union, _ForwardRef, Callable


def proc_forward(etype, namespace: Dict[str, Any]):
    """ Resolve etype to an actual type if it is a forward reference """
    return etype._eval_type(namespace, namespace) if type(etype) is _ForwardRef else etype


def is_union(etype) -> bool:
    """ Determine whether etype is a Union """
    return type(etype) == type(Union)


def is_dict(etype) -> bool:
    """ Determine whether etype is a Dict """
    return type(etype) is GenericMeta and etype.__extra__ is dict


def is_iterable(etype) -> bool:
    """ Determine whether etype is a List or other iterable """
    return type(etype) is GenericMeta and issubclass(etype.__extra__, Iterable)


def union_conforms(element: Union, etype, namespace: Dict[str, Any], conforms: Callable) -> bool:
    """ Determine whether element conforms to at least one of the types in etype

    :param element: element to test
    :param etype: type to test against
    :param namespace: Namespace to use for resolving forward references
    :param conforms: conformance test function
    :return: True if element conforms to at least one type in etype
    """
    union_vals = etype.__union_params__ if sys.version_info < (3, 6) else etype.__args__
    return any(conforms(element, t, namespace) for t in union_vals)

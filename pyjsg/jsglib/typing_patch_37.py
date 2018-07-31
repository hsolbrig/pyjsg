import sys

from typing import Dict, Any, List, Union, ForwardRef
from collections.abc import Iterable


def proc_forward(etype, namespace: Dict[str, Any]):
    """ Resolve etype to an actual type if it is a forward reference """
    return etype._evaluate(namespace, namespace) if type(etype) is ForwardRef else etype


def is_union(etype) -> bool:
    """ Determine whether etype is a Union """
    return getattr(etype, '__origin__', None) is not None and\
           getattr(etype.__origin__, '_name', None) and\
           etype.__origin__._name == 'Union'


def is_dict(etype) -> bool:
    """ Determine whether etype is a Dict """
    return issubclass(type(etype), dict)


def is_iterable(etype) -> bool:
    """ Determine whether etype is a List or other iterable """
    return getattr(etype, '__origin__', None) is not None and issubclass(etype.__origin__, Iterable)


def conforms(element, etype, namespace: Dict[str, Any]) -> bool:
    """ Determine whether element conforms to etype

    :param element: Element to test for conformance
    :param etype: Type to test against
    :param namespace: Namespace to use to resolve forward references
    :return:
    """
    etype = proc_forward(etype, namespace)
    if is_union(etype):
        return union_conforms(element, etype, namespace)
    elif is_dict(etype):
        return dict_conforms(element, etype, namespace)
    elif is_iterable(etype):
        return iterable_conforms(element, etype, namespace)
    else:
        return element_conforms(element, etype)


def union_conforms(element: Union, etype, namespace: Dict[str, Any]) -> bool:
    """ Determine whether element conforms to at least one of the types in etype

    :param element: element to test
    :param etype: type to test against
    :param namespace: Namespace to use for resolving forward references
    :return: True if element conforms to at least one type in etype
    """
    return any(conforms(element, t, namespace) for t in etype.__args__)


def dict_conforms(element: Dict, etype, namespace: Dict[str, Any]) -> bool:
    """ Test whether all keys in element conform to the key specification in etype and all values in element
    conform to the value specification in etype

    :param element: element to test
    :param etype: type to test against
    :param namespace: Namespace to use for resolving forward references
    :return:
    """
    if isinstance(element, dict):
        kt, vt = etype.__args__
        return all(conforms(k, kt, namespace) and
                   conforms(v, vt, namespace) for k, v in element.items())
    return False


def iterable_conforms(element: Iterable, etype, namespace: Dict[str, Any]) -> bool:
    """ Determine whether all items in element conform to etype

    :param element: iterator providing items
    :param etype: type to test against
    :param namespace: Namespace to use for resolving forward references
    :return:
    """
    if isinstance(element, Iterable):
        vt = etype.__args__[0]
        return all(conforms(e, vt, namespace) for e in element)
    return False


def element_conforms(element, etype) -> bool:
    """ Determine whether element conforms to etype"""
    from pyjsg.jsglib import Empty
    from pyjsg.jsglib import AnyType

    if getattr(etype, '_special', None) is not None and not etype._special:
        return issubclass(type(element), type(etype))
    elif getattr(etype, '__origin__', None):
        return isinstance(element, etype.__origin__)
    elif isinstance(element, etype):
        return True
    # TODO: Clean this up
    if (element is None or element is Empty) and issubclass(etype, type(None)):
        return True
    elif element is Empty:
        return False
    elif element is None and (etype == object or etype is AnyType):
        return True
    elif isinstance(etype, type(type)) and (issubclass(etype, type(None))):
        return element is None
    elif element is None:
        return False
    elif getattr(etype, '_special', None) is not None and not etype._special:
        return issubclass(type(element), type(etype))
    elif getattr(etype, '__origin__', None):
        return isinstance(element, etype.__origin__)
    else:
        return isinstance(element, etype)

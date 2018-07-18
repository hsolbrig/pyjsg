import json
import sys
import types
from abc import abstractmethod, ABCMeta
from typing import Union, Any, Dict, List


from .logger import *

if sys.version_info < (3, 7):
    from .typing_patch_36 import conforms, is_union
else:
    from .typing_patch_37 import conforms, is_union



class JSGContext:
    """ Context available to all JSG constructs """
    def __init__(self):
        # the object member name, if any, that identifies the type of object. If present, must match the name of
        # a JSGObject
        self.TYPE: str = ""

        # Objects that lack type identifiers.  Any objects lacking a TYPE variable will be matched against
        # the list below in order
        self.TYPE_EXCEPTIONS: List[str] = []

        # Object pair names that can always exist in an object
        self.IGNORE: List[str] = []                    # type: List[str]

        # True means that we allow JSON_LD constructs (parameters starting with "@")
        self.JSON_LD = True

        # NAMESPACE prevents references from being resolved against other JSG modules
        self.NAMESPACE: Dict[str, Any] = None

    def unvalidated_parm(self, parm: str) -> bool:
        """Return true if the pair name should be ignored

        :param parm: string part of pair string:value
        :return: True if it should be accepted
        """
        return parm.startswith("_") or parm == self.TYPE or parm in self.IGNORE or \
            (self.JSON_LD and parm.startswith('@'))


class JSGValidateable:
    """
    Mixin -- any class with an _is_valid function
    """
    @abstractmethod
    def _is_valid(self, log: Optional[Union[TextIO, Logger]] = None) -> bool:
        """Mixin

        :param log: Logger or IO device to record errors
        :return: True if valid, false otherwise
        """
        raise NotImplementedError("_is_valid must be implemented")

    @property
    def _class_name(self) -> str:
        return type(self).__name__


# We have to be able to differentiate between AnyType with a valid None value ("x": null) and
# an uninitialized AnyType.  EmptyAny is the default value for the latter case
class _EmptyAny:
    pass


EmptyAny = _EmptyAny()


class AnyTypeMeta(type):

    def __instancecheck__(self, instance) -> bool:
        return instance is not EmptyAny


class AnyType(JSGValidateable, metaclass=AnyTypeMeta):
    _strict = False

    def __init__(self, val: Any, **kwargs):
        """ Construct a wild card variable

        :param val: value
        :param kwargs: named arguments
        """
        self.val = val
        super().__init__(**kwargs)

    def _is_valid(self, log: Optional[Union[TextIO, Logger]] = None) -> bool:
        return self.val is not EmptyAny

    def _is_initialized(self) -> bool:
        return self.val is not EmptyAny


UNKNOWN_TYPE_EXCEPTION = "Type '{}' is undefined"


class JSGFactory(metaclass=ABCMeta):
    @abstractmethod
    def instance_(self, element: Any) -> bool:
        ...

    @abstractmethod
    def factory(self, value: Any) -> JSGValidateable:
        ...


def loads_loader(load_module: types.ModuleType, pairs: Dict[str, str]) -> Optional[JSGValidateable]:
    """
    json loader objecthook.
    :param load_module: Module that contains the various types
    :param pairs: key/value tuples (In our case, they are str/str)
    :return:
    """
    cntxt = load_module._CONTEXT

    # If the type element is a member of the JSON, load it
    possible_type = pairs[cntxt.TYPE] if cntxt.TYPE in pairs else None
    target_class = getattr(load_module, possible_type, None) if isinstance(possible_type, str) else None
    if target_class:
        return target_class(**pairs)

    # See whether there are any exception types that are valid for the incoming data
    for type_exception in cntxt.TYPE_EXCEPTIONS:
        if not hasattr(load_module, type_exception):
            raise ValueError(UNKNOWN_TYPE_EXCEPTION.format(type_exception))
        target_class = getattr(load_module, type_exception)
        target_strict = target_class._strict
        target_class._strict = False
        try:
            rval = target_class(**pairs)
        finally:
            target_class._strict = target_strict
        if is_valid(rval):
            return rval

    # If there is not a type variable and nothing fits, just load up the first (and perhaps only) exception
    # It will later fail any is_valid tests
    if not cntxt.TYPE and cntxt.TYPE_EXCEPTIONS:
        return getattr(load_module, cntxt.TYPE_EXCEPTIONS[0])(**pairs)

    if cntxt.TYPE in pairs:
        raise ValueError(f'Unknown reference type: "{cntxt.TYPE}": "{pairs[cntxt.TYPE]}"')
    else:
        raise ValueError(f'Missing "{cntxt.TYPE}" element')


def loads(s: str, load_module: types.ModuleType, **kwargs):
    """ Convert a JSON string into a JSGObject

    :param s: string representation of JSON document
    :param load_module: module that contains declarations for types
    :param kwargs: arguments see: json.load for details
    :return: JSGObject representing the json string
    """
    return json.loads(s, object_hook=lambda pairs: loads_loader(load_module, pairs), **kwargs)


def load(fp: Union[TextIO, str], load_module: types.ModuleType, **kwargs):
    """ Convert a file name or file-like object containing stringified JSON into a JSGObject
    :param fp: file-like object to deserialize
    :param load_module: module that contains declarations for types
    :param kwargs: arguments see: json.load for details
    :return: JSGObject representing the json string
    """
    if isinstance(fp, str):
        with open(fp) as f:
            return loads(f.read(), load_module, **kwargs)
    else:
        return loads(fp.read(), load_module, **kwargs)


def isinstance_(x, A_tuple):
    """ native isinstance_ with the test for typing.Union overridden """
    if is_union(A_tuple):
        return any(isinstance_(x, t) for t in A_tuple.__args__)
    elif getattr(A_tuple, '__origin__', None) is not None:
        return isinstance(x, A_tuple.__origin__)
    else:
        return isinstance(x, A_tuple)


def is_valid(obj: JSGValidateable, log: Optional[Union[TextIO, Logger]] = None) -> bool:
    """ Determine whether obj is valid

    :param obj: Object to validate
    :param log: Logger to record validation failures.  If absent, no information is recorded
    """
    return obj._is_valid(log)

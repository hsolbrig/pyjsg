import json
import sys
import types
from collections import OrderedDict
from typing import Union, Any, Dict

from jsonasobj import JsonObj

from .logger import *

if sys.version_info < (3, 7):
    from .typing_patch_36 import conforms, is_union
else:
    from .typing_patch_37 import conforms, is_union


class JSGException(Exception):
    pass


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

    @abstractmethod
    def _is_initialized(self) -> bool:
        """ Return true if the object has not been assigned a value
        """
        raise NotImplementedError("_is_initialized must be implemented")


class JSGObjectMeta(type):
    _reference_types: List["JSGObject"] = []
    _reference_names: List[str]                 # Names of objects in _reference_types

    def __init__(cls, *args, **kwargs):
        super().__init__(*args, **kwargs)
        cls._reference_names = [t.__name__ for t in cls._reference_types]


class JSGObject(JsonObj, JSGValidateable, metaclass=JSGObjectMeta):
    """
    JSGObject is a JsonObj with constraints.

    Note that methods and variables in JSGObject should always begin with "_", as we currently restrict the set of
    JSON names to those that begin with [a-zA-Z]
    """
    _reference_types: List["JSGObject"] = []
    _reference_names: List[str] = []
    _members: Dict[str, type] = {}      #
    _strict: bool = True                # True means treat extra elements as errors

    def __init__(self, context: JSGContext, **kwargs):
        """ Generic constructor

        :param context: Context for TYPE and IGNORE variables
        :param kwargs: Initial values - object specific
        """
        JsonObj.__init__(self)
        self._context = context
        if self._class_name not in context.TYPE_EXCEPTIONS and context.TYPE:
            self[context.TYPE] = self._class_name
        for k, v in kwargs.items():
            setattr(self, k, kwargs[k])

    def _set_value(self, key, value) -> None:
        from pyjsg.jsglib.jsg_strings import JSGString
        if not isinstance(value, (str, int, bool, float)):
            self[key] = value
        else:
            cur_val = self.__dict__.get(key)
            if cur_val is None or not issubclass(type(cur_val), JSGString):
                self[key] = value
            else:
                self[key] = cur_val.__class__(value)

    def __setattr__(self, key: str, value: Any) -> None:
        """ Attribute setter.  Any attribute that is part of the members list or not validated passes.  Otherwise
        setting is only allowed if the class level _strict mode is False

        :param key:
        :param value:
        :return:
        """
        # Note: The initial startswith below is the only way we can SEE _members or _context...
        if key.startswith('_') or key in self._members or self._context.unvalidated_parm(key):
            self._set_value(key, value)
        elif self._strict:
            raise ValueError("Unknown attribute: {}={}".format(key, value))
        else:
            super().__setattr__(key, value)

    def __delattr__(self, item):
        from pyjsg.jsglib.jsg_strings import JSGString
        attr = getattr(self, item)
        setattr(self, item, type(attr)(None) if issubclass(type(attr), JSGString) else None)

    @staticmethod
    def _strip_nones(d: Dict[str, Any])-> Dict[str, Any]:
        """
        An attribute with type None is equivalent to an absent attribute.
        :param d: Object with attributes
        :return: Object dictionary w/ Nones and underscores removed
        """
        from pyjsg.jsglib.jsg_strings import JSGString, JSGNull
        return OrderedDict({k: None if isinstance(v, JSGNull) and v.val is None else v for k, v in d.items()
                            if not k.startswith("_") and v is not None and v and
                            (issubclass(type(v), JSGObject) or
                                (not issubclass(type(v), JSGString) or v.val is not None) and
                                (not issubclass(type(v), AnyType) or v.val is not EmptyAny))})

    @staticmethod
    def _test(entry, log: Logger) -> bool:
        """
        Test whether entry conforms to its type
        :param entry: entry to test
        :param log: place to record issues
        :return: True if it meets requirements
        """
        if isinstance(entry, dict):
            for k, v in entry.items():
                if isinstance(k, JSGValidateable) and not k._is_valid(log) and not log.logging:
                    return False
                if isinstance(v, JSGValidateable) and not v._is_valid(log) and not log.logging:
                    return False
        elif isinstance(entry, list):
            for v in entry:
                if isinstance(v, JSGValidateable) and not v._is_valid(log) and not log.logging:
                    return False
        elif isinstance(entry, JSGValidateable):
            if not entry._is_valid(log) and not log.logging:
                return False
        return True

    def _default(self, obj: object):
        """ Return a serializable version of obj. Overrides JsonObj _default method
        :param obj: Object to be serialized
        :return: Serialized version of obj
        """
        from pyjsg.jsglib.jsg_strings import JSGString, JSGNull
        return None if isinstance(obj, JSGNull) else \
            JSGObject._strip_nones(obj.__dict__) if isinstance(obj, JsonObj) \
            else cast(JSGString, obj).val if issubclass(type(obj), JSGString) else str(obj)

    def _is_valid_element(self, log: Logger, name: str, entry: JSGValidateable) -> bool:
        from pyjsg.jsglib.jsg_strings import JSGString
        if name not in self._members:
            return any(e._is_valid_element for e in self._reference_types)
        else:
            etype = self._members[name]
            if (etype is str or etype is int or etype is float or etype is bool or etype is object) and \
                    (issubclass(type(entry), (JSGString, AnyType)) or isinstance(entry, AnyType)):
                val = getattr(entry, "val", None)
            else:
                val = entry
            if val is not None and val is not EmptyAny and getattr(entry, "_is_valid", None):
                if not entry._is_valid(log) and not log.logging:
                    return False
            elif not conforms(val, etype, self._context.NAMESPACE):        # Note: None and absent are equivalent
                if val is None or val is EmptyAny:
                    if log.log("{}: Missing required field: '{}'".format(self.__class__.__name__, name)):
                        return False
                else:
                    if log.log("{}: Type mismatch for {}. Expecting: {} Got: {}"
                               .format(self.__class__.__name__, name, etype, type(entry))):
                        return False
            elif val is not None and not self._test(val, log):  # Make sure that entry conforms to its own type
                return False
        return True

    def _is_valid(self, log_file: Optional[Union[Logger, TextIO]] = None) -> bool:
        if log_file is None:
            log = Logger()
        elif isinstance(log_file, Logger):
            log = log_file
        else:
            log = Logger(log_file)
        nerrors = log.nerrors

        if self._context.TYPE and getattr(self, self._context.TYPE, "") != self._class_name \
                and self._class_name not in self._context.TYPE_EXCEPTIONS:
            if log.log("Type mismatch - Expected: {} Actual: {}"
                       .format(self._class_name, getattr(self, self._context.TYPE))):
                return False

        for name in self._members.keys():
            entry = getattr(self, name)
            if not self._is_valid_element(log, name, entry):
                return False

        if self._strict:
            # Test each attribute against the schema
            for k, v in self._strip_nones(self.__dict__).items():
                if k not in self._members and k != self._context.TYPE \
                        and k not in self._context.IGNORE and k != "@context":
                    if not self._is_valid_element(log, k, v):
                        if log.log("Extra element: {}: {}".format(k, v)):
                            return False

        return log.nerrors == nerrors

    def _is_initialized(self) -> bool:
        return True             # Dictionaries always count as initialized - the variables are set to None if not


class JSGObjectMap(JSGObject):
    """
    An object map is a JsonObj with constraints on the attribute names, value types of both
    """
    _name_filter = None
    _value_type = object

    def __init__(self, _context, **_kwargs: Dict[str, Any]):
        super().__init__(_context, **_kwargs)

    def __setattr__(self, key: str, value: Any):
        """
        Screen attributes for name and type.  Anything starting with underscore ('_') goes, anything in the IGNORE list
        and anything declared in the __init_ signature
        :param key:
        :param value:
        :return:
        """
        if not key.startswith("_") and not self._context.unvalidated_parm(key):
            if self._name_filter is not None and not self._name_filter.matches(key):
                raise ValueError("Illegal key: {}={}".format(key, value))
            else:
                if not conforms(value, self._value_type, self._context.NAMESPACE):
                    raise ValueError("Illegal value type {} = {}".format(key, value))
        self[key] = value

    def _is_valid(self, log: Optional[Logger] = None, strict: bool = True) -> bool:
        if log is None:
            log = Logger()
        nerrors = log.nerrors

        if (self._context.TYPE and getattr(self, self._context.TYPE) != self._class_name) \
                and self._class_name not in self._context.TYPE_EXCEPTIONS:
            if log.log("Type mismatch - Expected: {} Actual: {}"
                       .format(self._class_name, getattr(self, self._context.TYPE))):
                return False

        for name, entry in self._strip_nones(self.__dict__).items():
            if self._name_filter is not None and not self._name_filter.matches(name):
                if log.log("{}: Illegal key value: {} = {}".format(self.__class__.__name__, name, entry)):
                    return False
            elif not conforms(entry, self._value_type, self._context.NAMESPACE):
                if entry is None:
                    if log.log("{}: Missing required field: '{}'".format(type(self).__name__, name)):
                        return False
                else:
                    if log.log("{}: Type mismatch for {}. Expecting: {} Got: {}"
                               .format(type(self).__name__, name, self._value_type, type(entry))):
                        return False
            elif entry is not None and not self._test(entry, log):
                return False

        return log.nerrors == nerrors


class Object(JSGObject):
    _strict = False

    def __init__(self, variable_name: str,  *args, **kwargs):
        self._variable_name = variable_name
        super().__init__(*args, **kwargs)


# We have to be able to differentiate between AnyType with a valid None value ("x": null) and
# an uninitialized AnyType.  EmptyAny is the default value for the latter case
class _EmptyAny:
    pass


EmptyAny = _EmptyAny()


class AnyTypeMeta(type):

    def __instancecheck__(self, instance) -> bool:
        return instance is not EmptyAny


class AnyType(JsonObj, JSGValidateable, metaclass=AnyTypeMeta):
    _strict = False

    def __init__(self, val: Any, **kwargs):
        """
        Construct a simple string variable
        :param val: any type that can be cooreced into a string
        :param kwargs: named arguments
        """
        self.val = val
        super().__init__(**kwargs)

    def _is_valid(self, log: Optional[Union[TextIO, Logger]] = None) -> bool:
        return self.val is not EmptyAny

    def _is_initialized(self) -> bool:
        return self.val is not EmptyAny


UNKNOWN_TYPE_EXCEPTION = "Type '{}' is undefined"


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
            raise JSGException(UNKNOWN_TYPE_EXCEPTION.format(type_exception))
        target_class = getattr(load_module, type_exception)
        target_strict = target_class._strict
        target_class._strict = False
        rval = target_class(**pairs)
        target_class._strict = target_strict
        if is_valid(rval):
            return rval

    # If there is not a type variable and nothing fits, just load up the first (and perhaps only) exception
    # It will later fail any is_valid tests
    if not cntxt.TYPE and cntxt.TYPE_EXCEPTIONS:
        return getattr(load_module, cntxt.TYPE_EXCEPTIONS[0])(**pairs)

    if cntxt.TYPE in pairs:
        raise JSGException('Unknown reference type: "{}": "{}"'.format(cntxt.TYPE, pairs[cntxt.TYPE]))
    else:
        raise JSGException('Missing "{}" element'.format(cntxt.TYPE))


def loads(s: str, load_module: types.ModuleType, **kwargs) -> JSGObject:
    """ Convert a JSON string into a JSGObject
    :param s: string representation of JSON document
    :param load_module: module that contains declarations for types
    :param kwargs: arguments see: json.load for details
    :return: JSGObject representing the json string
    """
    return json.loads(s, object_hook=lambda pairs: loads_loader(load_module, pairs), **kwargs)


def load(fp: Union[TextIO, str], load_module: types.ModuleType, **kwargs) -> JSGObject:
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

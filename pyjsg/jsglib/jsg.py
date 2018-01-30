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
import json
import types

from collections import OrderedDict
from typing import Union, Any, Dict, TextIO

from jsonasobj import JsonObj
from .logger import *

from .typing_patch import conforms


# TODO: Extend List to include a minimum and maximum value

class JSGException(Exception):
    pass


class JSGContext:
    """ JSG Context environment
    TYPE - the property that identifies the type of object. If present, must match the name of
           a JSGObject in the generated module
    TYPE_EXCEPTIONS - a list of objects that lack type identifiers.  At the moment, this program
           can deal with at most one of these, which becomes the default for anything that lacks
           a type variable OR has a type variable that doesn't name a known module
    IGNORE - a list of properties that do not generate errors if present in an object
    JSON_LD - True means we allow JSON_LD constructs (parameters w/ "@")
    """
    def __init__(self):
        self.TYPE = ""                      # type: str
        self.TYPE_EXCEPTIONS = []           # type: List[str]
        self.IGNORE = []                    # type: List[str]
        self.JSON_LD = True                 # type: Boolean
        self.NAMESPACE = None               # type: Dict[str, Any]

    def unvalidated_parm(self, parm: str) -> bool:
        """
        Return true if the parameter shouldn't be validated
        :param parm: name of parm
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
        return False

    @property
    def _class_name(self):
        return type(self).__name__


class JSGObjectMeta(type):
    _reference_types = []          # type: List[JSGObject]

    def __init__(cls, *args, **kwargs):
        super().__init__(*args, **kwargs)
        cls._reference_names = [t.__name__ for t in cls._reference_types]


class JSGObject(JsonObj, JSGValidateable, metaclass=JSGObjectMeta):
    """
    JSGObject is a JsonObj with constraints.

    Note that methods and variables in JSGObject should always begin with "_", as we currently restrict the set of
    JSON names to those that begin with [a-zA-Z]
    """
    _reference_types = []           # type: List[JSGObject]
    _reference_names = []           # type: List[str]
    _members = {}                   # type: Dict[str, type]
    _strict = True                  # type: bool

    def __init__(self, context: JSGContext, **kwargs):
        """
        Generic constructor
        :param context: Context for TYPE and IGNORE variables
        :param kwargs: Initial values - object specific
        """
        JsonObj.__init__(self)
        self._context = context
        if self._class_name not in context.TYPE_EXCEPTIONS and context.TYPE:
            self[context.TYPE] = self._class_name
        for k, v in kwargs.items():
            setattr(self, k, kwargs[k])

    def _set_value(self, key, value):
        if not isinstance(value, (str, int, bool, float)):
            self[key] = value
        else:
            cur_val = self.__dict__.get(key)
            if cur_val is None or not issubclass(type(cur_val), JSGString):
                self[key] = value
            else:
                self[key] = cur_val.__class__(value)

    def __setattr__(self, key: str, value: Any):
        """
        Screen attributes for name and type.  Anything starting with underscore ('_') goes, anything in the IGNORE list
        and anything declared in the __init_ signature
        :param key:
        :param value:
        :return:
        """
        if key == "_context":
            self[key] = value
        elif key in self._members or self._context.unvalidated_parm(key):
            self._set_value(key, value)
        elif self._strict:
            raise ValueError("Unknown attribute: {}={}".format(key, value))

    def __delattr__(self, item):
        attr = getattr(self, item)
        setattr(self, item, type(attr)(None) if issubclass(type(attr), JSGString) else None)

    @staticmethod
    def _strip_nones(d: Dict[str, Any])-> Dict[str, Any]:
        """
        An attribute with type None is equivalent to an absent attribute.
        :param d: Object with attributes
        :return: Object dictionary w/ Nones and underscores removed
        """
        return OrderedDict({k: None if isinstance(v, JSGNull) and v.val is not None else v for k, v in d.items()
                            if not k.startswith("_") and v is not None and
                            (not issubclass(type(v), JSGString) or v.val is not None)})

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
        return JSGObject._strip_nones(obj.__dict__) if isinstance(obj, JsonObj) \
            else cast(JSGString, obj).val if issubclass(type(obj), JSGString) else str(obj)

    def _is_valid_element(self, log: Logger, name: str, entry: JSGValidateable) -> bool:
        if name not in self._members:
            return any(e._is_valid_element for e in self._reference_types)
        else:
            etype = self._members[name]
            if (etype is str or etype is int or etype is float or etype is bool) and \
                    issubclass(type(entry), JSGString):
                val = getattr(entry, "val", None)
            else:
                val = entry
            if val is not None and getattr(entry, "_is_valid", None):
                if not entry._is_valid(log) and not log.logging:
                    return False
            elif not conforms(val, etype, self._context.NAMESPACE):        # Note: None and absent are equivalent
                if val is None:
                    if log.log("{}: Missing required field: {}".format(self.__class__.__name__, name)):
                        return False
                else:
                    # TODO: Debugging
                    conforms(val, etype, self._context.NAMESPACE)
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


class JSGObjectMap(JSGObject):
    """
    An object map is a JsonObj with constraints on the attribute names, value types of both
    """
    _name_filter = None               # type: Optional[JSGPattern]
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
                    if log.log("{}: Missing required field: {}".format(type(self).__name__, name)):
                        return False
                else:
                    if log.log("{}: Type mismatch for {}. Expecting: {} Got: {}"
                               .format(type(self).__name__, name, self._value_type, type(entry))):
                        return False
            elif entry is not None and not self._test(entry, log):
                return False

        return log.nerrors == nerrors


class JSGPattern:
    """
    A lexerRuleBlock
    """
    def __init__(self, pattern: str):
        """
        Compile and record a match pattern
        :param pattern:
        """
        self.pattern_re = re.compile(pattern, flags=re.DOTALL)

    def __str__(self):
        return self.pattern_re.pattern

    def matches(self, txt: str) -> bool:
        """
        Determine whether txt matches pattern
        :param txt: text to check
        :return: True if match
        """
        # rval = ref.getText()[1:-1].encode('utf-8').decode('unicode-escape')
        if r'\\u' in self.pattern_re.pattern:
            txt = txt.encode('utf-8').decode('unicode-escape')
        match = self.pattern_re.match(txt)
        return match is not None and match.end() == len(txt)


class JSGStringMeta(type):
    pattern = None          # type: Optional[JSGPattern]

    def __init__(cls, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __instancecheck__(self, instance) -> bool:
        # Note: IDE warning on pattern is ok
        if not self.pattern:
            return isinstance(instance, str)
        else:
            return instance is not None and \
                   self.pattern.matches(str(instance).lower() if isinstance(instance, bool) else str(instance))


class JSGString(JSGValidateable, metaclass=JSGStringMeta):
    """
    A lexerRuleSpec implementation
    """
    pattern = None          # type: Optional[JSGPattern]

    def __init__(self, val: Any, validate: bool=True):
        """
        Construct a simple string variable
        :param val: any type that can be cooreced into a string
        :param validate: validate on entry
        """
        if validate and not self._is_valid_value(val):
            raise ValueError('Invalid {} value: "{}"'.format(self._class_name, val))
        super().__setattr__("val", self._adjust_for_json(val))

    @classmethod
    def _is_valid_value(cls, val: str) -> bool:
        """
        Determine whether val is a valid value for this string
        :param val: value to test
        :return:
        """
        return cls.pattern is None or val is None or cls.pattern.matches(cls._adjust_for_json(val))

    @staticmethod
    def _adjust_for_json(val: Any) -> Any:
        return str(val).lower() if isinstance(val, bool) else str(val) if val is not None else None

    def _is_valid(self, log: Optional[Logger] = None) -> bool:
        """
        Determine whether the string is valid
        :param log: function for reporting the result
        :return: Result
        """
        if self._is_valid_value(self.val):
            return True
        if log:
            log.log('Invalid {} value: "{}"'.format(self._class_name, self.val))
        return False

    def __str__(self):
        return str(self.val)

    def __eq__(self, other):
        return self.val == (other.val if issubclass(type(other), JSGString) else other)

    def __hash__(self):
        return hash(self.val)


class Array(JSGObject):
    pass


class String(JSGString):

    def __setattr__(self, key, value):
        self.__dict__[key] = str(value) if key == "val" and value is not None else value


class Number(JSGString):
    pattern = JSGPattern(r'-?(0|[1-9][0-9]*)(.[0-9]+)?([eE][+-]?[0-9]+)?')
    int_pattern = JSGPattern(r'-?(0|[1-9][0-9]*)')

    def __getattribute__(self, item):
        attval = super().__getattribute__(item)
        return attval if item != "val" or attval is None else int(attval) \
            if self.int_pattern.matches(attval) else float(attval)


class Integer(Number):
    pattern = JSGPattern(r'-?(0|[1-9][0-9]*)')

    def __getattribute__(self, item):
        attval = super().__getattribute__(item)
        return attval if item != "val" or attval is None else int(attval)


class Boolean(JSGString):
    true_pattern = JSGPattern(r'[Tt]rue')
    false_pattern = JSGPattern(r'[Ff]alse')
    pattern = JSGPattern(r'{}|{}'.format(true_pattern, false_pattern))

    def __setattr__(self, key, value):
        if key == "val" and value is not None:
            # Note - final value below causes an exception
            self.__dict__[key] = str(value).lower() if isinstance(value, bool) \
                else str(value.val) if type(value) == Boolean else Boolean(value)
        else:
            self.__dict__[key] = value

    def __getattribute__(self, item):
        attval = super().__getattribute__(item)
        return attval if item != "val" or attval is None else self.true_pattern.matches(attval)


class JSGNull(JSGString):
    pattern = JSGPattern(r'null|None')

    def __init__(self, val: Optional[Any] = None, validate: bool=True):
        self.val = val
        super().__init__(val, validate)

    def __setattr__(self, key, value):
        self.__dict__[key] = "null" if key == "val" and value is not None else value

    def __str__(self):
        return str(self.val)

    def _is_valid(self, log: Optional[Logger] = None, strict: bool = True) -> bool:
        return self.val is None or self.val == "null"


Null = JSGNull("null")


class Object(JSGObject):
    pass


class AnyType(JsonObj, JSGValidateable):
    def __init__(self, val: Any, **kwargs):
        """
        Construct a simple string variable
        :param val: any type that can be cooreced into a string
        :param kwargs: named arguments
        """
        self.val = val
        super().__init__(**kwargs)

    def _is_valid(self, log: Optional[Logger] = None):
        return True


def loads_loader(load_module: types.ModuleType, pairs: Dict[str, str]) -> Optional[JSGValidateable]:
    """
    json loader objecthook.
    :param load_module: Module that contains the various types
    :param pairs: key/value tuples (In our case, they are str/str)
    :return:
    """
    # Note: At the moment, this package assumes that there is, at most, one JSON object that
    #       doesn't have a type identifier.  For various and sundry reasons, we will assume that it
    #       is the first entry in the exceptions list (because, of there is NO context type, then we
    #       add all object definitions to the exception list...)
    target_class = getattr(load_module, pairs[load_module._CONTEXT.TYPE], None) \
        if load_module._CONTEXT.TYPE in pairs else None
    if not target_class and len(load_module._CONTEXT.TYPE_EXCEPTIONS) == 1:
        target_class = getattr(load_module, load_module._CONTEXT.TYPE_EXCEPTIONS[0], None)
    if target_class:
        return target_class(**pairs)
    if load_module._CONTEXT.TYPE in pairs:
        raise JSGException("Unknown type: {}".format(pairs[load_module._CONTEXT.TYPE]))
    else:
        raise JSGException("Missing {} var".format(load_module._CONTEXT.TYPE))


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
    if type(A_tuple) == type(Union):
        return any(isinstance_(x, t) for t in A_tuple.__args__)
    return isinstance(x, A_tuple)

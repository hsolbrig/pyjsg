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
from typing import TextIO, Union, Optional, Any, Dict
from inspect import signature, Parameter

from jsonasobj import JsonObj
from .logger import Logger

from .typing_patch import conforms


class JSGContext:
    def __init__(self):
        self.TYPE = ""
        self.TYPE_EXCEPTIONS = []
        self.IGNORE = []


# TODO: Extend List to include a minimum and maximum value

class JSGValidateable:
    """
    Mixin -- any class with an _is_valid function
    """
    def _is_valid(self, log: Optional[Logger] = None) -> bool:
        """
        Mixin
        :param log: Logger to record reason for non validation.
        :return: True if valid, false otherwise
        """
        log.log("Unimplemented validate function")
        return False

    @property
    def _class_name(self):
        return type(self).__name__


class JSGObject(JsonObj, JSGValidateable):
    """
    JSGObject is a JsonObj with constraints.

    Note that methods and variables in JSGObject should always begin with "_", as we currently restrict the set of
    JSON names to those that begin with [a-zA-Z]
    """

    def __init__(self, context: JSGContext, **kwargs):
        """
        Generic constructor
        """
        JsonObj.__init__(self)
        self._context = context
        self[context.TYPE] = self._class_name  # type: str
        for k, v in kwargs.items():
            setattr(self, k, kwargs[k])

    def __setattr__(self, key: str, value: Any):
        """
        Screen attributes for name and type.  Anything starting with underscore ('_') goes, anything in the IGNORE list
        and anything declared in the __init_ signature
        :param key:
        :param value:
        :return:
        """
        if key in signature(self.__init__).parameters:
            parm = signature(self.__init__).parameters[key]
            if parm.kind == Parameter.POSITIONAL_OR_KEYWORD:
                self[key] = value
            elif parm.kind == Parameter.VAR_KEYWORD:
                for k, v in value:
                    setattr(self, k, v)
            elif key.startswith("_") or key in self._context.IGNORE:
                self[key] = value
            else:
                raise ValueError("Unknown attribute: {}={}".format(key, value))
        elif key.startswith("_") or key in self._context.IGNORE or key == "@context" or key == self._context.TYPE:      # TODO: generalize this
            self[key] = value
        else:
            raise ValueError("Unknown attribute: {}={}".format(key, value))

    @staticmethod
    def _strip_nones(d: Dict[str, Any])-> Dict[str, Any]:
        """
        An attribute with type None is equivalent to an absent attribute.
        :param d: Object with attributes
        :return: Object dictionary w/ Nones and underscores removed
        """
        return OrderedDict({k: v for k, v in d.items() if not k.startswith("_") and v is not None})

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
        return JSGObject._strip_nones(obj.__dict__) if isinstance(obj, JsonObj)\
            else str(obj) if isinstance(obj, JSGString) else json.JSONEncoder().default(obj)

    def _is_valid(self, log: Optional[Logger] = None, strict: bool = True) -> bool:
        if log is None:
            log = Logger()
        nerrors = log.nerrors

        if getattr(self, self._context.TYPE) != self._class_name:
            if log.log("Type mismatch - Expected: {} Actual: {}"
                            .format(self._class_name, getattr(self, self._context.TYPE))):
                return False

        sig = signature(self.__init__)
        for name, parm in sig.parameters.items():
            if name != "self" and parm.kind == Parameter.POSITIONAL_OR_KEYWORD:
                typ = parm.annotation
                entry = getattr(self, name)         # Note: None and absent are equivalent
                if not conforms(entry, typ):
                    if entry is None:
                        if log.log("{}: Missing required field: {}".format(type(self).__name__, name)):
                            return False
                    else:
                        if log.log("{}: Type mismatch for {}. Expecting: {} Got: {}"
                                   .format(type(self).__name__, name, typ, type(entry))):
                            return False
                elif entry is not None and not self._test(entry, log):  # Make sure that entry conforms to its own type
                    return False

        if strict:
            # Test each attribute against the schema
            for k, v in self._strip_nones(self.__dict__).items():
                if k not in sig.parameters and k != self._context.TYPE \
                        and k not in self._context.IGNORE and k != "@context":  # TODO: Address this
                    if log.log("Extra element: {}: {}".format(k, v)):
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
        self.pattern = re.compile(pattern)

    def matches(self, txt: str) -> bool:
        """
        Determine whether txt matches pattern
        :param txt: text to check
        :return: True if match
        """
        match = self.pattern.match(txt)
        return match and match.endpos == len(txt)


class JSGStringMeta(type):

    def __instancecheck__(self, instance) -> bool:
        return not self.pattern or self.pattern.matches(str(instance).lower()
                                                        if isinstance(instance, bool) else str(instance))


class JSGString(JSGValidateable, metaclass=JSGStringMeta):
    """
    A lexerRuleSpec
    """
    pattern = None          # type: JSGPattern

    def __init__(self, val):
        """
        Construct a simple string variable
        :param val: any type that can be cooreced into a string
        """
        self.val = self._adjust_for_json(val)

    @staticmethod
    def _adjust_for_json(val: Any) -> str:
        return str(val).lower() if isinstance(val, bool) else str(val)

    def _is_valid(self, log: Optional[Logger] = None) -> bool:
        """
        Determine whether the string is valid
        :param log: function for reporting the result
        :return: Result
        """
        if self.pattern:
            if self.pattern.matches(self.val):
                return True
            log.log("Wrong type: {}: {}".format(self._class_name, self.val))
            return False
        return True

    def __str__(self):
        return self.val

    def __eq__(self, other):
        return self.val == str(other)

    def __hash__(self):
        return hash(self.val)


def loads_loader(module: types.ModuleType, pairs: Dict[str, object]) -> Optional[JSGValidateable]:
    """
    json loader objecthook
    :param module: Module that contains the various types
    :param pairs: key/value tuples
    :return:
    """
    if module._CONTEXT.TYPE in pairs:
        cls = getattr(module, pairs[module._CONTEXT.TYPE], None)
        if cls:
            return cls(**pairs)
        raise Exception("Unknown type: {}".format(pairs[module._CONTEXT.TYPE]))
    return None


def loads(s: str, module: types.ModuleType, **kwargs) -> JSGObject:
    """ Convert a JSON string into a JSGObject
    :param s: string representation of JSON document
    :param module: module that contains declarations for types
    :param kwargs: arguments see: json.load for details
    :return: JSGObject representing the json string
    """
    return json.loads(s, object_hook=lambda pairs: loads_loader(module, pairs), **kwargs)


def load(fp: Union[TextIO, str], module: types.ModuleType, context: JSGContext, **kwargs) -> JSGObject:
    """ Convert a file name or file-like object containing stringified JSON into a JSGObject
    :param fp: file-like object to deserialize
    :param module: module that contains declarations for types
    :param kwargs: arguments see: json.load for details
    :return: JSGObject representing the json string
    """
    if isinstance(fp, str):
        with open(fp) as f:
            return loads(f.read(), module, **kwargs)
    else:
        return loads(fp.read(), module, **kwargs)

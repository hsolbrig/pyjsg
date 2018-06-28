import re
from typing import Optional, Any

from pyjsg.jsglib.jsg import JSGValidateable, Logger


class JSGPattern:
    """
    A lexerRuleBlock
    """
    def __init__(self, pattern: str):
        """
        Compile and record a match pattern

        :param pattern: regular expression
        """
        self.pattern_re = re.compile(pattern, flags=re.DOTALL)

    def __str__(self):
        return self.pattern_re.pattern

    def matches(self, txt: str) -> bool:
        """Determine whether txt matches pattern

        :param txt: text to check
        :return: True if match
        """
        # rval = ref.getText()[1:-1].encode('utf-8').decode('unicode-escape')
        if r'\\u' in self.pattern_re.pattern:
            txt = txt.encode('utf-8').decode('unicode-escape')
        match = self.pattern_re.match(txt)
        return match is not None and match.end() == len(txt)


class JSGStringMeta(type):
    pattern: Optional[JSGPattern]

    def __instancecheck__(self, instance) -> bool:
        if not self.pattern:
            return isinstance(instance, str)
        else:
            return instance is not None and \
                   self.pattern.matches(str(instance).lower() if isinstance(instance, bool) else str(instance))


class JSGString(JSGValidateable, metaclass=JSGStringMeta):
    """
    A lexerRuleSpec implementation
    """
    pattern: Optional[JSGPattern] = None
    val: str

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
    def _is_valid_value(cls, val) -> bool:
        """ Determine whether val is a valid value for this string

        :param val: value to test
        :return:
        """
        return val is None or \
            (isinstance(val, str) and (cls.pattern is None or cls.pattern.matches(cls._adjust_for_json(val))))

    def _is_initialized(self) -> bool:
        return self.val is not None

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


class String(JSGString):

    def __setattr__(self, key, value):
        self.__dict__[key] = str(value) if key == "val" and value is not None else value


class Number(JSGString):
    pattern = JSGPattern(r'-?(0|[1-9][0-9]*)(.[0-9]+)?([eE][+-]?[0-9]+)?')
    int_pattern = JSGPattern(r'-?(0|[1-9][0-9]*)')

    @classmethod
    def _is_valid_value(cls, val) -> bool:
        """ Determine whether val is a valid value for this string

        :param val: value to test
        :return:
        """
        return val is None or cls.pattern.matches(str(val))

    def __getattribute__(self, item):
        attval = super().__getattribute__(item)
        return attval if item != "val" or attval is None else int(attval) \
            if self.int_pattern.matches(attval) else float(attval)

    def __int__(self) -> int:
        return int(self.val)

    def __float__(self) -> float:
        return float(self.val)


class Integer(Number):
    pattern = JSGPattern(r'-?(0|[1-9][0-9]*)')

    @classmethod
    def _is_valid_value(cls, val) -> bool:
        """ Determine whether val is a valid value for this string

        :param val: value to test
        :return:
        """
        return val is None or cls.pattern.matches(str(val))

    def __getattribute__(self, item) -> Optional[int]:
        attval = super().__getattribute__(item)
        return attval if item != "val" or attval is None else int(attval)

    def __int__(self) -> int:
        return int(self.val)


class Boolean(JSGString):
    true_pattern = JSGPattern(r'[Tt]rue')
    false_pattern = JSGPattern(r'[Ff]alse')
    pattern = JSGPattern(r'{}|{}'.format(true_pattern, false_pattern))

    @classmethod
    def _is_valid_value(cls, val) -> bool:
        return val is None or cls.pattern.matches(str(val))

    def __setattr__(self, key: str, value: Any) -> None:
        if key == "val" and value is not None:
            # Note - final value below causes an exception
            self.__dict__[key] = str(value).lower() if isinstance(value, bool) \
                else str(value.val) if type(value) == Boolean else Boolean(value)
        else:
            self.__dict__[key] = value

    def __getattribute__(self, item):
        attval = super().__getattribute__(item)
        return attval if item != "val" or attval is None else self.true_pattern.matches(attval)

    def __bool__(self) -> bool:
        return bool(self.val)


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

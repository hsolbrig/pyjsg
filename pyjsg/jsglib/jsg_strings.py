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
    pattern: Optional[JSGPattern] = None

    def __instancecheck__(self, instance) -> bool:
        if not self.pattern:
            return isinstance(instance, str)
        else:
            return instance is not None and self.pattern.matches(instance)


class JSGString(JSGValidateable, metaclass=JSGStringMeta):
    """
    A lexerRuleSpec implementation
    """
    pattern: Optional[JSGPattern] = None

    def __init__(self, val: Any) -> None:
        """Construct a simple string variable

        :param val: any type that can be cooreced into a string
        """
        self.val = val

    def __setattr__(self, key: str, val: Optional[str]) -> None:
        if key == 'val' and not self._is_valid_value(val):
            raise ValueError('Invalid {} value: "{}"'.format(self._class_name, val))
        super().__setattr__(key, val)

    @classmethod
    def _is_valid_value(cls, val) -> bool:
        """ Determine whether val is a valid value for this string

        :param val: value to test
        :return:
        """
        return val is None or \
            (isinstance(val, str) and (cls.pattern is None or cls.pattern.matches(cls._adjust_for_json(val))))

    @staticmethod
    def _adjust_for_json(val: Any) -> Any:
        return str(val).lower() if isinstance(val, bool) else str(val) if val is not None else None

    def _is_valid(self, log: Optional[Logger] = None) -> bool:
        """ Determine whether the string is valid

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
    """ Implementation of the '@string' type """

    def __setattr__(self, key, value):
        self.__dict__[key] = str(value) if key == "val" and value is not None else value


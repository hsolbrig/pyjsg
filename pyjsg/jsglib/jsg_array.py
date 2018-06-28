import sys
from typing import Optional, Union, TextIO

from pyjsg.jsglib.jsg import JSGValidateable, Logger, JSGContext

if sys.version_info < (3, 7):
    from .typing_patch_36 import conforms
else:
    from .typing_patch_37 import conforms


class JSGArray(JSGValidateable):
    def __init__(self, variable_name: str, context: JSGContext, typ, min_: int, max_: Optional[int], value) -> None:
        self.variable_name = variable_name
        self.context = context
        self.type = typ
        self.min: int = min_
        self.max: Optional[int] = max_
        self.val = [] if value is None else value

    def _is_valid(self, log: Optional[Union[TextIO, Logger]] = None) -> bool:
        if not isinstance(self.val, list):
            log.log(f"{self.variable_name}: {repr(self.val)} is not an array")
            return False

        for i in range(0, len(self.val)):
            v = self.val[i]
            if not conforms(v, self.type, self.context.NAMESPACE):
                if log.log(f"{self.variable_name} element {i}: {v} is not a {self.type.__name__}"):
                    return False

        if len(self.val) < self.min:
            if log.log(f"{self.variable_name}: at least {self.min} value{'s' if self.min > 1 else ''} required - "
                       f"element has {len(self.val) if len(self.val) else 'none'}"):
                return False
        if self.max is not None and len(self.val) > self.max:
            if log.log(f"{self.variable_name}: no more than {self.max} values permitted"
                       f" - element has {len(self.val)}"):
                return False

    def _is_initialized(self):
        return True             # Presence means initialized


class Array(JSGArray):
    """ Implementation of the '@array' and '[]' types """
    _strict = False

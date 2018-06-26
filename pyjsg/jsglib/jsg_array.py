import sys
from typing import Optional, Union, TextIO

from pyjsg.jsglib.jsg import JSGValidateable, Logger, JSGContext

if sys.version_info < (3, 7):
    from .typing_patch_36 import conforms
else:
    from .typing_patch_37 import conforms


class JSGArray(JSGValidateable):
    def __init__(self, context: JSGContext, typ, min_: int, max_: Optional[int], value) -> None:
        self.context = context
        self.type = typ
        self.min: int = min_
        self.max: Optional[int] = max_
        self.value = [] if value is None else value

    def _is_valid(self, log: Optional[Union[TextIO, Logger]] = None) -> bool:
        for v in self.value:
            if not conforms(v, self.type, self.context):
                if log.log(f"{v} does not conform to {self.type}"):
                    return False

        if len(self.value) < self.min:
            if log.log(f"size ({len(v)}) is less than minimum ({self.min})"):
                return False
        if self.max is not None and len(self.value) > self.max:
            if log.log(f"size ({len(v)} is greater tham maximum ({self.max}"):
                return False



class Array(JSGArray):
    """ Implementation of the '@array' and '[]' types """
    pass

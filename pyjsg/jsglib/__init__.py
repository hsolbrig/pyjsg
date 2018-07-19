import sys

from .jsg_strings import JSGPattern, JSGString, JSGNull, Boolean, Integer, Number, String, Null, JSGPatternedValMeta
from .jsg_array import JSGArray, Array, ArrayFactory
from .jsg_object import JSGObject, Object, JSGObjectMap, ObjectFactory
from .jsg_base import AnyType, EmptyAny, JSGValidateable, JSGContext, isinstance_

if sys.version_info < (3, 7):
    from typing import _ForwardRef as ForwardRef
    from .typing_patch_36 import *
else:
    from typing import ForwardRef
    from .typing_patch_37 import *

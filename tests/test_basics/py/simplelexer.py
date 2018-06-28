# Auto generated from test_basics/jsg/simplelexer.jsg by PyJSG version 0.7.0
# Generation date: 2018-06-28 11:40
#
import sys
from typing import Optional, Dict, List, Union
if sys.version_info < (3, 7):
    from typing import _ForwardRef as ForwardRef
    from pyjsg.jsglib import typing_patch_36
else:
    from typing import ForwardRef
    from pyjsg.jsglib import typing_patch_37

from pyjsg.jsglib import *
from pyjsg.jsglib.jsg import isinstance_

# .TYPE and .IGNORE settings
_CONTEXT = JSGContext()





class HEX(JSGString):
    pattern = JSGPattern(r'[0-9]|[A-F]|[a-f]')


class EXPONENT(JSGString):
    pattern = JSGPattern(r'[eE][+-]?[0-9]+')


class LANGTAG(JSGString):
    pattern = JSGPattern(r'@[a-zA-Z]+(\-[a-zA-Z0-9]+)*')

_CONTEXT.NAMESPACE = locals()

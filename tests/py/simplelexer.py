# Auto generated from jsg/simplelexer.jsg by PyJSG version 1.0.0
# Generation date: 2017-05-15 11:10
#
from typing import Optional, Dict, List, Union, _ForwardRef

from pyjsg.jsglib.jsg import *
from pyjsg.jsglib.typing_patch import fix_forwards

# .TYPE and .IGNORE settings
_CONTEXT = JSGContext()


class HEX(JSGString):
    pattern = JSGPattern(r'[0-9]|[A-F]|[a-f]')


class EXPONENT(JSGString):
    pattern = JSGPattern(r'[eE][+-]?[0-9]+')


class LANGTAG(JSGString):
    pattern = JSGPattern(r'\@[a-zA-Z]+(\-[a-zA-Z0-9]+)*')

fix_forwards(locals())

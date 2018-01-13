# Auto generated from jsg/simplelexer.jsg by PyJSG version 0.4.2
# Generation date: 2018-01-13 16:20
#
from typing import Optional, Dict, List, Union, _ForwardRef

from pyjsg.jsglib import jsg
from pyjsg.jsglib.jsg import isinstance_

# .TYPE and .IGNORE settings
_CONTEXT = jsg.JSGContext()





class HEX(jsg.JSGString):
    pattern = jsg.JSGPattern(r'[0-9]|[A-F]|[a-f]')


class EXPONENT(jsg.JSGString):
    pattern = jsg.JSGPattern(r'[eE][+-]?[0-9]+')


class LANGTAG(jsg.JSGString):
    pattern = jsg.JSGPattern(r'\@[a-zA-Z]+(\-[a-zA-Z0-9]+)*')

_CONTEXT.NAMESPACE = locals()

# Auto generated from jsg/lexer.jsg by PyJSG version 0.1.0-DEV
# Generation date: 2017-03-22 13:51
#
from typing import Optional, Dict, List, Union, _ForwardRef

from jsglib.jsg import JSGString, JSGPattern, JSGObject, JSGContext
from jsglib.typing_patch import fix_forwards

# .TYPE and .IGNORE settings
_CONTEXT = JSGContext()






class BOOL(JSGString):
    pattern = JSGPattern(r'true|false')


class INTEGER(JSGString):
    pattern = JSGPattern(r'[+-]?[0-9]+')


class DECIMAL(JSGString):
    pattern = JSGPattern(r'[+-]?[0-9]*\.[0-9]+')


class STRING(JSGString):
    pattern = JSGPattern(r'.*')


class PN_CHARS_BASE(JSGString):
    pattern = JSGPattern(r'[A-Z]|[a-z]|[\u00C0-\u00D6]|[\u00D8-\u00F6]|[\u00F8-\u02FF]|[\u0370-\u037D]|[\u037F-\u1FFF]|[\u200C-\u200D]|[\u2070-\u218F]|[\u2C00-\u2FEF]|[\u3001-\uD7FF]|[\uF900-\uFDCF]|[\uFDF0-\uFFFD]|[\u10000-\uEFFFF]')


class HEX(JSGString):
    pattern = JSGPattern(r'[0-9]|[A-F]|[a-f]')


class EXPONENT(JSGString):
    pattern = JSGPattern(r'[eE][+-]?[0-9]+')


class LANGTAG(JSGString):
    pattern = JSGPattern(r'\@[a-zA-Z]+(\-[a-zA-Z0-9]+)*')


class DOUBLE(JSGString):
    pattern = JSGPattern(r'[+-]?([0-9]+\.[0-9]*{EXPONENT}|\.[0-9]+{EXPONENT}|[0-9]+{EXPONENT})'.format(EXPONENT=EXPONENT.pattern))


class PN_CHARS_U(JSGString):
    pattern = JSGPattern(r'{PN_CHARS_BASE}|_'.format(PN_CHARS_BASE=PN_CHARS_BASE.pattern))


class UCHAR(JSGString):
    pattern = JSGPattern(r'\\\\u{HEX}{HEX}{HEX}{HEX}|\\\\U{HEX}{HEX}{HEX}{HEX}{HEX}{HEX}{HEX}{HEX}'.format(HEX=HEX.pattern))


class PN_CHARS(JSGString):
    pattern = JSGPattern(r'{PN_CHARS_U}|\-|[0-9]|\\u00B7|[\u0300-\u036F]|[\u203F-\u2040]'.format(PN_CHARS_U=PN_CHARS_U.pattern))


class IRI(JSGString):
    pattern = JSGPattern(r'({PN_CHARS}|\.|\:|\/|\\\\|\#|\@|\%|\&|{UCHAR})*'.format(PN_CHARS=PN_CHARS.pattern, UCHAR=UCHAR.pattern))


class BNODE(JSGString):
    pattern = JSGPattern(r'_\:({PN_CHARS_U}|[0-9])(({PN_CHARS}|\.)*{PN_CHARS})?'.format(PN_CHARS_U=PN_CHARS_U.pattern, PN_CHARS=PN_CHARS.pattern))


class PN_PREFIX(JSGString):
    pattern = JSGPattern(r'{PN_CHARS_BASE}(({PN_CHARS}|\.)*{PN_CHARS})?'.format(PN_CHARS=PN_CHARS.pattern, PN_CHARS_BASE=PN_CHARS_BASE.pattern))

fix_forwards(globals())

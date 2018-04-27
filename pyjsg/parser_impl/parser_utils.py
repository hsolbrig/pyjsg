import ast
import keyword
from collections.abc import Iterable
from typing import List, Set

from pyjsg.parser.jsgParser import ParserRuleContext


def flatten(l: Iterable) -> List:
    """
    Return a list of all non-list items in l
    :param l: list to be flattened
    :return:
    """
    rval = []
    for e in l:
        if not isinstance(e, str) and isinstance(e, Iterable):
            rval += flatten(e)
        else:
            rval.append(e)
    return rval


def optional(v: str, always_optional: bool) -> str:
    return v if not always_optional or v.startswith("Optional[") else "Optional[{}]".format(v)


def as_set(l: Iterable) -> Set:
    """
    Return the set of all terminals in list l
    :param l:
    :return:
    """
    return set(flatten(l))


identifier_types = ['ID', 'LEXER_ID', 'LEXER_ID_REF', 'idref', 'STRING']


def as_token(ctx: ParserRuleContext) -> str:
    """
    Return a tokenized identifier from ctx.
    :param ctx: JSG parser item with some sort of identifier
    :return:
    """
    tkn = None
    for ele_name in identifier_types:
        ele = getattr(ctx, ele_name, None)
        if ele and ele():
            tkn = ele().getText()[1:-1] if ele_name == 'STRING' else ele().getText()
    return esc_kw(str(tkn))


def as_tokens(ctx: List[ParserRuleContext]) -> List[str]:
    """
    Return a stringified list of identifiers in ctx
    :param ctx: JSG parser item with a set of identifiers
    :return:
    """
    return [as_token(e) for e in ctx]


def is_valid_python(tkn: str) -> bool:
    """
    Determine whether tkn is a valid python identifier
    :param tkn:
    :return:
    """
    try:
        root = ast.parse(tkn)
    except SyntaxError:
        return False
    return len(root.body) == 1 and isinstance(root.body[0].value, ast.Name)


def esc_kw(token: str) -> str:
    """
    Escape python keywords
    :param token: token
    :return: token with '_' suffixed if it is a keyword
    """
    return token + '_' if keyword.iskeyword(token) else token

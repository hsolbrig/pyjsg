# Copyright (c) 2017, Mayo Clinic
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without modification,
# are permitted provided that the following conditions are met:
#
# Redistributions of source code must retain the above copyright notice, this
#     list of conditions and the following disclaimer.
#
#     Redistributions in binary form must reproduce the above copyright notice,
#     this list of conditions and the following disclaimer in the documentation
#     and/or other materials provided with the distribution.
#
#     Neither the name of the Mayo Clinic nor the names of its contributors
#     may be used to endorse or promote products derived from this software
#     without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED.
# IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT,
# INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, 
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
# LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE
# OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED
# OF THE POSSIBILITY OF SUCH DAMAGE.
import ast
import keyword
from collections import Iterable
from typing import List, Union, Set, Optional

from pyjsg.parser.jsgParser import jsgParser, ParserRuleContext


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


def as_set(l: Iterable) -> Set:
    """
    Return the set of all terminals in list l
    :param l:
    :return:
    """
    return set(flatten(l))


def as_token(ctx: ParserRuleContext) -> str:
    """
    Return the text of ID or STRING from ctx
    :param ctx: JSG parser item with an ID or STRING value
    :return:
    """
    tkn = ctx.ID().getText() if ctx.ID() else ctx.STRING().getText()[1:-1]
    return esc_kw(str(tkn))


def as_tokens(ctx: ParserRuleContext) -> List[str]:
    """
    Return a stringified list of all ID's in ctx
    :param ctx: JSG parser item with ID as a list
    :return:
    """
    return [esc_kw(str(tkn)) for tkn in ctx.ID()]


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


def map_ebnf(target: str, ebnf: Union[str, jsgParser.EbnfSuffixContext]) -> str:
    """
    Map '?', '*', '+', '{n,m|*}' to a python type
    :param target: identifier to be surrounded
    :param ebnf: ebnf to map
    :return: python interpretation
    """
    if isinstance(ebnf, jsgParser.EbnfSuffixContext):
        ebnf = ebnf.getText()
    if not ebnf:
        return target
    if ebnf == '?':
        return "Optional[{}]".format(target)
    else:
        return "List[{}]".format(target)    # TODO: add cardinalities to the model


class AnonymousIdentifierFactory:
    """
    Anonymous identifiers are required in two cases:
    1) Where JSON identifiers are STRING rather than ID constructs and need to be wrapped in an outer name
    2) Anonymous inner constructs -- not strictly necessary, the code becomes way too complex without them
    """

    def __init__(self):
        self._nextid = 0

    def next_id(self, base: Optional[str] = None) -> str:
        self._nextid += 1
        return "_" + (base if base is not None else "A") + "{:d}".format(self._nextid)

from typing import Optional

from pyjsg.parser.jsgParser import *
from pyjsg.parser.jsgParserVisitor import jsgParserVisitor
from pyjsg.parser_impl.jsg_doc_context import JSGDocContext


class JSGEbnf(jsgParserVisitor):
    def __init__(self, context: JSGDocContext, ctx: Optional[jsgParser.EbnfSuffixContext] = None):
        self._context = context
        self._ebnftext = ""                 # type: str
        self.min = 1                        # type: int
        self.max = 1                        # type: Optional[int]

        if ctx:
            self.visit(ctx)

    def __str__(self):
        return self._ebnftext

    @property
    def is_optional(self):
        return self.min == 0 and self.max == 1

    @property
    def is_list(self):
        return self.max is None or self.max > 1

    def python_type(self, subject: str) -> str:
        """
        Add the appropriate python typing to subject (e.g. Optional, List, ...)
        :param subject: Subject to be decorated
        :return: Typed subject
        """
        return "List[{}]".format(subject) if self.is_list else\
            "Optional[{}]".format(subject) if self.is_optional else "None" if self.max == 0 else subject

    def visitEbnfSuffix(self, ctx: jsgParser.EbnfSuffixContext):
        """ ebnfSuffix: QMARK | STAR | PLUS | OBRACE INT (COMMA (INT|STAR)?)? CBRACE """
        self._ebnftext = ctx.getText()
        if ctx.INT():
            self.min = int(ctx.INT(0).getText())
            if ctx.COMMA():
                if len(ctx.INT()) > 1:
                    self.max = int(ctx.INT(1).getText())
                else:
                    self.max = None
            else:
                self.max = self.min
        elif ctx.QMARK():
            self.min = 0
            self.max = 1
        elif ctx.STAR():
            self.min = 0
            self.max = None
        elif ctx.PLUS():
            self.min = 1
            self.max = None
        else:
            raise NotImplementedError("Unknown ebnf construct: {}".format(self._ebnftext))

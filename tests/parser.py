from typing import Callable

from antlr4 import InputStream, CommonTokenStream

from pyjsg.parser.jsgLexer import jsgLexer
from pyjsg.parser.jsgParser import jsgParser
from pyjsg.parser.jsgParserVisitor import jsgParserVisitor
from pyjsg.parser_impl.jsg_doc_context import JSGDocContext


def parse(text: str, production_rule: str, listener) -> jsgParserVisitor:
    """ 
    Parse text fragment according to supplied production rule and evaluate with listener class.
    
    Example: parse("{1,*}", "ebnfSuffix", JSGEbnf)
    """
    lexer = jsgLexer(InputStream(text))
    tokens = CommonTokenStream(lexer)
    tokens.fill()
    parser = jsgParser(tokens)
    base_node = getattr(parser, production_rule)()
    listener_module = listener(JSGDocContext())
    listener_module.visit(base_node)
    return listener_module

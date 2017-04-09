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
import os
from argparse import ArgumentParser
from typing import Optional, Union

from antlr4 import CommonTokenStream
from antlr4 import FileStream, InputStream
from antlr4.error.ErrorListener import ErrorListener
from pyjsg.parser.jsgParser import jsgParser

from pyjsg.parser.jsgLexer import jsgLexer
from pyjsg.parser_impl.jsg_doc_parser import JSGDocParser


class ParseErrorListener(ErrorListener):

    def __init__(self):
        self.n_errors = 0

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        self.n_errors += 1

    def reportAmbiguity(self, recognizer, dfa, startIndex, stopIndex, exact, ambigAlts, configs):
        self.n_errors += 1

    def reportAttemptingFullContext(self, recognizer, dfa, startIndex, stopIndex, conflictingAlts, configs):
        self.n_errors += 1

    def reportContextSensitivity(self, recognizer, dfa, startIndex, stopIndex, prediction, configs):
        self.n_errors += 1


def do_parse(infilename: str, outfilename: str) -> bool:
    """
    Parse the jsg in infilename and save the results in outfilename
    :param infilename: file containing jsg
    :param outfilename: target python file
    :return: true if success
    """
    python = parse(FileStream(infilename, encoding="utf-8"), infilename)
    if python is not None:
        with open(outfilename, 'w') as outfile:
            outfile.write(python)
        return True
    return False


def parse(input_: Union[str, FileStream], source: str) -> Optional[str]:
    """
    Parse the text in infile and save the results in outfile
    :param input_: string or stream to parse
    :param source: source name for python file header
    :return: python text if successful
    """

    # Step 1: Tokenize the input stream
    error_listener = ParseErrorListener()
    if not isinstance(input_, FileStream):
        input_ = InputStream(input_)
    lexer = jsgLexer(input_)
    lexer.addErrorListener(error_listener)
    tokens = CommonTokenStream(lexer)
    tokens.fill()
    if error_listener.n_errors:
        return None

    # Step 2: Generate the parse tree
    parser = jsgParser(tokens)
    parser.addErrorListener(error_listener)
    parse_tree = parser.doc()
    if error_listener.n_errors:
        return None

    # Step 3: Transform the results the results
    parser = JSGDocParser()
    parser.visit(parse_tree)

    if parser.undefined_tokens():
        for tkn in parser.undefined_tokens():
            print("Undefined token: " + tkn)
        return None

    return parser.python(source)


def genargs() -> ArgumentParser:
    """
    Create a command line parser
    :return: parser
    """
    parser = ArgumentParser()
    parser.add_argument("infile", help="Input JSG specification")
    parser.add_argument("-o", "--outfile", help="Output python file (Default: {infile}.py)")
    parser.add_argument("-e", "--evaluate", help="Evaluate resulting python file as a test", action="store_true")
    return parser


def generate(argv) -> bool:
    opts = genargs().parse_args(argv)
    if not opts.outfile:
        opts.outfile = os.path.join(os.path.dirname(opts.infile),
                                    str(os.path.basename(opts.infile).rsplit('.', 1)[0]) + ".py")
    if do_parse(opts.infile, opts.outfile):
        print("Output written to {}".format(opts.outfile))
        if opts.evaluate:
            with open(opts.outfile) as f:
                exec(f.read(), globals())
        return True
    else:
        print("Conversion failed")
        return False

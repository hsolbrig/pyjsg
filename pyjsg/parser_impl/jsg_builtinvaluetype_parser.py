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
from typing import Optional, Tuple, Dict

from pyjsg.jsglib.jsg import JSGStringMeta, String, Object, Integer, Number, JSGNull, Array, Boolean, AnyType
from pyjsg.parser.jsgParser import *
from pyjsg.parser.jsgParserVisitor import jsgParserVisitor
from pyjsg.parser_impl.jsg_doc_context import JSGDocContext


class JSGBuiltinValueType(jsgParserVisitor):
    parserTypeToImplClass: Dict[str, Tuple[JSGStringMeta, object]] = \
        {"@string": (String, str),
         "@object": (Object, object),
         "@int": (Integer, int),
         "@number": (Number, float),
         "@null": (JSGNull, JSGNull),
         "@array": (Array, list),
         "@bool": (Boolean, bool),
         ".": (AnyType, object)}

    def __init__(self, context: JSGDocContext, ctx: Optional[jsgParser.BuiltinValueTypeContext] = None):
        self._context = context

        self._value_type_text = ""             # type: Optional[str]
        if ctx:
            self.visit(ctx)

    def __str__(self):
        return "builtinValueType: {}".format(self.basetype)

    @property
    def typeid(self):
        id = self.parserTypeToImplClass[self._value_type_text][1]
        return "jsg.JSGNull" if id == JSGNull else id.__name__

    @property
    def basetype(self):
        return "jsg." + self.parserTypeToImplClass[self._value_type_text][0].__name__

    def set_anytype(self) -> jsgParserVisitor:
        self._value_type_text = "."
        return self

    # ***************
    #   Visitors
    # ***************
    def visitBuiltinValueType(self, ctx: jsgParser.BuiltinValueTypeContext):
        """ valueTypeExpr: JSON_STRING | JSON_NUMBER | JSON_INT | JSON_BOOL | JSON_NULL | JSON_ARRAY | JSON_OBJECT """
        self._value_type_text = ctx.getText()

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
from typing import Optional, Union, List, Set

from pyjsg.parser.jsgParser import *
from pyjsg.parser_impl.jsg_objectexprdef_parser import JSGObjectExprDef
from pyjsg.parser_impl.jsg_particle_parser import JSGParticle
from pyjsg.parser_impl.jsg_propertytype_parser import JSGPropertyType

from pyjsg.parser.jsgParserVisitor import jsgParserVisitor
from pyjsg.parser_impl.jsg_doc_context import JSGDocContext
from .parser_utils import as_token


_object_template = """    def __init__(self{opts_list},
                 **_extra: Dict[str, object]):
        JSGObject.__init__(self, _CONTEXT, **_extra)
        {opts_init}
"""
indent1 = ",\n                 "
indent2 = "\n        "


class JSGObjectExpr(jsgParserVisitor):
    def __init__(self, context: JSGDocContext,
                 ctx: Optional[Union[jsgParser.ObjectExprObjContext,
                                     jsgParser.ObjectExprMapContext]] = None):
        self._context = context
        self._object_def = None             # JSGObjextExprDef
        self._map = None                   # Tuple(str, JSGPropertyType)

        if ctx:
            self.visit(ctx)

    def inner_signature(self) -> List[str]:
        if self._object_def:
            return self._object_def.signature()
        elif self._map:
            return ["Dict[{}, {}]".format(self._map[0], self._map[1].signature())]
        else:
            return []

    def inner_initializer(self) -> List[str]:
        if self._object_def:
            return self._object_def.initializer()
        else:
            return []

    def set_object_def(self, objdef: JSGObjectExprDef) -> None:
        self._object_def = objdef

    def dependency_list(self) -> List[str]:
        if self._object_def:
            return self._object_def.dependency_list()
        elif self._map:
            return [self._map[0]] + self._map[1].dependency_list()
        else:
            return []

    def dependencies(self) -> Set[str]:
        return set(self.dependency_list())

    def __str__(self):
        return "objectExpr{{{}}}".format(str(self._object_def) if self._object_def else str(self._map))

    def __repr__(self):
        if self._object_def:
            if self._object_def.is_object():
                opts_list = indent1.join(self._object_def.signature())
                opts_init = indent2.join(self._object_def.initializer())
                if opts_list:
                    opts_list = indent1 + opts_list
                return _object_template.format(**locals())
            else:
                return ", ".join(self._object_def.signature())
        else:
            return _object_template.format(opts_list="", opts_init="")

    def is_object(self):
        return self._object_def is None or self._object_def.is_object()

    def _eval(self, p: jsgParser.ParticleContext):
        particle_parser = JSGParticle(self._context)
        particle_parser.visit(p)
        return particle_parser

    def visitObjectExprObj(self, ctx: jsgParser.ObjectExprObjContext):
        """ objectExpr: OBRACE objectExprDef? CBRACE """
        if ctx.objectExprDef():
            self._object_def = JSGObjectExprDef(self._context, ctx.objectExprDef())

    def visitObjectExprMap(self, ctx: jsgParser.ObjectExprMapContext):
        """ objectExpr: OBRACE ID '->' propertype CBRACE """
        self._map[as_token(ctx)] = JSGPropertyType(self._context, ctx.propertyType())

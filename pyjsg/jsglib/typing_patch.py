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
import sys

# Note: ModuleType and _ForwardRef and _Union IDE errors are expected
from types import ModuleType
from typing import GenericMeta, Dict, Any, List, Union, _ForwardRef
from collections import Iterable


# TODO: Pay attention to the goings on at the python development (http://bugs.python.org/issue29262) and #377

def conforms(element, etype, namespace: Dict[str, Any]) -> bool:
    if isinstance(element, str) and element == '_context':
        return True
    elif is_forward(etype):
        etype = etype._eval_type(namespace, namespace)      # Everything should have been resolved
    if is_union(etype):
        return union_conforms(element, etype, namespace)
    elif is_dict(etype):
        return dict_conforms(element, etype, namespace)
    elif is_iterable(etype):
        return iterable_conforms(element, etype, namespace)
    else:
        return element_conforms(element, etype)


def is_typing_type(etype) -> bool:
    return is_union(etype) or is_dict(etype) or is_iterable(etype)


def is_forward(etype) -> bool:
    return type(etype) is _ForwardRef


def is_union(etype) -> bool:
    return type(etype) == type(Union)


def is_dict(etype) -> bool:
    return type(etype) is GenericMeta and etype.__extra__ is dict


def is_iterable(etype) -> bool:
    return type(etype) is GenericMeta and issubclass(etype.__extra__, Iterable)


def union_conforms(element, etype, namespace: Dict[str, Any]) -> bool:
    if is_union(etype):
        union_vals = etype.__union_params__ if sys.version_info < (3, 6) else etype.__args__
        return any(conforms(element, t, namespace) for t in union_vals)
    return False


def dict_conforms(element, etype, namespace: Dict[str, Any]) -> bool:
    if is_dict(etype) and isinstance(element, dict):
        kt, vt = etype.__args__
        return all(conforms(k, kt, namespace) and
                   conforms(v, vt, namespace) for k, v in element.items())
    return False


def iterable_conforms(element, etype, namespace: Dict[str, Any]) -> bool:
    if element is None and issubclass(etype, List):
        element = []
    if is_iterable(etype) and isinstance(element, Iterable):
        vt = etype.__args__[0]
        return all(conforms(e, vt, namespace) for e in element)
    return False


def element_conforms(element, etype) -> bool:
    if element is None and etype == object:
        return True
    elif isinstance(etype, type(type)) and (issubclass(etype, type(None))):
        return element is None
    elif element is None:
        return False
    return isinstance(element, etype)

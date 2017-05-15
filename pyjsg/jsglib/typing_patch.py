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
from typing import GenericMeta, _ForwardRef, Dict, Any

if sys.version_info < (3, 6):
    from typing import Union
else:
    from typing import _Union

from collections import Iterable


# TODO: Pay attention to the goings on at the python development (http://bugs.python.org/issue29262) and #377

def conforms(element, etype) -> bool:
    if isinstance(element, str) and element == '_context':
        return True
    elif is_forward(etype):
        ns = {}
        etype = etype._eval_type(ns, ns)        # All forwards have to already be fixed
    if is_union(etype):
        return union_conforms(element, etype)
    elif is_dict(etype):
        return dict_conforms(element, etype)
    elif is_iterable(etype):
        return iterable_conforms(element, etype)
    else:
        return element_conforms(element, etype)


def is_typing_type(etype) -> bool:
    return is_union(etype) or is_dict(etype) or is_iterable(etype)


def as_type(element, etype) -> object:
    if element is None:
        return element
    if is_forward(etype):
        etype = etype._eval_type(None, None)        # All forwards should already be vixed
    if is_union(etype):
        if union_conforms(element, etype):
            return as_union(element, etype)
    elif is_dict(etype):
        if dict_conforms(element, etype):
            return element
    elif is_iterable(etype):
        if iterable_conforms(element, etype):
            return etype.__extra__(element)
    elif element_conforms(element, etype):
        return etype(element)
    return None


def is_forward(etype) -> bool:
    return type(etype) is _ForwardRef


def is_union(etype) -> bool:
    if sys.version_info < (3, 6):
        return issubclass(etype, Union)
    else:
        return type(etype) is _Union


def is_dict(etype) -> bool:
    return type(etype) is GenericMeta and etype.__extra__ is dict


def is_iterable(etype) -> bool:
    return type(etype) is GenericMeta and issubclass(etype.__extra__, Iterable)


def union_conforms(element, etype) -> bool:
    if is_union(etype):
        union_vals = etype.__union_params__ if sys.version_info < (3, 6) else etype.__args__
        return any(conforms(element, t) for t in union_vals)
    return False


def as_union(element, etype) -> object:
    union_vals = etype.__union_params__ if sys.version_info < (3, 6) else etype.__args__
    for t in union_vals:
        if conforms(element, t):
            return element
    return None


def dict_conforms(element, etype) -> bool:
    if is_dict(etype) and isinstance(element, dict):
        kt, vt = etype.__args__
        return all(conforms(k, kt) and conforms(v, vt) for k, v in element.items())
    return False


def iterable_conforms(element, etype) -> bool:
    if is_iterable(etype) and isinstance(element, Iterable):
        vt = etype.__args__[0]
        return all(conforms(e, vt) for e in element)
    return False


def element_conforms(element, etype) -> bool:
    if element is None and etype == object:
        return True
    elif isinstance(etype, type(type)) and (issubclass(etype, type(None))):
        return element is None
    elif element is None:
        return False
    return isinstance(element, etype)


def fix_forwards(ns: Dict[str, Any]) -> None:
    for k, val in ns.items():
        fix_forward(ns, val)


def fix_forward(ns: Dict[str, Any], val: Any) -> None:
        if isinstance(val, GenericMeta):                # Skip the types themselves
            pass
        elif is_forward(val):
            val.__forward_evaluated__ = False           # Force resolution to local namespace
            val._eval_type(ns, {})
        elif is_union(val):
            union_vals = val.__union_params__ if sys.version_info < (3, 6) else val.__args__
            if union_vals is not None:
                [fix_forward(ns, t) for t in union_vals]
        elif is_dict(val) and val.__args__ is not None:
            [fix_forward(ns, t) for t in val.__args__]
        elif is_iterable(val) and val.__extra__ is not None:
            [fix_forward(ns, v) for v in val.__extra__]

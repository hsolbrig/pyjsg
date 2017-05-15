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

import unittest
from typing import List

from pyjsg.jsglib.jsg import JSGObjectMap, JSGPattern, JSGContext, JSGString, Null
from tests.test_jsglib.iri_defn import *
from jsonasobj import loads as jsonloads

_CONTEXT = JSGContext()


class ObjectMapTestCase(unittest.TestCase):

    def test_basic_map(self):
        class IntObjectMap(JSGObjectMap):
            _name_filter = JSGPattern(r'[A-Za-z][0-9]+')
            _value_type = List[int]

            def __init__(self,
                         **_kwargs):
                super().__init__(_CONTEXT, **_kwargs)

        x = IntObjectMap()
        x.a17 = [1,2,3]
        self.assertTrue(x._is_valid())
        self.assertEqual(x._as_json, jsonloads('{"a17":[1,2,3]}')._as_json)
        with self.assertRaises(ValueError):
            x.ab = [1, 2, 4]
        with self.assertRaises(ValueError):
            x.t1 = 1
        with self.assertRaises(ValueError):
            x = IntObjectMap(aa=[1])

    def test_any_key(self):
        class ALPHA(JSGString):
            pattern = JSGPattern(r'[A-Za-z]')

        class AnyKeyObjectMap(JSGObjectMap):
            _value_type = ALPHA

            def __init__(self,
                         **_kwargs):
                super().__init__(_CONTEXT, **_kwargs)

        x = AnyKeyObjectMap(I1="a")
        x["item 2"] = "b"
        self.assertTrue(x._is_valid())
        with self.assertRaises(ValueError):
            x.c = "1"

    def test_any_value(self):
        class IRIKey(JSGObjectMap):
            _name_filter = IRI.pattern

            def __init__(self,
                         **_kwargs):
                super().__init__(_CONTEXT, **_kwargs)

        x = IRIKey(**{"http://example.org": 42, "http://ex.org?id=1": Null})
        self.assertEqual('{"http://example.org": 42, "http://ex.org?id=1": null}', x._as_json)
        self.assertTrue(x._is_valid())
        self.assertEqual(x["http://example.org"], 42)
        self.assertEqual(x["http://ex.org?id=1"], Null)


if __name__ == '__main__':
    unittest.main()

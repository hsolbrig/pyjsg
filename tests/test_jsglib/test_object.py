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
from typing import Dict, Union

from pyjsg.jsglib.jsg import JSGObject, String, Integer, JSGContext, Boolean, Number, Null, Optional, JSGNull
from jsonasobj import loads as json_loads
from dict_compare import dict_compare

from pyjsg.jsglib.logger import Logger
from tests.memlogger import MemLogger

_CONTEXT = JSGContext()


class ObjectTestCase(unittest.TestCase):
    def check_json(self, t: JSGObject, c: str):
        self.assertTrue(dict_compare(json_loads(c)._as_dict, t._as_json_obj()))

    def test_simple_object(self):
        class Person(JSGObject):
            def __init__(self,
                         name: str = None,
                         age: int = None,
                         married: bool = None,
                         weight: float = None,
                         tag: Optional[JSGNull] = None,
                         **_kwargs: Dict[str, object]):
                super().__init__(_CONTEXT, **_kwargs)
                self.name = String(name)
                self.age = Integer(age)
                self.married = Boolean(married)
                self.weight = Number(weight)
                self.tag = tag

        log = Logger(MemLogger())


        x = Person()
        x.name = "Grunt P Snooter"
        x = Person(name="Sally Pope", age=42, married=True, weight=117)
        x.name="Joe"
        self.check_json(x, '{"name": "Sally Pope", "age": 42, "married": true, "weight": 117.5}')
        x = Person("Sally Pope", "42")
        self.check_json(x, '{"name": "Sally Pope", "age": 42}')
        x = Person("Sally Pope")
        self.assertFalse(x._is_valid(log))
        self.assertEqual(['Person: Missing required field: age',
                          'Person: Missing required field: married',
                          'Person: Missing required field: weight'], log.messages)
        log.clear()
        x.age = 99
        self.assertFalse(x._is_valid())
        x.married = False
        self.assertFalse(x._is_valid())
        x.weight = "112"
        self.assertTrue(x._is_valid())
        self.check_json(x, '{"name": "Sally Pope", "age": 99, "married": false, "weight": 112}')
        x.tag = Null
        self.check_json(x, '{"name": "Sally Pope", "age": 99, "married": false, "weight": 112, "tag": null}')
        with self.assertRaises(ValueError):
            x.age = "abc"
        del(x.weight)
        x._is_valid(log)
        self.assertEqual(['Person: Missing required field: weight'], log.messages)



if __name__ == '__main__':
    unittest.main()

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
from io import StringIO

import os


json_str = """{
  "@context": "http://www.w3.org/ns/shex.jsonld",
  "type": "Schema",
  "shapes": [
    {
      "id": "http://a.example/S1",
      "type": "Shape"
    }
  ]
}"""


class NamespaceTestIssue(unittest.TestCase):
    def test_namespace(self):
        """ There is something pretty subtle about caching and loading ShExJ.py in two different namespaces. The
        test_jsg_files.py test includes a validate function, which dynamically loads all of the generated python
        modules in tests/data/py.  Pretty much no matter how we do it, the module for that dynamic load isn't going
        to be the same as what you get from a straight import.

        We've tried clearing the cache, giving each python file a different name, setting the _ForwardRef
        __forward_evaluated__ to false, but nothing seems to work.  Long and short of it is, you shouldn't
        run test_shexj.py in the same thread as test_jsg_files.

        Update: we removed the _ForwardRef entries and switched to the internal forward typing (x:"Foo") if class Foo
        is further down in the class.  We add a NAMESPACE to the context at the very end of the file and pass it
        through to all of the resolution functions.  BIG HIGH FIVE on this one!
        """
        from pyjsg.parser_impl.generate_python import evaluate
        from pyjsg.jsglib.jsg import loads as jsg_loads

        # # First load done from the testing namespace
        filepath = os.path.join(os.path.dirname(__file__))
        pyfile = os.path.abspath(os.path.join(filepath, '..', 'py', 'ShExJ.py'))
        evaluate("test_namespace", pyfile, False)

        # Second load from a different file
        import tests.test_jsglib.py.ShExJ as ShExJ

        shex_obj = jsg_loads(json_str, ShExJ)

        log = StringIO()
        rval = shex_obj._is_valid(log)
        if not rval:
            print('\n'.join(log.read()))
        self.assertTrue(rval)


if __name__ == '__main__':
    unittest.main()

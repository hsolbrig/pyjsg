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
import os
import unittest

from importlib import import_module

from pyjsg.jsglib.jsg import load, JSGException
from pyjsg.jsglib.logger import Logger
from pyjsg.parser_impl.generate_python import generate
from jsonasobj import load as json_load

log = Logger(sys.stdout)


class JSGReadMeTestCase(unittest.TestCase):

    log = Logger(sys.stdout)

    def eval_for_error(self, fn: str, mod, error: str):
        fn_in_json = json_load(fn)
        expected = fn_in_json._ERROR
        del fn_in_json._ERROR
        with self.assertRaises(JSGException) as context:
            r = load(fn, mod)
        self.assertEqual(expected, str(context.exception))

    def eval_python(self, cwd: str, dirpath: str, fn: str) -> None:
        basefile = fn.rsplit('.', 1)[0]
        outfile = os.path.abspath(os.path.join(cwd, "py", basefile + ".py"))
        generate([os.path.relpath(os.path.join(dirpath, fn)), "-o", outfile])
        mod = import_module("tests.test_jsg_readme.py." + basefile)
        for dirpath, _, filenames in os.walk("json"):
            for fn in filenames:
                if fn.startswith(basefile) and fn.endswith(".json"):
                    full_fn = os.path.join(dirpath, fn)
                    if "_f" not in os.path.basename(full_fn):
                        r = load(full_fn, mod)
                        self.assertTrue(r._is_valid(log))
                    else:
                        self.eval_for_error(full_fn, mod, "ValueError: Unknown attribute: text=left in 2017")

    def test_jsg_readme(self):
        cwd = os.path.abspath(os.path.dirname(__file__))
        for dirpath, _, filenames in os.walk(os.path.join(cwd, "jsg")):
            for fn in filenames:
                if fn.endswith(".jsg"):
                    self.eval_python(cwd, dirpath, fn)


if __name__ == '__main__':
    unittest.main()

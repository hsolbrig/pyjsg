# Copyright (c) 2018, Mayo Clinic
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
from typing import Union

import os


class IsInstanceTestCase(unittest.TestCase):
    def test_isinstance_issue(self):
        from pyjsg.jsglib.jsg import isinstance_
        x = Union[int, str]
        with self.assertRaises(TypeError):
            isinstance(17, x)
        self.assertTrue(isinstance_(17, x))

    def test_issue_with_shexj(self):
        from pyjsg.parser_impl.generate_python import generate
        data_root = os.path.join(os.path.split(os.path.abspath(__file__))[0], '..',)
        jsg_path = os.path.relpath(os.path.join(data_root, 'jsg', 'ShExJ.jsg'))
        py_path = os.path.abspath(os.path.join(data_root, 'py', 'ShExJ.py'))
        self.assertTrue(generate([jsg_path, "-o", py_path, "-e"]))
        from tests.py import ShExJ
        self.assertTrue(ShExJ.isinstance_(ShExJ.IRIREF("http://foo.bar"), ShExJ.shapeExprLabel))

if __name__ == '__main__':
    unittest.main()

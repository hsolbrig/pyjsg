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
from typing import cast

from pyjsg.parser_impl.jsg_ebnf_parser import JSGEbnf

from tests.parser import parse


class EBNFTestCase(unittest.TestCase):
    tests = [('*', 0, None, "List[k]"),
             ('?', 0, 1, "Optional[k]"),
             ('+', 1, None, "List[k]"),
             ('{0}', 0, 0, "None"),
             ('{1}', 1, 1, "k"),
             ('{1,}', 1, None, "List[k]"),
             ('{2}', 2, 2, "List[k]"),
             ('{2,}', 2, None, "List[k]"),
             ('{3,*}', 3, None, "List[k]"),
             ('{3,7}', 3, 7, "List[k]")]

    def test1(self):
        for text, min_, max_, ptype in self.tests:
            t = cast(JSGEbnf, parse(text, "ebnfSuffix", JSGEbnf))
            self.assertEqual(min_, t.min)
            self.assertEqual(max_, t.max)
            self.assertEqual(ptype, t.python_type("k"))


if __name__ == '__main__':
    unittest.main()

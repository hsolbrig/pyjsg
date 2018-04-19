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
import os
import unittest


class GeneratePythonTestCase(unittest.TestCase):
    # Generate some bad python and verify that an error is detected in the output
    def test_execute_item(self):
        from pyjsg.parser_impl.generate_python import generate, evaluate

        basedir = os.path.abspath(os.path.dirname(__file__))
        goodfile = os.path.join(basedir, 'py', 'goodjsg.py')
        badfile = os.path.join(basedir, 'py', 'badjsg.py')

        # Make sure that a simple generate works
        self.assertTrue(generate([os.path.join(basedir, "jsg", "complexfacet.jsg"), "-o", goodfile, "-e"]))

        # Make sure that we can detect exceptions and errors
        with open(badfile, 'w') as bf:
            bf.write("i=1/0")
            with open(goodfile) as gf:
                bf.write(gf.read())
        with self.assertRaises(ZeroDivisionError):
            evaluate("bar", badfile, False)

        # Make sure that our namespace hasn't been messed up
        self.assertFalse('bar' in globals())
        os.remove(goodfile)
        os.remove(badfile)


if __name__ == '__main__':
    unittest.main()

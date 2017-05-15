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

from pyjsg.jsglib.jsg import JSGString, JSGPattern
from tests.test_jsglib.iri_defn import *



class JSGStringTestCase(unittest.TestCase):
    def _do_test(self, jsgstr, val) -> bool:
        return jsgstr(val, validate=False)._is_valid()


    def test_wildcard(self):
        class WildCard(JSGString):
            pattern = JSGPattern(r'.*')
        self.assertTrue(self._do_test(WildCard, ""))
        self.assertTrue(self._do_test(WildCard, False))
        self.assertTrue(self._do_test(WildCard, "any block of text"))
        self.assertTrue(self._do_test(WildCard, "^<80>߿ࠀ࿿က쿿퀀퟿�𐀀𿿽񀀀󿿽􀀀􏿽$/"))
        self.assertTrue(self._do_test(WildCard, "\n\uFDF0*"))

    def test_fixedvalues(self):
        class IRI(JSGString):
            pattern = JSGPattern(r'http:\/\/www\.w3\.org\/ns\/shex\.jsonld')
            
        self.assertTrue(self._do_test(IRI,"http://www.w3.org/ns/shex.jsonld"))
        self.assertFalse(self._do_test(IRI,"http://www.w3.org/ns/shex/jsonldx"))
        self.assertFalse(self._do_test(IRI,"http://www.w3.org/ns/shex/jsonld "))
        self.assertFalse(self._do_test(IRI,"http://www.w3.org/ns/shex/jsonld\n"))
        self.assertFalse(self._do_test(IRI," http://www.w3.org/ns/shex/jsonld"))

    def test_alternatives(self):
        class Alts(JSGString):
            pattern = JSGPattern(r'iri|bnode|nonliteral|literal')
        self.assertTrue(self._do_test(Alts,'iri'))
        self.assertTrue(self._do_test(Alts,'literal'))
        self.assertTrue(self._do_test(Alts,'nonliteral'))
        self.assertTrue(self._do_test(Alts,'bnode'))
        self.assertFalse(self._do_test(Alts,'node'))
        self.assertFalse(self._do_test(Alts,'bnod'))
        self.assertFalse(self._do_test(Alts,'IRI'))
        self.assertFalse(self._do_test(Alts,' iri'))
        self.assertFalse(self._do_test(Alts,'iri '))

    def test_bool(self):
        class BOOL(JSGString):
            pattern = JSGPattern(r'true|false')
        self.assertTrue(self._do_test(BOOL, 'true'))
        self.assertTrue(self._do_test(BOOL, 'false'))
        self.assertFalse(self._do_test(BOOL, 'TRUE'))
        self.assertFalse(self._do_test(BOOL, 'True'))
        self.assertFalse(self._do_test(BOOL, 'False'))
        self.assertTrue(self._do_test(BOOL, True))
        self.assertTrue(self._do_test(BOOL, False))
        self.assertFalse(self._do_test(BOOL, 0))
        self.assertIsNone(BOOL(None).val)

    def test_assorted(self):
        class INT(JSGString):
            pattern = JSGPattern(r'[+-]?[0-9]+')
            
        self.assertTrue(self._do_test(INT, "0"))
        self.assertTrue(self._do_test(INT, str(-173)))
        self.assertTrue(self._do_test(INT, "+11720000845197308888890"))
        self.assertTrue(self._do_test(INT, "01"))
        self.assertFalse(self._do_test(INT, "--17"))
        self.assertFalse(self._do_test(INT, "1.0"))
    
        class NUM(JSGString):
            pattern = JSGPattern(r'[+-]?[0-9]*\.[0-9]+')
            
        self.assertFalse(self._do_test(NUM, "0"))
        self.assertTrue(self._do_test(NUM, "0.0"))
        self.assertTrue(self._do_test(NUM, str(float(-173))))
        self.assertTrue(self._do_test(NUM, "1.0"))
        self.assertTrue(self._do_test(NUM, "+11720000845197308888.0000000000"))

        self.assertTrue(self._do_test(IRI, "http://a.example/p\u0031"))

if __name__ == '__main__':
    unittest.main()

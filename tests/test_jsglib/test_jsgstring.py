
import unittest

from pyjsg.jsglib import JSGString, JSGPattern
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


import unittest
from typing import Any

from pyjsg.jsglib import JSGString, JSGPattern
from tests.test_jsglib.iri_defn import *


class JSGStringTestCase(unittest.TestCase):
    def _do_test(self, jsgstr, val: Any, is_valid: bool=True) -> None:
        if not is_valid:
            with self.assertRaises(ValueError):
                jsgstr(val)
        else:
            v = jsgstr(val)
            self.assertEqual(v, str(val))

    def test_wildcard(self):
        class WildCard(JSGString):
            pattern = JSGPattern(r'.*')
            python_type = object

        self._do_test(WildCard, "")
        self._do_test(WildCard, False)
        self._do_test(WildCard, "any block of text")
        self._do_test(WildCard, "^<80>߿ࠀ࿿က쿿퀀퟿�𐀀𿿽񀀀󿿽􀀀􏿽$/")
        self._do_test(WildCard, "\n\uFDF0*")

    def test_fixedvalues(self):
        class IRI(JSGString):
            pattern = JSGPattern(r'http:\/\/www\.w3\.org\/ns\/shex\.jsonld')
            
        self._do_test(IRI,"http://www.w3.org/ns/shex.jsonld")
        self._do_test(IRI,"http://www.w3.org/ns/shex/jsonldx", False)
        self._do_test(IRI,"http://www.w3.org/ns/shex/jsonld ", False)
        self._do_test(IRI,"http://www.w3.org/ns/shex/jsonld\n", False)
        self._do_test(IRI," http://www.w3.org/ns/shex/jsonld", False)

    def test_alternatives(self):
        class Alts(JSGString):
            pattern = JSGPattern(r'iri|bnode|nonliteral|literal')
        self._do_test(Alts,'iri')
        self._do_test(Alts,'literal')
        self._do_test(Alts,'nonliteral')
        self._do_test(Alts,'bnode')
        self._do_test(Alts,'node', False)
        self._do_test(Alts,'bnod', False)
        self._do_test(Alts,'IRI', False)
        self._do_test(Alts,' iri', False)
        self._do_test(Alts,'iri ', False)

    def test_bool(self):
        class BOOL(JSGString):
            pattern = JSGPattern(r'[Tt]rue|[Ff]alse')
            python_type = (str, bool)

        self._do_test(BOOL, 'true')
        self._do_test(BOOL, 'false')
        self._do_test(BOOL, 'TRUE', False)
        self._do_test(BOOL, 'True')
        self._do_test(BOOL, 'False')
        self._do_test(BOOL, True)
        self._do_test(BOOL, False)
        self._do_test(BOOL, 0, False)
        self._do_test(BOOL, None, False)

    def test_assorted(self):
        class INT(JSGString):
            pattern = JSGPattern(r'[+-]?[0-9]+')
            
        self._do_test(INT, "0")
        self._do_test(INT, str(-173))
        self._do_test(INT, "+11720000845197308888890")
        self._do_test(INT, "01")
        self._do_test(INT, "--17", False)
        self._do_test(INT, "1.0", False)
    
        class NUM(JSGString):
            pattern = JSGPattern(r'[+-]?[0-9]*\.[0-9]+')
            
        self._do_test(NUM, "0", False)
        self._do_test(NUM, "0.0")
        self._do_test(NUM, str(float(-173)))
        self._do_test(NUM, "1.0")
        self._do_test(NUM, "+11720000845197308888.0000000000")

        self._do_test(IRI, "http://a.example/p\u0031")

if __name__ == '__main__':
    unittest.main()

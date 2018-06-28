
import unittest
from pyjsg.jsglib import JSGPattern
from tests.test_jsglib.iri_defn import IRI

class JSGPatternTest(unittest.TestCase):
    def test_wild_card(self):
        pattern = JSGPattern(r'.*')
        self.assertTrue(pattern.matches(""))
        self.assertTrue(pattern.matches("any block of text"))
        self.assertTrue(pattern.matches("\n\uFDF0*"))

    def test_fixed_values(self):
        pattern = JSGPattern(r'http:\/\/www\.w3\.org\/ns\/shex\.jsonld')
        self.assertTrue(pattern.matches("http://www.w3.org/ns/shex.jsonld"))
        self.assertFalse(pattern.matches("http://www.w3.org/ns/shex/jsonldx"))
        self.assertFalse(pattern.matches("http://www.w3.org/ns/shex/jsonld "))
        self.assertFalse(pattern.matches("http://www.w3.org/ns/shex/jsonld\n"))
        self.assertFalse(pattern.matches(" http://www.w3.org/ns/shex/jsonld"))

    def test_alternatives(self):
        pattern = JSGPattern(r'iri|bnode|nonliteral|literal')
        self.assertTrue(pattern.matches('iri'))
        self.assertTrue(pattern.matches('literal'))
        self.assertTrue(pattern.matches('nonliteral'))
        self.assertTrue(pattern.matches('bnode'))
        self.assertFalse(pattern.matches('node'))
        self.assertFalse(pattern.matches('bnod'))
        self.assertFalse(pattern.matches('IRI'))
        self.assertFalse(pattern.matches(' iri'))
        self.assertFalse(pattern.matches('iri '))

    def test_assorted_patterns(self):
        pattern = JSGPattern(r'[+-]?[0-9]+')
        self.assertTrue(pattern.matches("0"))
        self.assertTrue(pattern.matches(str(-173)))
        self.assertTrue(pattern.matches("+11720000845197308888890"))
        self.assertTrue(pattern.matches("01"))
        self.assertFalse(pattern.matches("--17"))
        self.assertFalse(pattern.matches("1.0"))

        pattern = JSGPattern(r'[+-]?[0-9]*\.[0-9]+')
        self.assertFalse(pattern.matches("0"))
        self.assertTrue(pattern.matches("0.0"))
        self.assertTrue(pattern.matches(str(float(-173))))
        self.assertTrue(pattern.matches("1.0"))
        self.assertTrue(pattern.matches("+11720000845197308888.0000000000"))

        PN_CHARS_BASE = r'[A-Z]|[a-z]|[\u00C0-\u00D6]|[\u00D8-\u00F6]|[\u00F8-\u02FF]|[\u0370-\u037D]|' \
                        r'[\u037F-\u1FFF]|[\u200C-\u200D]|[\u2070-\u218F]|[\u2C00-\u2FEF]|[\u3001-\uD7FF]|' \
                        r'[\uF900-\uFDCF]|[\uFDF0-\uFFFD]|[\u10000-\uEFFFF]'

        HEX = r'[0-9]|[A-F]|[a-f]'
        UCHAR = r'\\\\u{HEX}{HEX}{HEX}{HEX}|\\\\U{HEX}{HEX}{HEX}{HEX}{HEX}{HEX}{HEX}{HEX}'.format(HEX=HEX)
        PN_CHARS_U = r'{PN_CHARS_BASE}|_'.format(PN_CHARS_BASE=PN_CHARS_BASE)
        PN_CHARS = r'{PN_CHARS_U}|\-|[0-9]|\\u00B7|[\u0300-\u036F]|[\u203F-\u2040]'.format(PN_CHARS_U=PN_CHARS_U)
        pattern = JSGPattern(r'({PN_CHARS}|\.|\:|\/|\\\\|\#|\@|\%|\&|{UCHAR})*'.format(PN_CHARS=PN_CHARS, UCHAR=UCHAR))
        self.assertTrue(pattern.matches("http://a.example/p\u0031"))
        self.assertTrue(IRI.pattern.matches("http://a.example/p\u0031"))




if __name__ == '__main__':
    unittest.main()

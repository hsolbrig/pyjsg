
import unittest

from jsonasobj import loads as jsonloads
from jsonasobj.jsonobj import as_json

from pyjsg.jsglib import JSGObjectMap, JSGContext, ArrayFactory, Integer
from tests.test_jsglib.iri_defn import *

_CONTEXT = JSGContext()


class ObjectMapTestCase(unittest.TestCase):

    def test_basic_map(self):
        class IntObjectMap(JSGObjectMap):
            _name_filter = HEX
            _value_type = ArrayFactory('', _CONTEXT, Integer, 0, None)

            def __init__(self,
                         **_kwargs):
                super().__init__(_CONTEXT, **_kwargs)


        x = IntObjectMap()
        x.E = [1,2,3]
        self.assertTrue(x._is_valid())
        self.assertEqual(as_json(x), as_json(jsonloads('{"E":[1,2,3]}')))
        with self.assertRaises(ValueError):
            x.G = [1, 2, 4]
        with self.assertRaises(ValueError):
            x.C = 1
        with self.assertRaises(ValueError):
            x = IntObjectMap(aa=[1])

    def test_any_key(self):
        class ALPHA(JSGString):
            pattern = JSGPattern(r'[A-Za-z]')

        class AnyKeyObjectMap(JSGObjectMap):
            _value_type = ALPHA

            def __init__(self,
                         **_kwargs):
                super().__init__(_CONTEXT, **_kwargs)

        x = AnyKeyObjectMap(**dict(I1="a"))
        x["item 2"] = "b"
        self.assertTrue(x._is_valid())
        with self.assertRaises(ValueError):
            x.c = "1"

    def test_any_value(self):
        class IRIKey(JSGObjectMap):
            _name_filter = IRI

            def __init__(self,
                         **_kwargs):
                super().__init__(_CONTEXT, **_kwargs)

        x = IRIKey(**{"http://example.org": 42, "http://ex.org?id=1": None})
        self.assertEqual('{"http://example.org": 42, "http://ex.org?id=1": null}', as_json(x, indent=None))
        self.assertTrue(x._is_valid())
        self.assertEqual(42, x["http://example.org"])
        self.assertIsNone(x["http://ex.org?id=1"])


if __name__ == '__main__':
    unittest.main()

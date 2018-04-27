
import unittest
from typing import List

from jsonasobj.jsonobj import as_json

from pyjsg.jsglib.jsg import JSGObjectMap, JSGPattern, JSGContext, JSGString, Null
from tests.test_jsglib.iri_defn import *
from jsonasobj import loads as jsonloads

_CONTEXT = JSGContext()


class ObjectMapTestCase(unittest.TestCase):

    def test_basic_map(self):
        class IntObjectMap(JSGObjectMap):
            _name_filter = JSGPattern(r'[A-Za-z][0-9]+')
            _value_type = List[int]

            def __init__(self,
                         **_kwargs):
                super().__init__(_CONTEXT, **_kwargs)

        x = IntObjectMap()
        x.a17 = [1,2,3]
        self.assertTrue(x._is_valid())
        self.assertEqual(as_json(x), as_json(jsonloads('{"a17":[1,2,3]}')))
        with self.assertRaises(ValueError):
            x.ab = [1, 2, 4]
        with self.assertRaises(ValueError):
            x.t1 = 1
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

        x = AnyKeyObjectMap(I1="a")
        x["item 2"] = "b"
        self.assertTrue(x._is_valid())
        with self.assertRaises(ValueError):
            x.c = "1"

    def test_any_value(self):
        class IRIKey(JSGObjectMap):
            _name_filter = IRI.pattern

            def __init__(self,
                         **_kwargs):
                super().__init__(_CONTEXT, **_kwargs)

        x = IRIKey(**{"http://example.org": 42, "http://ex.org?id=1": Null})
        self.assertEqual('{"http://example.org": 42, "http://ex.org?id=1": null}', as_json(x, indent=None))
        self.assertTrue(x._is_valid())
        self.assertEqual(x["http://example.org"], 42)
        self.assertEqual(x["http://ex.org?id=1"], Null)


if __name__ == '__main__':
    unittest.main()

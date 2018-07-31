import unittest

from jsonasobj.jsonobj import as_json

from pyjsg.jsglib.loader import is_valid, loads
from pyjsg.jsglib import Empty
from pyjsg.validate_json import JSGPython


class JSGNullTestCase(unittest.TestCase):
    def test_required_null(self):
        j = JSGPython('doc { x: @null }', print_python=False)
        rslt = j.conforms('{"x": null}')
        if not rslt.success:
            print(str(rslt))
        self.assertTrue(rslt.success)
        jclass = getattr(j.module, 'doc')
        j2 = jclass()
        self.assertEqual('{}', as_json(j2))
        self.assertFalse(is_valid(j2))
        j2.x = None
        self.assertEqual('{"x": null}', as_json(j2, indent=None))
        self.assertTrue(is_valid(j2))
        j2.x = Empty
        self.assertEqual('{}', as_json(j2))
        self.assertFalse(is_valid(j2))
        with self.assertRaises(ValueError):
            j2.x = 17

    def test_optional_null(self):
        j = JSGPython('doc { x: @null? }', print_python=False)
        rslt = j.conforms('{"x": null}')
        if not rslt.success:
            print(str(rslt))
        self.assertTrue(rslt.success)
        jclass = getattr(j.module, 'doc')
        j2 = jclass()
        self.assertEqual('{}', as_json(j2))
        self.assertTrue(is_valid(j2))
        j2.x = None
        self.assertEqual('{"x": null}', as_json(j2, indent=None))
        self.assertTrue(is_valid(j2))
        j2.x = Empty
        self.assertEqual('{}', as_json(j2))
        self.assertTrue(is_valid(j2))
        with self.assertRaises(ValueError):
            j2.x = 17

    def test_required_any(self):
        j = JSGPython('doc { x: . }', print_python=False)
        rslt = j.conforms('{"x": null}')
        if not rslt.success:
            print(str(rslt))
        self.assertTrue(rslt.success)
        jclass = getattr(j.module, 'doc')
        j2 = jclass()
        self.assertEqual('{}', as_json(j2))
        self.assertFalse(is_valid(j2))
        j2.x = None
        self.assertEqual('{"x": null}', as_json(j2, indent=None))
        self.assertTrue(is_valid(j2))
        j2.x = Empty
        self.assertEqual('{}', as_json(j2))
        self.assertFalse(is_valid(j2))

    def test_various_anys(self):
        j = JSGPython('doc {x: . }')
        for v in ['null', '17', '-22', '-22.0', 'true', '"A string"', '{"x": 243}']:
            json = f'{{"x": {v}}}'
            j2 = loads(json, j.module)
            self.assertEqual(json, as_json(j2, indent=None))
        json = '{"x": -17395e-2}'
        self.assertEqual('{"x": -173.95}', as_json(loads(json, j.module), indent=None))

    def test_various_optional_anys(self):
        j = JSGPython('doc {x: .? }')
        for v in ['null', '17', '-22', '-22.0', 'false', '"A string"', '{"x": null}']:
            json = f'{{"x": {v}}}'
            j2 = loads(json, j.module)
            self.assertEqual(json, as_json(j2, indent=None))
        json = '{"x": -17395e-2}'
        self.assertEqual('{"x": -173.95}', as_json(loads(json, j.module), indent=None))

    def test_optional_any(self):
        j = JSGPython('doc { x: .? }', print_python=False)
        rslt = j.conforms('{"x": null}')
        if not rslt.success:
            print(str(rslt))
        self.assertTrue(rslt.success)
        jclass = getattr(j.module, 'doc')
        j2 = jclass()
        self.assertEqual('{}', as_json(j2))
        self.assertTrue(is_valid(j2))
        j2.x = None
        self.assertEqual('{"x": null}', as_json(j2, indent=None))
        self.assertTrue(is_valid(j2))
        j2.x = Empty
        self.assertEqual('{}', as_json(j2))
        self.assertTrue(is_valid(j2))


if __name__ == '__main__':
    unittest.main()

import unittest
from typing import cast

from pyjsg.parser_impl.jsg_builtinvaluetype_parser import JSGBuiltinValueType
from pyjsg.parser_impl.jsg_valuetype_parser import JSGValueType
from tests.test_basics.parser import parse

builtin_tests = [("@string", "jsg.String", "str", "None"),
                 ("@number", "jsg.Number", "float", "None"),
                 ("@int", "jsg.Integer", "int", "None"),
                 ("@bool", "jsg.Boolean", "bool", "None"),
                 ("@null", "jsg.JSGNull", "type(None)", "jsg.Empty"),
                 ("@array", "jsg.ArrayFactory('{name}', _CONTEXT, jsg.AnyType, 0, None)", "list", "None"),
                 ("@object", "jsg.ObjectFactory('{name}', _CONTEXT, jsg.Object)", "object", "None"),
                 (".", "jsg.AnyTypeFactory('{name}', _CONTEXT)", "object", "jsg.Empty")]


class BuiltinValueTypeTestCase(unittest.TestCase):
    def test_builtins(self):
        for text, sig, typ_, mt_typ in builtin_tests:
            t = cast(JSGValueType, parse(text, "builtinValueType", JSGBuiltinValueType))
            self.assertEqual(sig, t.signature_type(), text)
            self.assertEqual(typ_, t.python_type(), text)
            self.assertEqual(f"builtinValueType: {text if text != '.' else 'jsg.AnyType'}", str(t), text)
            self.assertEqual(mt_typ, t.mt_value(), text)
            self.assertEqual([], t.members_entries(), text)
            self.assertEqual([], t.dependency_list(), text)


if __name__ == '__main__':
    unittest.main()

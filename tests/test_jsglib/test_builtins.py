import unittest
from typing import Union

from pyjsg.jsglib.jsg import String, JSGPattern, Number, Integer, Boolean, Null, JSGNull


class JSGBuiltinsTestCase(unittest.TestCase):
    def do_test(self,
                cls,
                val: Union[str, int, float, bool, None],
                rslt: Union[str, int, float, bool]=None) -> Union[str, int, float, bool]:
        t = cls(val)
        self.assertTrue(t._is_valid())
        self.assertEqual(rslt if rslt is not None else val, t.val)
        return t.val

    def test_string(self):
        self.do_test(String, "a simple string")
        # self.do_test(String, True, "true")
        # self.do_test(String, False, "false")
        # self.do_test(String, 143, "143")
        # self.do_test(String, 95.221E+5, "9522100.0")
        self.do_test(String, "95.221E+5")
        self.do_test(String, "^<80>߿ࠀ࿿က쿿퀀퟿�𐀀𿿽񀀀󿿽􀀀􏿽$/")
        self.do_test(String, "^\/\t\n\r\-\\\u0061\U0001D4B8$", "^\\/\t\n\r\\-\\a𝒸$")
        self.assertIsNone(String(None).val)
        # self.do_test(String, -119, "-119")

        class PAT_STR(String):
            pattern = JSGPattern(r'[a-z][0-9]+')

        self.do_test(PAT_STR, 'a143')

        with self.assertRaises(ValueError):
            x = PAT_STR('17')
        x = PAT_STR('17', validate=False)
        self.assertFalse(x._is_valid())

        class INT_STR(String):
            pattern = JSGPattern(r'0|([1-9][0-9]*)')

        self.do_test(INT_STR, "17")
        # self.do_test(INT_STR, 17, "17")
        with self.assertRaises(ValueError):
            x = INT_STR("-17")
        with self.assertRaises(ValueError):
            x = INT_STR("something")

    def test_number(self):
        self.assertIsInstance(self.do_test(Number, 42), int)
        self.assertIsInstance(self.do_test(Number, -173), int)
        self.assertIsInstance(self.do_test(Number, 0.1723), float)
        with self.assertRaises(ValueError):
            x = Number("+173.0003E-5")          # JSON doesn't allow plus signs
        self.do_test(Number, "-173.0003E-5", -0.001730003)

        class POS_NUMBER(Number):
            pattern = JSGPattern(r'(0|[1-9][0-9]*)(.[0-9]+)?([eE][+-]?[0-9]+)?')

        self.do_test(POS_NUMBER, 1003675)
        with self.assertRaises(ValueError):
            x = POS_NUMBER(-1)
        with self.assertRaises(ValueError):
            x = POS_NUMBER("-117.438")

    def test_integer(self):
        self.assertIsInstance(self.do_test(Integer, 42), int)
        self.assertIsInstance(self.do_test(Integer, -173), int)
        self.assertIsInstance(self.do_test(Integer, 0), int)
        self.assertIsInstance(self.do_test(Integer, "-119221", -119221), int)
        with self.assertRaises(ValueError):
            x = Integer(0.1723)
        with self.assertRaises(ValueError):
            x = Integer("-173.0003E-5")
        with self.assertRaises(ValueError):
            x = Integer("a")
        with self.assertRaises(ValueError):
            x = Integer("")
        with self.assertRaises(ValueError):
            x = Integer(False)
        self.assertIsNone(Integer(None).val)

        class NEG_INTEGER(Integer):
            pattern = JSGPattern(r'-(0|[1-9][0-9]*)')

        self.assertIsInstance(self.do_test(NEG_INTEGER, -119), int)
        with self.assertRaises(ValueError):
            x = NEG_INTEGER(17)

    def test_bool(self):
        self.assertIsInstance(self.do_test(Boolean, True), bool)
        self.assertIsInstance(self.do_test(Boolean, "True", True), bool)
        self.assertIsInstance(self.do_test(Boolean, "true", True), bool)
        self.assertIsInstance(self.do_test(Boolean, False), bool)
        self.assertIsInstance(self.do_test(Boolean, "False", False), bool)
        self.assertIsInstance(self.do_test(Boolean, "false", False), bool)
        self.assertIsNone(Boolean(None).val)
        with self.assertRaises(ValueError):
            x = Boolean(0)
        with self.assertRaises(ValueError):
            x = Boolean("")

        class TRUE_ONLY(Boolean):
            pattern = Boolean.true_pattern

        self.assertIsInstance(self.do_test(TRUE_ONLY, True), bool)
        with self.assertRaises(ValueError):
            x = TRUE_ONLY(False)

    def test_incompatible_pattern(self):
        class INCOMPAT(Integer):
            pattern = JSGPattern(r'[a-z]+')

        x = INCOMPAT("a")

        with self.assertRaises(ValueError):
            x = INCOMPAT(17)

    def test_null(self):
        self.assertIsNone(JSGNull(None).val)
        self.assertIsNotNone(Null.val)
        self.assertEqual("null", str(Null))

if __name__ == '__main__':
    unittest.main()

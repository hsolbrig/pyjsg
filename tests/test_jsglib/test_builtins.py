import unittest
from typing import Union

from pyjsg.jsglib import String, JSGPattern, Number, Integer, Boolean, JSGNull, Empty


class JSGBuiltinsTestCase(unittest.TestCase):
    def do_test(self,
                cls,
                val: Union[str, int, float, bool, None],
                rslt: Union[str, int, float, bool]=None,
                fail: bool=False) -> Union[str, int, float, bool]:
        if fail:
            with self.assertRaises(ValueError):
                cls(val)
        else:
            t = cls(val)
            self.assertEqual(rslt if rslt is not None else val, t)
            if not isinstance(t, bool):
                self.assertEqual(rslt if rslt is not None else val, t.val)
            return t

    def test_string(self):
        self.do_test(String, "a simple string")
        self.do_test(String, True, "true", fail=True)
        self.do_test(String, False, "false", fail=True)
        self.do_test(String, 143, "143", fail=True)
        self.do_test(String, 95.221E+5, "9522100.0", fail=True)
        self.do_test(String, "95.221E+5")
        self.do_test(String, "^<80>߿ࠀ࿿က쿿퀀퟿�𐀀𿿽񀀀󿿽􀀀􏿽$/")
        self.do_test(String, "^\/\t\n\r\-\\\u0061\U0001D4B8$", "^\\/\t\n\r\\-\\a𝒸$")
        self.do_test(String, None, fail=True)
        self.do_test(String, -119, "-119", fail=True)

        class PAT_STR(String):
            pattern = JSGPattern(r'[a-z][0-9]+')

        self.do_test(PAT_STR, 'a143')

        with self.assertRaises(ValueError):
            x = PAT_STR('17')

        class INT_STR(String):
            pattern = JSGPattern(r'0|([1-9][0-9]*)')

        self.do_test(INT_STR, "17")
        # self.do_test(INT_STR, 17, "17")
        with self.assertRaises(ValueError):
            x = INT_STR("-17")
        with self.assertRaises(ValueError):
            x = INT_STR("something")

    def test_number(self):
        self.assertIsInstance(self.do_test(Number, 42), float)
        self.assertIsInstance(self.do_test(Number, -173), float)
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
        with self.assertRaises(ValueError):
            x = Integer(None)

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
        with self.assertRaises(ValueError):
            Boolean(None)
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

        with self.assertRaises(ValueError):
            x = INCOMPAT("a")

        with self.assertRaises(ValueError):
            x = INCOMPAT(17)

    def test_null(self):
        self.assertIsNone(JSGNull(None).val)
        self.assertIsNone(JSGNull(JSGNull).val)
        with self.assertRaises(ValueError):
            JSGNull(Empty)
        with self.assertRaises(ValueError):
            JSGNull('null')

    def test_empty_type(self):
        """ Make sure that Empty is a class only thingie """
        self.assertTrue(Empty is Empty())

if __name__ == '__main__':
    unittest.main()

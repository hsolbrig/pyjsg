
import unittest

from pyjsg.jsglib import jsg


class Issue7Test(unittest.TestCase):
    def test_issue_7(self):
        class LANGTAG(jsg.JSGString):
            pattern = jsg.JSGPattern(r'[a-zA-Z]+(\-([a-zA-Z0-9])+)*')

        x = LANGTAG("de")
        self.assertNotEqual("fr", x)

    def test_issue_7_bool(self):
        # def __setattr__(self, key, value):
        #     if key == "val" and value is not None:
        #         self.__dict__[key] = value if isinstance(value, bool) else Boolean.true_pattern.matches(str(value))
        #     else:
        #         self.__dict__[key] = value
        b1 = jsg.Boolean("True")
        with self.assertRaises(ValueError):
            jsg.Boolean("Aardvark")
        b2 = jsg.Boolean("False")
        b1.val = b2
        self.assertFalse(b1.val)
        b1.val = jsg.Boolean("False")
        b1.val = "True"
        b1.val = "False"
        with self.assertRaises(ValueError):
            b1.val = 0


if __name__ == '__main__':
    unittest.main()

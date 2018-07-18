
import unittest

from pyjsg.jsglib import JSGString, JSGPattern, Boolean


class Issue7Test(unittest.TestCase):
    def test_issue_7(self):
        class LANGTAG(JSGString):
            pattern = JSGPattern(r'[a-zA-Z]+(\-([a-zA-Z0-9])+)*')

        x = LANGTAG("de")
        self.assertNotEqual("fr", x)

    def test_issue_7_bool(self):
        # def __setattr__(self, key, value):
        #     if key == "val" and value is not None:
        #         self.__dict__[key] = value if isinstance(value, bool) else Boolean.true_pattern.matches(str(value))
        #     else:
        #         self.__dict__[key] = value

        # Update: Bool simply can't be wrapped -- skip the val stuff
        b1 = Boolean("True")
        with self.assertRaises(ValueError):
            Boolean("Aardvark")
        b2 = Boolean("False")
        b1 = b2
        self.assertFalse(b1)
        b1 = Boolean("False")
        b1 = "True"
        b1 = "False"
        with self.assertRaises(ValueError):
            b1 = Boolean(0)


if __name__ == '__main__':
    unittest.main()

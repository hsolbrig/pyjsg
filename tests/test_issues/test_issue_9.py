
import unittest

from pyjsg.jsglib import JSGString, JSGPattern


class Issue9TestCase(unittest.TestCase):
    def test_issue_9(self):
        self.assertTrue(isinstance("abc", JSGString))
        self.assertTrue(isinstance("", JSGString))
        self.assertFalse(isinstance(None, JSGString))
        self.assertFalse(isinstance(1, JSGString))
        self.assertFalse(isinstance([], JSGString))
        self.assertTrue(JSGString("abc"), JSGString)

        class T(JSGString):
            pass
        self.assertTrue(T("abc"), JSGString)

        class TP(JSGString):
            pattern = JSGPattern("[a-zA-Z]+")
        self.assertTrue(TP("abc"), JSGString)


if __name__ == '__main__':
    unittest.main()

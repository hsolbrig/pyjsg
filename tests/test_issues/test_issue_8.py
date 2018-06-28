
import unittest


class Issue8TestCase(unittest.TestCase):

    def test_none_as_string_instance(self):
        from pyjsg.jsglib import JSGString, JSGPattern

        class S(JSGString):
            pattern = JSGPattern(r'[a-zA-Z]+')

        self.assertTrue(isinstance('abc', S))
        self.assertFalse(isinstance('abc1', S))
        self.assertFalse(isinstance('', S))
        self.assertFalse(isinstance(None, S))


if __name__ == '__main__':
    unittest.main()

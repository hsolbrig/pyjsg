import unittest

from pyjsg.validate_json import JSGPython


class ExtraTestCase(unittest.TestCase):
    def test_extra(self):
        x = JSGPython('doc {a:@string}')
        self.assertFalse(x.conforms('{"a":"hello", "target":"earthling"}').success)


if __name__ == '__main__':
    unittest.main()

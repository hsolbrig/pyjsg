import unittest

from pyjsg.validate_json import JSGPython


class IgnoreTestCase(unittest.TestCase):
    """ Test list of sequences in documentation """
    def test_1(self):
        x = JSGPython('''
.IGNORE target;
doc {a:@string}
''')

        rslt = x.conforms('{"a":"hello", "target":"earthling"}')
        self.assertTrue(rslt.success)


if __name__ == '__main__':
    unittest.main()

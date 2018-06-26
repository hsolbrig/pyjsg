import unittest

from pyjsg.validate_json import JSGPython


class MemberExampleTestCase(unittest.TestCase):
    def test1(self):
        x = JSGPython('''doc {
            last_name : @string,       # exactly one last name of type string
            first_name : @string+      # array or one or more first names
            age : @int?,               # optional age of type int
            weight : @number*          # array of zero or more weights
        }
        ''')
        rslts = x.conforms('''
        { "last_name" : "snooter",
          "first_name" : ["grunt", "peter"],
          "weight" : []
        }''')
        self.assertTrue(rslts.success)


if __name__ == '__main__':
    unittest.main()

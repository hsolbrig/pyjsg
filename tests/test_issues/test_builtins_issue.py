import unittest

from pyjsg.validate_json import JSGPython


class BuiltinSyntaxTestCase(unittest.TestCase):
    def test_1(self):
        x = JSGPython('''doc {
    v1: @string,
    v2: @number,
    v3: @int,
    v4: @bool,
    v5: @null,
    v6: @array,
    v7: @object 
}
obj {a: . , }''')

        rslt = x.conforms('''
        { "v1": "This is text!",
          "v2": -117.432e+2,
          "v3": -100173,
          "v4": false,
          "v5": null,
          "v6": [12, "text", null],
          "v7": {"q": "life", "a": 42}
        }''')
        self.assertTrue(rslt.success)


if __name__ == '__main__':
    unittest.main()

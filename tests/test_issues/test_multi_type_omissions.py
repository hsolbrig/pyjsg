import unittest

from tests.utils.harness import Harness

jsg1 = '''
.TYPE t - id val ;
doc {a:.,}
id {b: @int}
val {c: @string}
'''


class MultiTypeOmissionsTestCase(Harness):
    def test_one_pass(self):
        self.do_test(jsg1, '{"t": "doc", "a": {"b": 173}}')
        self.do_test(jsg1, '{"c": "sails"}')
        self.do_test(jsg1, '{"b": -117}')

    def test_one_fail(self):
        self.do_test(jsg1, '{"t": "doc", "a": {"b": "x"}}', False, False, False, 'Invalid Integer value: "x"')
        self.do_test(jsg1, '{"c": 112}', False, False, False, 'Invalid String value "112"')
        self.do_test(jsg1, '{"b": "test"}', False, False, False, 'Invalid Integer value: "x"')
        self.do_test(jsg1, '{"d": 117}', False)


if __name__ == '__main__':
    unittest.main()

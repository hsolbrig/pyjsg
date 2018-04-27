import unittest

from tests.utils.harness import Harness


class MissingItemTestCase(Harness):
    def test1(self):
        # If status is misssing completely, we fail
        self.do_test("doc {status: .}", "{}", False, False, True)
        # If status is present in ANY form, it passes
        self.do_test("doc {status: .}", '{"status": null}', True)
        self.do_test("doc {status: .}", '{"status": 17}', True)
        self.do_test("doc {status: .}", '{"status": "stuff"}', True)


if __name__ == '__main__':
    unittest.main()

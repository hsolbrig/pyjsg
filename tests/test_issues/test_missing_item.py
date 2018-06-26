import unittest

from tests.utils.harness import Harness


class MissingItemTestCase(Harness):
    def test1(self):
        # If status is misssing completely, we fail
        # Args: jsg, json, should_pass, raises_exception, fails_validation
        # Fails because of required status
        self.do_test("doc {status: .}", "{}", False, False, True, "doc: Missing required field: 'status'")
        # Passes because item matches
        self.do_test("doc {status: .} item {}", "{}")
        # Fails because neither status nor v present
        self.do_test("doc {status: .} item {v: .}", "{}", False, False, True, "doc: Missing required field: 'status'")
        self.do_test("item {v: .} doc {status: .} ", "{}", False, False, True, "item: Missing required field: 'v'")
        # If status is present in ANY form, it passes
        self.do_test("doc {status: .} item {v: .}", '{"status": null}')
        self.do_test("doc {status: .} item {v: .}", '{"status": 17}')
        self.do_test("doc {status: .} item {v: .}", '{"status": "stuff"}')
        # If v is present in any for it passes as well
        self.do_test("doc {status: .} item {v: .}", '{"v": true}', True)


if __name__ == '__main__':
    unittest.main()

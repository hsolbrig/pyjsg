import unittest

from tests.utils.harness import Harness


class MissingItemTestCase(Harness):
    def test1(self):
        self.do_test("doc {status: .}", "{}", False, False, True)


if __name__ == '__main__':
    unittest.main()

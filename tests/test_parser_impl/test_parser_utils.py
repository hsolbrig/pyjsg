import unittest

from pyjsg.parser_impl.parser_utils import flatten, flatten_unique, as_set, is_valid_python, esc_kw


class ParserUtilsTestCase(unittest.TestCase):

    def test_flatten(self) -> None:
        self.assertEqual([], flatten([]))
        self.assertEqual([1, 2, 3, 4, 5, 6], flatten([1, [2], [3, [4, 5], [6], []]]))
        self.assertEqual(["a", "c", "a", "e", "e", "a"], flatten([["a", "c"], ["a", "e"], ["e", "a"]]))

    def test_flatten_unique(self) -> None:
        self.assertEqual([], flatten_unique([]))
        self.assertEqual([1, 2, 3, 4, 5, 6], flatten_unique([1, [2], [3, [4, 5], [[[6]]], []]]))
        self.assertEqual(["a", "c", "e"], flatten_unique([["a", "c"], ["a", "e"], ["e", "a"]]))

    def test_as_set(self) -> None:
        self.assertEqual(set(), as_set([]))
        self.assertEqual({1, 2, 3, 4, 5, 6}, as_set([1, [2], [3, [4, 5], [[[6]]], []]]))
        self.assertEqual({"a", "c", "e"}, as_set([["a", "c"], ["a", "e"], ["e", "a"]]))

    def test_is_valid_python(self) -> None:
        self.assertTrue(is_valid_python('a'))
        self.assertTrue(is_valid_python('is_valid_python'))
        self.assertFalse(is_valid_python('def'))
        self.assertFalse(is_valid_python('class'))
        self.assertFalse(is_valid_python('a 1'))
        self.assertFalse(is_valid_python('a-1'))
        self.assertFalse(is_valid_python('1a'))

    def test_esc_kw(self) -> None:
        import keyword
        self.assertEqual('a', esc_kw('a'))
        self.assertEqual('def_', esc_kw('def'))
        for k in keyword.kwlist:
            self.assertEqual(k + '_', esc_kw(k))
            self.assertEqual(k + 'x', esc_kw((k + 'x')))


if __name__ == '__main__':
    unittest.main()

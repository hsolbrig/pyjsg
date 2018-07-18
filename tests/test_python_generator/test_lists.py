import unittest

from tests.test_python_generator.utils import PythonGeneratorUtils


class ListTestCase(PythonGeneratorUtils):
    save_output_files: bool = False

    def test_list(self):
        import tests.test_python_generator.py.list as doc

        jsg = 'l {e:@string*}'
        test_cases = [
            '{"e": []}',
            '{"e": ["abc"]}'
        ]
        self.do_test(jsg, 'list', doc, test_cases, {})

        import tests.test_python_generator.py.list_2 as doc2
        jsg2 = 'l {e:@string+}'
        test_cases2 = [
            '{"e": ["abc"]}'
        ]
        fail_test_cases2 = [
            '{}',
            '{"e": null}',
            '{"e": []}',
        ]
        self.do_test(jsg2, 'list_2', doc2, test_cases2, {}, fail_test_cases2)


if __name__ == '__main__':
    unittest.main()

import unittest

from tests.test_python_generator.utils import PythonGeneratorUtils


class AnyTypeTestCase(PythonGeneratorUtils):
    save_output_files: bool = False

    def test_any_object(self):
        import tests.test_python_generator.py.any_type as doc

        jsg = 'doc {status: .}'
        test_cases = [
            '{"status": 17}',
            '{"status": "test"}',
            '{"status": null}',
            '{"status": []}',
            '{"status": {"status": -117.2}}',
            '{"status": [{"status": "inside"}]}'
        ]
        self.do_test(jsg, 'any_type', doc, test_cases, {})

        import tests.test_python_generator.py.any_type_2 as doc2
        jsg2 = 'doc {class: .}'
        test_cases2 = [
            '{"class": 17}',
            '{"class": "test"}',
            '{"class": null}',
            '{"class": []}',
            '{"class": {"class": -117.2}}',
            '{"class": [{"class": "inside"}]}'
        ]
        self.do_test(jsg2, 'any_type_2', doc2, test_cases2, {})

        import tests.test_python_generator.py.any_type_3 as doc3
        jsg3 = 'doc {"A 1": .}'
        test_cases3 = [
            '{"A 1": 17}',
            '{"A 1": "test"}',
            '{"A 1": null}',
            '{"A 1": []}',
            '{"A 1": {"A 1": -117.2}}',
            '{"A 1": [{"A 1": "inside"}]}'
        ]
        self.do_test(jsg3, 'any_type_3', doc3, test_cases3, {})

if __name__ == '__main__':
    unittest.main()

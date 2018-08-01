import sys
import unittest

from tests.test_python_generator.utils import PythonGeneratorUtils


class MacroTestCase(PythonGeneratorUtils):
    save_output_files: bool = False

    def test_macro1(self):
        import tests.test_python_generator.py.macrotest_1 as doc

        jsg = 'Shape {id:(@int|@string)?}'
        test_cases = [
            '{"id": 17}',
            '{"id": "abc"}'
        ]
        fail_cases = [
            '{"id": 12.2}',
            '{"id": 17, "j": 1}'
        ]
        self.do_test(jsg, 'macrotest_1', doc, test_cases, {}, fail_cases)

    def test_macro2(self):
        import tests.test_python_generator.py.macrotest_2 as doc2
        jsg2 = """
shapeExprLabel   = @int|@string ;
Shape            {id:shapeExprLabel?}
"""
        test_cases = [
            '{"id": 17}',
            '{"id": "abc"}'
        ]
        fail_cases = [
            '{"id": 12.2}',
            '{"id": 17, "j": 1}'
        ]
        self.do_test(jsg2, 'macrotest_2', doc2, test_cases, {}, fail_cases)

    def test_macro3(self):
        # Subtle change in earlier python - ':' is escaped in regular expression strings
        if sys.version_info < (3, 7):
            import tests.test_python_generator.py.macrotest_3_36 as doc3
            testfile = "macrotest_3_36"
        else:
            import tests.test_python_generator.py.macrotest_3 as doc3
            testfile = "macrotest_3"

        jsg3 = """
shapeExprLabel   = IRIREF|BNODE ;
Shape            {id:shapeExprLabel?}

@terminals
IRIREF           : [A-Z]+ ;
BNODE            : '_:' [A-Z]+ ;\
"""
        test_cases = [
            '{"id": "AAA"}',
            '{"id": "_:AAA"}'
        ]
        fail_cases = [
            '{"id": "aaa"}',
            '{"id": "AAA", "j": 1}'
        ]
        self.do_test(jsg3, testfile, doc3, test_cases, {}, fail_cases, print_python=False)


if __name__ == '__main__':
    unittest.main()

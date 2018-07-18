import unittest

from tests.test_python_generator.utils import PythonGeneratorUtils


class CardinalityTestCase(PythonGeneratorUtils):
    save_output_files: bool = False

    def test_list_cardinalities(self):
        import tests.test_python_generator.py.cardinality_1 as doc

        jsg = '''
        doc {opt: .?
          req: .
          l0n: .*
          l1n: .+
          l01: [.?]
          l11: [.{1}]
          l0na: [.*]
          l1na: [.+]
          optl0n: [.*]?
          optl1n: [.+]?
        }'''
        test_cases = []
        self.do_test(jsg, 'cardinality_1', doc, test_cases, {})

    def test_list_cardinalities_2(self):
        import tests.test_python_generator.py.cardinality_2 as doc

        jsg = '''
           doc {opt: @string?
             req: @string
             l0n: @string*
             l1n: @string+
             l01: [@string?]
             l11: [@string]
             l0na: [@string*]
             l1na: [@string+]
             optl0n: [@string*]?
             optl1n: [@string+]?
           }'''
        test_cases = []
        self.do_test(jsg, 'cardinality_2', doc, test_cases, {})

    def test_nested_lists(self):
        import tests.test_python_generator.py.cardinality_3 as doc

        jsg = '''
        doc {l0nl0n: [.*]*} '''
        test_cases = []
        self.do_test(jsg, 'cardinality_3', doc, test_cases, {})

    def test_nested_cardinalities(self):
        import tests.test_python_generator.py.cardinality_4 as doc
        # TODO: Need to be able to pass a constructor template so that we can have an either 2 or 3 arrays
        # each consisting of an array of 2 to 8 strings.  At the moment, the inner cardinality is lost
        # Probably the correct solution is to create an anonymous inner constructor?
        jsg = 'doc {"l23 38n": [@string{2,8}]{2, 3}}'
        test_cases = []
        self.do_test(jsg, 'cardinality_4', doc, test_cases, {})


if __name__ == '__main__':
    unittest.main()

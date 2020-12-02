import os
import unittest


class GeneratePythonTestCase(unittest.TestCase):
    # Generate some bad python and verify that an error is detected in the output
    def test_execute_item(self):
        from pyjsg.parser_impl.generate_python import generate, evaluate

        basedir = os.path.abspath(os.path.dirname(__file__))
        goodfile = os.path.join(basedir, 'py', 'goodjsg.py')
        badfile = os.path.join(basedir, 'py', 'badjsg.py')

        # Make sure that a simple generate works
        self.assertEqual(0, generate([os.path.join(basedir, "jsg", "complexfacet.jsg"), "-o", goodfile, "-e", "-nh"]))

        # Make sure that we can detect exceptions and errors
        with open(badfile, 'w') as bf:
            bf.write("i=1/0\n")
            with open(goodfile) as gf:
                bf.write(gf.read())
        with self.assertRaises(ZeroDivisionError):
            evaluate("bar", badfile, False)

        # Make sure that our namespace hasn't been messed up
        self.assertFalse('bar' in globals())
        os.remove(goodfile)
        os.remove(badfile)


if __name__ == '__main__':
    unittest.main()

import unittest
from io import StringIO
from types import ModuleType
from typing import cast, TextIO

from pyjsg.jsglib.loader import loads, Logger, is_valid
from pyjsg.parser_impl.generate_python import parse


class Harness(unittest.TestCase):

    def do_test(self, jsg: str, json: str, should_pass: bool=True, _: bool=True,
                fails_validation: bool=False, expected: str=None) \
            -> None:
        """ Validate JSON against JSG

        :param jsg: JSG definition
        :param json: JSON to validate
        :param should_pass: True means expect success
        :param jsg_exception: (unused)
        :param fails_validation: True means fails is_valid, false means raises exception
        :param expected:
        :return:
        """
        python = parse(jsg, self.__class__.__name__)
        spec = compile(python, self.__class__.__name__, 'exec')
        module = ModuleType(self.__class__.__name__)
        exec(spec, module.__dict__)

        if should_pass:
            self.assertTrue(is_valid(loads(json, module)))
        elif fails_validation:
            logf = StringIO()
            logger = Logger(cast(TextIO, logf))
            self.assertFalse(is_valid(loads(json, module), logger))
            if expected:
                self.assertEqual(expected, logf.getvalue().strip('\n'))
            else:
                print(logf.getvalue())
            self.assertTrue(logger.nerrors > 0)
        else:
            with self.assertRaises(ValueError):
                is_valid(loads(json, module))

import sys
import unittest
from io import StringIO
from types import ModuleType
from typing import cast, TextIO

from pyjsg.jsglib.jsg import loads, JSGException, Logger
from pyjsg.parser_impl.generate_python import parse


class Harness(unittest.TestCase):

    def do_test(self, jsg: str, json: str, should_pass: bool=True, is_exception: bool=True, fails_validation: bool=False) \
            -> None:
        python = parse(jsg, self.__class__.__name__)
        spec = compile(python, self.__class__.__name__, 'exec')
        module = ModuleType(self.__class__.__name__)
        exec(spec, module.__dict__)

        if should_pass:
            loads(json, module)
        elif fails_validation:
            logf = StringIO()
            logger = Logger(cast(TextIO, logf))
            loads(json, module)._is_valid(logger)
            print(logf.getvalue())
            self.assertTrue(logger.nerrors > 0)
        else:
            with self.assertRaises(JSGException if is_exception else ValueError):
                loads(json, module)._is_valid()



import unittest
from typing import cast

from pyjsg.parser_impl.jsg_doc_parser import JSGDocParser
from tests.test_basics.parser import parse


class ObjectMacroTestCase(unittest.TestCase):
    def test_single_option(self):
        t = cast(JSGDocParser, parse("macro = labeledShapeOr ; labeledShapeOr {}", "doc", JSGDocParser))
        exec(t.as_python(self.__class__.__name__), dict())
        t = cast(JSGDocParser, parse("macro = a:@int | b:@int ;", "doc", JSGDocParser))
        exec(t.as_python(self.__class__.__name__), dict())
        t = cast(JSGDocParser, parse("macro = a| b ; a {} b {}", "doc", JSGDocParser))
        exec(t.as_python(self.__class__.__name__), dict())


if __name__ == '__main__':
    unittest.main()

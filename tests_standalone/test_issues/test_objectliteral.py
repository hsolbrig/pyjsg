import os
import unittest

from pyjsg.validate_json import JSGPython

json = """
{
  "@context": "http://www.w3.org/ns/shex.jsonld",
  "type": "Schema",
  "shapes": [
    {
      "id": "http://a.example/S1",
      "type": "Shape",
      "expression": {
        "type": "TripleConstraint",
        "predicate": "http://a.example/p1",
        "valueExpr": {
          "type": "NodeConstraint",
          "values": [
            {
              "value": "0.0",
              "type": "http://www.w3.org/2001/XMLSchema#decimal"
            }
          ]
        }
      }
    }
  ]
}
"""


class ObjectLiteralTestCase(unittest.TestCase):
    @unittest.skipIf(False, "Must be run standalone -- context issues prevent running in test suite")
    def test_ol(self):
        """ Test that the 'type' variable in the ObjectLiteral is not mistaken as a real, unresolved type.
        """
        shexj_jsg = os.path.join(os.path.dirname(__file__), '..', '..', 'tests', 'test_basics', 'jsg', 'ShExJ.jsg')
        rval = JSGPython(shexj_jsg).conforms(json, "1val1DECIMAL")
        self.assertEqual("1val1DECIMAL: Conforms to Schema", str(rval))
        self.assertTrue(rval.success)


if __name__ == '__main__':
    unittest.main()

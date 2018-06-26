
import unittest
from typing import Dict, Optional

from dict_compare import dict_compare
from io import StringIO
from jsonasobj import loads as json_loads

from pyjsg.jsglib import jsg
from pyjsg.jsglib.logger import Logger

_CONTEXT = jsg.JSGContext()


class ObjectTestCase(unittest.TestCase):
    def check_json(self, t: jsg.JSGObject, c: str):
        self.assertTrue(dict_compare(json_loads(c)._as_dict, t._as_json_obj()))

    def test_simple_object(self):
        class Person(jsg.JSGObject):
            _reference_types = []
            _members = {'name': str,
                        'age': int,
                        'married': bool,
                        'weight': float,
                        'tag': Optional[jsg.JSGNull]}
            _strict = True

            def __init__(self,
                         name: str = None,
                         age: int = None,
                         married: bool = None,
                         weight: float = None,
                         tag: Optional[jsg.JSGNull] = None,
                         **_kwargs: Dict[str, object]):
                super().__init__(_CONTEXT, **_kwargs)
                self.name = jsg.String(name)
                self.age = jsg.Integer(age)
                self.married = jsg.Boolean(married)
                self.weight = jsg.Number(weight)
                self.tag = tag

        log = StringIO()

        x = Person()
        x.name = "Grunt P Snooter"
        x = Person(name="Sally Pope", age=42, married=True, weight=117)
        x.name = "Joe"
        self.check_json(x, '{"name": "Sally Pope", "age": 42, "married": true, "weight": 117.5}')
        x = Person("Sally Pope", "42")
        self.check_json(x, '{"name": "Sally Pope", "age": 42}')
        x = Person("Sally Pope")
        self.assertFalse(x._is_valid(log))
        self.assertEqual('Person: Missing required field: \'age\'\n'
                         'Person: Missing required field: \'married\'\n'
                         'Person: Missing required field: \'weight\'\n', log.getvalue())
        log = StringIO()
        x.age = 99
        self.assertFalse(x._is_valid())
        x.married = False
        self.assertFalse(x._is_valid())
        x.weight = "112"
        self.assertTrue(x._is_valid())
        self.check_json(x, '{"name": "Sally Pope", "age": 99, "married": false, "weight": 112}')
        x.tag = jsg.Null
        self.check_json(x, '{"name": "Sally Pope", "age": 99, "married": false, "weight": 112, "tag": null}')
        with self.assertRaises(ValueError):
            x.age = "abc"
        del x.weight
        x._is_valid(log)
        self.assertEqual('Person: Missing required field: \'weight\'\n', log.getvalue())


if __name__ == '__main__':
    unittest.main()

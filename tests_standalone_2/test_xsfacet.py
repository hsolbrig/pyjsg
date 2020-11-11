import os
import unittest

from dict_compare import compare_dicts
from jsonasobj.jsonobj import as_json, as_dict

import tests.test_basics.py.ShExJ as ShExJ
from pyjsg.jsglib.loader import loads, is_valid, Logger
from jsonasobj import loads as jao_loads


class XSFacetTestCase(unittest.TestCase):
    def test_facet(self):
        file_loc = os.path.join(os.path.dirname(__file__), 'data', '1bnodeLength.json')
        with open(file_loc)  as f:
            text = f.read()
        facets = loads(text, ShExJ)
        # print(as_json(facets))
        log = Logger()
        val = is_valid(facets, log)
        # print(log.getvalue())
        self.assertTrue(val)
        d1 = jao_loads(text)
        d2 = jao_loads(as_json(facets))
        self.assertTrue(compare_dicts(as_dict(d1), as_dict(d2)))

if __name__ == '__main__':
    unittest.main()

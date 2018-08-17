import unittest

from pyjsg.validate_json import JSGPython


class GeneSeqTestCase(unittest.TestCase):
    """ Test list of sequences in documentation """
    def test_1(self):
        x = JSGPython('''
doc {
    sequences: [(RNASEQ|DNASEQ)]
}

@terminals
RNASEQ: [ACGU]+ ;
DNASEQ: [ACGT]+ ;
''')

        rslt = x.conforms('''
{ "sequences": [
    "GCUACGGAGCUUGGAGCUAG",
    "ATTTTGCGAGGTCCC"
   ]
}''')
        self.assertTrue(rslt.success)


if __name__ == '__main__':
    unittest.main()

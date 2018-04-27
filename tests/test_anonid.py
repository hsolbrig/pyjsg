
import unittest

from pyjsg.parser_impl.anonymousidentifierfactory import AnonymousIdentifierFactory


class AnonIdTestCase(unittest.TestCase):
    from pyjsg.parser_impl.anonymousidentifierfactory import AnonymousIdentifierFactory

    def test1(self):
        fact = AnonymousIdentifierFactory()
        self.assertEqual("_Anon1", fact.next_id())
        self.assertEqual("_Anon2", fact.next_id())
        self.assertTrue(fact.is_anon("_Anon173"))
        self.assertFalse(fact.is_anon("_Anon01"))
        self.assertFalse(fact.is_anon("_Anona1"))
        fact = AnonymousIdentifierFactory("ID")
        self.assertEqual("ID1", fact.next_id())
        self.assertEqual("ID2", fact.next_id())
        self.assertTrue(fact.is_anon("ID1173"))
        self.assertFalse(fact.is_anon("ID01"))
        self.assertFalse(fact.is_anon("_Anon1"))


if __name__ == '__main__':
    unittest.main()

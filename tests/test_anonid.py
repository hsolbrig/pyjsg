# Copyright (c) 2017, Mayo Clinic
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without modification,
# are permitted provided that the following conditions are met:
#
# Redistributions of source code must retain the above copyright notice, this
#     list of conditions and the following disclaimer.
#
#     Redistributions in binary form must reproduce the above copyright notice,
#     this list of conditions and the following disclaimer in the documentation
#     and/or other materials provided with the distribution.
#
#     Neither the name of the Mayo Clinic nor the names of its contributors
#     may be used to endorse or promote products derived from this software
#     without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED.
# IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT,
# INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, 
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
# LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE
# OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED
# OF THE POSSIBILITY OF SUCH DAMAGE.

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

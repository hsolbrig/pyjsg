import unittest
from dataclasses import dataclass
from typing import cast, List, Tuple, Optional

from pyjsg.parser_impl.jsg_doc_parser import JSGDocParser
from pyjsg.parser_impl.jsg_objectexpr_parser import JSGObjectExpr
from tests.test_basics.parser import parse


@dataclass
class TestEntry:
    text: str
    name: str
    deps: List[str]
    sigs: List[str]
    membs: List[Tuple[str, str]]
    inits: List[str]

    @staticmethod
    def gen_entry(t: JSGObjectExpr, text: Optional[str]=None) -> str:
        return str(TestEntry(text if text else t.text, str(t),
                             t.dependency_list(), t.signatures(), t.members_entries(), t.initializers()))


i0 = TestEntry(text='a {}', name='objectExpr: simple object', deps=[], sigs=[], membs=[], inits=[])
i1 = TestEntry(text='a {,}', name='objectExpr: simple object', deps=[], sigs=[], membs=[], inits=[])
i2 = TestEntry(text='a {a: @int}', name='objectExpr: simple object', deps=[], sigs=['a: int = None'], 
               membs=[('a', 'jsg.Integer')], inits=['self.a = a'])
i3 = TestEntry(text='a {b: .}', name='objectExpr: simple object', deps=[], sigs=['b: object = jsg.Empty'],
               membs=[('b', "jsg.AnyTypeFactory('b', _CONTEXT)")], inits=['self.b = b'])
i4 = TestEntry(text='a {b: .? c: . d: .* e: .+ f: a}', 
               name='objectExpr: simple object', 
               deps=['a'], 
               sigs=['b: typing.Optional[object] = jsg.Empty', 'c: object = jsg.Empty',
                     'd: typing.List[object] = None',
                     'e: typing.List[object] = None', 'f: a = None'],
               membs=[('b', "typing.Optional[jsg.AnyTypeFactory('b', _CONTEXT)]"),
                      ('c', "jsg.AnyTypeFactory('c', _CONTEXT)"),
                      ('d', "jsg.ArrayFactory('d', _CONTEXT, jsg.AnyTypeFactory('d', _CONTEXT), 0, None)"),
                      ('e', "jsg.ArrayFactory('e', _CONTEXT, jsg.AnyTypeFactory('e', _CONTEXT), 1, None)"),
                      ('f', 'a')], 
               inits=['self.b = b',
                      'self.c = c',
                      "self.d = d",
                      "self.e = e",
                      'self.f = f'])
i5 = TestEntry(text='a {b: @int c:@string |, }', 
               name='objectExpr: object choices', 
               deps=['a_1_', 'a_2_'], 
               sigs=['opts_: typing.Union[a_1_, a_2_] = None'],
               membs=[('b', 'typing.Optional[jsg.Integer]'), ('c', 'typing.Optional[jsg.String]')],
               inits=['if opts_ is not None:', '    if isinstance(opts_, a_1_):', '        self.b = opts_.b',
                      '        self.c = opts_.c', '    elif isinstance(opts_, a_2_):', '        pass', '    else:',
                      '        raise ValueError(f"Unrecognized value type: {opts_}")'])
i6 = TestEntry(text='a {b: . | c: .}', 
               name='objectExpr: object choices', 
               deps=['a_1_', 'a_2_'], 
               sigs=['opts_: typing.Union[a_1_, a_2_] = None'],
               membs=[('b', "typing.Optional[jsg.AnyTypeFactory('b', _CONTEXT)]"),
                      ('c', "typing.Optional[jsg.AnyTypeFactory('c', _CONTEXT)]")],
               inits=['if opts_ is not None:', '    if isinstance(opts_, a_1_):', '        self.b = opts_.b',
                      '    elif isinstance(opts_, a_2_):', '        self.c = opts_.c', '    else:',
                      '        raise ValueError(f"Unrecognized value type: {opts_}")'])
i7 = TestEntry(text='a {b: .? c: . | d: .*, e: .+ | f: a, }', 
               name='objectExpr: object choices', 
               deps=['a_1_', 'a_2_', 'a', 'a_3_'], 
               sigs=['opts_: typing.Union[a_1_, a_2_, a_3_] = None'],
               membs=[('b', "typing.Optional[jsg.AnyTypeFactory('b', _CONTEXT)]"),
                      ('c', "typing.Optional[jsg.AnyTypeFactory('c', _CONTEXT)]"),
                      ('d',
                       "typing.Optional[jsg.ArrayFactory('d', _CONTEXT, jsg.AnyTypeFactory('d', _CONTEXT), 0, None)]"),
                      ('e',
                       "typing.Optional[jsg.ArrayFactory('e', _CONTEXT, jsg.AnyTypeFactory('e', _CONTEXT), 1, None)]"),
                      ('f', 'typing.Optional[a]')],
               inits=['if opts_ is not None:', '    if isinstance(opts_, a_1_):', '        self.b = opts_.b',
                      '        self.c = opts_.c', '    elif isinstance(opts_, a_2_):', '        self.d = opts_.d',
                      '        self.e = opts_.e', '    elif isinstance(opts_, a_3_):', '        self.f = opts_.f',
                      '    else:',
                      '        raise ValueError(f"Unrecognized value type: {opts_}")'])


o0 = TestEntry(text='{}', name='objectExpr: simple object', deps=[], sigs=[], membs=[], inits=[])
o1 = TestEntry(text='{,}', name='objectExpr: simple object', deps=[], sigs=[], membs=[], inits=[])
o2 = TestEntry(text='{a: @int}', name='objectExpr: simple object', deps=[], sigs=['a: int = None'], 
               membs=[('a', 'jsg.Integer')], inits=['self.a = a'])
o3 = TestEntry(text='{b: .}', name='objectExpr: simple object', deps=[], sigs=['b: object = jsg.Empty'],
               membs=[('b', "jsg.AnyTypeFactory('b', _CONTEXT)")], inits=['self.b = b'])
o4 = TestEntry(text='{b: .? c: . d: .* e: .+ f: a}', 
               name='objectExpr: simple object', 
               deps=['a'], 
               sigs=['b: typing.Optional[object] = jsg.Empty', 'c: object = jsg.Empty',
                     'd: typing.List[object] = None',
                     'e: typing.List[object] = None', 'f: Undefined(a) = None'],
               membs=[('b', "typing.Optional[jsg.AnyTypeFactory('b', _CONTEXT)]"),
                      ('c', "jsg.AnyTypeFactory('c', _CONTEXT)"),
                      ('d', "jsg.ArrayFactory('d', _CONTEXT, jsg.AnyTypeFactory('d', _CONTEXT), 0, None)"),
                      ('e', "jsg.ArrayFactory('e', _CONTEXT, jsg.AnyTypeFactory('e', _CONTEXT), 1, None)"),
                      ('f', 'Undefined(a)')],
               inits=['self.b = b',
                      'self.c = c',
                      "self.d = d",
                      "self.e = e",
                      'self.f = f'])
o5 = TestEntry(text='{b: @int c:@string |, }', 
               name='objectExpr: object choices', 
               deps=['_Anon1_1_', '_Anon1_2_'],
               sigs=['opts_: typing.Union[_Anon1_1_, _Anon1_2_] = None'],
               membs=[('b', 'typing.Optional[jsg.Integer]'), ('c', 'typing.Optional[jsg.String]')],
               inits=['if opts_ is not None:', '    if isinstance(opts_, _Anon1_1_):', '        self.b = opts_.b',
                      '        self.c = opts_.c', '    elif isinstance(opts_, _Anon1_2_):', '        pass', '    else:',
                      '        raise ValueError(f"Unrecognized value type: {opts_}")'])
o6 = TestEntry(text='{b: . | c: .}', 
               name='objectExpr: object choices', 
               deps=['_Anon1_1_', '_Anon1_2_'], 
               sigs=['opts_: typing.Union[_Anon1_1_, _Anon1_2_] = None'],
               membs=[('b', "typing.Optional[jsg.AnyTypeFactory('b', _CONTEXT)]"),
                      ('c', "typing.Optional[jsg.AnyTypeFactory('c', _CONTEXT)]")],
               inits=['if opts_ is not None:', '    if isinstance(opts_, _Anon1_1_):', '        self.b = opts_.b',
                      '    elif isinstance(opts_, _Anon1_2_):', '        self.c = opts_.c', '    else:',
                      '        raise ValueError(f"Unrecognized value type: {opts_}")'])
o7 = TestEntry(text='{b: .? c: . | d: .*, e: .+ | f: a, }', 
               name='objectExpr: object choices', 
               deps=['_Anon1_1_', '_Anon1_2_', 'a', '_Anon1_3_'], 
               sigs=['opts_: typing.Union[_Anon1_1_, _Anon1_2_, _Anon1_3_] = None'],
               membs=[('b', "typing.Optional[jsg.AnyTypeFactory('b', _CONTEXT)]"),
                      ('c', "typing.Optional[jsg.AnyTypeFactory('c', _CONTEXT)]"),
                      ('d',
                       "typing.Optional[jsg.ArrayFactory('d', _CONTEXT, jsg.AnyTypeFactory('d', _CONTEXT), 0, None)]"),
                      ('e',
                       "typing.Optional[jsg.ArrayFactory('e', _CONTEXT, jsg.AnyTypeFactory('e', _CONTEXT), 1, None)]"),
                      ('f', 'typing.Optional[Undefined(a)]')],
               inits=['if opts_ is not None:', '    if isinstance(opts_, _Anon1_1_):', '        self.b = opts_.b',
                      '        self.c = opts_.c', '    elif isinstance(opts_, _Anon1_2_):', '        self.d = opts_.d',
                      '        self.e = opts_.e', '    elif isinstance(opts_, _Anon1_3_):', '        self.f = opts_.f',
                      '    else:',
                      '        raise ValueError(f"Unrecognized value type: {opts_}")'])

test_entries: List[Tuple[str, TestEntry, TestEntry]] = [
    ('{}', i0, o0),
    ('{,}', i1, o1),
    ('{a: @int}', i2, o2),
    ('{b: .}', i3, o3),
    ('{b: .? c: . d: .* e: .+ f: a}', i4, o4),
    ('{b: @int c:@string |, }', i5, o5),
    ('{b: . | c: .}', i6, o6),
    ('{b: .? c: . | d: .*, e: .+ | f: a, }', i7, o7),
]


class ObjectExprParserTestCase(unittest.TestCase):
    def test_basics(self):
        d = cast(JSGDocParser, parse('a ' + test_entries[0][0], "objectDef", JSGDocParser))
        t = d._context.reference('a')
        self.assertEqual("None", t.mt_value())

        for te in test_entries:
            text = "a " + te[0]
            e = te[1]
            d = cast(JSGDocParser, parse(text, "objectDef", JSGDocParser))
            self.assertIsNotNone(d, f"Parse error: {text}")
            t = d._context.reference('a')
            self.assertEqual(e.name, str(t))
            self.assertEqual('a', t.signature_type(), text)
            self.assertEqual('a', t.python_type(), text)
            self.assertEqual(e.deps, t.dependency_list(), text)
            self.assertEqual(e.sigs, t.signatures(), text)
            self.assertEqual(e.membs, t.members_entries(), text)
            self.assertEqual(e.inits, t.initializers(), text)

    def test_anonymous_entries(self):
        for te in test_entries:
            e = te[2]
            t = cast(JSGObjectExpr, parse(te[0], "objectExpr", JSGObjectExpr))
            self.assertIsNotNone(t, f"Parse error: {e.text}")
            self.assertEqual(e.name, str(t))
            self.assertEqual('_Anon1', t.signature_type(), e.text)
            self.assertEqual('_Anon1', t.python_type(), e.text)
            self.assertEqual(e.deps, t.dependency_list(), e.text)
            self.assertEqual(e.sigs, t.signatures(), e.text)
            self.assertEqual(e.membs, t.members_entries(), e.text)
            self.assertEqual(e.inits, t.initializers(), e.text)

    def test_opt_choice_branch(self):
        text = '{id: @string |}'
        t = cast(JSGObjectExpr, parse(text, 'objectExpr', JSGObjectExpr))
        self.assertIsNotNone(t, f"Parse error")
        self.assertEqual('objectExpr: object choices', str(t))
        self.assertEqual('_Anon1', t.signature_type(), text)
        self.assertEqual('_Anon1', t.python_type(), text)
        self.assertEqual(['_Anon1_1_', '_Anon1_2_'], t.dependency_list(), text)
        self.assertEqual(['opts_: typing.Union[_Anon1_1_, _Anon1_2_] = None'], t.signatures(), text)
        self.assertEqual([('id', 'typing.Optional[jsg.String]')], t.members_entries(), text)
        self.assertEqual([
            'if opts_ is not None:',
            '    if isinstance(opts_, _Anon1_1_):',
            '        self.id = opts_.id',
            '    elif isinstance(opts_, _Anon1_2_):',
            '        pass',
            '    else:',
            '        raise ValueError(f"Unrecognized value type: {opts_}")'], t.initializers(), text)


if __name__ == '__main__':
    unittest.main()

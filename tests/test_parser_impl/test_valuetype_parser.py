import unittest
from typing import cast

from pyjsg.parser_impl.jsg_objectexpr_parser import JSGObjectExpr
from pyjsg.parser_impl.jsg_valuetype_parser import JSGValueType
from tests.test_basics.parser import parse

builtin_tests = [("@string", "jsg.String", "str", "None"),
                 ("@number", "jsg.Number", "float", "None"),
                 ("@int", "jsg.Integer", "int", "None"),
                 ("@bool", "jsg.Boolean", "bool", "None"),
                 ("@null", "jsg.JSGNull", "type(None)", "jsg.Empty"),
                 ("@array", "jsg.ArrayFactory('{name}', _CONTEXT, jsg.AnyType, 0, None)", "list", "None"),
                 ("@object", "jsg.ObjectFactory('{name}', _CONTEXT, jsg.Object)", "object", "None"),
                 (".", "jsg.AnyTypeFactory('{name}', _CONTEXT)", "object", "jsg.Empty")]

ref_tests = [("A", "ID"),
             ("a", "ID"),
             ("ABCt", "ID"),
             ("aNID", "ID"),
             ("AA", "LEXER_ID_REF"),
             ("HEX_NUM", "LEXER_ID_REF")]

constructor_tests = [
    ("@string", "jsg.String(getter('v 1', None))"),
    ("@number", "jsg.Number(getter('v 1', None))"),
    ("@int", "jsg.Integer(getter('v 1', None))"),
    ("@bool", "jsg.Boolean(getter('v 1', None))"),
    ("@null", "jsg.JSGNull(getter('v 1', None))"),
    ("@array", "Array('k', self._context, jsg.AnyType, 0, None, getter('v 1', None))"),
    ("@object", "jsg.Object('k', self._context, getter('v 1', None))"),
    (".", "jsg.AnyType('k', self._context, getter('v 1', None))")]


class ValueTypeTestCase(unittest.TestCase):
    def test_builtins(self):
        for text, sig, typ_, mt_typ in builtin_tests:
            t = cast(JSGValueType, parse(text, "valueType", JSGValueType))
            self.assertEqual(sig, t.signature_type(), text)
            self.assertEqual(typ_, t.python_type(), text)
            self.assertEqual(f"valueType: builtinValueType: {'jsg.AnyType' if text == '.' else text}", str(t), text)
            self.assertEqual(mt_typ, t.mt_value(), text)
            self.assertEqual([], t.members_entries(), text)
            self.assertEqual([], t.dependency_list(), text)

    def test_refs(self):
        for text, typ in ref_tests:
            t = cast(JSGValueType, parse(text, "valueType", JSGValueType))
            self.assertEqual(f'Undefined({text})' if typ != 'LEXER_ID_REF' else text, t.signature_type())
            self.assertEqual(f'Undefined({text})' if typ != 'LEXER_ID_REF' else 'str', t.python_type())
            self.assertEqual(f"valueType: {typ}: {text}", str(t))
            self.assertEqual([text], t.dependency_list())
            self.assertEqual([], t.members_entries())
            self.assertEqual("None", t.mt_value())

    def test_ref_escapes(self):
        self.assertEqual("Undefined(Class)", cast(JSGValueType, parse("Class", "valueType", JSGValueType))
                         .signature_type())
        t = cast(JSGValueType, parse("class", "valueType", JSGValueType))
        self.assertEqual("Undefined(class_)", t.signature_type())
        self.assertEqual("Undefined(class_)", t.python_type())
        self.assertEqual([], t.members_entries())

    def test_literals(self):
        t = cast(JSGValueType, parse("'literal'", "valueType", JSGValueType))
        self.assertEqual("_Anon1", t.signature_type())
        self.assertEqual("str", t.python_type())
        self.assertEqual("valueType: STRING: pattern: r'literal'", str(t))

    def test_any(self):
        t = cast(JSGValueType, parse("id = .;", "valueTypeMacro", JSGValueType))
        self.assertEqual("object", t.python_type())
        self.assertEqual("jsg.AnyTypeFactory('{name}', _CONTEXT)", t.signature_type())
        self.assertEqual("jsg.Empty", t.mt_value())
        self.assertEqual([], t.members_entries())
        self.assertEqual([], t.dependency_list())
        self.assertEqual("valueType: builtinValueType: jsg.AnyType", str(t))

    def test_alternatives(self):
        t = cast(JSGValueType, parse("id = ('x'|'y') ;", "valueTypeMacro", JSGValueType))
        self.assertEqual("_Anon1", t.signature_type())
        self.assertEqual("str", t.python_type())
        self.assertEqual("valueType: STRING: pattern: r'(x)|(y)'", str(t))
        t = cast(JSGValueType, parse("id = (Aa | Bb | (Cc | Dd)) ;", "valueTypeMacro", JSGValueType))
        self.assertEqual("typing.Union[Undefined(Aa), Undefined(Bb), typing.Union[Undefined(Cc), Undefined(Dd)]]",
                         t.signature_type())
        self.assertEqual("typing.Union[Undefined(Aa), Undefined(Bb), typing.Union[Undefined(Cc), Undefined(Dd)]]",
                         t.python_type())
        self.assertEqual(t.dependency_list(), ['Aa', 'Bb', 'Cc', 'Dd'])
        self.assertEqual("valueType: (Undefined(Aa) | Undefined(Bb) | typing.Union[Undefined(Cc), Undefined(Dd)])",
                         str(t))
        self.assertEqual([], t.members_entries())
        t = cast(JSGValueType, parse("id = (Aa | Bb | 'foo' | (Cc | Dd) | 'bar') ;", "valueTypeMacro", JSGValueType))
        self.assertEqual("typing.Union[_Anon1, Undefined(Aa), Undefined(Bb), "
                         "typing.Union[Undefined(Cc), Undefined(Dd)]]",
                         t.signature_type())
        self.assertEqual("typing.Union[str, Undefined(Aa), Undefined(Bb), typing.Union[Undefined(Cc), Undefined(Dd)]]",
                         t.python_type())
        self.assertEqual(['_Anon1', 'Aa', 'Bb', 'Cc', 'Dd'], t.dependency_list())
        self.assertEqual("valueType: ((STRING: pattern: r'(foo)|(bar)') | Undefined(Aa) | Undefined(Bb) | "
                         "typing.Union[Undefined(Cc), Undefined(Dd)])", str(t))

    def test_array(self):
        t = cast(JSGValueType, parse('id = [.] ;', "valueTypeMacro", JSGValueType))
        self.assertEqual('valueType: arrayExpr: [valueType: builtinValueType: jsg.AnyType]', str(t))
        self.assertEqual([], t.dependency_list())
        self.assertEqual([], t.members_entries())
        self.assertEqual('typing.List[object]', t.python_type())
        self.assertEqual("jsg.ArrayFactory('{name}', _CONTEXT, jsg.AnyTypeFactory('{name}', _CONTEXT), 0, None)",
                         t.signature_type())
        self.assertEqual('None', t.mt_value())

        t = cast(JSGValueType, parse('id = [@int | "AB*" +] ;', "valueTypeMacro", JSGValueType))
        self.assertEqual("valueType: arrayExpr: [(valueType: builtinValueType: "
                         "@int | valueType: STRING: pattern: r'AB\*')+]", str(t))
        self.assertEqual(['_Anon1'], t.dependency_list())
        self.assertEqual([], t.members_entries())
        self.assertEqual('typing.List[typing.Union[int, str]]', t.python_type())
        self.assertEqual("jsg.ArrayFactory('{name}', _CONTEXT, typing.Union[jsg.Integer, _Anon1], 1, None)",
                         t.signature_type())
        self.assertEqual('None', t.mt_value())

    def test_lexeridref(self):
        t = cast(JSGValueType, parse('("[a-z]*" | "0-9*")', "valueType", JSGValueType))
        self.assertEqual("valueType: STRING: pattern: r'(\[a\-z\]\*)|(0\-9\*)'", str(t))
        self.assertEqual("_Anon1", t.signature_type())
        self.assertEqual("str", t.python_type())
        self.assertEqual("None", t.mt_value())
        self.assertEqual([], t.members_entries())

        t = cast(JSGValueType, parse('("[a-z]*" | "0-9*" | ID)', "valueType", JSGValueType))
        self.assertEqual("valueType: ((STRING: pattern: r'(\[a\-z\]\*)|(0\-9\*)') | ID)", str(t))
        self.assertEqual("typing.Union[_Anon1, ID]", t.signature_type())
        self.assertEqual("typing.Union[str, str]", t.python_type())
        self.assertEqual("None", t.mt_value())
        self.assertEqual([], t.members_entries())

    def test_anon_typeid(self):
        t = cast(JSGValueType, parse("{a: @int b: @string+}", "valueType", JSGValueType))
        self.assertEqual('valueType: (anonymous: _Anon1): objectExpr: simple object', str(t))
        self.assertEqual('_Anon1', t.signature_type())
        self.assertEqual('_Anon1', t.python_type())
        self.assertEqual('None', t.mt_value())
        self.assertEqual([], t.members_entries())

    def test_objectmacro_opts(self):
        t = cast(JSGValueType, parse("a = @string | KT | {} ;", "valueTypeMacro", JSGValueType))
        self.assertEqual('valueType: (jsg.String | KT | _Anon1)', str(t))
        self.assertEqual('typing.Union[jsg.String, KT, _Anon1]', t.signature_type())
        self.assertEqual('typing.Union[str, str, _Anon1]', t.python_type())
        self.assertEqual('None', t.mt_value())
        self.assertEqual([], t.members_entries())

    def test_objectmacro(self):
        t = cast(JSGObjectExpr, parse("stringFacet = (length minlength maxlength):"
                                      "INTEGER pattern:STRING flags:STRING? ;", "objectMacro", JSGObjectExpr))
        self.assertEqual("""class stringFacet(jsg.JSGObject):
    _reference_types = []
    _members = {'length': INTEGER,
                'minlength': INTEGER,
                'maxlength': INTEGER,
                'pattern': STRING,
                'flags': typing.Optional[STRING]}
    _strict = True

    def __init__(self,
                 length: str = None,
                 minlength: str = None,
                 maxlength: str = None,
                 pattern: str = None,
                 flags: typing.Optional[str] = None,
                 **_kwargs: typing.Dict[str, object]):
        super().__init__(_CONTEXT, **_kwargs)
        self.length = length
        self.minlength = minlength
        self.maxlength = maxlength
        self.pattern = pattern
        self.flags = flags""", t.as_python('stringFacet').strip())
        self.assertEqual(['INTEGER', 'STRING'], t.dependency_list())

        t = cast(JSGObjectExpr, parse("stringFacet = (length minlength maxlength):INTEGER "
                                      "pattern:STRING | flags:STRING? ;", "objectMacro", JSGObjectExpr))
        self.assertEqual("""class stringFacet(jsg.JSGObject):
    _reference_types = [_Anon1_1_, _Anon1_2_]
    _members = {'length': typing.Optional[INTEGER],
                'minlength': typing.Optional[INTEGER],
                'maxlength': typing.Optional[INTEGER],
                'pattern': typing.Optional[STRING],
                'flags': typing.Optional[STRING]}
    _strict = True

    def __init__(self,
                 opts_: typing.Union[_Anon1_1_, _Anon1_2_] = None,
                 **_kwargs: typing.Dict[str, object]):
        super().__init__(_CONTEXT, **_kwargs)
        if opts_ is not None:
            if isinstance(opts_, _Anon1_1_):
                self.length = opts_.length
                self.minlength = opts_.minlength
                self.maxlength = opts_.maxlength
                self.pattern = opts_.pattern
            elif isinstance(opts_, _Anon1_2_):
                self.flags = opts_.flags
            else:
                raise ValueError(f"Unrecognized value type: {opts_}")""", t.as_python('stringFacet').strip())
        self.assertEqual(['INTEGER', 'STRING', '_Anon1_1_', '_Anon1_2_'], t.dependency_list())

        t = cast(JSGObjectExpr, parse("x = a:@number | b:@null | ;", "objectMacro", JSGObjectExpr))
        self.assertEqual("""class stringFacet(jsg.JSGObject):
    _reference_types = [_Anon1_1_, _Anon1_2_, _Anon1_3_]
    _members = {'a': typing.Optional[jsg.Number],
                'b': typing.Optional[jsg.JSGNull]}
    _strict = True

    def __init__(self,
                 opts_: typing.Union[_Anon1_1_, _Anon1_2_, _Anon1_3_] = None,
                 **_kwargs: typing.Dict[str, object]):
        super().__init__(_CONTEXT, **_kwargs)
        if opts_ is not None:
            if isinstance(opts_, _Anon1_1_):
                self.a = opts_.a
            elif isinstance(opts_, _Anon1_2_):
                self.b = opts_.b
            elif isinstance(opts_, _Anon1_3_):
                pass
            else:
                raise ValueError(f"Unrecognized value type: {opts_}")""",
                         t.as_python('stringFacet').strip())
        self.assertEqual(['_Anon1_1_', '_Anon1_2_', '_Anon1_3_'], t.dependency_list())


if __name__ == '__main__':
    unittest.main()

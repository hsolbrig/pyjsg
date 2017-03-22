# PyJSG -- JSON Schema Grammar Bindings for Python
Translate [JSON Schema Grammar](http://github.com/ericprud/jsglib) into Python objects.

This tool generates Python 3 objects that represent the JSON objects defined in a JSG schema.  It uses the [Python Typing library](https://docs.python.org/3/library/typing.html) to add type hints to Python IDE's and includes a library to validate the python objects against the library definitions.

## Examples

<table><thead>
<tr><th>JSON Grammar</th><th>Python Objects</th><th></th></tr>
</thead><tbody>
<tr><td><pre>doc { status:"ready" }</pre></td><td><pre>
class doc(JSGObject):
    def __init__(self,
                 status: str = None,
                 **_extra: Dict[str, object]):
        JSGObject.__init__(self, _CONTEXT, **_extra)
        self.status = "ready"
</td></tr>
<tr><td><pre>doc { street:NAME no:NUM }
NAME : .*;
NUM : [0-9]+[a-e]?;</pre></td><td><pre>
class NAME(JSGString):
    pattern = JSGPattern(r'.*')<br/>


class NUM(JSGString):
    pattern = JSGPattern(r'[0-9]+[a-e]?')

class doc(JSGObject):
    def __init__(self,
                 street: NAME = None,
                 no: NUM = None,
                 **_extra: Dict[str, object]):
        JSGObject.__init__(self, _CONTEXT, **_extra)
        self.street = street
        self.no = no</pre></td></tr>
<tr><td><pre>doc { street:(NAME|"*"|TEMPLATE) }
NAME : .*;
TEMPLATE : '{' .* '}';</pre></td><td><pre>class _A1(JSGString):
    pattern = JSGPattern(r'\*')<br/>


class NAME(JSGString):
    pattern = JSGPattern(r'.*')


class TEMPLATE(JSGString):
    pattern = JSGPattern(r'\{.*\}')

class doc(JSGObject):
    def __init__(self,
                 street: Union[_A1, NAME, TEMPLATE] = None,
                 **_extra: Dict[str, object]):
        JSGObject.__init__(self, _CONTEXT, **_extra)
        self.street = street</pre></td></tr>
<tr><td><pre>doc { street:nameOrTemplate }
nameOrTemplate = NAME | "*" | TEMPLATE ;
NAME : .*;
TEMPLATE : '{' .* '}';</pre></td><td>(invalid)</td></tr>
<tr><td><pre>doc { street:[(NAME | "*" | TEMPLATE){2,}] }
NAME : .*;
TEMPLATE : '{' .* '}';</pre></td><td><pre>class _A1(JSGString):
    pattern = JSGPattern(r'\*')<br/>


class NAME(JSGString):
    pattern = JSGPattern(r'.*')


class TEMPLATE(JSGString):
    pattern = JSGPattern(r'\{.*\}'<br/>

class doc(JSGObject):
    def __init__(self,
                 street: List[Union[_A1, NAME, TEMPLATE]] = None,
                 **_extra: Dict[str, object]):
        JSGObject.__init__(self, _CONTEXT, **_extra)
        self.street = street</pre></td></tr>
</tbody></table>
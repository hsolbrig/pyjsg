# JSON Schema Grammar
## A JSG definition consists of three sections:
1) Directives -- `.TYPE` and `.IGNORE` directives
2) Definitions -- JSON Object and Arrary definitions
3) Lexical Rules -- string and number matching rules


## Directives
### .TYPE directive
The `.TYPE` directive:
1) Identifies a single property that names the JSG production type of a JSON object
2) (Optionally) lists one or more production types that do not use the `.TYPE` discriminator

#### Syntax
  `.TYPE` \<type\> [`-` \<type\> [\<type\> ...]] `;`

| JSG | JSON | result |
| --- | ---- | ------ |
| doc { a:. } | {"a":"hello"} | pass |
| | {"type": "doc", "a":"hello"} | fail |
| .TYPE type; doc {a:.} | {"type": "doc", "a":"hello"} | pass |
| | {"type": "doc", "a":{"a":0}} | fail |
| | {"a":"hello"} | (depends on context) |

### .IGNORE directive
The `.IGNORE` directive identifies a list of properties to globally ignore.

#### Syntax
  `.IGNORE` \<type\> \[\<type\> ...] `;`
  
#### Examples

| JSG | JSON | result |
| --- | ---- | ------ |
| doc {a:@string} | {"a":"hello"} | pass |
| | {"id": "doc", "a":"hello"} | fail |
| .IGNORE id, idx; doc {a:@string} | {"id": "doc", "a":"hello", "idx":243} | pass |
| | {"id": "doc", "a":"hello", "foo":243} | fail |

## Definitions
A JSG definition consists of the definition name followed by the definition enclosed in curly braces (`{` ... `}`) 

| JSG | Description |
| --- | ----------- |
| \<identifier\> `:` \<valueType\> [\<cardinality\>] | \<identifier\> is any valid JSON string, with the exception that the enclosing quotes can be double (`"`), single (`'`) or omitted completely if the string consists solely of a-z, A-Z, 0-9 and @ characters. |


### Value Type
| Type | Description | Example |
| ---- | ----------- | ------- |
| \<quoted string\> | Fixed value | doc {a:"hello"} |
| \<builtin type\> | Builtin JSON type (w/ extensions). Possible values are:<br/><br/>@string   : JSON `string` <br/>@number : JSON `number`<br/>@int : JSON `number` without `.`, `e` or `E` characters<br/>@bool: `true` or `false`<br/>@null : `null`<br/>@array : a JSON `array` (`[` ... `]`)<br/>@object : a JSON `object` ( `{` ... `}`) | doc {a:@number}
| \<any\> | Any JSON type.  Represented by a single dot (`.`) | doc {a: .} |
| \<pattern reference\> | The name of a lexical pattern defined in the Lexical Rules | doc {a: HEX4 }<br/><br/>@terminals<br/>HEX4: HEX HEX HEX HEX<br/>HEX : [0-9] | [A-F] | [a-f] ; |
| \<identifier reference\>| A reference to a JSG definition.  | person {legal: name, alt: alias }<br/>name {first: @string, last: @string}<br/>alias [name] |
| (empty) | An empty object. | doc {} |
| \<sequence\> | 
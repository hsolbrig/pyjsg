// Grammar for jsg files
// Derived from https://github.com/ericprud/jsglib/blob/master/doc/jsglib.bnf

parser grammar jsgParser;

options {tokenVocab = jsgLexer; }

doc					: typeDirective? ignoreDirective* grammarElt* lexerRules? EOF ;
typeDirective       : TYPE name typeExceptions? SEMI ;
typeExceptions      : DASH idref+ ;
ignoreDirective	    : IGNORE name* SEMI ;                          // references to objects, arrays

grammarElt			: objectDef
                    | arrayDef
                    | objectMacro
                    | valueTypeMacro
                    ;

// JSON object definition
objectDef			: ID objectExpr ;
objectExpr			: OBRACE membersDef? CBRACE
					| OBRACE (LEXER_ID_REF | ANY)? MAPSTO valueType ebnfSuffix? CBRACE
					;

// JSON object members
membersDef          : COMMA
                    | member+ (BAR altMemberDef)* (BAR lastComma)? ;
altMemberDef        : member* ;
member              : pairDef COMMA? ;
lastComma           : COMMA ;


// JSON pair definition
pairDef     		: name COLON valueType ebnfSuffix?                  // name : value [cardinality]
                    | idref ebnfSuffix?                                 // Must reference an objectDef or objectMacro
					| OPREN name+ CPREN COLON valueType ebnfSuffix?     // shorthand for above
					;
name                : ID|STRING ;


// JSON array definition
arrayDef			: ID arrayExpr ;
arrayExpr			: OBRACKET valueType (BAR valueType)* ebnfSuffix? CBRACKET;

// Substitution parameters
objectMacro         : ID EQUALS membersDef SEMI;
valueTypeMacro      : ID EQUALS nonRefValueType (BAR nonRefValueType)* SEMI;

builtinValueType    : JSON_STRING
                    | JSON_NUMBER
                    | JSON_INT
                    | JSON_BOOL
                    | JSON_NULL
                    | JSON_ARRAY
                    | JSON_OBJECT
                    | ANY
                    ;
valueType  		    : idref                             // reference to objectDef, arrayDef or valueTypeMacro
                    | nonRefValueType
                    ;
nonRefValueType  	: LEXER_ID_REF                      // string / number / bool constraint
					| STRING                            // fixed value string
					| builtinValueType                  // builtin json type
					| objectExpr                        // unnamed objectDef
					| arrayExpr                         // unnamed arrayDef
					| OPREN typeAlternatives CPREN      // choice of any of the above
					;
typeAlternatives    : valueType (BAR valueType)+ ;

idref               : ID ;

// Cardinality -- {n} == {n,n}, {n,} == {n,*}
ebnfSuffix          : QMARK
					| STAR
					| PLUS
					| OBRACE INT (COMMA (INT|STAR)?)? CBRACE
					;


// JSON string / number / bool / null constraints
lexerRules          : TERMINALS lexerRuleSpec* ;
lexerRuleSpec		: LEXER_ID COLON lexerRuleBlock SEMI ;
lexerRuleBlock   	: lexerAltList (builtinValueType)? ;
lexerAltList     	: lexerAlt (BAR lexerAlt)* ;
lexerAlt         	: lexerElements | ;
lexerElements    	: lexerElement+ ;
lexerElement     	: lexerAtom ebnfSuffix?
					| lexerBlock ebnfSuffix?
					;
lexerBlock       	: OPREN lexerAltList CPREN ;
lexerAtom        	: lexerTerminal
					| LEXER_CHAR_SET
					| ANY
					;
lexerTerminal       : LEXER_ID
					| STRING
					;


lexer grammar jsgLexer;

// A LEXER_ID consists of a cap letter followed by one or more caps digits and underscore
LEXER_ID_REF                 : LEXER_ID_START_CHAR LEXER_ID_CHAR+ ;
fragment LEXER_ID_START_CHAR : [A-Z] ;
fragment LEXER_ID_CHAR       : LEXER_ID_START_CHAR | [0-9_] ;

// AN ID must contain at least one ID_CHAR
ID                      : (ID_START_CHAR ANY_CHAR*) | LEXER_ID_START_CHAR | (LEXER_ID_START_CHAR LEXER_ID_CHAR* ID_CHAR ANY_CHAR*) ;
fragment ID_START_CHAR	: [a-z] | [\u00C0-\u00D6] | [\u00D8-\u00F6] | [\u00F8-\u02FF] | [\u0370-\u037D] |
					  	  [\u037F-\u1FFF] | [\u200C-\u200D] | [\u2070-\u218F] | [\u2C00-\u2FEF] |
					  	  [\u3001-\uD7FF] | [\uF900-\uFDCF] | [\uFDF0-\uFFFD];	// ignores | [\u10000-\uEFFFF] ;

fragment ID_CHAR	    : ID_START_CHAR | [\u00B7] | [\u0300-\u036F] | [\u203F-\u2040] ;
fragment ANY_CHAR       : ID_CHAR | LEXER_ID_CHAR ;


STRING      : '"' (~["] | '\\"')+ '"'
            | '\'' (~['] | '\u005c\u0039')+ '\'' ;

INT         : [0-9]+ ;
ANY         : '.' ;

TERMINALS   : '@terminals' -> mode(LEXER) ;
TYPE        : '.TYPE' ;
IGNORE      : '.IGNORE' ;
MAPSTO      : '->' ;

JSON_STRING : '@string' ;
JSON_NUMBER : '@number' ;
JSON_INT    : '@int' ;
JSON_BOOL   : '@bool' ;
JSON_NULL   : '@null' ;
JSON_ARRAY  : '@array' ;
JSON_OBJECT : '@object' ;


OBRACKET: '[' ;
CBRACKET: ']' ;
SEMI    : ';' ;
DASH    : '-' ;
OBRACE  : '{' ;
CBRACE  : '}' ;
COMMA   : ',' ;
STAR    : '*' ;
QMARK   : '?' ;
PLUS    : '+' ;
OPREN   : '(' ;
CPREN   : ')' ;
BAR     : '|' ;
COLON   : ':' ;
EQUALS  : '=' ;


PASS		: [ \t\r\n]+ -> skip;
COMMENT		: '#' ~[\r\n]* -> skip;


mode LEXER ;

LEXER_ID                     : LEXER_ID_S_CHAR LEXER_ID_C+ ;
fragment LEXER_ID_S_CHAR     : [A-Z] ;
fragment LEXER_ID_C          : LEXER_ID_START_CHAR | [0-9_] ;

LEXER_JSON_STRING : '@string' -> type(JSON_STRING);
LEXER_JSON_NUMBER : '@number' -> type(JSON_NUMBER);
LEXER_JSON_INT    : '@int'    -> type(JSON_INT);
LEXER_JSON_BOOL   : '@bool'   -> type(JSON_BOOL);
LEXER_JSON_NULL   : '@null'   -> type(JSON_NULL);
LEXER_JSON_ARRAY  : '@array'  -> type(JSON_ARRAY);
LEXER_JSON_OBJECT : '@object' -> type(JSON_OBJECT);

LEXER_SEMI    : ';' -> type(SEMI);
LEXER_DASH    : '-' -> type(DASH);
LEXER_OBRACE  : '{' -> type(OBRACE);
LEXER_CBRACE  : '}' -> type(CBRACE);
LEXER_COMMA   : ',' -> type(COMMA);
LEXER_STAR    : '*' -> type(STAR);
LEXER_QMARK   : '?' -> type(QMARK);
LEXER_PLUS    : '+' -> type(PLUS);
LEXER_OPREN   : '(' -> type(OPREN);
LEXER_CPREN   : ')' -> type(CPREN);
LEXER_COLON   : ':' -> type(COLON);
LEXER_BAR     : '|' -> type(BAR);

LEXER_STRING    : ('"' (~["] | '\\"')+ '"'
                | '\'' (~['] | '\u005c\u0039')+ '\'') -> type(STRING) ;
LEXER_ANY       : '.' -> type(ANY);
LEXER_CHAR_SET  : '['  (~[\]] | '\\]')+ ']';
LEXER_INT       : [0-9]+ -> type(INT);


LEXER_PASS		: [ \t\r\n]+ -> skip;
LEXER_COMMENT	: '#' ~[\r\n]* -> skip;

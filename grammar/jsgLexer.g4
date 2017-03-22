lexer grammar jsgLexer;


// Default mode - directive / grammardef
TYPE						: '.TYPE' ;
IGNORE						: '.IGNORE' ;
ID							: NAME_START_CHAR NAME_CHAR*;
fragment NAME_CHAR			: NAME_START_CHAR | [0-9] | '_' | [\u00B7] | [\u0300-\u036F] | [\u203F-\u2040] ;
fragment NAME_START_CHAR	: [A-Z] | [a-z] | [\u00C0-\u00D6] | [\u00D8-\u00F6] | [\u00F8-\u02FF] | [\u0370-\u037D] |
					  		  [\u037F-\u1FFF] | [\u200C-\u200D] | [\u2070-\u218F] | [\u2C00-\u2FEF] |
					  		  [\u3001-\uD7FF] | [\uF900-\uFDCF] | [\uFDF0-\uFFFD];	// ignores | [\u10000-\uEFFFF] ;

OBRACE		: '{' -> pushMode(NONLEX);
OBRACKET	: '[' -> pushMode(NONLEX);
EQUALS 		: '=' -> pushMode(NONLEX);
COLON		: ':' -> pushMode(LEXERRULE);
DASH		: '-' ;
SEMI		: ';' ;

PASS		: [ \t\r\n]+ -> skip;
COMMENT		: '#' ~[\r\n]* -> skip;

// Any mode except a lex rule
mode NONLEX;
ID1			: NAME_START_CHAR NAME_CHAR* -> type(ID);
STRING      : '"' (~["] | '\\\"')+ '"'
              | '\'' (~['] | '\u005c\u0039')+ '\'' ;

INT         : [0-9]+ ;

OBRACE1		: '{' -> pushMode(NONLEX), type(OBRACE);
OBRACKET1	: '[' -> pushMode(NONLEX), type(OBRACKET);
EQUALS1		: '=' -> type(EQUALS);
COLON1		: ':' -> type(COLON);

CBRACE		: '}' -> popMode;
CBRACKET    : ']' -> popMode, type(CBRACKET);
SEMI1		: ';' -> popMode, type(SEMI);
DASH1		: '-' -> type(DASH);
OPREN		: '(' ;
CPREN	    : ')' ;

ARROW		: '->' ;
STAR        : '*' ;
QMARK		: '?' ;
DOT			: '.' ;
PLUS		: '+' ;
COMMA		: ',' ;
BAR			: '|' ;


PASS1		: [ \t\r\n]+ -> skip;
COMMENT1	: '#' ~[\r\n]* -> skip;


mode LEXERRULE;
LEXER_ID	: NAME_START_CHAR NAME_CHAR* ;
LEXER_STRING : ('"' (~["] | '\\\"')+ '"'
             | '\'' (~['] | '\u005c\u0039')+ '\'') ;
LBAR		: '|';
LSTAR       : '*';
LQMARK		: '?';
LDOT		: '.';
LPLUS		: '+';
LOPREN		: '(';
LCPREN	    : ')';
LCOMMA		: ',';
LOBRACE     : '{';
LCBRACE     : '}';
LSEMI		: ';' -> popMode;
LINT		: [0-9]+;
LEXER_CHAR_SET : '[' (~[\]] | '\\]')+ ']';

LPASS		: [ \t\r\n]+ -> skip;
LCOMMENT	: '#' ~[\r\n]* -> skip;

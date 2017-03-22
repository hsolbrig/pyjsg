// Grammar for jsg files
// Derived from https://github.com/ericprud/jsglib/blob/master/doc/jsglib.bnf

parser grammar jsgParser;

options {tokenVocab = jsgLexer; }


doc					: directive* grammarElt* EOF ;
directive			: '.TYPE' ID (DASH typeExceptions)? SEMI    #typeDirective
					| '.IGNORE' ID* SEMI                        #ignoreDirective
					;
typeExceptions      : ID+ ;
grammarElt			: objectDef
                    | arrayDef
                    | nonObject
                    | lexerRuleSpec
                    ;
objectDef			: ID objectExpr ;
objectExpr			: OBRACE objectExprDef? CBRACE               #objectExprObj
					| OBRACE ID '->' propertyType CBRACE         #objectExprMap
					;
objectExprDef       : particle+ (BAR particleOpt)* ;
particleOpt         : particle* ;
arrayDef			: ID arrayExpr ;
arrayExpr			: '[' propertyType (BAR propertyType)* ebnfSuffix? ']' ;
particle			: ID ebnfSuffix? COMMA?
					| propertyOrGroup COMMA?
					;
propertyOrGroup		: (ID|STRING) COLON propertyType ebnfSuffix?                  #propertyOrGroupSimple
					| OPREN ID (BAR ID)+ CPREN COLON propertyType ebnfSuffix?     #propertyOrGroupShorthand
					| OPREN propertyOrGroupList (BAR propertyOrGroupList)+ CPREN  #propertyOrGroupChoice
					;
propertyOrGroupList : propertyOrGroup+ ;
propertyType		: ID                            #propertyTypeID
					| STRING                        #propertyTypeSTRING
					| objectExpr                    #propertyTypeObjectExpr
					| arrayExpr                     #propertyTypeArrayExpr
					| OPREN typeAlternatives CPREN  #propertyTypeChoice
					| DOT                           #propertyTypeAny
					;
typeAlternatives	: (ID|STRING) (BAR (ID|STRING))+ ;
nonObject			: ID EQUALS objectExprDef SEMI ;

ebnfSuffix			: QMARK
					| STAR
					| PLUS
					| OBRACE INT (COMMA (INT|STAR)?)? CBRACE
					;

// lexer rules from https://github.com/antlr/grammars-v4/raw/master/antlr4/ANTLRv4Parser.g4
lexerRuleSpec		: ID COLON lexerRuleBlock LSEMI ;
lexerebnf			: LQMARK
					| LSTAR
					| LPLUS
					| LOBRACE LINT (LCOMMA (LINT|LSTAR)?)? LCBRACE
					;
lexerRuleBlock   	: lexerAltList ;
lexerAltList     	: lexerAlt (LBAR lexerAlt)* ;
lexerAlt         	: lexerElements | ;
lexerElements    	: lexerElement+ ;
lexerElement     	: lexerAtom lexerebnf?
					| lexerBlock lexerebnf?
					;
lexerBlock       	: LOPREN lexerAltList LCPREN ;
lexerAtom        	: terminal              #lexerAtomTerminal
					| LEXER_CHAR_SET        #lexerAtomCharSet
					| LDOT                  #lexerAtomDot
					;
terminal         	: LEXER_ID              #lexerTerminalID
					| LEXER_STRING          #lexerTerminalString
					;

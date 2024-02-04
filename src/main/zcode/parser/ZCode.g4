grammar ZCode;

@lexer::header {
from lexererr import *
}

options {
	language=Python3;
}

program: other* mainfunc other* EOF;
other: funcdecl | stmt ;
valdecl: (TYPE | DYNAMIC) ID arraydecl?| (TYPE | IMPLIKEYS) ID arraydecl? ASSIGN allexp;
mainfunc: FUNC MAIN LB RB NEWLINE* funcblock;
funcdecl: FUNC ID LB paramlist RB funcblock;
funcblock: NEWLINE* BEGIN NEWLINE+ stmtlist END NEWLINE+ | stmt;

//Statements
stmts: ;
stmt: (valdecl | assignstmt | funcall | exp | RETURN allexp) NEWLINE+ | ifstmt;
stmtblock: funcblock | NEWLINE* ;
stmtlist: stmt stmtlist | stmt | ;

assignstmt: (ID | indexp) ASSIGN allexp ;

//ifstmt
ifstmt:;

// ifblock: LB allexp RB funcblock;
// elseblk: ELSE funcblock | ;
// elifblk: elifblk_0 elifblk | elifblk_0 | ;
// elifblk_0: ELIF ifblock;
//forstmt
forstmt: FOR (ID | NUMLIT) UNTIL logicexp BY exp loopblock ;
loopblock: BEGIN NEWLINE+ (stmtlist (loopkey NEWLINE+)? ) END NEWLINE+ | stmt;
loopkey: BREAK | CONTINUE;

//Array
arraydecl: LS NUMLIT (COMMA NUMLIT)* RS;
funcall: ID LB explist RB;
paramcall: (exp) (COMMA (exp))*;
paramlist: params (COMMA params)* | ;
params: TYPE ID ; //Parameter

TYPE: NUMBER | STRING | BOOL;
IMPLIKEYS: VAR | DYNAMIC;
//Expressions
allexp: exp | relatexp | stringexp;
exp: exp_01 NUMOP exp | exp_01;
exp_01: ariexp | expall | array | LB exp RB;
exp_00: NUMLIT | STRINGLIT | BOOLIT;
expall: ID | indexp | funcall;

array: LS explist RS;
explist: explist_1| explist_2 | explist_3 ;
explist_1: NUMLIT COMMA explist_1 | NUMLIT | expall;
explist_2: STRINGLIT COMMA explist_2 | STRINGLIT | expall;
explist_3: BOOLIT COMMA explist_3 | BOOLIT | expall;

//Index operators

indexp: ID LS indop RS;
indop: indop (COMMA indop) | indop_0;
indop_0: indop_0 NUMOP indop_1 | indop_1;
indop_1: NUMLIT | ariexp | expall;

NUMOP: PLUS | STAR | PERCENT | MINUS | SLASH;

//Arithmetic operators
ariexp: ariexp_00 NUMOP ariexp | MINUS ariexp | ariexp_00;
ariexp_00: NUMLIT | expall | LB ariexp RB;

//Relation operators
relatexp: LB relatexp_00 RB | relatexp_00;
relatexp_00: exp NUMRELAOPS exp | relatexp_01 EQUALITY relatexp_01 ;
relatexp_01: STRINGLIT | expall;
NUMRELAOPS: EQUAL | LESSTHAN | LESSEQUAL | MOREEQUAL | MORETHAN | INEQUAL;

//Logic operators
logicexp:
		logicexp LOGICOPBIN logicexp_00 | logicexp_00 | NOT logicexp;
logicexp_00: BOOLIT | relatexp | expall;
LOGICOPBIN: AND | OR;
//string op

stringexp: stringexp_00 ELLIPSIS stringexp_00 ;
stringexp_00: STRINGLIT | expall;

//LITERALS
fragment SUBSTR: ('\'"' .*? '\'"');
STRINGLIT: 
	'"' (~('\'' | '"')| SUBSTR)*? '"' 
	{self.text = self.text[1:-1]};
NUMLIT: INTERGER EXPONENT? | INTERGER DECIMAL EXPONENT?;
fragment INTERGER: ( '0' | [1-9] ) [0-9]*;
fragment DECIMAL: '.' [0-9]*;
fragment EXPONENT: ('e' | 'E') ('-' | '+')? [0-9]*;
BOOLIT: TRUE | FALSE;

//Keywords
TRUE: 'true';
FALSE: 'false';
NUMBER: 'number';
BOOL: 'bool';
STRING: 'string';
RETURN: 'return';
VAR: 'var';
DYNAMIC: 'dynamic';
FUNC: 'func';
FOR: 'for';
UNTIL: 'until';
BY: 'by';
BREAK: 'break';
CONTINUE: 'continue';
IF: 'if';
ELIF: 'elif';
ELSE: 'else';
BEGIN: 'begin';
END: 'end';
MAIN: 'main';

//Operators
PLUS: '+';
MINUS: '-';
STAR: '*';
SLASH: '/';
PERCENT: '%';
NOT: 'not';	//keyword
AND: 'and'; //keyword
OR: 'or'; //keyword
EQUAL: '=';
ASSIGN: '<-';
INEQUAL: '!=';
LESSTHAN: '<';
LESSEQUAL: '<=';
MORETHAN: '>';
MOREEQUAL: '>=';
ELLIPSIS: '...';
EQUALITY: '==';
LB: '(';
RB: ')';
LC: '{';
RC: '}';
LS: '[';
RS: ']';
COMMA: ',';

COMMENT: '#' '#' (.)*? ('\r' | EOF );
ID: ('_' | [a-zA-Z]) ('_' | [a-zA-Z0-9])*;
NEWLINE: '\r'? '\n';
WS : [ \t]+ -> skip ; // skip spaces, tabs
ERROR_CHAR: . {raise ErrorToken(self.text)};
UNCLOSE_STRING:
	'"' (~'"' | '\'"')* EOF {self.text = self.text.replace("\"",""); raise UncloseString(self.text)};
ILLEGAL_ESCAPE:
	'"' (.)* (ES) (.)* ('"' | EOF) {
					self.text = self.text.replace("\"", "")
					pos = self.text.find("\\") + 2
					self.text = self.text[0:pos:]; raise IllegalEscape(self.text)};
ES: '\\' ~('b' | 't' | 'r' | 'n' | 'f' | '\'' | '\\');
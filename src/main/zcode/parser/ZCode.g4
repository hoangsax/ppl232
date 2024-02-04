grammar ZCode;

@lexer::header {
from lexererr import *
}

options {
	language=Python3;
}

program: (other)* mainfunc other* EOF;
main: mainfunc;
other: funcdecl | valdecl | stmt ;
mainblock: '\\r' BEGIN '\\r' stmt* (RETURN exp)? '\\r' END '\\r' | RETURN exp | ;
valdecl: (TYPE | DYNAMIC) ID array? | (TYPE | IMPLIKEYS) ID array? ASSIGN exp;
mainfunc: FUNC MAIN LB RB funcblock;
funcdecl: FUNC ID LB paramlist RB funcblock;
funcblock: BEGIN stmt* END | RETURN exp ;

//Statements
stmts: ;
stmt: valdecl | assignstmt | funcall | exp | ifstmt | RETURN exp;
stmtblock: BEGIN (stmt)* END | stmt | ;

assignstmt: (ID | indexp) ASSIGN exp ;

//ifstmt
ifstmt: IF ifblock elifblk* elseblk?;

ifblock: LB exp RB stmtblock;
elseblk: ELSE stmtblock;
elifblk: ELIF ifblock;
//forstmt
forstmt: FOR (ID | NUMLIT) UNTIL logicexp BY exp loopblock ;
loopblock: BEGIN (stmt+ loopkey?)? END | stmt;
loopkey: BREAK | CONTINUE;

//Array
array: LS NUMLIT (COMMA NUMLIT)* RS;
funcall: ID LB exp? RB;
paramcall: (exp) (COMMA (exp))*;
paramlist: params (COMMA params)* | ;
params: TYPE ID ; //Parameter

TYPE: NUMBER | STRING | BOOL;
IMPLIKEYS: VAR | DYNAMIC;
//Expressions
exp: exp NUMOP exp_01 | exp_01 ;
exp_01: ariexp | logicexp | relatexp | expall | STRINGLIT | LB exp_01 RB;
exp_00: NUMLIT | STRINGLIT | BOOLIT;
expall: ID | indexp | funcall;

//Index operators

indexp: ID LS indop RS;
indop: indop NUMOP indop_1 | indop_1;
indop_1: NUMLIT | ariexp | expall;

NUMOP: PLUS | STAR | PERCENT | MINUS;

//Arithmetic operators
ariexp: ariexp_00 NUMOP ariexp | MINUS ariexp | ariexp_00;
ariexp_00: NUMLIT | expall;

//Logic operators
logicexp:
		logicexp LOGICOPBIN logicexp_00 | logicexp_00 | NOT logicexp;
logicexp_00: BOOLIT | relatexp | expall;
LOGICOPBIN: AND | OR;

//Relation operators
relatexp: relatexp_00 NUMRELAOPS relatexp_00 | relatexp_01 EQUALITY relatexp_01 ;
relatexp_00: NUMLIT | expall;
relatexp_01: STRINGLIT | expall;
NUMRELAOPS: EQUAL | INEQUAL | LESSTHAN | LESSEQUAL | MOREEQUAL | MORETHAN;

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

WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines
ERROR_CHAR: . {raise ErrorToken(self.text)};
UNCLOSE_STRING:
	'"' (~'"' | '\'"')* EOF {self.text = self.text.replace("\"",""); raise UncloseString(self.text)};
ILLEGAL_ESCAPE:
	'"' (.)* (ES) (.)* ('"' | EOF) {
					self.text = self.text.replace("\"", "")
					pos = self.text.find("\\") + 2
					self.text = self.text[0:pos:]; raise IllegalEscape(self.text)};
ES: '\\' ~('b' | 't' | 'r' | 'n' | 'f' | '\'' | '\\');
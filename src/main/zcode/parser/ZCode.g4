grammar ZCode;

@lexer::header {
from lexererr import *
}

options {
	language=Python3;
}

program: (other)* mainfunc other* EOF;
other: funcdecl | valdecl NEWLINE+ | stmt ;
valdecl: (TYPE | DYNAMIC) ID arraydecl?| (TYPE | IMPLIKEYS) ID arraydecl? ASSIGN exp;
mainfunc: FUNC MAIN LB RB funcblock;
funcdecl: FUNC ID LB paramlist RB funcblock;
funcblock: NEWLINE* BEGIN NEWLINE+ stmtlist END NEWLINE+ | stmt;

//Statements
stmts: ;
stmt: (valdecl | assignstmt | funcall | exp | ifstmt | RETURN exp) NEWLINE+;
stmtblock: BEGIN stmtlist END | stmt | ;
stmtlist: stmt stmtlist | stmt | ;

assignstmt: (ID | indexp) ASSIGN exp ;

//ifstmt
ifstmt: IF ifblock elifblk elseblk;

ifblock: LB exp RB stmtblock;
elseblk: ELSE stmtblock | ;
elifblk: elifblk_0 elifblk | elifblk_0 | ;
elifblk_0: ELIF ifblock;
//forstmt
forstmt: FOR (ID | NUMLIT) UNTIL logicexp BY exp loopblock ;
loopblock: BEGIN (stmt+ (loopkey NEWLINE+)? )? END | stmt;
loopkey: BREAK | CONTINUE;

//Array
arraydecl: LS NUMLIT (COMMA NUMLIT)* RS;
funcall: ID LB exp? RB;
paramcall: (exp) (COMMA (exp))*;
paramlist: params (COMMA params)* | ;
params: TYPE ID ; //Parameter

TYPE: NUMBER | STRING | BOOL;
IMPLIKEYS: VAR | DYNAMIC;
//Expressions
exp: exp NUMOP exp_01 | exp_01 ;
exp_01: ariexp | logicexp | relatexp | expall | array | STRINGLIT | LB exp_01 RB;
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
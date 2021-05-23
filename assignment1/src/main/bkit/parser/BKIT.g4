//StudentID: 1813694

grammar BKIT;

@lexer::header {
from lexererr import *
}

@lexer::members {
def emit(self):
    tk = self.type
    result = super().emit()
    if tk == self.UNCLOSE_STRING:       
        raise UncloseString(result.text)
    elif tk == self.ILLEGAL_ESCAPE:
        raise IllegalEscape(result.text)
    elif tk == self.ERROR_CHAR:
        raise ErrorToken(result.text)
    elif tk == self.UNTERMINATED_COMMENT:
        raise UnterminatedComment()
    else:
        return result;
}

options{
    language=Python3;
}

program: (var_decl | func_decl )+ EOF;

// Declaration
// Variable declaration

// a = 5
// b[2] = {1,2}
// c[2][2] = {{1,2},{1,2}}
var_decl: VAR COLON declaration (CM declaration)* SM;

declaration : value_decl | array_decl ;

value_decl: ID (ASSIGN expr)?;

postfix_array_exp_for_decl: LSB expr RSB ;
postfix_array_exp_for_call: LSB expr RSB ;

array_assignment: (ASSIGN ARRAYLIT)? ;

array_decl: (array_1d_decl | array_nd_decl) ;
array_nd_decl: ID postfix_array_exp_for_decl+ (array_assignment ) ;
array_1d_decl: ID postfix_array_exp_for_decl (array_assignment );


//Function declaration
func_decl: FUNCTION COLON ID (param)? body;
//Function: fib
//Parameter: n ( , x,y,z)  

param: PARAMETER COLON (ID| (ID ('[' (expr)? ']')+)) (CM (ID| (ID ('[' (expr)? ']')+)))* ;

body: BODY COLON (statement_list)? return_statement? ENDBODY DOT;

// Function call
func_call: ID '(' (arguement (CM arguement)*)? ')' postfix_array_exp_for_decl* ;

arguement :  ID | literals | expr;

// Type coercions
int_of_float: 'int_of_float' LP ( ID | REAL | func_call) RP ; 
float_of_int: 'float_of_int' LP (ID | INTLIT | func_call) RP;
int_of_string: 'int_of_string' LP (STRINGLIT | ID | func_call) RP ;
string_of_int: 'string_of_int' LP ( ID | INTLIT | func_call) RP;
float_of_string: 'float_of_string' LP ( STRINGLIT | ID | func_call) RP;
string_of_float: 'string_of_float' LP (REAL | ID | func_call) RP;
bool_of_string: 'bool_of_string' LP ( TRUE | FALSE | ID | func_call ) RP;
string_of_bool: 'string_of_bool' LP ( BOOLINT | ID | func_call ) RP ;
 


statement
            : var_decl
            | array_decl
            | assignment_statement SM
            | if_statement
            | for_statement
            | while_statement
            | do_while_statement
            | break_statement
            | continue_statement
            | func_call SM
            | println
            | printstr
            | printstrln
            | read
            ;

statement_list:  statement+ ;

// Assignment statement 
assignment_statement: ID (postfix_array_exp_for_call)* ASSIGN expr ;
                    

// Expresstion
arithmetic 
            : INTLIT (ADD | SUB | MUL | DIV | MOD) INTLIT
            | REAL (ADDPOINT | SUBPOINT | MULPOINT | DIVPOINT) REAL ;



expr    : expr (AND | OR) expr1 | expr1;
expr1   : expr1 ( ADD | ADDPOINT | SUB | SUBPOINT) expr2 | expr2;
expr2   : expr2 (MUL | MULPOINT | DIV | DIVPOINT | MOD | MOD2) expr3 |expr3 ;                   //left
expr3   : (NOT) expr4 | expr4 ;                     //right
expr4   : ( SUB | SUBPOINT) expr4 | operand;       //right


expr_cond   : operand (LTE | GTE | EQ | NEQ | LT | GT) operand
            | operand (LTEPOINT | GTEPOINT | NEQPOINT | LTPOINT | GTPOINT) operand
            ;
            
operand : literals
        | LP expr RP
        | ID postfix_array_exp_for_call*
        | func_call
        ;

// If statement
// If Then (ElseIf Then)* (Else Then)?
if_statement: if_stmt (elseif_stmt)* (else_stmt)? ENDIF DOT ;

if_stmt: IF expr_cond ((OR| AND) expr_cond)* THEN statement_list? return_statement? ;
elseif_stmt: ELSEIF expr_cond THEN statement_list? return_statement?; 
else_stmt: ELSE statement_list return_statement?;

// For statement
// FOR (scalar-variable = initExpr, conditionExpr, updateExpr) DO statement_list 
for_statement: FOR  assignment_statement CM expr_cond CM expr  DO statement_list? return_statement? ENDFOR DOT;

// While statement
while_statement: WHILE expr_cond ((OR| AND) expr_cond)* DO statement_list? return_statement? ENDWHILE DOT;

// Do-while statement
do_while_statement: DO statement_list? return_statement? WHILE expr_cond ((OR| AND) expr_cond)* ENDDO DOT; 

// Break statement
break_statement: BREAK SM;

// Continue statement
continue_statement: CONTINUE SM;

// Return statement
return_statement: RETURN (ID | func_call | literals |expr)? SM;


// Built-in functions
println: 'printLn' '(' ')' ;
printstr: 'print' '(' operand ')' SM;
printstrln: 'printStrLn' '(' operand ')' SM;
read: 'read' '('')'   SM;

literals
        : INTLIT
        | REAL
        | bool_lit
        | STRINGLIT
        | ARRAYLIT
        ;

//Keywordss
BODY : 'Body';
BREAK: 'Break';
CONTINUE: 'Continue';
DO: 'Do';
ELSE: 'Else';
ELSEIF: 'ElseIf';
ENDBODY: 'EndBody';
ENDIF: 'EndIf';
ENDFOR: 'EndFor';
ENDWHILE: 'EndWhile';
FOR: 'For';
FUNCTION: 'Function';
IF: 'If';
PARAMETER: 'Parameter';
RETURN: 'Return';
THEN:'Then';
VAR: 'Var';
WHILE: 'While';
TRUE: 'True';
FALSE: 'False';
ENDDO: 'EndDo';


CM: ',';
LP : '(';
RP : ')';
LB : '{';
RB : '}';
LSB : '[';
RSB : ']';
SM: ';' ;
COLON: ':' ;
DOT: '.';


ADD: '+';
SUB: '-';
MUL: '*';
DIV: '\\';
MOD: '%';
MOD2: '\\%';

NOT: '!';
AND: '&&';
OR: '||';

ADDPOINT: '+.';
SUBPOINT: '-.';
MULPOINT: '*.';
DIVPOINT: '\\.';

LTE: '<=';
GTE: '>=';
LT : '<' ;
GT : '>' ;

LTEPOINT: '<=.';
GTEPOINT: '>=.';
LTPOINT : '<.' ;
GTPOINT : '>.' ;


NEQPOINT: '=/=';
NEQ: '!=';
EQ : '==' ;
ASSIGN: '=';

ARRAYLIT : ARRAY1DLIT | ARRAYNDLIT;

ARRAY1DLIT
            : LB REAL ( CM REAL)* RB 
            | LB INTLIT ( CM INTLIT)* RB 
            | LB BOOLINT ( CM BOOLINT)* RB 
            | LB STRINGLIT ( CM STRINGLIT)* RB 
            ;
ARRAYNDLIT : LB ARRAY1DLIT? (CM ARRAY1DLIT)* RB | LB ARRAYNDLIT RB;


STRINGLIT: '"' CHAR* '"'
    {
        y = str(self.text)
        self.text = y[1:-1]
    }
    ;


bool_lit: (TRUE|FALSE);

BOOLINT : (TRUE|FALSE);

REAL:  DIGIT+ ('.'DIGIT+|'.')? (('e'|'E')SIGN? DIGIT+)?;
//Integer

DECIMAL: ('0'| [1-9]DIGIT*);
HEXADECIMAL: '0'[xX]([0-9]|[A-F])+ ;
OCTAL: '0'('o'|'O')([0-7])+ ;

INTLIT: (DECIMAL | HEXADECIMAL | OCTAL);


fragment LOWER: [a-z] ;
fragment UPPER: [A-Z] ;
fragment LETTER: [a-zA-Z];
fragment UNDERSCORES: '_';
fragment DIGIT: [0-9];
fragment SIGN: [-+];

ID: [a-z][a-zA-Z0-9]*;


BLOCK_COMMENT: '**' (.*? | '*') '**' -> skip ;

LINE_COMMENT: '**' .*? '**'-> skip ;

WS : [ \t\r\n\f\b]+ -> skip ; 

UNCLOSE_STRING: '"' CHAR* ( [\b\t\n\f\r'"\\] | EOF )
    {
        y = str(self.text)
        possible = ['\b', '\t', '\n', '\f', '\r', '"', '\'', '\\']
        if y[-1] in possible:
            raise UncloseString(y[1:-1])
        else:
            raise UncloseString(y[1:])
    }
    ;
ILLEGAL_ESCAPE: '"' CHAR* ESC_ILLEGAL
    {
        y = str(self.text)
        raise IllegalEscape(y[1:])
    }
    ;

fragment CHAR: ~[\b\t\n\f\r'"\\] | ESC_SEQ ;

fragment ESC_SEQ: '\\' [btnfr'\\] | ['] ["] | [\\]['];
fragment ESC_ILLEGAL: '\\' ~[btnfr"'\\] | ~'\\' ;
ERROR_CHAR: .
    {
        raise ErrorToken(self.text)
    }
    ;

UNTERMINATED_COMMENT: '**' (~[*])?
    {
        y = str(self.text)
        raise UnterminatedComment()
    }
    ;

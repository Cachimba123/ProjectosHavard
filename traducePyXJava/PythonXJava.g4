grammar PythonXJava;

// Lexer rules
DEF         : 'def';
IDENTIFIER  : [a-zA-Z_][a-zA-Z_0-9]*;
LPAREN      : '(';
RPAREN      : ')';
COMMA       : ',';
COLON       : ':';
ASSIGN      : '=';
PRINT       : 'print';
RETURN      : 'return';
PLUS        : '+';
MULTIPLY    : '*';
REST        : '-';
DIVIDE      : '/';
NUMBER      : [0-9]+;
WS          : [ \t]+ -> skip;
NEWLINE     : '\r'? '\n' -> skip;

// Parser rules
program         : (function | statement)* EOF;
function        : DEF IDENTIFIER LPAREN params? RPAREN COLON NEWLINE indented_block;
params          : IDENTIFIER (COMMA IDENTIFIER)*;
indented_block  : (statement)+;

statement       : print_statement
                | return_statement
                | var_assign NEWLINE
                | function_call NEWLINE;

var_assign      : IDENTIFIER ASSIGN expr;
print_statement : PRINT LPAREN function_call RPAREN NEWLINE; // Específicamente llamando a `function_call`
return_statement: RETURN expr? NEWLINE;
function_call   : IDENTIFIER LPAREN (expr (COMMA expr)*)? RPAREN;

expr            : expr (PLUS | MULTIPLY | REST | DIVIDE) expr
                | IDENTIFIER
                | NUMBER
                | function_call;

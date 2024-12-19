grammar BaaxalXPython;

// Lexer Rules

// Estructura del programa
KAAJAL       : 'Káajal';
XUUL         : 'Xuul';

// Declaración y Asignación
TSAAJ        : 'Ts’áaj';

// Entrada y Salida
TSAATI       : 'Ts\'áa_ti\'_pantalla';
UYOKOL       : 'U_yokol';

// Estructuras de Control
WAJAAJ       : 'Wa_jaaj_lela\'';
BAALE        : 'Ba\'ale\'';
KUCH_COND    : 'Ts\'o\'oksik_le condición';

// Bucles
KAALIKIL     : 'Ka\'alikil';
UTIAL        : 'Uti\'al';
AMAL         : 'Amal';
KUCH_BUCLE   : 'Ts\'o\'oksik_le bucle';

// Funciones
FUUNSION     : 'Fúunsion';
KUCH_FUNC    : 'Ts\'o\'oksik_le función';

// Operadores Lógicos
AND          : 'Yéetel'; // AND lógico
OR           : 'Wa';     // OR lógico

// Operadores Aritméticos
PLUS         : '+';
REST         : '-';
MULTIPLY     : '*';
DIVIDE       : '/';
POWER        : '**';

// Operadores Relacionales
EQUALS       : '==';
DIFFERENT    : '!=';
LESS_THAN    : '<';
GREATER_THAN : '>';
LESS_EQUAL   : '<=';
GREATER_EQUAL: '>=';

// Booleanos
TRUE         : 'true';
FALSE        : 'false';

// Literales y Delimitadores
IDENTIFIER   : [a-zA-Z_][a-zA-Z0-9_]*;
NUMBER       : [0-9]+ ('.' [0-9]+)?;
STRING       : '"' .*? '"';
LPAREN       : '(';
RPAREN       : ')';
COLON        : ':';
COMMA        : ',';
LBRACK       : '[';
RBRACK       : ']';

// Espacios y Saltos de Línea
NEWLINE      : '\r'? '\n' -> skip;
WS           : [ \t]+ -> skip;

//Comentarios
COMMENT      : '//' ~[\r\n]* -> skip;       // Comentario de una línea
MULTI_COMMENT: '"""' .*? '"""' -> skip;     // Comentario de varias líneas


// Parser Rules

program          : KAAJAL COLON statement* XUUL;

statement        : var_assignment
                 | print_statement
                 | input_statement
                 | conditional_block
                 | while_loop
                 | for_loop
                 | function_definition
                 | comment;

comment          : COMMENT | MULTI_COMMENT;

var_assignment   : TSAAJ LPAREN IDENTIFIER COMMA expr RPAREN;

print_statement  : TSAATI LPAREN expr RPAREN;

input_statement  : UYOKOL LPAREN IDENTIFIER RPAREN;

conditional_block: WAJAAJ LPAREN expr RPAREN COLON statement* KUCH_COND
                 | BAALE COLON statement* KUCH_COND;

while_loop       : KAALIKIL LPAREN expr RPAREN COLON statement* KUCH_BUCLE;

for_loop         : UTIAL IDENTIFIER AMAL expr COLON statement* KUCH_BUCLE;

function_definition: FUUNSION IDENTIFIER LPAREN (IDENTIFIER (COMMA IDENTIFIER)*)? RPAREN 
                    '->' IDENTIFIER COLON statement* KUCH_FUNC;

// Expresiones con jerarquía de operaciones
expr             : logical_expr;                 // Punto de entrada principal a expresiones

logical_expr     : relational_expr ( (AND | OR) relational_expr )*;   // AND y OR

relational_expr  : additive_expr ( (EQUALS | DIFFERENT | LESS_THAN 
                                  | GREATER_THAN | LESS_EQUAL | GREATER_EQUAL) additive_expr )*;

additive_expr    : multiplicative_expr ( (PLUS | REST) multiplicative_expr )*;

multiplicative_expr : power_expr ( (MULTIPLY | DIVIDE) power_expr )*;

power_expr       : base (POWER base)*;

base
                : NUMBER
                | STRING
                | TRUE
                | FALSE
                | IDENTIFIER LPAREN (expr (COMMA expr)*)? RPAREN
                | IDENTIFIER
                | LBRACK expr (COMMA expr)* RBRACK
                | LPAREN expr RPAREN;




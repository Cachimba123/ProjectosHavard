import ply.lex as lex

#Token definitions
tokens = (
    'INTEGER',
    'IDENTIFER'
)

# Regilar expression rules
t_INTEGER=r'\d+'
t_IDENTIFER=r'[a-zA-z_][a-zA-z_0-9]*'

#Ignored characters
t_ignore=' \t\n'

#Error handling rule
def t_error(t):
    print(f"Invalid character: {t.value[0]} ")
    t.lexer.skip(1)

#Contruir el lexico
lexer=lex.lex()

lexer.input('42 var_name')

for token in lexer:
    print(token)
# Tabla_Driven Lexical Analyzer
# A table driven lexical analyzer , alse referred to as
# a finite state machin 

state_t_table = {
    0:{'digit':(1,'append'),'letter':(2,'append')},
    1:{'digit':(1,'append'),'ws':(0,'create_token')},
    2:{'letter':(2,'append'),'digit':(2,'append'),'ws':(0,'create_token')}
}
def analize_code(codestr):
    state = 0
    tokens = []
    current_t = ''
    for char in codestr:
        if char.isdigit():
            input_symbol="digit"
        elif char.isalpha() or char == '_' :
            input_symbol = 'letter'
        elif char in {' ','\t','\n'}:
            input_symbol = 'ws'
        else:
            input_symbol = char

        next_state = state_t_table[state][input_symbol][0]
        action = state_t_table[state][input_symbol][1]

        if action == 'append':
            current_t += char
        elif action == 'create_token':
            tokens.append(current_t)
            current_t=''
        state = next_state
    if current_t != '':
        tokens.append(current_t)
    return tokens
# State transition table

# test token analizer
in_code = '42 var_name'
result = analize_code(in_code)
print(result)
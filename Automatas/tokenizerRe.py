import re

def tokenizerRe(in_code):
    tokens=[]
    position=0
    while position<len(in_code):
        if in_code[position]!=' ':
            match1=None
            for pattern,token_type in t_patterns.items():
                regex=re.compile(pattern)
                match1=regex.match(in_code,position)
                if match1:
                    value=match1.group()
                    tokens.append((token_type,value))
                    position=match1.end()
                    break
        elif not match1:
            raise ValueError(f'Invalid character at position {position}: {in_code[position]}')
        else:
            position+=1
    return tokens



t_patterns={
    r'[0-9]+':'INTEGER',
    r'[a-zA-z_]+[a-zA-Z0-9_]*':'IDENTIFIER',
    r'=':'ASSIGN',
    r'\+':'PLUS',
    r'-':'MINUS',
    r'\*':'MULTIPLY',
    r'/':'DIVIDE',
    r'\(':'LPAREN',
    r'\)':'RPAREN',
    r';':'SEMICOLON'
}

#Example
in_code='x = 10 + y;'

try:
    tokens=tokenizerRe(in_code)
    for token_type,value in tokens:
        print(f'Token: {value}, tipo de token: {token_type}')
except ValueError as e:
    print(str(e))

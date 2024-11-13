def tokenJachi (codeline):
  tokens= []
  currentToken = "" 
  for char in codeline:
    if char.isdigit():
      currentToken += char
    elif char in ('+','-'):
      if currentToken:
        tokens.append(('INTEGER', int(currentToken)))
        currentToken=""
      tokens.append(('OPERATOR', char))
    elif char.isspace():
      if currentToken:
        tokens.append(('INTEGER',int(currentToken)))
        currentToken =""
    else:
      raise ValueError(f"Invalid character: {char}")
  if currentToken:
    tokens.append(('INTEGER', int(currentToken)))
  return tokens
  
codeline= "10 + 6 -3"

tokens = tokenJachi(codeline)
print(tokens)
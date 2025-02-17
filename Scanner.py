##Dillon Patel and Rei Thao ProjectPhase 2.2
import re


class Token:
  def __init__(self, token_type, token_value):
      self.type = token_type
      self.value = token_value

def tokenize(input_line):
  tokens = []
  while input_line:
    # Check for whitespace at the beginning of the line and remove it
    match = re.match(r'\s+', input_line)
    if match:
        input_line = input_line[len(match.group(0)):]

    # Check for NUMBER
    match = re.match(r'\d+', input_line)
    if match:
        tokens.append(Token('NUMBER', match.group(0)))
        input_line = input_line[len(match.group(0)):]
        continue
      
    # Check for KEYWORD
    match = re.match(r'if|then|else|endif|while|do|endwhile|skip', input_line)
    if match:
        tokens.append(Token('KEYWORD', match.group(0)))
        input_line = input_line[len(match.group(0)):]
        continue
      
    # Check for IDENTIFIER
    match = re.match(r'[a-zA-Z][a-zA-Z0-9]*', input_line)
    if match:
        tokens.append(Token('IDENTIFIER', match.group(0)))
        input_line = input_line[len(match.group(0)):]
        continue

    # Check for SYMBOL
    match = re.match(r'\+|-|\*|/|\(|\)|:=|;', input_line)
    if match:
        tokens.append(Token('SYMBOL', match.group(0)))
        input_line = input_line[len(match.group(0)):]
        continue
    # If no valid token is found, raise an error
    raise SyntaxError("Invalid token")

  return tokens

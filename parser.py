##Dillon Patel and Rei Thao ProjectPhase 3.2
import sys


class Token:
    def __init__(self, token_type, token_value):
        self.type = token_type
        self.value = token_value

class RecursiveDescentParser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.current_token = None
        self.advance()

    def advance(self):
        if self.tokens:
            self.current_token = self.tokens.pop(0)
        else:
            self.current_token = None

    def parse(self):
        return self.parse_statement()

    def parse_statement(self):
      term = self.parse_basestatement()
      while self.current_token and self.current_token.value == ';':
          operator = self.current_token
          self.advance()
          right_term = self.parse_basestatement()
          term = {
              "SYMBOL": operator.value,
              "left": term,
              "right": right_term
          }
      return term

    def parse_basestatement(self):
      if self.current_token and self.current_token.value == 'while':
          return self.parse_whilestatement()
      else:
          return self.parse_assignment()

    def parse_assignment(self):
      term = self.parse_expression()
      while self.current_token and self.current_token.value == ':=':
          operator = self.current_token
          self.advance()
          right_term = self.parse_expression()
          term = {
              "SYMBOL": operator.value,
              "left": term,
              "right": right_term
          }
      return term

    def parse_whilestatement(self):
      if self.current_token and self.current_token.value == 'while':
          operator = self.current_token
          self.advance()
          condition = self.parse_expression()
          if self.current_token and self.current_token.value == 'do':
              self.advance()
              body = self.parse_statement()
              if self.current_token and self.current_token.value == 'endwhile':
                  self.advance()
                  return {
                      "WHILE-LOOP": operator.value,
                      "condition": condition,
                      "body": body
                  }
              else:
                  raise SyntaxError("Expected 'endwhile'")
          else:
              raise SyntaxError("Expected 'do'")
      else:
          raise SyntaxError("Expected 'while'")
    
    def parse_expression(self):
        term = self.parse_term()
        while self.current_token and self.current_token.value == '+':
            operator = self.current_token
            self.advance()
            right_term = self.parse_term()
            term = {
                "SYMBOL": operator.value,
                "left": term,
                "right": right_term
            }
        return term

    def parse_term(self):
        factor = self.parse_factor()
        while self.current_token and self.current_token.value == '-':
            operator = self.current_token
            self.advance()
            right_factor = self.parse_factor()
            factor = {
                "SYMBOL": operator.value,
                "left": factor,
                "right": right_factor
            }
        return factor

    def parse_factor(self):
        piece = self.parse_piece()
        while self.current_token and self.current_token.value == '/':
            operator = self.current_token
            self.advance()
            right_piece = self.parse_piece()
            piece = {
                "SYMBOL": operator.value,
                "left": piece,
                "right": right_piece
            }
        return piece

    def parse_piece(self):
        element = self.parse_element()
        while self.current_token and self.current_token.value == '*':
            operator = self.current_token
            self.advance()
            right_element = self.parse_element()
            element = {
                "SYMBOL": operator.value,
                "left": element,
                "right": right_element
            }
        return element

    def parse_element(self):
        if self.current_token and self.current_token.value == '(':
            self.advance()
            expression = self.parse_expression()
            if self.current_token and self.current_token.value == ')':
                self.advance()
                return expression
            else:
                raise SyntaxError("Expected closing parenthesis ')'")
        elif self.current_token and (self.current_token.type == 'NUMBER'):
            token = self.current_token
            self.advance()
            return {
                "NUMBER": token.value
            }
        elif self.current_token and (self.current_token.type == 'IDENTIFIER'):
            token = self.current_token
            self.advance()
            return {
                "IDENTIFIER": token.value
            }
        elif self.current_token and (self.current_token.type == 'KEYWORD'):
          token = self.current_token
          self.advance()
          return {
                "WHILE-LOOP": token.value
          }
        else:
            raise SyntaxError(f"Unexpected token: {self.current_token}")

def print_ast(node, indent='', output_file=None):
  if output_file is None:
    output_file = sys.stdout
  if isinstance(node, dict):
    for key, value in node.items():
        if isinstance(value, dict):
            print_ast(value, indent + '    ', output_file)
        else:
            print(f"{indent}{key} {value}", file=output_file)
  elif isinstance(node, list):
    for item in node:
        print_ast(item, indent, output_file)
  else:
        print(f"{indent}{node}", file=output_file)
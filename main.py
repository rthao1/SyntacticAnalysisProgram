#Dillon Patel and Rei Thao ProjectPhase 3.2
import re
from parser import RecursiveDescentParser, print_ast
from Scanner import tokenize
from evaluator import evaluate, evalLoop, print_eval


def process_input_file(input_file, output_file):
  with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
    original_text = infile.read()
    modText = original_text.replace("\n", " ")
    tokens = tokenize(modText)
    outfile.write("Tokens:\n")
    for token in tokens:
      outfile.write(f"{token.type} {token.value}\n")
    outfile.write("AST:\n")
    try:
      ast = RecursiveDescentParser(tokens)
      ast = ast.parse()
      print_ast(ast, "", outfile)
      outfile.write("Output:\n")
      ##outfile.write(f"{evaluate(ast)} ")
      eval = evaluate(ast)
      eval = evalLoop()
      print_eval(eval, outfile)
      for i in eval:
        outfile.write(f"{i} = {eval[i+1]}")
    except SyntaxError as e:
      outfile.write(f"Syntax Error: {str(e)}\n")


if __name__ == "__main__":
  input_file = "input.txt"
  output_file = "output.txt"

  process_input_file(input_file, output_file)

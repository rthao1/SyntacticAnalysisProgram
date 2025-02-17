import sys

evaluateList = []
numbers = []
loop = []

def checkLoop():
  global numbers
  global loop
  if len(loop)!=3:
    return
  else:
    checknum1 = int(numbers[numbers.index(loop[0])+1]) 
    checknum2= int(numbers[numbers.index(loop[2])+1]) 
    if loop[1] == '-':
      result = checknum1 - checknum2
    elif loop[1] == '*':
      result = checknum1 * checknum2 
    elif loop[1] == '/':
      if checknum2 == 0:
          return "Error: Division by zero"
      result = checknum1 // checknum2
    return (result > 0) 
  
def evalCheck():
  global evaluateList
  global numbers
  global loop
  
  if (len(evaluateList) > 0 and evaluateList[-1] == ';'):
    evaluateList = evaluateList[:-1]
  if ('while' not in evaluateList and len(evaluateList) >= 3 and evaluateList[-3] == ':='):
    numbers.append(evaluateList[-2]) 
    numbers.append(evaluateList[-1]) 
    evaluateList = evaluateList[:-3] 
  if 'while' in evaluateList and len(evaluateList) == 4:
    var1 = evaluateList[-2]
    op = evaluateList[-3]
    var2 = evaluateList[-1]
    if var1 not in loop:
      loop.append(var1)
    if op not in loop:
      loop.append(op)
    if var2 not in loop:
      loop.append(var2)

def evalLoop():
  global loop 
  global evaluateList
  while 'while' in evaluateList and checkLoop():
      tempList = evaluateList.copy()
      while len(tempList) >= 5 and checkLoop():
        op = tempList[-3] 
        variable = tempList[-4] 
        if not tempList[-2].isdigit():
          num1 = int(numbers[numbers.index(tempList[-2])+1])
        else:
          num1 = int(tempList[-2])
        if not tempList[-1].isdigit():
          num2 = int(numbers[numbers.index(tempList[-1])+1])
        else:
          num2 = int(tempList[-1])
        if op == '+':
            result = num1 + num2
        elif op == '-':
            result = num1 - num2
        elif op == '*':
            result = num1 * num2
        elif op == '/':
            if num2 == 0:
                return "Error: Division by zero"
            result = num1 // num2
        numbers[numbers.index(variable)+1] = str(result)
        tempList = tempList[:-5] 
  return numbers
  
def evaluate(node):
  global evaluateList
  if isinstance(node, dict):
    for key, value in node.items():
      if isinstance(value, dict):
        evaluate(value)
      else:
        evaluateList.append(str(value))
        evalCheck() 
  elif isinstance(node, list):
    for item in node:
      evaluate(item)
  return numbers

def print_eval(eval, output_file=None):
  if output_file is None:
    output_file = sys.stdout
  while len(eval) > 0:
    print(f"{eval[0]} = {eval[1]}",file=output_file)
    del eval[:2]
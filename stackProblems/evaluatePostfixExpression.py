#Evaluate a postfix expression using the stack data structure

def evaluatePostFixExpression(expression):
  stack = []
  if(expression == ''):
    print('String is empty, returning 0')
    return 0
  
  for character in expression:
    if(character.isdigit()):
      print('digit = ', character)
      stack.append(int(character))
    else:
      first = stack.pop()
      second = stack.pop()
      operator = character
      print('operator = ', operator)
      if(operator == '+'):
        result = second + first
      elif(operator == '-'):
        result = second - first
      elif(operator == '*'):
        result = second * first
      elif(operator == '/'):
        result = second / first

      stack.append(result)
      print('result = ', result)
  print('total stack = ', stack)
  return stack.pop()


# evaluatePostFixExpression('231*+9-')
# evaluatePostFixExpression('')

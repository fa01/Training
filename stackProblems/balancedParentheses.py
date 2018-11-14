# Check balanced parentheses in an expression
# Return true if balanced, false otherwise

def balancedParentheses(expression):
  closedParens = {')' : '(', '}' : '{', ']' : '['}


  temp = []
  for paren in expression:
    print('paren = ', paren)
    if paren in ['(', '{', '[']:
      temp.append(paren)
    elif(closedParens[paren] != temp.pop()):
      print('closedParens[paren]', closedParens[paren])
      print('temp = ', temp)
      print('This is NOT a valid parentheses expression')
      return False
  
  if(len(temp) > 0):
    print('Temp at end is not empty, returning False', temp)
    return False
  else:
    print('This is a valid parentheses expression')
    return True

# balancedParentheses("[()]{()}{[()()]()}")
# balancedParentheses('[(])')
# balancedParentheses("((")

# Sort the values in a stack using another temporary stack to complete the process and return sorted stack

def sortValues(arr):
  if(len(arr) == 0 or len(arr) == 1):
    print('len is 0 or 1, returning original array')
    return arr

  sortedStack = []
  value = arr.pop()
  sortedStack.append(value)


  while(len(arr) != 0):
    value = arr.pop()
    print('current Value adding = ', value)
    if(sortedStack[len(sortedStack) - 1] < value):
      sortedStack.append(value)
      print('appended to sortedStack', sortedStack)
    else:
      print('cant add value = ', value, ' to sortedStack right away', sortedStack)
      tempStack = []
      while(len(sortedStack) != 0 and sortedStack[len(sortedStack) - 1] > value):
        tempStack.append(sortedStack.pop())
        print('length of sortedStack after pop now is ', len(sortedStack))
        print('sortedStack = ', sortedStack)
        print('tempStack = ', tempStack)
      sortedStack.append(value)
      for i in range(len(tempStack)):
        sortedStack.append(tempStack.pop())

    print('done sorting', sortedStack)
  return sortedStack


# sortValues([1, 3, 2, 5, 4])
# sortValues([])
# sortValues([1])
# sortValues([1, 3])
# sortValues([1, 2, 3, 4, 5])
sortValues([1000, 10, 100, 99, 85, 3, 95, 85, 56, 76, 89, 99])

# Find the first non-repeating element in a given array of integers.

def firstNonRepeating(arr):
  newDict = {}
  for i in range(len(arr)):
    value = arr[i]
    if(value not in newDict):
      newDict[value] = 1
    else:
      newDict[value] = newDict[value] + 1
  for key, value in newDict.items():
    if(value == 1):
      print('Key = ', key, ' Value = ', value)
      break


firstNonRepeating([1, 2, 3, 4, 5, 1, 2, 3])
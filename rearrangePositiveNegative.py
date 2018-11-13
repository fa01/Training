def rearrangePostiveNegative(arr):
  positive = []
  negative = []
  
  for i in range(len(arr)):
    if(arr[i] < 0):
      negative.append(arr[i])
    else:
      positive.append(arr[i])

  positiveCount = 0
  negativeCount = 0
  result = []

  while(positiveCount < len(positive) and negativeCount < len(negative)):
    result.append(positive[positiveCount])
    result.append(negative[negativeCount])
    positiveCount += 1
    negativeCount += 1
  
  if(positiveCount < len(positive)):
    for i in range(positiveCount, len(positive)):
      result.append(positive[positiveCount])
      positiveCount += 1
  elif(negativeCount < len(negative)):
    for i in range(negativeCount, len(negative)):
      result.append(negative[negativeCount])
      negativeCount += 1

  print('Result =', result)
  return result


# rearrangePostiveNegative([1, 2, 3, 4, 5, 6, -1, -2, -3, -4, -5, -6])
# rearrangePostiveNegative([1, -5, 7, -15, 6, -90, 100, -2, 98, -6, 5, -6])
# rearrangePostiveNegative([1, -5, 7, -15, 6, -90, 100, -2, 98, -6, 5, -6, 1, 2, 3, 4, 5])
rearrangePostiveNegative([1, -5, 7, -15, 6, -90, 100, -2, 98, -6, 5, -6, 1, 2, 3, 4, 5, -5, -4, -2])

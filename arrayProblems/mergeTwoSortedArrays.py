# Merge Two Sorted Arrays

def mergeSortedArrays(arr1, arr2):
  len1 = len(arr1)
  len2 = len(arr2)
  count1 = 0
  count2 = 0
  arr3 = []

  if(len1 == 0 and len2 == 0):
    print('Both are empty, returning empty array')
    return []
  elif(len1 == 0):
    print('array1 is empty, sending back array2')
    print(arr2)
    return arr2
  elif(len2 == 0):
    print('array2 is empty, sending back array2')
    print(arr1)
    return arr1
  while(count1 < len1 and count2 < len2):
    if(arr1[count1] <= arr2[count2]):
      arr3.append(arr1[count1])
      count1 += 1
    else:
      arr3.append(arr1[count2])
      count2 += 1

  if(count1 == len1):
    for i in range(count2, len(arr2)):
      arr3.append(arr2[i])
  if(count2 == len2):
    for i in range(count1, len(arr1)):
      arr3.append(arr1[i])

  print('New Sorted Array', arr3)
  return arr3


# mergeSortedArrays([1,2,3], [4,5,6])
# mergeSortedArrays([], [])
# mergeSortedArrays([1, 2, 3], [])
# mergeSortedArrays([], [4, 5, 6])
# mergeSortedArrays([1, 2], [4, 5, 6])
mergeSortedArrays([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25,
                   26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50], 
                   [51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 
                   79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100])



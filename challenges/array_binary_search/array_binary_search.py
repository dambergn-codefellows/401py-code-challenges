def binary_search(array, value):
  '''
  Use a binary search method to look for a values position in a sorted list.
  '''
  left = 0
  right = len(array) - 1
  while(left <= right):
    mid = (left + right) // 2
    if array[mid] is value:
      print(mid)
      return mid
    elif value < array[mid]:
      right = mid - 1
    elif value > array[mid]:
      left = mid + 1

  print(-1)
  return -1

# binary_search([1,2,3,4,5,6,7,8,9], 5) # 4
# binary_search([1,2,3,4,5,6,7,8,9], 2) # 1
# binary_search([1,2,3,4,5,6,7,8,9], 8) # 7
# binary_search([1,2,3,4,5,6,7,8,9], 4.5) # -1
# binary_search([2,4,6,8,10,12,14,16,18], 10) # 4

binary_search([4,8,15,16,23,42], 15) # 2
# binary_search([11,22,33,44,55,66,77], 90) # -1
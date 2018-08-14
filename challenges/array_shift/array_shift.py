def insertShiftArray(array, value):
  '''
  inserts a value in middle of array.
  '''
  if len(array)%2 !=0:
    oddOrEven = 1
  else:
    oddOrEven = 0
  half = len(array)//2 + oddOrEven
  # print(array[:half] + [value] + array[half:])
  return array[:half] + [value] + array[half:]


#insertShiftArray([1,2,4,5], 3)

#insertShiftArray([1,2,4,5,6], 3)
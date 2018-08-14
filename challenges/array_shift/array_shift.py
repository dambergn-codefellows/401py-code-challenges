def insertShiftArray(array, value):
  '''
  inserts a value in middle of array.
  '''
  half = len(array)//2
  # print(array[:half] + [value] + array[half:])
  return array[:half] + [value] + array[half:]


#insertShiftArray([1,2,4,5], 3)

#insertShiftArray([1,2,4,5,6], 3)
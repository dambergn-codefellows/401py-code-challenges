input_list = [1, 2, 3, 4]


# def reverse_array(input_list):
#   for i in range(0, (len(input_list) // 2)):
#     input_list[i], input_list[i-1] = input_list[i-1], input_list[i]
#   return input_list


def reverse_array(arr):
  if type(arr) is not list:
    raise TypeError('There was an error')

  mid = len(arr) // 2
  p1, p2 = 0, -1

  for _ in range(mid):
    arr[p1], arr[p2] = arr[p2], arr[p1]
    p1 += 1
    p2 -= 1

  return arr


def reverse_cute(input_list):
  return input_list[::-1]


print(reverse_array(input_list))
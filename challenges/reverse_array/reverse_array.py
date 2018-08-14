input_list = [1, 2, 3, 4]


def reverse_array(input_list):
  for i in range(0, (len(input_list) // 2)):
    input_list[i], input_list[i-1] = input_list[i-1], input_list[i]
  return input_list


def reverse_cute(input_list):
  return input_list[::-1]


print(reverse_array(input_list))
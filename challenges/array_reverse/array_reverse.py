list = [1, 2, 3, 4]


def reverse_array(list):
  for i in range(0, (len(list)/2)):
    list[i], list[i-1] = list[i-1], list[i]
  return list


def reverse_cute(list):
  return list[::-1]
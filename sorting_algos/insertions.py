def insertion_sort(unsorted):
    if type(unsorted) is not list:
        raise TypeError('Input argument must me list')

    for i in range(1, len(unsorted)):
        current = unsorted[i]
        position = i

        while current < unsorted[position - 1] and position > 0:
            unsorted[position], unsorted[position - 1] = unsorted[position - 1], unsorted[position]
            position -= 1
    
    return unsorted

print(insertion_sort([3,7,4,1]))
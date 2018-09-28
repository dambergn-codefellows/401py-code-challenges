def selection_sort(unsorted):
    if type(unsorted) is not list:
        raise TypeError('Input argument must me list')

    for i in range(len(unsorted)): 
        min_idx = i 
        for j in range(i+1, len(unsorted)): 
            if unsorted[min_idx] > unsorted[j]: 
                min_idx = j 
                	 
        unsorted[i], unsorted[min_idx] = unsorted[min_idx], unsorted[i]
    
    return unsorted

print(selection_sort([14,33,27,10,35,19,42,44]))
# result = [10,14,19,27,33,35,42,44]
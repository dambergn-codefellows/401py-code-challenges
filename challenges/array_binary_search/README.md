# Challenge 03 / Array Binary Search

## Problem Domain
- Use a binary search method to look for a values position in a sorted list.
- Do not use built in methods.

## Visual
- [1,2,4,5], 3 <-Input
- 2  <-Result

## Algorithm
- Function takes in two arguments
- First parameter is an array.
- Second parameter is a value.
- Determine midpoint of array.
- Compare midpoint to input value.
- If midpoint = to value, return index.
- If value < midpoint set midpoint to midpoint / 2
- If value > midpoint set midpoint to midpoint + (midpoint / 2)
- loop through if statements till value found or reaches 0
- if 0 return -1

## Pseudo Code
```
function(array, value)
  first half of array = array length / 2 -1
  second half of array = array length - first half of array
  return new array = first half of array + value + second half of array
```

## Code
```
def insertShiftArray(array, value):
  half = len(array)//2
  return array[:half] + [value] + array[half:]
```

## Big 'O'
- array_binary_search
 - Time: O(log2N)
 - Space: O(1)

## Whiteboard
Inline-style: 
![alt text](./../../assets/array_binary_search.jpg "Whiteboard")
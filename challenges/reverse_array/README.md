# Challenge 01 / Array Reverse

## Problem Domain
- reverse an array in place

## Visual
- Draw a visual representation
- [1,2,3,4]
- [4,3,2,1]

## Algorithm
- With bracket notation, begin at end of list.
- Flip each index.

## Pseudo Code
- Language Agnostic
ALGORITHM <- Reverse Array
||INPUT <- a list
||OUTPUT <- a list
return [::-1]

## Code
```
def reverse_array(list):
  for i in range(0, (len(list)/2)):
    list[i], list[i-1] = list[i-1], list[i]
  return list
```
```
def reverse_cute(list):
  return list[::-1]
```

## Big 'O'
- reverse_array
 - Space: O(1)
 - Time: O(N)

- reverse_cute
 - Space: O(N)
 - Time: O(N)
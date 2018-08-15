from .array_binary_search import binary_search
import pytest


def test_array_array_module_exists():
  '''
  Checks to see if function exists
  '''
  assert binary_search


def test_array_middle():
  '''
  Checks for value in middle of array
  '''
  expected = 4
  actual = binary_search([1,2,3,4,5,6,7,8,9], 5)
  assert expected == actual


def test_array_left():
  '''
  Checks for value on the left side of the array
  '''
  expected = 1
  actual = binary_search([1,2,3,4,5,6,7,8,9], 2)
  assert expected == actual


def test_array_add_right():
  '''
  Checks for value on the right side of the array
  '''
  expected = 7
  actual = binary_search([1,2,3,4,5,6,7,8,9], 8)
  assert expected == actual


def test_array_add_none():
  '''
  Checks for value not found in array
  '''
  expected = -1
  actual = binary_search([1,2,3,4,5,6,7,8,9], 4.5)
  assert expected == actual


def test_array_add_non_sequential():
  '''
  Checks for non sequence array
  '''
  expected = 4
  actual = binary_search([2,4,6,8,10,12,14,16,18], 10)
  assert expected == actual


def test_array_add_example1():
  '''
  Checks first example given
  '''
  expected = 2
  actual = binary_search([4,8,15,16,23,42], 15)
  assert expected == actual


def test_array_add_example2():
  '''
  Checks second example given
  '''
  expected = -1
  actual = binary_search([11,22,33,44,55,66,77], 90)
  assert expected == actual
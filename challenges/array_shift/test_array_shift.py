from .array_shift import insertShiftArray
import pytest


def test_array_array_module_exists():
  assert insertShiftArray


def test_array_add_middle_even():
  expected = [1,2,3,4,5]
  actual = insertShiftArray([1,2,4,5], 3)
  assert expected == actual


def test_array_add_middle_odd():
  expected = [1,2,3,4,5,6]
  actual = insertShiftArray([1,2,3,5,6], 4)
  assert expected == actual


def test_array_add_middle_example1():
  expected = [2,4,5,6,8]
  actual = insertShiftArray([2,4,6,8], 5)
  assert expected == actual


def test_array_add_middle_example2():
  expected = [4,8,15,16,23,42]
  actual = insertShiftArray([4,8,15,23,42], 16)
  assert expected == actual
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
  actual = insertShiftArray([1,2,4,5,6], 3)
  assert expected == actual

def test_array_add_middle_fail():
  expected = [1,2,4,3,5,6]
  actual = insertShiftArray([1,2,4,5,6], 3)
  assert expected != actual
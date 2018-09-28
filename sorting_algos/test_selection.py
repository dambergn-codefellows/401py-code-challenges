from selection import selection_sort
from random import shuffle
import pytest
# to run cd to sorting_algos directory and run "pytest test_selection.py"

def test_sort_validates_expected_input():
    with pytest.raises(TypeError):
        selection_sort('hello world')


def test_sorts_list_of_duplicates():
    unsorted = [14,33,27,10,35,19,42,44]
    expected = [10,14,19,27,33,35,42,44]
    now_sorted = selection_sort(unsorted)
    assert expected == now_sorted


def test_shuffled_list_gets_sorted():
    expected = [num for num in range(42)]
    unsorted = expected[:]
    shuffle(unsorted)
    now_sorted = selection_sort(unsorted)
    assert expected == now_sorted


def test_sorts_already_sorted():
    expected = [num for num in range(42)]
    now_sorted = selection_sort(expected)
    assert expected == now_sorted






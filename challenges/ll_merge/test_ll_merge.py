from challenges.ll_merge.ll_merge import ll_merge, LinkedList, Node
import pytest

def test_linked_list_merge_returns_not_valid_list(empty_list, empty_list_two):
    """ assert empty lists give back None
    """
    expected = None
    actual = LinkedList.ll_merge(empty_list, empty_list_two)
    assert expected == actual


def test_linked_list_merge_merges_lists_equal_lengths(small_list, empty_list):
    """ Test empty list and list input gives back list
    """
    expected = small_list
    actual = LinkedList.ll_merge(small_list, empty_list)
    assert expected == actual


def test_linked_list_merge_merges_lists_equal_lengths_other(small_list, empty_list):
    """ Test empty list and list input gives back list
    """
    expected = small_list
    actual = LinkedList.ll_merge(empty_list, small_list)
    assert expected == actual


def test_linked_list_ll_merge_exists():
    """ Test ll_merge exists
    """
    assert LinkedList.ll_merge
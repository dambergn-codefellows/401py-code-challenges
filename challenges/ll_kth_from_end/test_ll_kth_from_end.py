from challenges.ll_kth_from_end.ll_kth_from_end import ll_kth_from_end, LinkedList, Node
import pytest

@pytest.fixture
def small_list():
  ll = LinkedList()
  ll.insert(1)
  ll.insert(2)
  ll.insert(3)
  ll.insert(4)
  return ll

def test_ll_kth_from_end_item_not_in_list(small_list):
    expected = 'Exemption'
    actual = ll_kth_from_end(small_list, 5)
    assert expected == actual


def test_ll_kth_from_end_last_num(small_list):
    expected = 4
    actual = ll_kth_from_end(small_list, 0)
    assert expected == actual


def test_ll_kth_from_end_item_first_num(small_list):
    expected = 1
    actual = ll_kth_from_end(small_list, 3)
    assert expected == actual


def test_ll_kth_from_end_item_middle_num(small_list):
    expected = 3
    actual = ll_kth_from_end(small_list, 1)
    assert expected == actual


def test_ll_kth_from_end_empty_list(empty_list):
    expexted = 'Exemption'
    actual = ll_kth_from_end(small_list, 5)
    assert expexted == actual
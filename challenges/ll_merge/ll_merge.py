from typing import Any #typing annotation
from data_structures.linked_list.linked_list import LinkedList, Node

def ll_merge(self, ll_two):
    try:
        ll_one_current = self.head
        ll_two_current = ll_two.head

        while ll_one_current is not None and ll_two_current is not None:
            ll_one_next = ll_one_current._next
            ll_two_next = ll_two_current._next

            ll_one_current._next, ll_two_current._next = ll_two_next, ll_one_next
            ll_one_current = ll_one_next
        ll_two.head = ll_two_current

    except None:
        'Not valid input'
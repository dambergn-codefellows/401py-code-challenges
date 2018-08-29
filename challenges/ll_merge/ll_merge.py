from typing import Any #typing annotation
from linked_list import LinkedList, Node

def ll_merge(ll_one, ll_two):
    result_list = LinkedList()

    try:
        ll_one_current = ll_one.head
        ll_two_current = ll_two.head

        while ll_one_current is not None or ll_two_current is not None:
            # ll_one_next = ll_one_current._next
            # ll_two_next = ll_two_current._next

            if ll_one_current is not None:
                result_list.insert(ll_one_current)
                ll_one_current = ll_one_current._next

            if ll_two_current is not None:    
                result_list.insert(ll_two_current)
                ll_two_current = ll_two_current._next

        result_list_current = result_list.head
        while result_list_current is not None:
            print(result_list_current)
            result_list_current = result_list_current._next
        # return result_list

        #     ll_one_current._next, ll_two_current._next = ll_two_next, ll_one_next
        #     ll_one_current = ll_one_next
        # ll_two.head = ll_two_current

    except None:
        'Not valid input'


myList = LinkedList([1,2,3,4,5,6])

print(str(myList))
myList.insert(10)
print('Head Value: ' + str(myList.head.val))
print('Includes 4: ' + str(myList.includes(4)))
print('Does not include 7: ' + str(myList.includes(7)))

myList2 = LinkedList(['a','b','c','d','e','f'])

print(str(myList2))
print(str(ll_merge(myList, myList2)))
print('Includes d: ' + str(myList.includes('d')))

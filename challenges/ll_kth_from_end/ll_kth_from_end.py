from typing import Any #typing annotation
from data_structures.linked_list.linked_list import LinkedList, Node

def ll_kth_from_end(self, k):
    '''
    '''
    counter = 0
    current_node = self.head
    while current_node._next is not None:
        counter = counter + 1
        current_node = current_node._next
    if k > counter:
        return('exception')
    r = counter - k - 1
    current_node = self.head
    while counter < r:
        current_node = current_node._next
        counter = counter + 1
    return current_node.val

# def ll_kth_from_end(linked_list, k):
#     head = None
#     current = linked_list.head
#     counter = 0
#     while current.next.val is not null:
#         current = current.next
#         counter = counter + 1
#     if counter < k:
#         return Exception()
#     else:
#         r = counter - k - 1
#         while k > r:
#             head = current
#             counter = counter + 1
#     return linked_list[r]

# if __name__ == '__main__':
#     myList = LinkedList()
#     def create_list():
#         myList.insert(1)
#         myList.insert(2)
#         myList.insert(4)
#         myList.insert(6)
#         myList.insert(8)

#     create_list()
#     print(str(myList))
#     myList.insert(10)
#     print('Head Value: ' + str(myList.head.val))

#     print(ll_kth_from_end(myList, 2))


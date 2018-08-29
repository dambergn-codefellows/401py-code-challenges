from node import Node
from typing import Any #typing annotation

class LinkedList(object):
    def __init__(self, iterable=[]):
        self.head = None
        self._length = int('0')
        
        for item in iterable:
            self.insert(item)

    def __str__(self):
        return f'Head: {self.head} | Length: {self._length}'

    def __rpr__(self):
        return f'<Linked List | Head: {self.head} | Length: {self._length}>'

    def __len__(self):
        '''Sets length of list
        '''
        return self._length

    # def __iter__(self):
    #     if self.head:
    #         self._current = self.head
    #     return self

    # def __next__(self):
    #     self.head = self
        # pass

        # def insert(self, val: Any) -> Any:
        #   new_node = Node(val, self.head)
        #   self.head = new_node
        #   self._length += 1

    def insert(self, val):
        '''
        '''
        node = Node(val) # Create new node in object
        node._next = self.head # Assigns next value to previous node.
        self.head = node # Assign head to new node
        # self.head = Node(val, self.head)

        self._length += 1 # tracks the lenght
        return self.head.val # returns newly created node.
    

    # def includes(self, val: str, data: int) -> bool:
    def includes(self, val: Any) -> bool:
        '''
        '''
        current = self.head # Current starts as head
        while current is not None: # none is end of the list
            if current.val == val: # 
                return True
            current = current._next
        return False

    def append(self, val: Any) -> bool:
        '''
        '''
        if self.head is None:
            node = Node(val)
            self.head = node
            self._length += 1
        else:
            current = self.head
            while current is not None:
                if current._next is None:
                    node = Node(val)
                    current._next = node
                    self._length += 1
                    break
                current =  current._next



            
# myList = LinkedList()
# def create_list():
#   myList.insert(1)
#   myList.insert(2)
#   myList.insert(4)
#   myList.insert(6)
#   myList.insert(8)

# create_list()
# print(str(myList))
# myList.insert(10)
# print('Head Value: ' + str(myList.head.val))
# print('Includes 4: ' + str(myList.includes(4)))
# print('Does not include 7: ' + str(myList.includes(7)))
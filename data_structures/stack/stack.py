# from data_structures.linked_list.linked_list import LinkedList, Node
from node import Node
from typing import Any #typing annotation

class Stack(object):
    def __init__(self, iterable=[]):
        self.top = None
        self._length = int('0')
        
        for item in iterable:
            self.push(item)
         
    def __str__(self):
        return f'top: {self.top} | Length: {self._length}'

    def __repr__(self):
        return f'<Stacked List | top: {self.top} | Length: {self._length}>'

    def __len__(self):
        '''Sets length of list
        '''
        return self._length

    # def __iter__(self):
    #     if self.top:
    #         self._current = self.top
    #     return self

    # def __next__(self):
    #     self.top = self

    # def isEmpty(self):
    #      return self.node == []

    def push(self, val):
        if self.top is None:
            node = Node(val)
            self.top = node
            self._length += 1
        else:
            node = Node(val)
            current_top = self.top
            self.top = node
            self.top._next = current_top
            self._length += 1

    def pop(self):
         return self.node.pop()

    def peek(self):
         return self.top.val


s=Stack([5,2,1])
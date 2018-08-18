from node import Node
from typing import Any #typing annotation

class LinkedList(object):
  def __init__(self, iterable=None):
    self.head = iterable
    self._length = int('0')

  def __str__(self):
    return f'Head: {self.head} | Length: {self._length}'

  def __rpr__(self):
    return f'<Linked List | Head: {self.head} | Length: {self._length}>'

  def __len__(self):
    '''Sets length of list
    '''
    return self._length

  def __iter__(self):
    if self.head:
      self._current = self.head
    return self

  def __next__(self):
    self.head = self
    # pass

  def insert(self, val: Any) -> Any:
    new_node = Node(val, self.head)
    self.head = new_node
    self._length += 1

  # def includes(self, val: str, data: int) -> bool:
  def includes(self, val: Any) -> bool:
    pass

myList = LinkedList()
def create_list():
  myList.insert(1)
  myList.insert(2)
  myList.insert(4)
  myList.insert(6)
  myList.insert(8)

create_list()
print(str(myList))
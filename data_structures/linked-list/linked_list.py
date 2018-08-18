from node import Node
from typing import Any #typing annotation

class LinkedList(object):
  def __init__(self, iterable=None):
    self.head = None
    self._length: int = 0
    if iterable is None:
      iterable = []
    for value in iterable:
      self.insert

  def __str__(self):
    return f'Head: {self.head} | Length: {self._length}'

  def __rpr__(self):
    return f'<Linked List | Head: {self.head} | Length: {self._length}>'

  def __len__(self):
    return self._length

  def __iter__(self):
    if self.head:
      self._current = self.head
    return self

  def __next__(self):
    self.head = self
    # pass

  def insert(self, val: Any) -> Any:
    # self.insert is value
    new_node = Node(val)
    new_node.set_next(self.head)
    self.head = new_node
    # pass

  # def includes(self, val: str, data: int) -> bool:
  def includes(self, val: Any) -> bool:
    pass
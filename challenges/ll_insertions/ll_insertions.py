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

  def insert(self, val):
  '''
  '''
  self.head = Node(val, self.head)
  self._length += 1
  return self.head.val
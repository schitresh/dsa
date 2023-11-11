class Node:
  def __init__(self, key):
    self.key = key
    self.prev = None
    self.next = None

class DoublyLinkedList:
  def __init__(self):
    self.head = None
    self.tail = None

  def print(self):
    temp = self.head
    while temp:
      print(temp.key, end=' ')
      temp = temp.next
    print()

  def print_backward(self):
    temp = self.tail
    while temp:
      print(temp.key, end=' ')
      temp = temp.prev
    print()

  def append(self, key):
    node = Node(key)
    if not self.tail:
      self.head = node
      self.tail = node
      return

    node.prev = self.tail
    self.tail.next = node
    self.tail = node

  def prepend(self, key):
    node = Node(key)
    if not self.head:
      self.head = node
      self.tail = node
      return

    node.next = self.head
    self.head.prev = node
    self.head = node

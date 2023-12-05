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

from doubly import DoublyLinkedList

def test():
  linked_list = DoublyLinkedList()

  for i in range(5):
    linked_list.append(i)
  for i in range(5, 10):
    linked_list.prepend(i)

  linked_list.prepend(7)
  linked_list.append(7)
  linked_list.print()
  linked_list.print_backward()

  linked_list.delete(7)
  linked_list.print()

  print(linked_list.search(5).key)

# test()

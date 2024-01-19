from circular_list import CircularList
from doubly_list import Node

class CircularDoublyList(CircularList):
  # Utils

  def print_backward(self):
    temp = self.head
    if not temp:
      print()
      return

    print(temp.key, end=' ')
    temp = temp.prev

    while temp != self.head:
      print(temp.key, end=' ')
      temp = temp.prev

    print()

  def last_node(self):
    return self.head.prev

  # Insertion

  def append(self, key):
    node = Node(key)

    if not self.head:
      node.prev = node
      node.next = node
      self.head = node
      return node

    last = self.last_node()
    last.next = node
    node.prev = last
    node.next = self.head
    self.head.prev = node
    return node

  def prepend(self, key):
    node = self.append(key)
    self.head = node
    return node

def test():
  linked_list = CircularDoublyList()

  print('Insertion:')
  for i in range(5):
    linked_list.append(i)
  for i in range(5, 10):
    linked_list.prepend(i)
  linked_list.prepend(7)
  linked_list.append(7)
  linked_list.print()
  linked_list.print_backward()

  print('Deletion(7):')
  linked_list.delete(7)
  linked_list.print()

  print('Search(5):')
  print(linked_list.search(5).key)
  print('Search(9):')
  print(linked_list.search(9).key)
  print('Search(4):')
  print(linked_list.search(4).key)

test()

from m7_linked_list.library.linked_list import LinkedList

class Node:
  def __init__(self, key):
    self.key = key
    self.prev = None
    self.next = None

class DoublyList(LinkedList):
  def __init__(self):
    super().__init__()
    self.tail = None

  # Utils

  def print_backward(self):
    temp = self.tail

    while temp:
      print(temp.key, end=' ')
      temp = temp.prev

    print()

  def last_node(self):
    return self.tail

  def elements_backward(self):
    result = []
    temp = self.tail

    while temp:
      result.append(temp.key)
      temp = temp.prev

    return result

  # Insertion

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

def doubly_list_from_array(array):
  doubly_list = DoublyList()

  for item in array:
    doubly_list.append(item)

  return doubly_list

def test():
  linked_list = DoublyList()

  print('Insertion:')
  for i in range(5):
    linked_list.append(i)
  for i in range(5, 10):
    linked_list.prepend(i)
  linked_list.prepend(7)
  linked_list.append(7)
  linked_list.print()

  print('Print Backwards:')
  linked_list.print_backward()

  print('Deletion(7):')
  linked_list.delete(7)
  linked_list.print()

  print('Search(5):', linked_list.search(5).key)

# Do not execute while importing it in another file
if __name__ == '__main__':
  test()

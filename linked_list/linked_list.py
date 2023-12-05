class Node:
  def __init__(self, key):
    self.key = key
    self.next = None

class LinkedList:
  def __init__(self):
    self.head = None

  def print(self):
    temp = self.head

    while temp:
      print(temp.key, end=' ')
      temp = temp.next

    print()

  def length(self):
    temp = self.head
    if not temp:
      return 0

    length = 1
    while temp.next:
      length += 1
      temp = temp.next

    return length

  def last_node(self):
    temp = self.head
    if not temp:
      return

    while temp.next:
      temp = temp.next

    return temp

  def append(self, key):
    node = Node(key)

    if not self.head:
      self.head = node
      return

    last = self.last_node()
    last.next = node

  def prepend(self, key):
    node = Node(key)
    node.next = self.head
    self.head = node

  def delete(self, key):
    prev = self.head
    temp = prev.next

    while prev.key == key:
      del prev
      self.head = temp
      prev = temp
      temp = temp.next

    while temp:
      if temp.key == key:
        prev.next = temp.next
        del temp
        temp = prev

      prev = temp
      temp = temp.next

  def search(self, key):
    temp = self.head

    while temp:
      if temp.key == key:
        return temp
      temp = temp.next

  def reverse(self):
    prev = self.head
    if not prev:
      return

    temp = prev.next
    prev.next = None
    while temp:
      temp_next = temp.next
      temp.next = prev
      prev = temp
      temp = temp_next

    self.head = prev

def linked_list_from_array(array):
  linked_list = LinkedList()

  for item in array:
    linked_list.append(item)

  return linked_list

def test():
  linked_list = LinkedList()

  for i in range(5):
    linked_list.append(i)

  for i in range(5, 10):
    linked_list.prepend(i)

  linked_list.prepend(7)
  linked_list.append(7)
  linked_list.print()

  linked_list.delete(7)
  linked_list.print()

  print(linked_list.search(5).key)
  linked_list.reverse()
  linked_list.print()

# test()

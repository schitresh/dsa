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

def linked_list_from_array(array):
  linked_list = LinkedList()

  for item in array:
    linked_list.append(item)

  return linked_list

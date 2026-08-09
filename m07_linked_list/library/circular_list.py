from library.linked_list import Node, LinkedList

class CircularList(LinkedList):
  # Utils

  def print(self):
    temp = self.head
    if not temp:
      print()
      return

    print(temp.key, end=' ')
    temp = temp.next

    while temp != self.head:
      print(temp.key, end=' ')
      temp = temp.next

    print()

  def length(self):
    temp = self.head
    if not temp:
      return 0

    length = 1
    while temp.next != self.head:
      length += 1
      temp = temp.next

    return length

  def last_node(self):
    temp = self.head
    if not temp:
      return

    while temp.next != self.head:
      temp = temp.next

    return temp

  # Insertion

  def append(self, key):
    node = Node(key)

    if not self.head:
      node.next = node
      self.head = node
      return node

    last = self.last_node()
    last.next = node
    node.next = self.head
    return node

  def prepend(self, key):
    node = self.append(key)
    self.head = node
    return node

  # Deletion

  def delete(self, key):
    prev = self.head
    temp = prev.next

    while prev.key == key:
      del prev
      self.head = temp
      prev = temp
      temp = temp.next

    while temp != self.head:
      if temp.key == key:
        prev.next = temp.next
        del temp
        temp = prev

      prev = temp
      temp = temp.next

  # Search

  def search(self, key):
    if not self.head:
      return

    if self.head.key == key:
      return self.head

    temp = self.head.next
    while temp != self.head:
      if temp.key == key:
        return temp
      temp = temp.next

  # Reversal

  def reverse(self):
    prev = self.head
    if not prev:
      return

    temp = prev.next
    prev.next = None
    while temp != self.head:
      temp_next = temp.next
      temp.next = prev
      prev = temp
      temp = temp_next

    self.head.next = prev

def circular_list_from_array(array):
  linked_list = CircularList()

  for item in array:
    linked_list.append(item)

  return linked_list

def test():
  linked_list = CircularList()

  print('Insertion:')
  for i in range(5):
    linked_list.append(i)
  for i in range(5, 10):
    linked_list.prepend(i)
  linked_list.prepend(7)
  linked_list.append(7)
  linked_list.print()

  print('Deletion(7):')
  linked_list.delete(7)
  linked_list.print()

  print('Search(5):', linked_list.search(5).key)
  print('Search(9):', linked_list.search(9).key)
  print('Search(4):', linked_list.search(4).key)

  print('Reversal:')
  linked_list.reverse()
  linked_list.print()

# Do not execute while importing it in another file
if __name__ == '__main__':
  test()

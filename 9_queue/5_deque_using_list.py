class Node:
  def __init__(self, key) -> None:
    self.key = key
    self.prev = None
    self.next = None

# Time Complexity: O(1) for both push & for pop
# Auxiliary Space: O(n)
class Deque:
  def __init__(self) -> None:
    self.head = None
    self.tail = None
    self.size = 0

  # Utils

  def print(self):
    temp = self.head
    while temp:
      if temp.next:
        print(temp.key, end=', ')
      else:
        print(temp.key)

      temp = temp.next

  def clear(self):
    temp = self.head
    while temp:
      next = temp.next
      del temp
      temp = next

  # Actions

  def append_left(self, item):
    node = Node(item)

    if self.head:
      self.head.prev = node
      node.next = self.head

    self.head = node

    if not self.tail:
      self.tail = node

  def append(self, item):
    node = Node(item)

    if self.tail:
      self.tail.next = node
      node.prev = self.tail

    self.tail = node

    if not self.head:
      self.head = node

  def pop_left(self):
    if not self.head:
      return

    item = self.head.key
    temp = self.head.next
    if temp:
      temp.prev = None

    if self.head == self.tail:
      self.tail = temp

    del self.head
    self.head = temp

    return item

  def pop(self):
    if not self.tail:
      return

    item = self.tail.key
    temp = self.tail.prev
    if temp:
      temp.next = None

    if self.head == self.tail:
      self.head = temp

    del self.tail
    self.tail = temp

    return item

def test():
  deque = Deque()
  deque.append_left(1)
  deque.append_left(2)
  deque.append(5)
  deque.append(6)
  deque.print()

  print(deque.pop_left())
  for _ in range(3): deque.pop_left()

  deque.append_left(1)
  deque.append_left(2)
  deque.print()

  print(deque.pop())
  for _ in range(3): deque.pop()

  deque.append(5)
  deque.append(6)
  deque.print()

test()

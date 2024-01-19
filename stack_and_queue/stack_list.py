class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

class Stack:
  def __init__(self):
    self.head = None
    self._size = 0

  def size(self):
    return self._size

  def empty(self):
    return self.head is None

  def top(self):
    if self.empty(): return -1
    return self.head.data

  def push(self, data):
    node = Node(data)

    if self.head: node.next = self.head
    self.head = node

    self._size += 1

  def pop(self):
    if self.empty(): return

    data = self.top()
    second = self.head.next
    del self.head
    self.head = second

    self._size -= 1
    return data

def test():
  stack = Stack()

  for i in range(1, 6):
    stack.push(i)

  print('Pop (5):', stack.pop())
  print('Size (4):', stack.size())
  print('Top (4):', stack.top())
  print('Empty (False):', stack.empty())

# test()

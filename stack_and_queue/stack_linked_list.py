class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

class Stack:
  def __init__(self):
    self.head = None
    self._size = 0

  def push(self, data):
    node = Node(data)

    if self.head: node.next = self.head
    self.head = node

    self._size += 1

  def pop(self):
    if self.empty(): return -1

    data = self.front()
    next = self.head.next
    del self.head
    self.head = next

    self._size -= 1
    return data

  def size(self):
    return self._size

  def front(self):
    if self.empty(): return -1
    return self.head.data

  def empty(self):
    return self.head == None

q = Stack()
q.push(1)
q.push(2)
q.push(3)
print('pop', q.pop())
print('size', q.size())
print('front', q.front())
print('empty', q.empty())

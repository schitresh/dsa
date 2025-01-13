class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

class Queue:
  def __init__(self):
    self.head = None
    self.tail = None
    self._size = 0

  def size(self):
    return self._size

  def empty(self):
    return self.head is None

  def front(self):
    if self.empty(): return
    return self.head.data

  def push(self, data):
    node = Node(data)

    if self.head: self.tail.next = node
    else: self.head = node

    self.tail = node
    self._size += 1

  def pop(self):
    if self.empty(): return
    if self.tail == self.head: self.tail = None

    data = self.front()
    second = self.head.next
    del self.head
    self.head = second

    self._size -= 1
    return data

def test():
  queue = Queue()

  for i in range(1, 6):
    queue.push(i)

  print('Pop (1):', queue.pop())
  print('Size (4):', queue.size())
  print('Top (2):', queue.front())
  print('Empty (False):', queue.empty())

test()

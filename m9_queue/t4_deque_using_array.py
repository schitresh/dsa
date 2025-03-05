# Time Complexity: O(1) for both push & for pop
# Auxiliary Space: O(n)
class Deque:
  def __init__(self, capacity) -> None:
    self.capacity = capacity
    self.array = [None] * capacity
    self.front = 0
    self.rear = 0
    self.size = 0

  # Utils

  def empty(self):
    return self.size == 0

  def full(self):
    return self.size == self.capacity

  def print(self):
    print(self.array)

  def clear(self):
    self.__init__(self.capacity)

  # Actions

  def append_left(self, item):
    if self.full():
      return

    if self.size > 0:
      self.front = (self.front - 1) % self.capacity

    self.size += 1
    self.array[self.front] = item

  def append(self, item):
    if self.full():
      return

    if self.size > 0:
      self.rear = (self.rear + 1) % self.capacity

    self.size += 1
    self.array[self.rear] = item

  def pop_left(self):
    if self.empty():
      return

    self.size -= 1
    item = self.array[self.front]
    self.array[self.front] = None

    if self.size > 0:
      self.front = (self.front + 1) % self.capacity
    return item

  def pop(self):
    if self.empty():
      return

    self.size -= 1
    item = self.array[self.rear]
    self.array[self.rear] = None

    if self.size > 0:
      self.rear = (self.rear - 1) % self.capacity

    return item

def test():
  deque = Deque(10)
  deque.append_left(1)
  deque.append_left(2)
  deque.append(5)
  deque.append(6)
  print(deque.front, deque.rear)
  deque.print()

  print(deque.pop_left())
  for _ in range(3): deque.pop_left()
  print(deque.front, deque.rear)

  deque.append_left(1)
  deque.append_left(2)
  deque.append(5)
  deque.append(6)
  print(deque.front, deque.rear)
  deque.print()

  print(deque.pop())
  for _ in range(3): deque.pop()
  print(deque.front, deque.rear)

test()

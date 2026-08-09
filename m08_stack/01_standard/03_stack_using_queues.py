from queue import PriorityQueue, Queue
from utils import print_class_name

# Push the new item in the queue directly, then pop all the old items and push them again.
# This way the new item will be at the front.
# Another way can be to do this while popping. Pop all the (size - 1) items and push them
# again. Pop the last item and return it.
# Time Complexity: O(n) for both push & pop
# Auxiliary Space: O(n)
class Stack:
  def __init__(self) -> None:
    self.queue = Queue()

  def put(self, item):
    count = self.queue.qsize()
    self.queue.put(item)

    for _ in range(count):
      front = self.queue.get()
      self.queue.put(front)

  def get(self):
    if not self.queue.empty():
      return self.queue.get()

# Using Priority Queue (or Heap)
# Time Complexity: O(log(n)) for both push & pop
# Auxiliary Space: O(n)
class Stack2:
  def __init__(self) -> None:
    self.queue = PriorityQueue()

  def put(self, item):
    count = self.queue.qsize() + 1
    self.queue.put([-count, item])

  def get(self):
    if not self.queue.empty():
      item = self.queue.get()
      return item[1]

def test(klass):
  print_class_name(klass)
  stack = klass()
  stack.put(1)
  stack.put(2)
  stack.put(3)
  print(stack.get())
  print(stack.get())

test(Stack)
test(Stack2)

from queue import LifoQueue

# Pop all the old items and push them to a temp stack
# Push the new item in the stack
# And move the items from the temp stack to the original stack

# Another way can be to do this while popping
# Pop all the (size - 1) and push them to a temp stack
# Pop the last item to return it and swap the original and the temp stack
# Time Complexity: O(n) for push & O(1) for pop
# Auxiliary Space: O(n)
class Queue:
  def __init__(self) -> None:
    self.stack = LifoQueue()
    self.temp_stack = LifoQueue()

  def put(self, item):
    while not self.stack.empty():
      top = self.stack.get()
      self.temp_stack.put(top)

    self.stack.put(item)

    while not self.temp_stack.empty():
      top = self.temp_stack.get()
      self.stack.put(top)

  def get(self):
    if not self.stack.empty():
      return self.stack.get()

def test(klass):
  queue = klass()
  queue.put(1)
  queue.put(2)
  queue.put(3)
  print(queue.get())
  print(queue.get())

test(Queue)

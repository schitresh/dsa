from queue import LifoQueue
from utils import print_class_name

# Pop all the old items and push them to a temp stack
# Push the new item in the stack
# And move the items from the temp stack to the original stack

# Another way can be to do this while popping
# Pop all the (size - 1) and push them to a temp stack
# Pop the last item to return it and swap the original and the temp stack
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
  print_class_name(klass)
  stack = klass()
  stack.put(1)
  stack.put(2)
  stack.put(3)
  print(stack.get())
  print(stack.get())

test(Queue)

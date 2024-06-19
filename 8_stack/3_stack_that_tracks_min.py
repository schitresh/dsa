from queue import LifoQueue
from utils import print_class_name

# Get minimum element in the stack in constant time
# An auxiliary stack can be maintained will be keep track of the min elements
# Modify put & get methods such that the top of the auxiliary stack in always the min
class Stack(LifoQueue):
  def __init__(self, maxsize: int = 0) -> None:
    super().__init__(maxsize)
    self.min_stack = LifoQueue()

  def put(self, item):
    if self.empty():
      super().put(item)
      self.min_stack.put(item)
    else:
      super().put(item)
      mini = self.min_stack.get()
      self.min_stack.put(mini)

      if item < mini:
        self.min_stack.put(item)

  def get(self):
    item = super().get()
    mini = self.min_stack.get()

    if item != mini:
      self.min_stack.put(mini)

    return item

  def min(self):
    mini = self.min_stack.get()
    self.min_stack.put(mini)
    return mini

# Store min element with each item
class Stack2(LifoQueue):
  def __init__(self, maxsize: int = 0) -> None:
    super().__init__(maxsize)
    self.min_item = None

  def put(self, item):
    if not self.min_item or item < self.min_item:
      self.min_item = item

    super().put([item, self.min_item])

  def get(self):
    item_and_min = super().get()
    return item_and_min[0]

  def min(self):
    return self.min_item

def test(klass):
  print_class_name(klass)

  stack = klass()
  stack.put(20)
  stack.put(30)
  print(stack.min())

  stack.put(40)
  stack.put(10)
  print(stack.min())

  stack.get()
  print(stack.min())
  print()

test(Stack)
test(Stack2)

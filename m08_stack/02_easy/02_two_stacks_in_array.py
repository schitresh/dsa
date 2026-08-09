from utils import print_class_name

# Create a data structure that can support two stacks using only one array.
# It should support the following functions:
# push1(x) pushes x to the first stack
# push2(x) pushes x to the second stack
# pop1() pops and returns an element from the first stack
# pop2() pops and returns an element from the second stack

# Divide the stack array in two parts
# Time Complexity: O(1) for both push & pop
# Auxiliary Space: O(n)
class Solution:
  def __init__(self, size):
    self.size = size
    self.stack = [None] * size
    self.top1 = size // 2 + 1
    self.top2 = size // 2

  def push1(self, item):
    if self.top1 == 0:
      print('Stack full:', item)
      return

    self.top1 -= 1
    self.stack[self.top1] = item

  def push2(self, item):
    if self.top2 == self.size - 1:
      print('Stack full:', item)
      return

    self.top2 += 1
    self.stack[self.top2] = item

  def pop1(self):
    if self.top1 == self.size // 2 + 1:
      print('Stack empty')
      return None

    item = self.stack[self.top1]
    self.top1 += 1
    return item

  def pop2(self):
    if self.top2 == self.size // 2:
      print('Stack empty')
      return None

    item = self.stack[self.top2]
    self.top2 -= 1
    return item

# Keep the stack sizes dynamic
# Time Complexity: O(1) for both push & pop
# Auxiliary Space: O(n)
class Solution2:
  def __init__(self, size):
    self.size = size
    self.stack = [None] * size
    self.top1 = -1
    self.top2 = size

  def push1(self, item):
    if self.top1 == self.top2 - 1:
      print('Stack full:', item)
      return

    self.top1 += 1
    self.stack[self.top1] = item

  def push2(self, item):
    if self.top2 == self.top1 + 1:
      print('Stack full:', item)
      return

    self.top2 -= 1
    self.stack[self.top2] = item

  def pop1(self):
    if self.top1 == -1:
      print('Stack empty')
      return None

    item = self.stack[self.top1]
    self.top1 -= 1
    return item

  def pop2(self):
    if self.top2 == self.size:
      print('Stack empty')
      return None

    item = self.stack[self.top2]
    self.top2 += 1
    return item

def test(klass):
  print_class_name(klass)
  stack = klass(5)
  stack.push1(5)
  stack.push2(10)
  stack.push2(15)
  stack.push1(11)
  stack.push2(7)
  stack.push2(40)
  print(stack.stack)

  print('Pop from stack 1:', stack.pop1())
  print('Pop from stack 2:', stack.pop2())
  print()

test(Solution)
test(Solution2)

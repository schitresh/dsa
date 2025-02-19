from utils import test_class

# Reverse a stack using recursion, without using any loop.

examples = [
  {
    'input': [[1, 2, 3, 4]],
    'output': [4, 3, 2, 1],
  },
  {
    'input': [[2, 4, 3, 1, 5]],
    'output': [5, 1, 3, 4, 2],
  },
]

# Using Stack
# Time Complexity: O(n^2)
# Auxiliary Space: O(n)
class Solution:
  def solve(self, stack):
    temp_stack = []
    len_items = len(stack)

    for i in range(len_items):
      top = stack.pop()

      for _ in range(len_items - i - 1):
        temp_stack.append(stack.pop())

      stack.append(top)

      while len(temp_stack) > 0:
        stack.append(temp_stack.pop())

    return stack

test_class(Solution, examples)

# Using Recursive Stack
# Time Complexity: O(n^2)
# Auxiliary Space: O(n), due to recursive stack
class Solution2:
  def solve(self, stack):
    self.stack = stack
    self.reverse()
    return stack

  def reverse(self):
    if len(self.stack) == 0: return

    top = self.stack.pop()
    self.reverse()
    self.insert_at_bottom(top)

  def insert_at_bottom(self, item):
    if len(self.stack) == 0:
      self.stack.append(item)
      return

    temp = self.stack.pop()
    self.insert_at_bottom(item)
    self.stack.append(temp)

test_class(Solution2, examples)

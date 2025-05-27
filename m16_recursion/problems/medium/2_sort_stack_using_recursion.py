from utils import test_class

# Sort a given stack using recursion. Only the standard stack operations are
# allowed, that is push, pop, empty?, front, size.

examples = [
  {
    'input': [[10, 7, 16, 9, 20, 5]],
    'output': [5, 7, 9, 10, 16, 20],
  },
  {
    'input': [[0, -2, 2, -1, 3, 1]],
    'output': [-2, -1, 0, 1, 2, 3]
  },
]

# Insertion Sort
# Time Complexity: O(n^2)
# Auxiliary Space: O(n), due to recursive stack
class Solution:
  def solve(self, stack):
    self.stack = stack
    self.sort_stack()
    return self.stack

  def sort_stack(self):
    if len(self.stack) == 0: return

    num = self.stack.pop()
    self.sort_stack()
    self.sorted_insert(num)

  def sorted_insert(self, num):
    if len(self.stack) == 0:
      self.stack.append(num)
      return

    curr = self.stack.pop()

    if curr <= num:
      self.stack.append(curr)
      self.stack.append(num)
    else:
      self.sorted_insert(num)
      self.stack.append(curr)

test_class(Solution, examples)

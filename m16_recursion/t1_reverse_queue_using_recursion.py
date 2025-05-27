from utils import test_class

# Reverse a given queue using recursion. Only the standard queue operations are
# allowed, that is push, pop, empty?, front, size.

examples = [
  {
    'input': [[10, 7, 16, 9, 20, 5]],
    'output': [5, 20, 9, 16, 7, 10],
  },
  {
    'input': [[0, -2, 2, -1, 3, 1]],
    'output': [1, 3, -1, 2, -2, 0]
  },
]

# Insertion Sort
# Time Complexity: O(n)
# Auxiliary Space: O(n), due to recursive stack
class Solution:
  def solve(self, queue):
    if len(queue) == 0: return

    num = queue.pop(0)
    self.solve(queue)
    queue.append(num)
    return queue

test_class(Solution, examples)

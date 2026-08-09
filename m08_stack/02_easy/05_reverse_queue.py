from queue import LifoQueue
from utils import test_class

# Given a queue, reverse it using stack.

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
# Time Complexity: O(n)
# Auxiliary Space: O(n)
class Solution:
  def solve(self, queue):
    stack = LifoQueue()

    while len(queue) > 0:
      front = queue.pop(0)
      stack.put(front)

    while not stack.empty():
      top = stack.get()
      queue.append(top)

    return queue

test_class(Solution, examples)

# Using Recursive Stack
# Time Complexity: O(n)
# Auxiliary Space: O(n), due to recursive stack
class Solution2:
  def solve(self, queue):
    self.queue = queue
    self.reverse()
    return queue

  def reverse(self):
    if len(self.queue) == 0: return
    front = self.queue.pop(0)
    self.reverse()
    self.queue.append(front)

test_class(Solution2, examples)

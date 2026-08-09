from queue import LifoQueue
from utils import test_class

# Given a queue, reverse it using stack.

examples = [
  {
    'input': [[1, 2, 3, 4], 2],
    'output': [2, 1, 3, 4],
  },
  {
    'input': [[2, 4, 3, 1, 5], 3],
    'output': [3, 4, 2, 1, 5],
  },
]

# Using Stack
# Time Complexity: O(n)
# Auxiliary Space: O(n)
class Solution:
  def solve(self, queue, k):
    stack = LifoQueue()
    i = 0

    while i < k and len(queue) > 0:
      front = queue.pop(0)
      stack.put(front)
      i += 1

    while not stack.empty():
      top = stack.get()
      queue.append(top)

    i = 0
    while i < len(queue) - k:
      front = queue.pop(0)
      queue.append(front)
      i += 1

    return queue

test_class(Solution, examples)

# Using Recursive Stack
# Time Complexity: O(n)
# Auxiliary Space: O(n), due to recursive stack
class Solution2:
  def solve(self, queue, k):
    self.queue = queue
    self.reverse_k(k)

    i = 0
    while i < len(queue) - k:
      front = queue.pop(0)
      queue.append(front)
      i += 1

    return queue

  def reverse_k(self, k):
    if k == 0 or len(self.queue) == 0: return
    front = self.queue.pop(0)
    self.reverse_k(k - 1)
    self.queue.append(front)

test_class(Solution2, examples)

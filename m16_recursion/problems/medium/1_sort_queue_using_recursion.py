from utils import test_class

# Sort a given queue using recursion. Only the standard queue operations are
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
  def solve(self, queue):
    self.queue = queue
    self.sort_queue()
    return self.queue

  def sort_queue(self):
    if len(self.queue) == 0: return

    num = self.queue.pop(0)
    self.sort_queue()
    self.sorted_insert(num, len(self.queue))

  def sorted_insert(self, sort_num, rem_len):
    if rem_len == 0:
      self.queue.append(sort_num)
      return

    num = self.queue.pop(0)

    if sort_num <= num:
      self.queue.append(sort_num)
      self.queue.append(num)
      self.move_to_last(rem_len - 1)
    else:
      self.queue.append(num)
      self.sorted_insert(sort_num, rem_len - 1)

  def move_to_last(self, n):
    if n == 0: return

    num = self.queue.pop(0)
    self.queue.append(num)
    self.move_to_last(n - 1)

test_class(Solution, examples)

from utils import test_class

# Generate all Subarrays
examples = [
  {
    'input': [[1, 2]],
    'output': [[1], [1, 2], [2]]
  },
  {
    'input': [[1, 2, 3]],
    'output': [[1], [1, 2], [1, 2, 3], [2], [2, 3], [3]]
  }
]

# Time Complexity: O(2^n)
# Space Complexity: O(2^n)
class Solution:
  def __init__(self):
    self.subarrays = []

  def generate_subarrays(self, array, left, right):
    if left >= len(array):
      return

    if right >= len(array):
      left += 1
      self.generate_subarrays(array, left, left)
      return

    self.subarrays.append(array[left : right + 1])
    self.generate_subarrays(array, left, right + 1)

  def solve(self, array):
    self.generate_subarrays(array, 0, 0)
    return self.subarrays

test_class(Solution, examples)

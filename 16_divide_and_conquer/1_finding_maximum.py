from utils import test_class

examples = [
  {
    'input': [[1, 2, 3, 4, 5]],
    'output': 5
  },
  {
    'input': [[5, 6, 3, 2, 1, 4]],
    'output': 6
  }
]

# Tournament Method
# Number of comparisons: (3/2) * n - 2
# In linear search: best case: ((n - 2) + 1),  worst case: (2 * (n - 2) + 1 )
# Time Complexity: O(n)
# Auxiliary Space: O(log(n)), due to recursive stack
class Solution:
  def find_max(self, array, left, right):
    if left > right:
      return float('inf')

    if left == right:
      return array[left]

    mid = left + (right - left) // 2
    left_max = self.find_max(array, left, mid)
    right_max = self.find_max(array, mid + 1, right)

    return max(left_max, right_max)

  def solve(self, array):
    return self.find_max(array, 0, len(array) - 1)

test_class(Solution, examples)

from utils import test_class

# Reverse an Array
examples = [
  {
    'input': [[1, 2, 3, 4, 5]],
    'output': [5, 4, 3, 2, 1]
  },
  {
    'input': [[1, 2, 3, 4, 5, 6]],
    'output': [6, 5, 4, 3, 2, 1]
  }
]

# Time Complexity: O(n)
# Space Complexity: O(1)
class Solution:
  def solve(self, array):
    left = 0
    right = len(array) - 1

    while left < right:
      array[left], array[right] = array[right], array[left]
      left += 1
      right -= 1

    return array

test_class(Solution, examples)

from utils import test_class

# Given a binary array which is sorted in non-increasing order, count the number of 1’s
# in it.

examples = [
  {
    'input': [[1, 1, 0, 0, 0, 0, 0]],
    'output': 2,
  },
  {
    'input': [[1, 1, 1, 0, 0, 0]],
    'output': 3,
  },
  {
    'input': [[1, 1, 1, 1, 0, 0]],
    'output': 4,
  },
  {
    'input': [[1, 1, 1, 1, 0, 0, 0]],
    'output': 4,
  },
  {
    'input': [[1, 1, 1, 1, 1, 1, 1]],
    'output': 7,
  },
  {
    'input': [[0, 0, 0, 0, 0, 0, 0]],
    'output': 0,
  },
]

# Time Complexity: O(log(n))
# Auxiliary Space: O(1)
class Solution:
  def solve(self, array):
    left = 0
    right = len(array) - 1

    while left <= right:
      mid = left + (right - left) // 2

      if array[mid] == 0:
        right = mid - 1
      else:
        left = mid + 1

    # If element is 0, we're always moving it before, hence last 1 should be at right
    # index. That is, count will be right + 1
    # If element is 1, we're always moving it after, hence last 1 should be just before
    # left index. That is, count will be left.
    return left

test_class(Solution, examples)

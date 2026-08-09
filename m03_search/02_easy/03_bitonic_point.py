from utils import test_class

# Given an array of integers which is initially strictly increasing and then strictly
# decreasing, find the bitonic point.
# Bitonic Point is a point in bitonic sequence before which elements are strictly
# increasing and after which elements are strictly decreasing.

examples = [
  {
    'input': [[1, 2, 4, 5, 7, 8, 3]],
    'output': 8,
  },
  {
    'input': [[1, 2, 6, 5, 4, 3]],
    'output': 6,
  },
  {
    'input': [[10, 20, 30, 40, 50]],
    'output': 50,
  },
  {
    'input': [[120, 100, 80, 20, 0]],
    'output': 120,
  },
]

# Linear Search
# Time Complexity: O(n)
# Auxiliary Space: O(1)
class Solution:
  def solve(self, array):
    biotonic_point = array[0]

    for i in range(1, len(array)):
      if array[i - 1] < array[i]:
        biotonic_point = array[i]
      else:
        break

    return biotonic_point

test_class(Solution, examples)

# Binary Search
# Time Complexity: O(log(n))
# Auxiliary Space: O(1)
class Solution2:
  def solve(self, array):
    left = 0
    right = len(array) - 1

    while left <= right:
      mid = left + (right - left) // 2

      if mid == 0:
        return array[0]
      elif array[mid - 1] < array[mid]:
        left = mid + 1
      else:
        right = mid - 1

    return array[right]


test_class(Solution2, examples)

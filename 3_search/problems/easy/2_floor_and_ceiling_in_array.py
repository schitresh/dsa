from utils import test_class

# Given a sorted array and a value k, find the floor and the ceiling of k.
# The ceiling of k is the smallest element in the array greater than or equal to k.
# The floor of k is the greatest element smaller than or equal to k.

examples = [
  {
    'input': [0, [1, 2, 8, 10, 10, 12, 19]],
    'output': [None, 1],
  },
  {
    'input': [1, [1, 2, 8, 10, 10, 12, 19]],
    'output': [1, 1],
  },
  {
    'input': [5, [1, 2, 8, 10, 10, 12, 19]],
    'output': [2, 8],
  },
  {
    'input': [20, [1, 2, 8, 10, 10, 12, 19]],
    'output': [19, None],
  },
  {
    'input': [4, [1, 2, 3, 5]],
    'output': [3, 5],
  },
]

# Linear Search
# Time Complexity: O(n)
# Auxiliary Space: O(1)
class Solution:
  def solve(self, key, array):
    floor = None
    ceiling = None

    for i in range(len(array)):
      if array[i] <= key:
        floor = array[i]

    for i in range(len(array) - 1, -1, -1):
      if key <= array[i]:
        ceiling = array[i]

    return [floor, ceiling]

test_class(Solution, examples)

# Binary Search
# Time Complexity: O(log(n))
# Auxiliary Space: O(1)
class Solution2:
  def solve(self, key, array):
    floor = None
    ceiling = None

    left = 0
    right = len(array) - 1

    while left <= right:
      mid = left + (right - left) // 2

      if array[mid] < key:
        left = mid + 1
      elif array[mid] > key:
        right = mid - 1
      else:
        floor = array[mid]
        ceiling = array[mid]
        break

    if right < 0: floor = None
    else: floor = array[right]

    if left >= len(array): ceiling = None
    else: ceiling = array[left]

    return [floor, ceiling]

test_class(Solution2, examples)

# Using in-built functions
# Time Complexity: O(log(n))
# Auxiliary Space: O(1)
from bisect import bisect_left

class Solution3:
  def solve(self, key, array):
    # Finds the index at which key should be inserted to maintain sorted order
    insert_at = bisect_left(array, key)
    floor = None
    ceiling = None

    if insert_at >= len(array):
      floor = array[-1]
    elif array[insert_at] == key:
      floor = array[insert_at]
    elif insert_at > 0:
      floor = array[insert_at - 1]

    if insert_at < len(array):
      ceiling = array[insert_at]

    return [floor, ceiling]

test_class(Solution3, examples)

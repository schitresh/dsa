from utils import test_class

# Given an array of integers, find the maximum sum of two elements such that sum is
# closest to zero. If we have multiple such pairs, return the maximum sum.

examples = [
  {
    'input': [[-8, 5, 2, -6]],
    'output': -1,
  },
  {
    'input': [[-8, 5, 2, -6, 4, -3]],
    'output': 1,
  },
  {
    'input': [[0, -8, -6, 3]],
    'output': 3,
  },
  {
    'input': [[4, 3, 2, 1]],
    'output': 3,
  },
]

# Generate all pairs, get the pair with the minimum absolute sum
# Time Complexity: O(n^2)
# Auxiliary Space: O(1)

# Sorting with binary search
# Time Complexity: O(n * log(n))
# Auxiliary Space: O(1)
class Solution:
  def solve(self, array):
    array.sort()
    closest_sum = float('inf')

    for i in range(len(array)):
      left = i + 1
      right = len(array) - 1

      while left <= right:
        mid = left + (right - left) // 2
        pair_sum = array[i] + array[mid]
        if pair_sum == 0: return 0

        if abs(pair_sum) < abs(closest_sum):
          closest_sum = pair_sum
        elif abs(pair_sum) == abs(closest_sum):
          closest_sum = max(closest_sum, pair_sum)

        if pair_sum < 0: left = mid + 1
        else: right = mid - 1

    return closest_sum

test_class(Solution, examples)

# Sorting with two pointers
# Time Complexity: O(n * log(n))
# Auxiliary Space: O(1)
class Solution2:
  def solve(self, array):
    array.sort()
    closest_sum = float('inf')
    left = 0
    right = len(array) - 1

    while left < right:
      pair_sum = array[left] + array[right]
      if pair_sum == 0: return 0

      if abs(pair_sum) < abs(closest_sum):
        closest_sum = pair_sum
      elif abs(pair_sum) == abs(closest_sum):
        closest_sum = max(closest_sum, pair_sum)

      if pair_sum < 0:
        left += 1
      else:
        right -= 1

    return closest_sum

test_class(Solution2, examples)

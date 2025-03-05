from utils import test_class

# Given an array of non-negative integers, find the minimum number of elements such that
# their sum should be greater than the sum of the rest of the elements of the array.

examples = [
  {
    'input': [[3, 1, 7, 1]],
    'output': 1
    # Smallest subset is [7], sum of this subset is greater than sum of all other
    # elements left after removing subset [7] from the array
  },
  {
    'input': [[2, 1, 2]],
    'output': 2, # [2, 1]
  }
]

# Time Complexity: O(n^2)
# Auxiliary Space: O(1)
class Solution:
  def solve(self, array):
    total_sum = sum(array)
    min_items = float('inf')

    for i in range(len(array)):
      curr_sum  = 0

      for j in range(i, len(array)):
        curr_sum += array[j]

        if curr_sum > total_sum - curr_sum:
          min_items = min(min_items, j - i + 1)
          break

    return min_items

test_class(Solution, examples)

# Time Complexity: O(n * log(n))
# Auxiliary Space: O(1)
class Solution2:
  def solve(self, array):
    array.sort()
    total_sum = sum(array)
    min_items = float('inf')

    curr_sum  = 0
    for i in range(len(array) - 1, -1, -1):
      curr_sum += array[i]
      if curr_sum > total_sum - curr_sum:
        min_items = min(min_items, len(array) - i)
        break

    return min_items

test_class(Solution2, examples)

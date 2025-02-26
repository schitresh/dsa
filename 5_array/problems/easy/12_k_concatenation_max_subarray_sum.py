from utils import test_class

# Given an array and a number k, find the largest sum of contiguous array in the
# modified array which is formed by repeating the given array k times.

examples = [
  {
    'input': [[-1, 10, 20], 2],
    'output': 59,
  },
  {
    'input': [[-1, -2, -3], 3],
    'output': -1,
  },
  {
    'input': [[10, 20, -30, -1], 3],
    'output': 30,
  },
]

# Kadane's Algorithm with array concatenated k times
# Time Complexity: O(n * k)
# Auxiliary Space: O(n * k), to stored the concatenated array
class Solution:
  def solve(self, array, k):
    array = array * k
    max_sum = array[0]
    local_sum = array[0]

    for i in range(1, len(array)):
      local_sum = max(local_sum + array[i], array[i])
      max_sum = max(max_sum, local_sum)

    return max_sum

test_class(Solution, examples)

# Kadane's Algorithm with modular arithmetic
# Time Complexity: O(n)
# Auxiliary Space: O(1)
class Solution2:
  def solve(self, array, k):
    max_sum = array[0]
    local_sum = array[0]

    for i in range(1, len(array) * k):
      idx = i % len(array)
      local_sum = max(local_sum + array[idx], array[idx])
      max_sum = max(max_sum, local_sum)

    return max_sum

test_class(Solution2, examples)

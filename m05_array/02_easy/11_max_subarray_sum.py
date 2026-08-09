from utils import test_class

# Given an array, find the subarray that has the maximum sum and return its sum.

examples = [
  {
    'input': [[-2, -4]],
    'output': -2,
  },
  {
    'input': [[5, 4, 1, 7, 8]],
    'output': 25,
  },
  {
    'input': [[2, 3, -8, 7, -1, 2, 3]],
    'output': 11,
  },
]

# Naive Approach: For each subarray, calculate the sum
# Time Complexity: O(n ^ 2)
# Auxiliary Space: O(1)

# Kadane's Algorithm
# Time Complexity: O(n)
# Auxiliary Space: O(1)
class Solution:
  def solve(self, array):
    max_sum = array[0]
    local_sum = array[0]

    for i in range(1, len(array)):
      local_sum = max(local_sum + array[i], array[i])
      max_sum = max(max_sum, local_sum)

    return max_sum

test_class(Solution, examples)

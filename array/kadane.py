from utils import test

# Kadane Algorithm
# Maximum sum of contiguous subarray
examples = [
  {
    'input': [[-2, -3, 4, -1, -2, 1, 5, -3]],
    'output': 7
  }
]

# Time Complexity: O(n)
# Space Complexity: O(1)
class Solution:
  def solve(self, array):
    global_max = array[0]
    local_max = 0

    for item in array:
      local_max += item
      local_max = max(local_max, item)
      global_max = max(global_max, local_max)

    return global_max

test(Solution, examples)

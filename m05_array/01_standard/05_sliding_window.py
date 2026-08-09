from utils import test_class

# Given an array, find the subarray of size k having the maximum sum

examples = [
  {
    'input': [[16, 12, 9, 19, 11, 8], 3],
    'output': 40
  }
]

# Sliding Window Algorithm
# Time Complexity: O(n)
# Auxiliary Space: O(1)
class Solution:
  def solve(self, array, window_size):
    if len(array) < window_size: return 0

    window_sum = sum(array[:window_size])
    max_sum = window_sum

    for index in range(len(array) - window_size):
      window_sum -= array[index]
      window_sum += array[index + window_size]
      max_sum = max(max_sum, window_sum)

    return max_sum

test_class(Solution, examples)

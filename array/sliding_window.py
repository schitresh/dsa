from utils import test

# Sliding Window Algo
# Given an array & size k, find the subarray of length with size k having the max sum
examples = [
  {
    'input': [[16, 12, 9, 19, 11, 8], 3],
    'output': 40
  }
]

class Solution:
  def solve(self, array, ksize):
    if len(array) < ksize:
      return 0

    window_sum = sum(array[:ksize])
    max_sum = window_sum

    for index in range(len(array) - ksize):
      window_sum -= array[index]
      window_sum += array[index + ksize]
      max_sum = max(max_sum, window_sum)

    return max_sum

test(Solution, examples)

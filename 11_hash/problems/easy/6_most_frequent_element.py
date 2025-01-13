from utils import test_class

# Given an array, find the most frequent element in it. If there are multiple elements
# that appear a maximum number of times, return any one of them.

examples = [
  {
    'input': [[1, 3, 2, 1, 4, 1]],
    'output': 1,
  },
  {
    'input': [[10, 20, 10, 20, 30, 20, 20]],
    'output': 20,
  },
]

# Hashing
# Time Complexity: O(n)
# Auxiliary Space: O(n)
class Solution:
  def solve(self, array):
    freq = {}

    for item in array:
      if item in freq: freq[item] += 1
      else: freq[item] = 1

    return max(freq, key = lambda x: freq[x])

test_class(Solution, examples)

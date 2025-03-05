from utils import test_class

# Given an array of size n and an integer k, find all elements in the array that appear
# more than n/k times.

examples = [
  {
    'input': [[3, 1, 2, 2, 1, 2, 3, 3], 4],
    'output': [2, 3],
  },
  {
    'input': [[9, 8, 7, 9, 2, 9, 7], 3],
    'output': [9],
  },
]

# Hashing
# Time Complexity: O(n)
# Auxiliary Space: O(n)
class Solution:
  def solve(self, array, k):
    target_count = len(array) // k
    result = []
    counts = {}

    for num in array:
      counts[num] = counts.get(num, 0) + 1

    for key, value in counts.items():
      if value > target_count:
        result.append(key)

    return result

test_class(Solution, examples)

# Todo: Moore's Voting Algorithm
# There can be at max k – 1 elements present in the array which appears more than n/k
# times. When we encounter an element which is one of our candidates then increment the
# count else decrement the count.
# Time Complexity: O(n)
#  Auxiliary Space: O(n)
class Solution2:
  def solve(self, array, k):
    counts = {}

    return

test_class(Solution2, examples)

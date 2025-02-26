from utils import test_class

# Given an array of integers, all numbers occur twice except one number which occurs
# once. Find this number.

examples = [
  {
    'input': [[2, 3, 5, 4, 5, 3, 4]],
    'output': 2,
  },
  {
    'input': [[2, 5, 2]],
    'output': 5,
  },
]

# Naive Approach
# Time Complexity: O(n^2)
# Auxiliary Space: O(1)
class Solution:
  def solve(self, array):
    for i in range(len(array)):
      count = 1

      for j in range(i + 1, len(array)):
        if array[i] == array[j]:
          count += 1
          break

      if count == 1:
        return array[i]

    return -1

test_class(Solution, examples)

# Using Hash
# Time Complexity: O(n)
# Auxiliary Space: O(1)
class Solution2:
  def solve(self, array):
    count = {}

    for item in array:
      count[item] = count.get(item, 0) + 1

    for item, freq in count.items():
      if freq == 1: return item

    return -1

test_class(Solution2, examples)

# Using XOR
# Since XOR of two same numbers is 0
# Time Complexity: O(n)
# Auxiliary Space: O(1)
class Solution3:
  def solve(self, array):
    xor = 0

    for item in array:
      xor = xor ^ item

    return xor

test_class(Solution3, examples)

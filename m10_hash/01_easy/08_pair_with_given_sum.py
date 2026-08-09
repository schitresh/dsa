from utils import test_class

# Given an array of n integers and a target value, find whether there is a pair of
# elements in the array whose sum is equal to the target.

examples = [
  {
    'input': [[0, -1, 2, -3, 1], -2],
    'output': [-3, 1],
  },
  {
    'input': [[1, -2, 1, 0, 5], 0],
    'output': [],
  },
]

# Sorting & Two pointers
# Time Complexity: O(n * log(n))
# Auxiliary Space: O(1)
class Solution:
  def solve(self, array, target):
    array.sort()
    left = 0
    right = len(array) - 1

    while left < right:
      pair_sum = array[left] + array[right]
      if pair_sum == target:
        return [array[left], array[right]]

      if pair_sum < target: left += 1
      else: right -= 1

    return []

test_class(Solution, examples)

# Hashing
# Time Complexity: O(n)
# Auxiliary Space: O(n)
class Solution2:
  def solve(self, array, target):
    # Hash set
    complements = set()

    for item in array:
      diff = target - item
      if diff in complements: return [diff, item]
      complements.add(item)

    return []

test_class(Solution2, examples)

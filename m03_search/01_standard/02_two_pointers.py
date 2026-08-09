from utils import test_class

# Given a sorted array and a target, find if there exists any pair of elements such that
# their sum is equal to the target.

examples = [
  {
    'input': [[2, 3, 5, 8, 9, 10, 11], 17],
    'output': [8, 9]
  },
    {
    'input': [[2, 3, 5, 8, 9, 10, 11], 4],
    'output': []
  }
]

# Two Pointer Technique
# Move pointers from either end of the sorted array
# To find a triplet, can loop over the array to keep the third element static
# Time Complexity: O(n)
# Auxiliary Space: O(1)
class Solution:
  def solve(self, array, target):
    left = 0
    right = len(array) - 1

    while left < right:
      pair_sum = array[left] + array[right]

      if pair_sum > target:
        right -= 1
      elif pair_sum < target:
        left += 1
      else:
        return [array[left], array[right]]

    return []

test_class(Solution, examples)

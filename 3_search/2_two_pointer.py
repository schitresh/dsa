from utils import test_class

# Find a pair whose sum is equal to the given number
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

# Time Complexity: O(n)
# Space Complexity: O(1)
class TwoPointer:
  def solve(self, array, target_sum):
    left = 0
    right = len(array) - 1

    while left < right:
      pair_sum = array[left] + array[right]

      if pair_sum > target_sum:
        right -= 1
      elif pair_sum < target_sum:
        left += 1
      else:
        return [array[left], array[right]]

    return []

test_class(TwoPointer, examples)

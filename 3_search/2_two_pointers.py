from utils import test_method

# Find a pair whose sum is equal to the given number in a sorted array
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

# Move pointers from either end of the sorted array
# To find a triplet, can loop over the array to keep the third element static
# Time Complexity: O(n)
# Auxiliary Space: O(1)
def two_pointers(array, target_sum):
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

test_method(two_pointers, examples)

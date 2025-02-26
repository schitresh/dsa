from utils import test_class

# Given an array of 0s and 1s in random order, segregate 0s on left side and 1s on right
# side of the array. Basically, sort the array.

examples = [
  {
    'input': [[0, 1, 0]],
    'output': [0, 0, 1],
  },
  {
    'input': [[1, 1]],
    'output': [1, 1],
  },
  {
    'input': [[0, 1, 0, 1, 0, 0, 1, 1, 1, 0]],
    'output': [0, 0, 0, 0, 0, 1, 1, 1, 1, 1],
  },
]

# Count 0s & 1s
# Time Complexity: O(n), two traversals
# Auxiliary Space: O(1)
class Solution:
  def solve(self, array):
    count_0 = 0
    count_1 = 0

    for num in array:
      if num == 0: count_0 += 1
      else: count_1 += 1

    i = 0
    while count_0 > 0:
      array[i] = 0
      i += 1
      count_0 -= 1

    while count_1 > 0:
      array[i] = 1
      i += 1
      count_1 -= 1

    return array

test_class(Solution, examples)

# Two pointers
# Time Complexity: O(n), one traversal
# Auxiliary Space: O(1)
class Solution2:
  def solve(self, array):
    left = 0
    right = len(array) - 1

    while left < right:
      if array[left] == 0:
        left += 1
      else:
        # Swap if left is 1 and right is 0. But if right is 1, find the next possible
        # right to swap left with i.e. move right but keep left at the same position.
        if array[right] == 0:
          array[left], array[right] = array[right], array[left]
          left += 1

        right -= 1

    return array

test_class(Solution2, examples)

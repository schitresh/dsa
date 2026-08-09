from utils import test_class
from random import randint

# Shuffle an array randomly

examples = [
  {
    'input': [[1, 6, 2, 5, 9, 8, 7, 3, 4]],
    'output': [] # No fixed output
  }
]

# Fisher Yates Algorithm
# Time Complexity: O(n)
# Auxiliary Space: O(1)
class Solution:
  def solve(self, array):
    for index in range(len(array) - 1, 0, -1):
      position = randint(0, index)
      self.swap(array, index, position)

    return array

  def swap(self, array, i, j):
    array[i], array[j] = array[j], array[i]

test_class(Solution, examples)

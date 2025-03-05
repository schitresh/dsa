from utils import test_class
from random import randint

# Shuffle an Array Randomly
examples = [
  {
    'input': [[1, 6, 2, 5, 9, 8, 7, 3, 4]],
  }
]

# Time Complexity: O(n)
# Auxiliary Space: O(1)
class FisherYatesShuffle:
  def swap(self, array, i, j):
    array[i], array[j] = array[j], array[i]

  def solve(self, array):
    for index in range(len(array) - 1, 0, -1):
      position = randint(0, index)
      self.swap(array, index, position)

    return array

for example in examples:
  output = FisherYatesShuffle().solve(*example['input'])
  print(output)

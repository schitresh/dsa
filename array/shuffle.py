from random import randint

examples = [
  {
    'input': [[1, 6, 2, 5, 9, 8, 7, 3, 4]],
  }
]

# Time Complexity: O(n)
# Space Complexity: O(1)
class FisherYatesShuffle:
  def swap(self, array, index_1, index_2):
    array[index_1], array[index_2] = array[index_2], array[index_1]

  def solve(self, array):
    for index in range(len(array) - 1, 0, -1):
      position = randint(0, index)
      self.swap(array, index, position)

    return array

for example in examples:
  output = FisherYatesShuffle().solve(*example['input'])
  print(output)

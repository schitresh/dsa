from utils import test

examples = [
  {
    'input': [[4, 5, 9, 8, 7, 3, 2, 1, 6]],
    'output': [1, 2, 3, 4, 5, 6, 7, 8, 9]
  }
]

# Time Complexity: O(n^2)
## Best Case: O(n)
## Worst Case: O(n^2)
# Space Complexity: O(1)
class BubbleSort:
  def swap(self, array, index_1, index_2):
    array[index_1], array[index_2] = array[index_2], array[index_1]

  def solve(self, array):
    for i in range(len(array)):
      for j in range(len(array) - 1 - i):
        if array[j] > array[j + 1]:
          self.swap(array, j, j + 1)

    return array

test(BubbleSort, examples)

from random import randint
from utils import test

examples = [
  {
    'input': [[4, 5, 9, 8, 7, 3, 2, 1, 6]],
    'output': [1, 2, 3, 4, 5, 6, 7, 8, 9]
  }
]

# Time Complexity: O(n * log(n))
## Best Case: O(n * log(n))
## Worst Case: O(n^2)
# Space Complexity: O(n)
class QuickSort:
  def random_index(self, start, end):
    return randint(start, end)

  def swap(self, array, index_1, index_2):
    array[index_1], array[index_2] = array[index_2], array[index_1]

  def pivot_sort(self, array, start, end):
    pivot = self.random_index(start, end)
    self.swap(array, start, pivot)
    position = start + 1

    for i in range(start + 1, end + 1):
      if array[i] < array[start]:
        self.swap(array, i, position)
        position += 1

    pivot = position - 1
    self.swap(array, start, pivot)
    return pivot

  def pivot_and_partition(self, array, start, end):
    if start >= end:
      return

    pivot = self.pivot_sort(array, start, end)
    self.pivot_and_partition(array, start, pivot - 1)
    self.pivot_and_partition(array, pivot + 1, end)

  def solve(self, array):
    self.pivot_and_partition(array, 0, len(array) - 1)
    return array

test(QuickSort, examples)

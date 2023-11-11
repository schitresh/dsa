from utils import test

examples = [
  {
    'input': [[4, 5, 9, 8, 7, 3, 2, 1, 6]],
    'output': [1, 2, 3, 4, 5, 6, 7, 8, 9]
  }
]

class SelectionSort:
  def swap(self, array, index_1, index_2):
    array[index_1], array[index_2] = array[index_2], array[index_1]

  def solve(self, array):
    for i in range(len(array)):
      min_index = i

      for j in range(i + 1, len(array)):
        if array[j] < array[min_index]:
          min_index = j

      self.swap(array, i, min_index)

    return array

test(SelectionSort, examples)

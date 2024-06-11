from utils import test_class

examples = [
  {
    'input': [[4, 5, 9, 8, 7, 3, 2, 1, 6]],
    'output': [1, 2, 3, 4, 5, 6, 7, 8, 9]
  }
]

# Selects the smallest element from the uniterated array and puts it at the front
# Not a stable sort, since the swapping can place an element at any index
# Time Complexity: O(n^2)
  # Best, Worst, Average: O(n^2)
# Auxiliary Space: O(1)
class SelectionSort:
  def swap(self, array, i, j):
    array[i], array[j] = array[j], array[i]

  def solve(self, array):
    for i in range(len(array)):
      min_index = i

      for j in range(i + 1, len(array)):
        if array[j] < array[min_index]:
          min_index = j

      self.swap(array, i, min_index)

    return array

test_class(SelectionSort, examples)

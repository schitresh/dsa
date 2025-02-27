from utils import test_class

examples = [
  {
    'input': [[4, 5, 9, 8, 7, 3, 2, 1, 6]],
    'output': [1, 2, 3, 4, 5, 6, 7, 8, 9]
  }
]

# Selects each element one by one, and inserts it at its correct position
# Stable sort
# Time Complexity: O(n^2)
  # Best: O(n)
  # Worst, Average: O(n^2)
# Auxiliary Space: O(1)
class InsertionSort:
  def solve(self, array):
    for i in range(len(array)):
      j = i
      curr = array[i]

      while j > 0 and array[j - 1] > curr:
        array[j] = array[j - 1]
        j -= 1

      array[j] = curr

    return array

test_class(InsertionSort, examples)

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
class InsertionSort:
  def solve(self, array):
    for i, element in enumerate(array):
      j = i

      while j > 0 and array[j - 1] > element:
        array[j] = array[j - 1]
        j -= 1

      array[j] = element

    return array

test(InsertionSort, examples)

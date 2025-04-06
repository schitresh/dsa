from utils import test_class

examples = [
  {
    'input': [[4, 5, 9, 8, 7, 3, 2, 1, 6]],
    'output': [1, 2, 3, 4, 5, 6, 7, 8, 9]
  }
]

# Bubble Sort
# Keep swapping the adjacent elements till the smallest element bubbles up at the front
# Stable sort since only the adjacent elements are swapped
# Time Complexity: O(n^2)
# Best: O(n), Worst & Average: O(n^2)
# Auxiliary Space: O(1)
class Solution:
  def solve(self, array):
    for i in range(len(array)):
      swapped = True

      for j in range(len(array) - 1 - i):
        if array[j] > array[j + 1]:
          self.swap(array, j, j + 1)
          swapped = True

      # If no element is swapped, it means array is sorted
      if not swapped:
        break

    return array

  def swap(self, array, i, j):
    array[i], array[j] = array[j], array[i]

test_class(Solution, examples)

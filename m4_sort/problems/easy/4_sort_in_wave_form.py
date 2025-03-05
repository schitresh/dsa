from utils import test_class

# Given an unsorted array of integers, sort the array into a wave array.
# That is, arr[0] >= arr[1] <= arr[2] >= arr[3] <= arr[4] >= ...

examples = [
  {
    'input': [[10, 5, 6, 3, 2, 20, 100, 80]],
    'output': [10, 5, 6, 2, 20, 3, 100, 80],
  },
  {
    'input': [[20, 10, 8, 6, 4, 2]],
    'output': [20, 8, 10, 4, 6, 2],
  },
  {
    'input': [[10, 90, 49, 2, 1, 5, 23]],
    'output': [90, 10, 49, 1, 5, 2, 23],
  },
]

# Sorting
# Time Complexity: O(n^2)
# Auxiliary Space: O(1)
class Solution:
  def solve(self, array):
    array.sort()

    for i in range(1, len(array), 2):
      array[i - 1], array[i] = array[i], array[i - 1]

    return array

test_class(Solution, examples)

# Make sure that all even positioned elements are greater than the next element.
# And the odd positioned elements are smaller than the next element.
# For example, we will get arr[0] > arr[1] after applying the first condition. Let's say
# arr[1] > arr[2], so we will get swap arr[1] & arr[2] using the second condition. And
# since arr[0] > arr[1], arr[0] must be > arr[2].
# Time Complexity: O(n)
# Auxiliary Space: O(1)
class Solution2:
  def solve(self, array):
    for i in range(1, len(array)):
      if i % 2 == 0:
        if array[i - 1] > array[i]:
          array[i - 1], array[i] = array[i], array[i - 1]
      else:
        if array[i - 1] < array[i]:
          array[i - 1], array[i] = array[i], array[i - 1]

    return array

test_class(Solution2, examples)

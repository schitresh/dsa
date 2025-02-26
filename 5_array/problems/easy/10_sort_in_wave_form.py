from utils import test_class

# Given an unsorted array of integers, sort the array into a wave array.
# arr[0..n-1] is sorted in wave form if:
# arr[0] >= arr[1] <= arr[2] >= arr[3] <= arr[4] >= ...

examples = [
  {
    'input': [[20, 10, 8, 6, 4, 2]],
    'output': [20, 8, 10, 4, 6, 2],
  },
  {
    'input': [[1, 2, 3, 4, 5, 6]],
    'output': [2, 1, 4, 3, 6, 5],
  },
  {
    'input': [[10, 90, 49, 2, 1, 5, 23]],
    'output': [90, 10, 49, 1, 5, 2, 23],
  },
  {
    'input': [[10, 5, 6, 3, 2, 20, 100, 80]],
    'output': [10, 5, 6, 2, 20, 3, 100, 80],
  },
]

# Sorting
# Time Complexity: O(n * log(n))
# Auxiliary Space: O(1)
class Solution:
  def solve(self, array):
    array.sort()

    for i in range(0, len(array) - 1, 2):
      array[i], array[i + 1] = array[i + 1], array[i]

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

    for i in range(len(array) - 1):
      if i % 2 == 0:
        if array[i] < array[i + 1]:
          array[i], array[i + 1] = array[i + 1], array[i]
      else:
        if array[i] > array[i + 1]:
          array[i], array[i + 1] = array[i + 1], array[i]

    return array

test_class(Solution2, examples)

# Make sure that all even positioned elements are greater than their adjacent odd
# elements, we don’t need to worry about oddly positioned elements.
# Time Complexity: O(n)
# Auxiliary Space: O(1)
class Solution3:
  def solve(self, array):

    for i in range(0, len(array), 2):
      if i > 0 and array[i - 1] > array[i]:
        array[i - 1], array[i] = array[i], array[i - 1]

      if i < len(array) - 1 and array[i] < array[i + 1]:
        array[i], array[i + 1] = array[i + 1], array[i]

    return array

test_class(Solution3, examples)

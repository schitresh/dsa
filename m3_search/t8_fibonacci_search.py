from utils import test_class

# Given an array of integers and a key, find whether the key is present in the array.
# Return the index of the first occurrence  or -1 if it doesn’t exist.

examples = [
  {
    'input': [[4, 5, 6, 7, 8, 9], 8],
    'output': 4
  },
  {
    'input': [[4, 5, 6, 7, 8, 9], 4],
    'output': 0
  },
  {
    'input': [[4, 5, 6, 7, 8, 9], 9],
    'output': 5
  },
  {
    'input': [[4, 5, 6, 7, 8, 9], 2],
    'output': -1
  }
]

# Fibonacci Search
# Useful for unbounded arrays with large size
# Time Complexity: O(log(n))
# Auxiliary Space: O(1)
class Solution:
  def solve(self, array, key):
    fib1 = 0
    fib2 = 1
    fib3 = fib1 + fib2

    # Figure out fib1, fib2, fib3 over the length of the array
    # fib3 will be the smallest fibonacci number greater than or equal to length
    # Either fib1 or fib2 can be used as the index under consideration during the search
    while fib3 < len(array):
      fib1 = fib2
      fib2 = fib3
      fib3 = fib1 + fib2

    # Eliminated range of index (less than and equal to it)
    offset = -1

    while fib3 > 1:
      index = min(offset + fib2, len(array) - 1)

      if key < array[index]:
        fib3 = fib1
        fib2 = fib2 - fib1
        fib1 = fib3 - fib2
      elif key > array[index]:
        fib3 = fib2
        fib2 = fib1
        fib1 = fib3 - fib2

        offset = index
      else:
        return index

    if fib2 == 1 and array[offset + 1] == key:
      return offset + 1

    return -1

test_class(Solution, examples)

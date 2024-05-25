from utils import test_class

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
    'input': [[4, 5, 6, 7, 8, 9], 2],
    'output': -1
  }
]

# Time Complexity: O(log(n))
# Space Complexity: O(1)
# Useful for unbounded arrays with large size
class FibonacciSearch:
  def solve(self, array, key):
    fib1 = 0
    fib2 = 1
    fib3 = fib1 + fib2

    while fib3 < len(array):
      fib1 = fib2
      fib2 = fib3
      fib3 = fib1 + fib2

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

test_class(FibonacciSearch, examples)

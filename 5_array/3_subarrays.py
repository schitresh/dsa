from utils import test_class

# Generate all Subarrays
examples = [
  {
    'input': [[1, 2]],
    'output': [[1], [1, 2], [2]]
  },
  {
    'input': [[1, 2, 3]],
    'output': [[1], [1, 2], [1, 2, 3], [2], [2, 3], [3]]
  }
]

# Maintain two pointers left & right
# Iterate left over all elements of the array
# For each left, generate all subarrays from right = left to n
# Time Complexity: O(n^2)
# Auxiliary Space: O(n)
class Solution:
  def solve(self, array):
    subarrays = []

    for left in range(len(array)):
      temp = []

      for right in range(left, len(array)):
        item = array[right]
        temp.append(item)
        subarrays.append(temp.copy())

    return subarrays

test_class(Solution, examples)

from utils import test_class

# Given an array, return an equilibrium index or -1 if no equilibrium index exists.
# The equilibrium index of an array is an index such that the sum of all elements at
# lower indexes equals the sum of all elements at higher indexes.
# When the index is at the start of the array, the left sum is considered 0, and
# when it’s at the end, the right sum is considered 0.

examples = [
  {
    'input': [[1, 2, 0, 3]],
    'output': 2,
  },
  {
    'input': [[1, 1, 1, 1]],
    'output': -1,
  },
  {
    'input': [[1, 7, 3, 6, 5, 6]],
    'output': 3,
  },
  {
    'input': [[-7, 1, 5, 2, -4, 3, 0]],
    'output': 3,
  },
]

# Calculate Prefix & Suffix sum for each element
# Time Complexity: O(n^2)
# Auxiliary Space: O(1)

# Iterate through array and store prefix & suffix sum in auxiliary space
# Time Complexity: O(n)
# Auxiliary Space: O(n)

# Running Prefix & Suffix sum
# Time Complexity: O(n)
# Auxiliary Space: O(1)
class Solution:
  def solve(self, array):
    total_sum = sum(array)
    curr_sum = 0

    for i in range(len(array)):
      left_sum = curr_sum
      curr_sum += array[i]
      right_sum = total_sum - curr_sum

      if left_sum == right_sum: return i

    return -1

test_class(Solution, examples)

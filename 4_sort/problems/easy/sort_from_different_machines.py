from utils import test_class

# Given N machines, each machine contains some numbers in sorted form. But the amount of
# numbers each machine has is not fixed. Sorte the numbers from all the machine in
# non-decreasing order.

examples = [
  {
    'input': [[30, 40, 50], [35, 45], [10, 60, 70, 80, 100]],
    'output': [10, 30, 35, 40, 45, 50, 60, 70, 80, 100],
  },
]

# Sorting
# Time Complexity: O(n^2)
# Auxiliary Space: O(1)
class Solution:
  def solve(self, machines):
    array = []

    return array

test_class(Solution, examples)

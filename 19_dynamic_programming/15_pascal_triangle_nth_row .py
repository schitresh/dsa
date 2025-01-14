from utils import test_class

# Given an integer n, find the nth row of Pascal’s triangle.

examples = [
  {
    'input': [4],
    'output': [1, 3, 3, 1],
  },
  {
    'input': [6],
    'output': [1, 5, 10, 10, 5, 1],
  },
]

# Recursion
# Time Complexity: O(n^2)
# Auxiliary Space: O(n)
class Solution:
  def solve(self, n):
    pascal_row = []
    pascal_row.append(1)
    if n == 1: return pascal_row

    prev = self.solve(n - 1)

    for i in range(1, len(prev)):
      item = prev[i - 1] + prev[i]
      pascal_row.append(item)

    pascal_row.append(1)
    return pascal_row

test_class(Solution, examples)

# Iteration
# Time Complexity: O(n^2)
# Auxiliary Space: O(n)
class Solution2:
  def solve(self, n):
    pascal_row = [1]
    if n == 1: return pascal_row

    for row in range(1, n):
      curr = [1]

      for i in range(1, row):
        item = pascal_row[i - 1] + pascal_row[i]
        curr.append(item)

      curr.append(1)
      pascal_row = curr

    return pascal_row

test_class(Solution2, examples)

# Using Binomial Coefficient
# Using the relationship: nCi = nC(i - 1) * (n - i + 1)/i
# Time Complexity: O(n)
# Auxiliary Space: O(n)
class Solution3:
  def solve(self, row_num):
    pascal_row = [1]
    prev = 1

    n = row_num - 1
    for i in range(1, n + 1):
      curr = prev * (n - i + 1) // i
      pascal_row.append(curr)
      prev = curr

    return pascal_row

test_class(Solution3, examples)

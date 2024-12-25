from utils import test_class

# Given an integer n, find the first n rows of Pascal’s triangle.
# Pascal’s triangle is a triangular array of binomial coefficients.

examples = [
  {
    'input': [4],
    'output': [
      [1],
      [1, 1],
      [1, 2, 1],
      [1, 3, 3, 1],
    ],
  },
  {
    'input': [6],
    'output': [
      [1],
      [1, 1],
      [1, 2, 1],
      [1, 3, 3, 1],
      [1, 4, 6, 4, 1],
      [1, 5, 10, 10, 5, 1],
    ],
  },
]

# Using Binomial Coefficient
# (a + b)^n = nC0 * a^n * b^0 + nC1 * a^(n - 1) * b^1 + ...
#             + nC(n-1) * a^1 * b^(n-1) + nCn * a^0 * b^n
# where nCi is binomial coefficient
# In pascal triangle, the value of ith entry in nth row is nCi
# (a + b)^0 -> [1]
# (a + b)^1 -> [1, 1]
# (a + b)^2 -> [1, 2, 1]
# (a + b)^3 -> [1, 3, 3, 1]
# Time Complexity: O(n^3)
# Auxiliary Space: O(1)
class Solution:
  def solve(self, n):
    matrix = []

    for row in range(n):
      array = []
      for i in range(row + 1):
        coeff = self.binomial_coeff(row, i)
        array.append(coeff)

      matrix.append(array)

    return matrix

  def binomial_coeff(self, n, k):
    coeff = 1

    if k > n - k:
      k = n - k

    # Expanded version of nCk
    for i in range(k):
      coeff *= (n - i)
      coeff //= (i + 1)

    return coeff

test_class(Solution, examples)

# Tabulation (Bottom-Up)
# Every entry is sum of the two values above it
# Time Complexity: O(n^2)
# Auxiliary Space: O(n^2)
class Solution2:
  def solve(self, n):
    matrix = []

    for row in range(n):
      array = []
      for i in range(row + 1):
        # First & last values in every row is 1
        if i == 0 or i == row:
          array.append(1)
        else:
          coeff = matrix[row - 1][i - 1] + matrix[row - 1][i]
          array.append(coeff)

      matrix.append(array)

    return matrix

test_class(Solution2, examples)

# Using Binomial Coefficient with optimization
# Using the relationship: nCi = nC(i - 1) * (n - i + 1)/i
# Time Complexity: O(n^2)
# Auxiliary Space: O(1)
class Solution3:
  def solve(self, n):
    matrix = []

    for row in range(1, n + 1):
      array = []
      coeff = 1

      for i in range(1, row + 1):
        array.append(coeff)
        # row = n + 1 since it's starting from 1
        # That's required to exclude the value of i as 0
        coeff = coeff * (row - i) // i

      matrix.append(array)

    return matrix

test_class(Solution3, examples)

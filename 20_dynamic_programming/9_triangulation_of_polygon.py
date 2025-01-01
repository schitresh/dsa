from utils import test_class

# Given a convex polygon with n sides, calculate the number of ways in which triangles
# can be formed by connecting vertices with non-crossing line segments.

examples = [
  {
    'input': [3],
    'output': 1,
    # Already a triangle
  },
  {
    'input': [4],
    'output': 2,
    # Square can be cut into 2 triangles through one of the diagonal
  },
  {
    'input': [6],
    'output': 14,
  },
]

# Using Catalan Numbers
# This follows catalan numbers: 1, 1, 2, 5, 14, 42, 132, 429, 1430, 4862, ...
# Total valid expressions for input n is n/2th catalan number if n is even, 0 if odd
# Time Complexity: O(n)
# Auxiliary Space: O(1)
class Solution:
  def solve(self, n):
    return self.catalan(n - 2)

  def catalan(self, n):
    coeff = self.binomial_coeff(2 * n, n)
    return coeff // (n + 1)

  def binomial_coeff(self, n, r):
    result = 1

    # Since C(n, r) = C(n, n - r) because C(n, r) = n!/(r! * (n - r)!)
    r = min(r, n - r)

    # On expanding the factorials in the formula, it can be simplified to:
    # C(n, r) = (n/1) * ((n-1)/2) * ... * ((n - (r - 1))/r)
    for i in range(r):
      result *= (n - i)
      result //= (i + 1)

    return result

test_class(Solution, examples)

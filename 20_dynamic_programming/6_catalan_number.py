from utils import test_class

# Catalan numbers are defined as a mathematical sequence that consists of positive
# integers, which can be used to find the number of possibilities of various combinations.
# The nth term in the sequence Cn = (2n)!/((n+1)!n!)
# The first few Catalan numbers are 1, 1, 2, 5, 14, 42, 132, 429, 1430, 4862, ...

# Catalan numbers occur in many interesting counting problems like:
# 1. Count the number of expressions containing n pairs of correctly matched parentheses
# For n = 3, possible expressions are ((())), ()(()), ()()(), (())(), (()())
# 2. Count the number of possible Binary Search Trees with n keys
# 3. Count the number of full binary trees with n+1 leaves
# A rooted binary tree is full if every vertex has either two or no children
# 4. Given a number n, return the number of ways you can draw n chords in a circle
# with 2 x n points such that no 2 chords intersect.

examples = [
  {
    'input': [6],
    'output': 132,
  },
  {
    'input': [8],
    'output': 1430,
  },
]

# Recursion
# Catalan numbers satisfy this recursive formula:
# C(n) = Sum(from i = 0 to n - 1)[C(i) * C(n - i - 1)] for n>= 2
# Time Complexity: Exponential
# Auxiliary Space: O(n), due to recursive stack
class Solution:
  def solve(self, n):
    if n <= 1: return 1

    result = 0
    for i in range(n):
      result += self.solve(i) * self.solve(n - i - 1)

    return result

test_class(Solution, examples)

# Tabulation (Bottom-Up)
# Time Complexity: O(n^2)
# Auxiliary Space: O(n)
class Solution2:
  def solve(self, n):
    catalan = [0] * (n + 1)
    catalan[0] = catalan[1] = 1

    for i in range(2, n + 1):
      for j in range(i):
        catalan[i] += catalan[j] * catalan[i - j - 1]

    return catalan[n]

test_class(Solution2, examples)

# Binomial Coefficient
# C(n) = (1/(n+1)) * Combinatorics(2n, n)
# Time Complexity: O(n)
# Auxiliary Space: O(1)
class Solution3:
  def solve(self, n):
    coeff = self.binomial_coeff(2 * n, n)
    return coeff // (n + 1)

  def binomial_coeff(self, n, r):
    result = 1

    # Since C(n, r) = C(n, n - r) because C(n, r) = n!/(r! * (n - r)!)
    # this
    if r > n - r:
      r = n - r

    # On expanding the factorials in the formula, it can be simplified to:
    # C(n, r) = (n/1) * ((n-1)/2) * ... * ((n - (r - 1))/r)
    for i in range(r):
      result *= (n - i)
      result //= (i + 1)

    return result

test_class(Solution3, examples)

# Dependent on (n - 1)th term
# C(n) = C(n - 1) * ((4n - 2) / (n + 1))
# Time Complexity: O(n)
# Auxiliary Space: O(1)
class Solution4:
  def solve(self, n):
    result = 1

    for i in range(2, n + 1):
      result = (result * (4 * i - 2)) // (i + 1)

    return result

test_class(Solution4, examples)

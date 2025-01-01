from utils import test_class

# Given a number n, find the number of valid parenthesis expressions of that length.

examples = [
  {
    'input': [2],
    'output': 1,
  },
  {
    'input': [4],
    'output': 2,
  },
  {
    'input': [6],
    'output': 5,
  },
]

# Recursion
# Time Complexity: O(2^n)
# Auxiliary Space: O(n), due to recursive stack
class Solution:
  def solve(self, n):
    self.n = n
    self.result = []
    self.parenthesis('', 0, 0)
    return len(self.result)

  def parenthesis(self, string, pos, balance):
    # If right parenthesis are more than left ones, it cannot become valid
    if balance < 0: return
    if pos == self.n:
      if balance == 0: self.result.append(string)
      return

    self.parenthesis(string + '(', pos + 1, balance + 1)
    self.parenthesis(string + ')', pos + 1, balance - 1)

test_class(Solution, examples)

# Recursion
# Time Complexity: O(2^n)
# Auxiliary Space: O(n), due to recursive stack
class Solution2:
  def solve(self, n):
    self.n = n
    self.result = 0

    # Odd number of parenthesis cannot be valid
    if n % 1 == 1: return 0

    self.parenthesis(n // 2, n // 2)
    return self.result

  def parenthesis(self, left, right):
    # If right parenthesis are more than left ones, it cannot become valid
    if right > left: return
    # If all the number of parenthesis consumed, add it to the result
    if left == 0 and right == 0:
      self.result += 1
      return

    if left > 0: self.parenthesis(left - 1, right)
    if right > 0: self.parenthesis(left, right - 1)

test_class(Solution2, examples)

# Using Catalan Numbers
# Total valid expressions for input n is n/2th catalan number if n is even, 0 if odd
# Time Complexity: O(n)
# Auxiliary Space: O(1)
class Solution3:
  def solve(self, n):
    # Odd number of parenthesis cannot be valid
    if n & 1: return 0
    return self.catalan(n // 2)

  def catalan(self, n):
    coeff = self.binomial_coeff(2 * n, n)
    return coeff // (n + 1)

  def binomial_coeff(self, n, r):
    result = 1

    # C(n, r) = C(n, n - r) because C(n, r) = n!/(r! * (n - r)!)
    r = min(r, n - r)

    # On expanding the factorials in the formula, it can be simplified to:
    # C(n, r) = (n/1) * ((n-1)/2) * ... * ((n - (r - 1))/r)
    for i in range(r):
      result *= (n - i)
      result //= (i + 1)

    return result

test_class(Solution3, examples)

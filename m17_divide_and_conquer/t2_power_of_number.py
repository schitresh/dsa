from utils import test_class

# Given x & n, calculate x ** n or pow(x, n)

examples = [
  {
    'input': [2, 3],
    'output': 8
  },
  {
    'input': [3, 4],
    'output': 81
  },
  {
    'input': [5, -2],
    'output': 0.04
  },
]

# Brute Force
# Iterate or recurse over n and keep multipying x
# Time complexity: O(n)
class Solution:
  def solve(self, x, n):
    result = 1

    for _ in range(n):
      result *= x

    if n < 0: result = 1 / result
    return result

test_class(Solution, examples)

# Divide & Conquer using recursion
# Time Complexity: O(log(n))
# Auxiliary Space: O(log(n)) due to recursive stack
class Solution2:
  def solve(self, x, n):
    if n == 0: return 1
    if n < 0: return 1 / self.solve(x, -n)

    half_power = self.solve(x, n // 2)
    result = half_power * half_power

    if n % 2 == 1: result *= x
    return result

test_class(Solution2, examples)

# Divide & Conquer using iteration
# Time Complexity: O(log(n))
# Auxiliary Space: O(1)
class Solution3:
  def solve(self, x, n):
    result = 1
    invert = False

    if n < 0:
      invert = True
      n = abs(n)

    while n > 0:
      if n % 2 == 0:
        x *= x
        n //= 2
      else:
        result *= x
        n -= 1

    if invert: result = 1 / result
    return result

test_class(Solution3, examples)

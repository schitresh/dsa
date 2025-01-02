from utils import test_class

# Calculate x^n or x ** n or pow(x, n) using divide and conquer.
examples = [
  {
    'input': [2, 3],
    'output': 8
  },
  {
    'input': [3, 4],
    'output': 81
  },
]

# Brute force: Iterate or recurse over n and keep multipying x.
# Time complexity: O(n)

# Recursion
# Time Complexity: O(log(n))
# Auxiliary Space: O(log(n)) for recursive stack
class Solution:
  def solve(self, x, n):
    if n == 0:
      return 1

    half_power = self.solve(x, n // 2)
    result = half_power * half_power

    if n % 2 == 1:
      result *= x

    return result

test_class(Solution, examples)

# Iteration
# Time Complexity: O(log(n))
# Auxiliary Space: O(1)
class Solution2:
  def solve(self, x, n):
    result = 1

    while n > 0:
      if n % 2 == 0:
        x *= x
        n /= 2
      else:
        result *= x
        n -= 1

    return result

test_class(Solution2, examples)

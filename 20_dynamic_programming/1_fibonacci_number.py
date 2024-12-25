from utils import test_class

# Given a positive integer n, find the nth Fibonacci number
# The Fibonacci sequence is a sequence where the next term is the sum of
# the previous two terms. The first two terms of the Fibonacci sequence are 0 & 1.
# The Fibonacci sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21

examples = [
  {
    'input': [8],
    'output': 21
  },
]

# Recursion
# Fibonacci number depends on previous two Fibonacci numbers
# This approach repeatedly breaks down the problem until it reaches the base cases.
# Time Complexity: O(2^n)
# Auxiliary Space: O(n), due to recursive stack
class Solution:
  def solve(self, n):
    if n <= 1: return n

    fib1 = self.solve(n - 1)
    fib2 = self.solve(n - 2)
    return fib1 + fib2

test_class(Solution, examples)

# Memoization (Top - Down)
# In recursion, there is a lot of redundant calculation
# So we can store the results of previously computed Fibonacci numbers in a memo table
# This will make sure that each Fibonacci number is only computed once
# Time Complexity: O(n)
# Auxiliary Space: O(n), due to recursive stack
class Solution2:
  def solve(self, n):
    self.fib_series = [None] * (n + 1)
    return self.fibonacci(n)

  def fibonacci(self, n):
    if n <= 1: return n
    if self.fib_series[n]:
      return self.fib_series[n]

    fib1 = self.fibonacci(n - 1)
    fib2 = self.fibonacci(n - 2)
    self.fib_series[n] = fib1 + fib2

    return self.fib_series[n]

test_class(Solution2, examples)

# Tabulation (Bottom - Up)
# This approach also avoids the repeated calculations of the recursive approach
# But instead of breaking down the problem recursively, it iteratively builds up the
# solution by calculating Fibonacci numbers from the bottom up.
# Time Complexity: O(n)
# Auxiliary Space: O(n), to store the numbers upto n
class Solution3:
  def solve(self, n):
    if n <= 1: return n
    fib_series = [None] * (n + 1)
    fib_series[0] = 0
    fib_series[1] = 1

    for i in range(2, n + 1):
      fib_series[i] = fib_series[i - 1] + fib_series[i - 2]

    return fib_series[n]

test_class(Solution3, examples)

# Tabulation (Bottom - Up) with space optimization
# This approach also avoids the repeated calculations of the recursive approach
# But instead of breaking down the problem recursively, it iteratively builds up the
# solution by calculating Fibonacci numbers from the bottom up.
# Time Complexity: O(n)
# Auxiliary Space: O(1)
class Solution4:
  def solve(self, n):
    if n <= 1: return n
    fib1 = 0
    fib2 = 1

    for _ in range(2, n + 1):
      fib3 = fib1 + fib2
      fib1 = fib2
      fib2 = fib3

    return fib3

test_class(Solution4, examples)

# Matrix Exponentiation
# Fibonacci numbers can be calculated much faster by working with matrices.
# There’s a special matrix (transformation matrix) that represents how Fibonacci numbers
# work, it looks like this: (1 1 1 0)
# If we multiply this matrix by itself multiple times, it can give us Fibonacci numbers.
# To find the Nth Fibonacci number we need to multiply transformation matrix (n-1) times
# the matrix equation for the Fibonacci sequence looks like:
# (1 1 1 0)^(n − 1) = (F(n) F(n−1) F(n−1) F(n−2))
# After raising the transformation matrix to the power n – 1, the top-left element F(n)
# will gives the nth Fibonacci number.
# Time Complexity: O(log(n))
# Auxiliary Space: O(log(n)), due to recursion stack
class Solution5:
  def solve(self, n):
    if n <= 1: return n

    self.base_matrix = [[1, 1], [1, 0]]
    self.matrix = [[1, 1], [1, 0]]
    self.matrix_power(n - 1)
    return self.matrix[0][0]

  def matrix_power(self, power_num):
    if power_num == 0 or power_num == 1: return

    # Break down the power by 2, and then keep calculating the square (next statement)
    self.matrix_power(power_num // 2)

    # Calculate the square of the matrix
    self.multiply_matrix_with(self.matrix)
    if power_num % 2 != 0:
      self.multiply_matrix_with(self.base_matrix)

  def multiply_matrix_with(self, matrix):
    x = self.matrix[0][0] * matrix[0][0] + self.matrix[0][1] * matrix[1][0]
    y = self.matrix[0][0] * matrix[0][1] + self.matrix[0][1] * matrix[1][1]
    z = self.matrix[1][0] * matrix[0][0] + self.matrix[1][1] * matrix[1][0]
    w = self.matrix[1][0] * matrix[0][1] + self.matrix[1][1] * matrix[1][1]

    self.matrix[0] = [x, y]
    self.matrix[1] = [z, w]

test_class(Solution5, examples)

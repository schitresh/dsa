import math
from queue import Queue
from utils import test_class

# Given a positive integer n, find the minimum number of squares that sum to n.
# A number can always be represented as a sum of squares of other numbers.
# Because 1 is a square number and it can be broken into any number as (1*1 + 1*1 + ...)

examples = [
  {
    'input': [100],
    'output': 1, # Can be written as [10^2] or [5^2 + 5^2 + 5^2 + 5^2], smallest is [10^2]
  },
  {
    'input': [6],
    'output': 3, # [2^2 + 1^2 + 1^2]
  },
]

# Recursion
# Time Complexity: Exponential
# Auxiliary Space: O(1)
class Solution:
  def solve(self, num):
    if num <= 3: return num

    # Any positive number can be represented as sum of 1^2 + 1^2 + ... n times,
    # so we can initialize count with n
    count = num

    n_sqrt = int(math.sqrt(num))
    for i in range(1, n_sqrt + 1):
      remaining_num = num - i * i
      remaining_count = self.solve(remaining_num)
      count = min(count, 1 + remaining_count)

    return count

# Can take too much time to run
# test_class(Solution, examples)

# Memoization (Top-Down)
# Time Complexity: O(n * sqrt(n))
# Auxiliary Space: O(n)
class Solution2:
  def solve(self, num):
    self.memo = [None] * (num + 1)
    return self.min_squares(num)

  def min_squares(self, num):
    if num <= 3: return num

    if self.memo[num]:
      return self.memo[num]

    # Any positive number can be represented as sum of 1^2 + 1^2 + ... n times,
    # so we can initialize count with n
    count = num

    n_sqrt = int(math.sqrt(num))
    for i in range(1, n_sqrt + 1):
      remaining_num = num - i * i
      remaining_count = self.min_squares(remaining_num)
      count = min(count, 1 + remaining_count)

    self.memo[num] = count
    return count

test_class(Solution2, examples)

# Tabulation (Bottom-Up)
# Time Complexity: O(n * sqrt(n))
# Auxiliary Space: O(n)
class Solution3:
  def solve(self, num):
    memo = [None] * (num + 1)
    memo[0] = 0
    memo[1] = 1

    for curr_num in range(2, num + 1):
      # Any positive number can be represented as sum of 1^2 + 1^2 + ... n times,
      # so we can initialize count with n
      memo[curr_num] = curr_num

      curr_num_sqrt = int(math.sqrt(curr_num))
      for i in range(1, curr_num_sqrt + 1):
        remaining_num = curr_num - i * i
        remaining_count = memo[remaining_num]
        memo[curr_num] = min(memo[curr_num], 1 + remaining_count)

    return memo[num]

test_class(Solution3, examples)

# BFS
# Time Complexity: O(n * sqrt(n))
# Auxiliary Space: O(n)
class Solution4:
  def solve(self, num):
    count = num

    queue = Queue()
    visited = [False] * (num + 1)

    # 0 indicates the current number of steps to reach num
    queue.put([num, 0])
    visited[num] = True

    while not queue.empty():
      node, steps = queue.get()

      if node == 0:
        count = min(count, steps)
        continue

      n_sqrt = int(math.sqrt(num))
      for i in range(1, n_sqrt + 1):
        remaining_num = node - i * i

        if remaining_num >= 0 and not visited[remaining_num]:
          visited[remaining_num] = True
          queue.put([remaining_num, steps + 1])

    return count

test_class(Solution4, examples)

# Todo
# Lagrange's Four Square Theorem
# Time Complexity: O(sqrt(n))
# Auxiliary Space: O(1)

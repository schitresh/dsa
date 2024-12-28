from utils import test_class

# Given an matrix of size m x n, with obstacles marked as 1 and space marked as 0.
# Find the count of all unique possible paths from the top left to the bottom right with
# the constraints that from each cell we can either move to right or down.

examples = [
  {
    'input': [[
      [0, 0, 0],
      [0, 1, 0],
      [0, 0, 0]
    ]],
    'output': 2,
  },
  {
    'input': [[
      [0, 1],
      [0, 0],
    ]],
    'output': 1,
  },
]

# Recursion
# Time Complexity: O(2^(m + n))
# Auxiliary Space: O(m + n), due to recursive stack
class Solution:
  def solve(self, matrix):
    self.matrix = matrix
    self.rows = len(matrix)
    self.cols = len(matrix[0])
    return self.path(0, 0)

  def path(self, row, col):
    if row == self.rows - 1 and col == self.cols - 1: return 1
    if row == self.rows or col == self.cols: return 0
    if self.matrix[row][col] == 1: return 0

    path1 = self.path(row, col + 1)
    path2 = self.path(row + 1, col)
    return path1 + path2

test_class(Solution, examples)

# Recursion
# Time Complexity: O(2^(m + n))
# Auxiliary Space: O(m + n), due to recursive stack
class Solution1b:
  def solve(self, matrix):
    self.matrix = matrix
    self.rows = len(matrix)
    self.cols = len(matrix[0])
    return self.path(self.rows - 1, self.cols - 1)

  def path(self, row, col):
    if row == 0 and col == 0: return 1
    if row < 0 or col < 0: return 0
    if self.matrix[row][col] == 1: return 0

    path1 = self.path(row, col - 1)
    path2 = self.path(row - 1, col)
    return path1 + path2

test_class(Solution1b, examples)

# Memoization
# Time Complexity: O(m * n)
# Auxiliary Space: O(m * n)
class Solution2:
  def solve(self, matrix):
    self.matrix = matrix
    self.rows = len(matrix)
    self.cols = len(matrix[0])
    self.memo = [[None] * self.cols  for _ in range(self.rows)]
    return self.path(self.rows - 1, self.cols - 1)

  def path(self, row, col):
    if row == 0 and col == 0: return 1
    if row < 0 or col < 0: return 0
    if self.matrix[row][col] == 1: return 0

    if self.memo[row][col]: return self.memo[row][col]

    path1 = self.path(row, col - 1)
    path2 = self.path(row - 1, col)
    self.memo[row][col] = path1 + path2
    return self.memo[row][col]

test_class(Solution2, examples)

# Tabulation
# Time Complexity: O(m * n)
# Auxiliary Space: O(m * n)
class Solution3:
  def solve(self, matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    dp = [[0] * cols  for _ in range(rows)]

    if matrix[0][0] == 0:
      dp[0][0] = 1

    for row in range(rows):
      for col in range(cols):
        if matrix[row][col] == 1:
          dp[row][col] = 0
          continue
        if col > 0: dp[row][col] += dp[row][col - 1]
        if row > 0: dp[row][col] += dp[row - 1][col]

    return dp[-1][-1]

test_class(Solution3, examples)

# Tabulation with space optimization
# Time Complexity: O(m * n)
# Auxiliary Space: O(n)
class Solution4:
  def solve(self, matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    dp = [0] * cols

    if matrix[0][0] == 0:
      dp[0] = 1

    for row in range(rows):
      for col in range(cols):
        if matrix[row][col] == 1:
          dp[col] = 0
        else:
          if col > 0: dp[col] += dp[col - 1]

    return dp[-1]

test_class(Solution4, examples)

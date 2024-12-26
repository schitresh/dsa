from utils import test_class

# Given an matrix of size m x n, find the count of all unique possible paths from the
# top left to the bottom right with the constraints that from each cell we can either
# move to right or down.

examples = [
  {
    'input': [2, 2],
    'output': 2,
  },
  {
    'input': [2, 3],
    'output': 3,
  },
]

# Recursion
# Time Complexity: O(2^(m + n))
# Auxiliary Space: O(m + n), due to recursive stack
class Solution:
  def solve(self, rows, cols):
    self.rows = rows
    self.cols = cols
    return self.path(0, 0)

  def path(self, row, col):
    if row == self.rows - 1 and col == self.cols - 1:
      return 1

    if row == self.rows or col == self.cols:
      return 0

    path1 = self.path(row, col + 1)
    path2 = self.path(row + 1, col)
    return path1 + path2

test_class(Solution, examples)

# Recursion
# Time Complexity: O(2^(m + n))
# Auxiliary Space: O(m + n), due to recursive stack
class Solution1b:
  def solve(self, rows, cols):
    self.rows = rows
    self.cols = cols
    return self.path(self.rows - 1, self.cols - 1)

  def path(self, row, col):
    # If it reaches the first row, there is only one path left to go i.e. left
    # Similarly, for the first col, the only way left is to go up
    if row == 0 or col == 0: return 1

    path1 = self.path(row, col - 1)
    path2 = self.path(row - 1, col)
    return path1 + path2

test_class(Solution1b, examples)

# Memoization
# Time Complexity: O(m * n)
# Auxiliary Space: O(m * n)
class Solution2:
  def solve(self, rows, cols):
    self.rows = rows
    self.cols = cols
    self.memo = [[None] * cols  for _ in range(rows)]
    return self.path(rows - 1, cols - 1)

  def path(self, row, col):
    # If it reaches the first row, there is only one path left to go i.e. left
    # Similarly, for the first col, the only way left is to go up
    if row == 0 or col == 0: return 1

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
  def solve(self, rows, cols):
    dp = [[0] * cols  for _ in range(rows)]

    # There is only one path to reach any cell in the first column
    for row in range(rows):
      dp[row][0] = 1

    # There is only one path to reach any cell in the first row
    for col in range(cols):
      dp[0][col] = 1

    for row in range(1, rows):
      for col in range(1, cols):
        dp[row][col] = dp[row][col - 1] + dp[row - 1][col]

    return dp[-1][-1]

test_class(Solution3, examples)

# Tabulation with space optimization
# Time Complexity: O(m * n)
# Auxiliary Space: O(n)
class Solution4:
  def solve(self, rows, cols):
    dp = [1] * cols

    for _ in range(1, rows):
      for col in range(1, cols):
        dp[col] = dp[col - 1] + dp[col]

    return dp[-1]

test_class(Solution4, examples)

# Combinatorics
# Since we are starting from (1, 1) that is not included, we need to move the total of
# (m - 1) steps right and (n - 1) steps down
# Hence, total_moves = right_moves + down_moves = (m - 1) + (n - 1) = m + n - 2
# Now, think of moves as a string of 'R' and 'D' chars. 'R' at any ith index will tell
# to move right and 'D' to move down. How many unique strings/moves we can make with the
# total of (m - 1 + n - 1) chars where there should be (m - 1) R chars and (n - 1) D chars
# Choosing positions of R chars results in the automatic choosing of D char positions
# Choosing positions for R chars
# = (positions)C(m - 1) = (positions)C(n - 1)
# = (m + n - 2)! / (m - 1)! * (n - 1)!
# Another way to think about this problem:
# Count the number of ways to make an N digit binary string with R zeros and D ones
# Time Complexity: O(m)
# Auxiliary Space: O(1)
class Solution5:
  def solve(self, rows, cols):
    paths = 1

    for i in range(cols, rows + cols - 1):
      paths *= i
      paths //= i - cols + 1

    return paths

test_class(Solution5, examples)

from utils import test_class

# Given a triangular array, find the minimum path sum from top to bottom.
# For each step, we can move to the adjacent numbers of the row below. i.e.,
# if we are on an index i of the current row, we can move to either index i or
# index i + 1 on the next row.

examples = [
  {
    'input': [[
      [2],
      [3, 7],
      [8, 5, 6],
      [6, 1, 9, 3]
    ]],
    'output': 11, # 2 -> 3 -> 5 -> 1
  },
  {
    'input': [[
      [3],
      [6, 9],
      [8, 7, 1],
      [9, 6, 8, 2]
    ]],
    'output': 15, # 3 -> 9 -> 1 -> 2
  },
]

# Recursion
# Time Complexity: O(2^(n^2))
# Auxiliary Space: O(n)
class Solution:
  def solve(self, tri_array):
    self.tri_array = tri_array
    return self.min_sum_path(0, 0)

  def min_sum_path(self, row, col):
    if row == len(self.tri_array): return 0

    sum1 = self.min_sum_path(row + 1, col)
    sum2 = self.min_sum_path(row + 1, col + 1)
    return self.tri_array[row][col] + min(sum1, sum2)

test_class(Solution, examples)

# Memoization (Top-Down)
# Optimal Substructure: min_sum(i, j) depends on the optimal solution of
# min_sum(i + 1, j) and min_sum(i + 1, j + 1)
# Overlapping Subproblems: min_sum(i + 1, j + 1) will be computed in min_sum(i, j)
# as well as min_sum(i, j + 1)
# Time Complexity: O(n^2)
# Auxiliary Space: O(n^2)
class Solution2:
  def solve(self, tri_array):
    self.tri_array = tri_array
    self.min_sum = [[None] * (i + 1) for i in range(len(tri_array))]
    return self.min_sum_path(0, 0)

  def min_sum_path(self, row, col):
    if row == len(self.tri_array): return 0

    if self.min_sum[row][col]:
      return self.min_sum[row][col]

    sum1 = self.min_sum_path(row + 1, col)
    sum2 = self.min_sum_path(row + 1, col + 1)
    self.min_sum[row][col] = self.tri_array[row][col] + min(sum1, sum2)
    return self.min_sum[row][col]

test_class(Solution2, examples)

# Tabulation (Bottom-Up)
# Time Complexity: O(n^2)
# Auxiliary Space: O(n^2)
class Solution3:
  def solve(self, tri_array):
    min_sum = [[None] * (i + 1) for i in range(len(tri_array))]
    min_sum[0][0] = tri_array[0][0]

    for i in range(1, len(tri_array)):
      min_sum[i][0] = tri_array[i][0] + min_sum[i - 1][0]
      min_sum[i][i] = tri_array[i][i] + min_sum[i - 1][i - 1]

      for j in range(1, i):
        sum1 = min_sum[i - 1][j - 1]
        sum2 = min_sum[i - 1][j]
        min_sum[i][j] = tri_array[i][j] + min(sum1, sum2)

    return min(min_sum[-1])

test_class(Solution3, examples)

# Tabulation (Bottom-Up)
# Time Complexity: O(n^2)
# Auxiliary Space: O(n^2)
class Solution3b:
  def solve(self, tri_array):
    min_sum = [[None] * (i + 1) for i in range(len(tri_array))]
    # Take last row as the base case
    min_sum[-1] = tri_array[-1].copy()

    for i in range(len(tri_array) - 2, -1, -1):
      for j in range(i + 1):
        sum1 = min_sum[i + 1][j]
        sum2 = min_sum[i + 1][j + 1]
        min_sum[i][j] = tri_array[i][j] + min(sum1, sum2)

    return min_sum[0][0]

test_class(Solution3b, examples)

# Tabulation (Bottom-Up) with space optimization
# Time Complexity: O(n^2)
# Auxiliary Space: O(n)
class Solution4:
  def solve(self, tri_array):
    # Take last row as the base case
    min_sum = tri_array[-1].copy()

    for i in range(len(tri_array) - 2, -1, -1):
      for j in range(i + 1):
        sum1 = min_sum[j]
        sum2 = min_sum[j + 1]
        min_sum[j] = tri_array[i][j] + min(sum1, sum2)

    return min_sum[0]

test_class(Solution4, examples)

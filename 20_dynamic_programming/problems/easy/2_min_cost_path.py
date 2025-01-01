from queue import PriorityQueue
from utils import test_class

# Given a 2d matrix cost[][], calculate the minimum cost path to reach (m, n) from (0, 0).
# Each cell of the matrix represents a cost to traverse through that cell. The total cost
# of a path to reach (m, n) is the sum of all the costs on that path (including both
# source and destination).
# We can only traverse down, right and diagonally lower cells from a given cell, i.e.
# from a given cell (i, j), cells (i+1, j), (i, j+1), and (i+1, j+1) can be traversed.

examples = [
  {
    'input': [[[1, 2, 3], [4, 8, 2], [1, 5, 3]]],
    'output': 8,
    # [0,0] -> [0,1] -> [1,2] -> [2,2]
  },
]

# Recursion
# Time Complexity: O(3^(m + n))
# Auxiliary Space: O(m + n), due to recursive stack
class Solution:
  def solve(self, cost):
    self.cost = cost
    return self.min_cost(0, 0)

  def min_cost(self, row, col):
    if row == len(self.cost) and col == len(self.cost[0]):
      return 0

    if not self.valid_move(row, col):
      return float('inf')

    cost1 = self.min_cost(row + 1, col)
    cost2 = self.min_cost(row, col + 1)
    cost3 = self.min_cost(row + 1, col + 1)
    return self.cost[row][col] + min(cost1, cost2, cost3)

  def valid_move(self, row, col):
    valid_row = row < len(self.cost)
    valid_col = col < len(self.cost[0])
    return valid_row and valid_col

test_class(Solution, examples)

# Memoization
# Time Complexity: O(m * n)
# Auxiliary Space: O(m * n)
class Solution2:
  def solve(self, cost):
    self.cost = cost
    self.memo = [[None] * len(cost[0]) for _ in range(len(cost))]
    return self.min_cost(0, 0)

  def min_cost(self, row, col):
    if row == len(self.cost) and col == len(self.cost[0]):
      return 0

    if not self.valid_move(row, col):
      return float('inf')

    if self.memo[row][col]:
      return self.memo[row][col]

    cost1 = self.min_cost(row + 1, col)
    cost2 = self.min_cost(row, col + 1)
    cost3 = self.min_cost(row + 1, col + 1)
    self.memo[row][col] = self.cost[row][col] + min(cost1, cost2, cost3)
    return self.memo[row][col]

  def valid_move(self, row, col):
    valid_row = row < len(self.cost)
    valid_col = col < len(self.cost[0])
    return valid_row and valid_col

test_class(Solution2, examples)

# Tabulation
# Time Complexity: O(m * n)
# Auxiliary Space: O(m * n)
class Solution3:
  def solve(self, cost):
    dp = [[None] * len(cost[0]) for _ in range(len(cost))]
    dp[0][0] = cost[0][0]

    for row in range(1, len(cost)):
      dp[row][0] = cost[row][0] + dp[row - 1][0]

    for col in range(1, len(cost[0])):
      dp[0][col] = cost[0][col] + dp[0][col - 1]

    for row in range(1, len(cost)):
      for col in range(1, len(cost[0])):
        cost1 = dp[row][col - 1]
        cost2 = dp[row - 1][col]
        cost3 = dp[row - 1][col - 1]
        dp[row][col] = cost[row][col] + min(cost1, cost2, cost3)

    return dp[-1][-1]

test_class(Solution3, examples)

# Tabulation with space optimization
# Time Complexity: O(m * n)
# Auxiliary Space: O(n)
class Solution4:
  def solve(self, cost):
    dp = [[None] * len(cost[0]) for _ in range(len(cost))]
    dp[0] = cost[0][0]

    for col in range(1, len(cost[0])):
      dp[col] = cost[0][col] + dp[col - 1]

    for row in range(1, len(cost)):
      prev = dp[0]
      dp[0] += cost[row][0]

      for col in range(1, len(cost[0])):
        curr = dp[col]

        cost1 = dp[col - 1]
        cost2 = curr
        cost3 = prev
        dp[col] = cost[row][col] + min(cost1, cost2, cost3)

        prev = curr

    return dp[-1]

test_class(Solution4, examples)

# Dijkstra
# Time Complexity: O(m * n * log(m * n))
# Auxiliary Space: O(m * n)
class Solution5:
  def solve(self, cost):
    moves = [[1, 0], [0, 1], [1, 1]]
    dist = [[float('inf')] * len(cost) for _ in range(len(cost[0]))]

    pqueue = PriorityQueue()
    pqueue.put([cost[0][0], [0, 0]])

    while not pqueue.empty():
      curr_cost, cell = pqueue.get()
      row, col = cell

      for move in moves:
        new_row = row + move[0]
        new_col = col + move[1]

        if new_row == len(cost) or new_col == len(cost[0]):
          continue

        new_cost = curr_cost + cost[new_row][new_col]
        if new_cost < dist[new_row][new_col]:
          dist[new_row][new_col] = new_cost
          pqueue.put([new_cost, [new_row, new_col]])

    return dist[-1][-1]

test_class(Solution5, examples)

from utils import test_class

# Given an array of integers cost[] of length n, where cost[i] is the cost of the ith
# step on a staircase.Once the cost is paid, a person can either climb one or two steps.
# A person can either start from the step with index 0, or the step with index 1. Find
# the minimum cost to reach the top of the floor.

examples = [
  {
    'input': [[10, 15, 20]],
    'output': 15,
    # Start at the stair 1, pay that cost and go to the top
  },
  {
    'input': [[1, 100, 1, 1, 1, 100, 1, 1, 100, 1]],
    'output': 6,
    # Start at the stair 0, and take steps only on 1s
  },
]

# Recursion
# Time Complexity: O(2^n)
# Auxiliary Space: O(n), due to recursive stack
class Solution:
  def solve(self, stair_costs):
    self.stair_costs = stair_costs
    stair_count = len(stair_costs)

    # Can reach the top by taking 1 step or 2 steps. Since the top doesn't have any
    # cost, need to calculate cost1 & cost2 separately and return min of them
    cost1 = self.climb(stair_count - 1)
    cost2 = self.climb(stair_count - 2)
    return min(cost1, cost2)

  def climb(self, stair):
    if stair in (0, 1):
      return self.stair_costs[stair]

    cost1 = self.climb(stair - 1)
    cost2 = self.climb(stair - 2)
    return self.stair_costs[stair] + min(cost1, cost2)

test_class(Solution, examples)

# Memoization (Top-Down)
# Time Complexity: O(n)
# Auxiliary Space: O(n), due to recursive stack
class Solution2:
  def solve(self, stair_costs):
    self.stair_costs = stair_costs
    stair_count = len(stair_costs)
    self.climb_costs = [None] * (stair_count + 1)

    # Can reach the top by taking 1 step or 2 steps. Since the top doesn't have any
    # cost, need to calculate cost1 & cost2 separately and return min of them
    cost1 = self.climb(stair_count - 1)
    cost2 = self.climb(stair_count - 2)
    return min(cost1, cost2)

  def climb(self, stair):
    if stair in (0, 1):
      return self.stair_costs[stair]

    if self.climb_costs[stair]:
      return self.climb_costs[stair]

    cost1 = self.climb(stair - 1)
    cost2 = self.climb(stair - 2)
    self.climb_costs[stair] = self.stair_costs[stair] + min(cost1, cost2)
    return self.climb_costs[stair]

test_class(Solution2, examples)

# Tabulation (Bottom-Up)
# Time Complexity: O(n)
# Auxiliary Space: O(n), due to recursive stack
class Solution3:
  def solve(self, stair_costs):
    stair_count = len(stair_costs)
    climb_costs = [False] * stair_count

    climb_costs[0] = stair_costs[0]
    climb_costs[1] = stair_costs[1]

    for stair in range(2, stair_count):
      cost1 = climb_costs[stair - 1]
      cost2 = climb_costs[stair - 2]
      climb_costs[stair] = stair_costs[stair] + min(cost1, cost2)

    return min(climb_costs[-1], climb_costs[-2])

test_class(Solution3, examples)

# Tabulation (Bottom-Up) with space optimization
# Time Complexity: O(n)
# Auxiliary Space: O(1)
class Solution4:
  def solve(self, stair_costs):
    stair_count = len(stair_costs)
    cost1 = stair_costs[0]
    cost2 = stair_costs[1]

    for stair in range(2, stair_count):
      climb_cost = stair_costs[stair] + min(cost1, cost2)
      cost1 = cost2
      cost2 = climb_cost

    return min(cost2, cost1)

test_class(Solution4, examples)

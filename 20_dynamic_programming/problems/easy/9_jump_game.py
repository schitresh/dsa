from utils import test_class

# Given an array of non-negative integers, where each element represents the maximum
# length of the jumps that can be made forward from that element. If arr[i] = x, then
# we can jump any distance y such that y ≤ x. Find the minimum number of jumps to reach
# the end of the array starting from the first element. If an element is 0, then we
# cannot move through that element. Return -1 if we can’t reach the end of the array.

examples = [
  {
    'input': [[1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]],
    'output': 3, # 1 -> 3 -> 9 -> 9
  },
  {
    'input': [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]],
    'output': 10,
  },
]

# Recursion
# Time Complexity: O(n^n)
# Auxiliary Space: O(n), due to recursive stack
class Solution:
  def solve(self, jumps):
    self.jumps = jumps
    return self.reach(0)

  def reach(self, pos):
    if pos >= len(self.jumps) - 1: return 0
    if self.jumps[pos] == 0: return float('inf')

    min_jump = float('inf')
    for jump in range(1, self.jumps[pos] + 1):
      curr_jump = 1 + self.reach(pos + jump)
      min_jump = min(min_jump, curr_jump)

    return min_jump

test_class(Solution, examples)

# Memoization
# Time Complexity: O(n^2)
# Auxiliary Space: O(n)
class Solution2:
  def solve(self, jumps):
    self.jumps = jumps
    self.memo = [None] * (len(jumps))
    return self.reach(0)

  def reach(self, pos):
    if pos >= len(self.jumps) - 1: return 0
    if self.jumps[pos] == 0: return float('inf')

    if self.memo[pos]: return self.memo[pos]

    min_jump = float('inf')
    for jump in range(1, self.jumps[pos] + 1):
      curr_jump = 1 + self.reach(pos + jump)
      min_jump = min(min_jump, curr_jump)

    self.memo[pos] = min_jump
    return min_jump

test_class(Solution2, examples)

# Tabulation
# Time Complexity: O(n^2)
# Auxiliary Space: O(n)
class Solution3:
  def solve(self, jumps):
    dp = [None] * len(jumps)
    dp[len(jumps) - 1] = 0

    for pos in range(len(jumps) - 2, -1, -1):
      min_jump = float('inf')

      for jump in range(1, jumps[pos] + 1):
        if pos + jump >= len(jumps): break
        curr_jump = 1 + dp[pos + jump]
        min_jump = min(min_jump, curr_jump)

      dp[pos] = min_jump

    return dp[0]

test_class(Solution3, examples)

from utils import test_class

# Given an integer array of coins[] of size n representing different types of
# denominations and an integer sum, count all combinations of coins required to make the
# given sum. Assume that you have an infinite supply of each type of coin.

examples = [
  {
    'input': [4, [1, 2, 3]],
    'output': 4,
    # There are 4 solutions: [1, 1, 1, 1], [1, 1, 2], [2, 2] and [1, 3]
  },
  {
    'input': [10, [2, 5, 3, 6]],
    'output': 5,
    # [2, 2, 2, 2, 2], [2, 2, 3, 3], [2, 2, 6], [2, 3, 5] and [5, 5]
  },
  {
    'input': [10, [10]],
    'output': 1,
    # [10]
  },
  {
    'input': [5, [4]],
    'output': 0,
  },
]

# Recursion
# Time Complexity: O(2^sum)
# Auxiliary Space: O(sum), due to recursive stack
class Solution:
  def solve(self, amount, coins):
    self.coins = coins
    return self.make_amount(0, amount)

  def make_amount(self, pos, rem_amt):
    if rem_amt < 0: return 0
    if rem_amt == 0: return 1
    if pos == len(self.coins): return 0

    way1 = self.make_amount(pos + 1, rem_amt)
    way2 = self.make_amount(pos, rem_amt - self.coins[pos])

    return way1 + way2

test_class(Solution, examples)

# Memoization
# Time Complexity: O(n * sum)
# Auxiliary Space: O(n * sum)
class Solution2:
  def solve(self, amount, coins):
    self.coins = coins
    self.memo = [[None] * (amount + 1) for _ in range(len(coins))]
    return self.make_amount(0, amount)

  def make_amount(self, pos, rem_amt):
    if rem_amt < 0: return 0
    if rem_amt == 0: return 1
    if pos == len(self.coins): return 0

    if self.memo[pos][rem_amt]:
      return self.memo[pos][rem_amt]

    way1 = self.make_amount(pos + 1, rem_amt)
    way2 = self.make_amount(pos, rem_amt - self.coins[pos])

    self.memo[pos][rem_amt] = way1 + way2
    return self.memo[pos][rem_amt]

test_class(Solution2, examples)

# Tabulation
# Time Complexity: O(n * sum)
# Auxiliary Space: O(n * sum)
class Solution3:
  def solve(self, amount, coins):
    dp = [[0] * (amount + 1) for _ in range(len(coins) + 1)]

    for pos in range(len(coins) + 1):
      dp[pos][0] = 1

    for pos in range(len(coins)):
      for req_amt in range(1, amount + 1):
        way1 = dp[pos][req_amt]

        amt2 = req_amt - coins[pos]
        way2 = 0
        if amt2 >= 0:
          way2 = dp[pos + 1][amt2]

        dp[pos + 1][req_amt] += way1 + way2

    return dp[-1][-1]

test_class(Solution3, examples)

# Tabulation with space optimization
# Time Complexity: O(n * sum)
# Auxiliary Space: O(sum)
class Solution4:
  def solve(self, amount, coins):
    dp = [0] * (amount + 1)
    dp[0] = 1

    for pos in range(len(coins)):
      for req_amt in range(coins[pos], amount + 1):
        dp[req_amt] += dp[req_amt - coins[pos]]

    return dp[-1]

test_class(Solution4, examples)

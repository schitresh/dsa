from utils import test_class

# Given an array of coins[] and a target value sum, find the minimum number of coins
# required to make the given value sum. You have an infinite supply of each of the
# coins. If it’s not possible to make a change, return -1.

examples = [
  {
    'input': [30, [25, 10, 5]],
    'output': 2,
    # [25, 5]
  },
  {
    'input': [19, [9, 6, 5, 1]],
    'output': 3,
    # [9, 9, 1]
  },
  {
    'input': [0, [5, 1]],
    'output': 0,
  },
  {
    'input': [5, [4, 6, 2]],
    'output': -1,
  },
]

# Recursion
# Time Complexity: O(2^sum)
# Auxiliary Space: O(sum), due to recursive stack
class Solution:
  def solve(self, amount, coins):
    self.coins = coins
    min_coins = self.make_amount(0, amount)

    if min_coins == float('inf'): return -1
    return min_coins

  def make_amount(self, pos, rem_amt):
    if rem_amt == 0: return 0
    if rem_amt < 0: return float('inf')
    if pos == len(self.coins): return float('inf')

    coins1 = self.make_amount(pos + 1, rem_amt)
    coins2 = 1 + self.make_amount(pos, rem_amt - self.coins[pos])

    return min(coins1, coins2)

test_class(Solution, examples)

# Memoization
# Time Complexity: O(n * sum)
# Auxiliary Space: O(n * sum)
class Solution2:
  def solve(self, amount, coins):
    self.coins = coins
    self.memo = [[None] * (amount + 1) for _ in range(len(coins))]
    min_coins = self.make_amount(0, amount)

    if min_coins == float('inf'): return -1
    return min_coins

  def make_amount(self, pos, rem_amt):
    if rem_amt == 0: return 0
    if rem_amt < 0: return float('inf')
    if pos == len(self.coins): return float('inf')

    if self.memo[pos][rem_amt]:
      return self.memo[pos][rem_amt]

    coins1 = self.make_amount(pos + 1, rem_amt)
    coins2 = 1 + self.make_amount(pos, rem_amt - self.coins[pos])

    self.memo[pos][rem_amt] = min(coins1, coins2)
    return self.memo[pos][rem_amt]

test_class(Solution2, examples)

# Tabulation
# Time Complexity: O(n * sum)
# Auxiliary Space: O(n * sum)
class Solution3:
  def solve(self, amount, coins):
    dp = [[float('inf')] * (amount + 1) for _ in range(len(coins) + 1)]

    for pos in range(len(coins) + 1):
      dp[pos][0] = 0

    for pos in range(len(coins)):
      for req_amt in range(1, amount + 1):
        amt1 = req_amt
        coins1 = dp[pos][amt1]

        amt2 = req_amt - coins[pos]
        coins2 = float('inf')
        if amt2 >= 0:
          coins2 = 1 + dp[pos + 1][amt2]

        dp[pos + 1][req_amt] = min(coins1, coins2)

    if dp[-1][-1] == float('inf'): return -1
    return dp[-1][-1]

test_class(Solution3, examples)

# Tabulation with space optimization
# Time Complexity: O(n * sum)
# Auxiliary Space: O(sum)
class Solution4:
  def solve(self, amount, coins):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0

    for pos in range(len(coins)):
      for req_amt in range(1, amount + 1):
        amt1 = req_amt
        coins1 = dp[amt1]

        amt2 = req_amt - coins[pos]
        coins2 = float('inf')
        if amt2 >= 0:
          coins2 = 1 + dp[amt2]

        dp[req_amt] = min(coins1, coins2)

    if dp[-1] == float('inf'): return -1
    return dp[-1]

test_class(Solution4, examples)

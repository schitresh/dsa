from utils import test_class

# Stickler the thief wants to loot money from a society having n houses in a single line.
# He is a weird person and follows a certain rule when looting the houses. According to
# the rule, he will never loot two consecutive houses. At the same time, he wants to
# maximize the amount he loots. The thief knows which house has what amount of money but
# is unable to come up with an optimal looting strategy. He asks for your help to find the
# maximum money he can get if he strictly follows the rule.

examples = [
  {
    'input': [[5, 5, 10, 100, 10, 5]],
    'output': 110,
    # [5, 100, 5]
  },
  {
    'input': [[3, 2, 7, 10]],
    'output': 13,
    # [3, 10]
  },
  {
    'input': [[3, 2, 5, 10, 7]],
    'output': 15,
    # [3, 5, 7]
  },
]

# Recursion
# Time Complexity: O(2^n)
# Auxiliary Space: O(n), due to recursive stack
class Solution:
  def solve(self, amounts):
    self.amounts = amounts
    return self.loot(0)

  def loot(self, num):
    if num >= len(self.amounts): return 0

    amt1 = self.loot(num + 1)
    amt2 = self.amounts[num] + self.loot(num + 2)
    return max(amt1, amt2)

test_class(Solution, examples)

# Memoization
# Time Complexity: O(n)
# Auxiliary Space: O(n)
class Solution2:
  def solve(self, amounts):
    self.amounts = amounts
    self.max_amt = [None] * len(amounts)
    return self.loot(0)

  def loot(self, num):
    if num >= len(self.amounts): return 0
    if self.max_amt[num]: return self.max_amt[num]

    amt1 = self.loot(num + 1)
    amt2 = self.amounts[num] + self.loot(num + 2)
    self.max_amt[num] = max(amt1, amt2)
    return self.max_amt[num]

test_class(Solution2, examples)

# Tabulation
# Time Complexity: O(n)
# Auxiliary Space: O(n)
class Solution3:
  def solve(self, amounts):
    max_amt = [None] * len(amounts)
    max_amt[0] = amounts[0]
    max_amt[1] = max(amounts[0], amounts[1])

    for house in range(2, len(amounts)):
      amt1 = max_amt[house - 1]
      amt2 = amounts[house] + max_amt[house - 2]
      max_amt[house] = max(amt1, amt2)

    return max_amt[-1]

test_class(Solution3, examples)

# Tabulation with space optimization
# Time Complexity: O(n)
# Auxiliary Space: O(1)
class Solution4:
  def solve(self, amounts):
    max_amt = [None] * len(amounts)
    prev2 = amounts[0]
    prev1 = max(amounts[0], amounts[1])

    for house in range(2, len(amounts)):
      amt1 = prev1
      amt2 = amounts[house] + prev2
      max_amt[house] = max(amt1, amt2)

      prev2 = prev1
      prev1 = max_amt[house]

    return prev1

test_class(Solution4, examples)

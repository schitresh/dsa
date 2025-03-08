from utils import test_class

# Given a number n, count number of n length binary strings with consecutive 1’s in them.

examples = [
  {
    'input': [2],
    'output': 1,
    # Only 11 has consecutive 1s among 00, 01, 10, 11
  },
  {
    'input': [3],
    'output': 3,
    # 011, 110, 111
  },
  {
    'input': [5],
    'output': 19,
  },
]

# Generate all binary strings
# Time Complexity: O(2^n * n)
# 2^n to generate all binary strings and n to traverse each binary string to check
# consecutive 1s
# Auxiliary Space: O(n)
class Solution:
  def solve(self, num):
    return self.binary_strings('', num)

  def binary_strings(self, string, rem_len):
    if rem_len == 0:
      for i in range(len(string) - 1):
        if string[i : i + 2] == '11':
          return 1

      return 0

    count1 = self.binary_strings(string + '0', rem_len - 1)
    count2 = self.binary_strings(string + '1', rem_len - 1)
    return count1 + count2

test_class(Solution, examples)

# Count without consecutive 1s and subtract from total
# Counting binary string with consecutive 1s will be difficult since we will have many
# duplicates. For example, 11011 have 2 substrings with consecutive 1s, so while
# traversing we need to keep in mind that it is counted only once.
# Instead we can count the number of strings without any consecutive 1s and subtract it
# from the total number of binary strings for a given length (i.e. 2^length)
# Time Complexity: O(n)
# Auxiliary Space: O(n)
class Solution2:
  def solve(self, num):
    # Count of binary strings that can be generated without any consecutive 1s
    without_count = self.count_without(num)
    # Total number of binary strings that can be generated for a given length
    total_count = 2**num
    return total_count - without_count

  def count_without(self, rem_len):
    # Empty string does not have any consecutive 1s, so count will be 1
    if rem_len <= 0: return 1

    # If we assign 1 at the current position, then the next position should have 0 to
    # avoid consecutive 1s. Hence, the count of strings without consecutive 1s will be
    # how many strings we can generate with from the position i + 2.
    count1 = self.count_without(rem_len - 2)

    # If we assign 0 at the current position, then the next position can have either 0
    # or 1. Hence, the count of strings without consecutive 1s will be how many strings
    # we can generate with from the position i + 1.
    count2 = self.count_without(rem_len - 1)
    return count1 + count2

test_class(Solution2, examples)

# Count without consecutive 1s with top-down DP
# Check the above solution for the explaination of counting
# Time Complexity: O(n)
# Auxiliary Space: O(n)
class Solution3:
  def solve(self, num):
    self.memo = [0] * (num + 1)
    # Empty string will have no consecutive 1s
    self.memo[0] = 1
    # Strings of length 1 will be '0' & '1' which no consecutive 1s
    self.memo[1] = 2
    without_count = self.count_without(num)

    total_count = 2**num
    return total_count - without_count

  def count_without(self, rem_len):
    if self.memo[rem_len] != 0:
      return self.memo[rem_len]

    count1 = self.count_without(rem_len - 2)
    count2 = self.count_without(rem_len - 1)

    self.memo[rem_len] = count1 + count2
    return self.memo[rem_len]

test_class(Solution3, examples)

# Count without consecutive 1s with bottom-up DP
# Time Complexity: O(n)
# Auxiliary Space: O(n)
class Solution4:
  def solve(self, num):
    dp = [0] * (num + 1)
    dp[0] = 1
    dp[1] = 2

    for i in range(2, num + 1):
      dp[i] = dp[i - 2] + dp[i - 1]

    total_count = 2**num
    return total_count - dp[num]

test_class(Solution4, examples)

# Bottom-up DP with sapce optimization
# Time Complexity: O(n)
# Auxiliary Space: O(1)
class Solution5:
  def solve(self, num):
    prev2 = 1
    prev1 = 2

    without_count = 0
    for i in range(2, num + 1):
      without_count = prev2 + prev1
      prev2 = prev1
      prev1 = without_count

    total_count = 2**num
    return total_count - without_count

test_class(Solution5, examples)

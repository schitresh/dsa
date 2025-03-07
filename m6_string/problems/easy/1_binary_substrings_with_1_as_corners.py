from utils import test_class

# Given a binary string, count the number of substrings that start and end with 1.

examples = [
  {
    'input': ['1001'],
    'output': 1,
  },
  {
    'input': ['00100101'],
    'output': 3,
    # '1001', '101', '100101'
  },
  {
    'input': ['00100101000100'],
    'output': 6,
    # '1001', '101', '10001', '100101', '1010001', '1001010001'
  },
]

# Using Combinatorics
# We need two subsequent ones to form such a substring, even if there are 1s in between.
# That means we need to choose two ones from the given number of ones. We can use
# combinatorics to choose two ones since permutations are valid for substrings.
# Time Complexity: O(n)
# Auxiliary Space: O(1)
class Solution:
  def solve(self, string):
    count_1 = 0
    for char in string:
      if char == '1': count_1 += 1

    return self.combinatorics(count_1, 2)

  def combinatorics(self, n, r):
    return self.factorial(n) // (self.factorial(n - r) * self.factorial(r))

  def factorial(self, num):
    fact = 1
    while num > 0:
      fact *= num
      num -= 1

    return fact

test_class(Solution, examples)

# By counting 1s
# Each new one can form substring with the previous ones. That means for the ith 1 in
# the string, it can be combined with the (i - 1) ones that occurred previously.
# Or, we can apply sum of first n integers with n as (count_1s - 1), that is
# (count_1s - 1) * (count_1s) / 2
# Time Complexity: O(n)
# Auxiliary Space: O(1)
class Solution2:
  def solve(self, string):
    count_1 = 0
    for char in string:
      if char == '1': count_1 += 1

    substr_count = 0
    for i in range(1, count_1):
      substr_count += i

    return substr_count

test_class(Solution2, examples)

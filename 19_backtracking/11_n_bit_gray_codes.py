from utils import test_class

# Given a number n, generate n bit Gray codes. That is, generate bit patterns from
# 0 to 2^n-1 such that successive patterns differ by one bit.

examples = [
  {
    'input': [2],
    'output': [0, 1, 3, 2]
    # 00 - 1, 01 - 1, 11 - 3, 10 - 2
  },
  {
    'input': [3],
    'output': [0, 1, 3, 2, 6, 7, 5, 4]
  },
]

# Time Complexity: O(2^n)
# Auxiliary Space: O(n), due to recursive stack
class Solution:
  def solve(self, n):
    self.codes = []
    self.num = 0
    self.gray_code(n)
    return self.codes

  def gray_code(self, n):
    if n == 0:
      self.codes.append(self.num)
      return

    # Ignore the bit
    self.gray_code(n - 1)

    # Invert the bit
    self.num = self.num ^ (1 << (n - 1))
    self.gray_code(n - 1)

test_class(Solution, examples)

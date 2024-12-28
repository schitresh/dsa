from utils import test_class

# Given a positive integer n, find its square root. If n is not a perfect square,
# then return its floor.

examples = [
  {
    'input': [4],
    'output': 2
  },
  {
    'input': [11],
    'output': 3
  }
]

# Loop
# Time Complexity: O(sqrt(n))
# Auxiliary Space: O(1)
class Solution:
  def solve(self, num):
    for i in range(num // 2, 0, -1):
      if i * i <= num:
        return i

test_class(Solution, examples)

# Binary Search
# Time Complexity: O(log(n))
# Auxiliary Space: O(1)
class Solution2:
  def solve(self, num):
    result = 1
    left = 0
    right = num // 2

    while left <= right:
      mid = left + (right - left) // 2
      square = mid * mid

      if square <= num:
        result = mid
        left = mid + 1
      else:
        right = mid - 1

    return result

test_class(Solution2, examples)

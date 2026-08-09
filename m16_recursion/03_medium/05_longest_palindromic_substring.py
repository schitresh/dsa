from utils import test_class

# Given a string, find the length of the longest substring which is a palindrome.

examples = [
  {
    'input': ['banana'],
    'output': 5,
  },
  {
    'input': ['caaabbaaca'],
    'output': 6,
  },
]

# Time Complexity: O(n^2)
# Auxiliary Space: O(n), due to recursive stack
class Solution:
  def solve(self, string):
    self.string = string
    return self.max_palindrome_len(0, len(string) - 1, 0)

  def max_palindrome_len(self, left, right, count):
    if left > right: return count
    if left == right: return count + 1

    curr_len = 0
    if self.string[left] == self.string[right]:
      curr_len = self.max_palindrome_len(left + 1, right - 1, count + 2)

    max_len1 = self.max_palindrome_len(left + 1, right, 0)
    max_len2 = self.max_palindrome_len(left, right - 1, 0)
    return max(curr_len, max_len1, max_len2)

test_class(Solution, examples)

from utils import test_class

# Given a string, check if it is a palindrome or not.

examples = [
  {
    'input': ['abcdcba'],
    'output': True
  },
  {
    'input': ['abcddcba'],
    'output': True
  },
  {
    'input': ['abcdba'],
    'output': False
  },
    {
    'input': ['abcdcbd'],
    'output': False
  },
]

# By Reversing
# Time Complexity: O(n)
# Auxiliary Space: O(n), to generate reversed string
class Solution:
  def solve(self, string):
    return string == string[::-1]

test_class(Solution, examples)

# Two Pointers
# Time Complexity: O(n)
# Auxiliary Space: O(1)
class Solution2:
  def solve(self, string):
    left = 0
    right = len(string) - 1

    while left < right:
      if string[left] != string[right]:
        return False

      left += 1
      right -= 1

    return True

test_class(Solution2, examples)

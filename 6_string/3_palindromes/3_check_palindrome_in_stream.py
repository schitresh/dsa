from utils import test_class

# Given a stream of chars, check if the string received till now is a palindrome
examples = [
  {
    'input': ['abcba'],
    # a, ab, abc, abcb, abcba
    'output': [True, False, False, False, True]
  }
]

# TODO: Using Rolling Hash
# A simple solution is to check palindrome for each iteration
# A better solution is to use the rolling hash used in rabin karp algorithm
# Keep track of reverse of first half and second half
# Time Complexity: O(n^2) but has better average case
  # Avoids complete substring comparison most of the time by comparing hash values
  # Worst caase occurs for strings with all same chars like 'aaaaaa'
# Auxiliary Space: O(1)
class Solution:
  def is_palindrome(self, string, start, end):
    for i in range((end - start) // 2):
      if string[start + i] != start[end - i]:
        return False

    return True

  def solve(self, string):
    result = []
    # A Prime number used to evaluate rabin karp's rolling hash
    prime = 103
    first = ord(string[0]) % prime
    second = ord(string[1]) % prime

    for i in range(len(string)):
      if first == second:
        is_palindrome = self.is_palindrome(string, 0, i)
        result.append(is_palindrome)
      else:
        result.append(is_palindrome)

test_class(Solution, examples)

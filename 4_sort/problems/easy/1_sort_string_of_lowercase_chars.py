from utils import test_class

# Given a string of lowercase characters from 'a' to 'z', sort the string.

examples = [
  {
    'input': ['dcab'],
    'output': 'abcd',
  },
  {
    'input': ['geeksforgeeks'],
    'output': 'eeeefggkkorss',
  },
]

# Time Complexity: O(n)
# Auxiliary Space: O(n), to store sorted string
class Solution:
  def solve(self, string):
    counts = [0] * 26

    for char in string:
      counts[ord(char) - ord('a')] += 1

    result = []
    for i in range(len(counts)):
      while counts[i] > 0:
        result.append(chr(i + ord('a')))
        counts[i] -= 1

    return ''.join(result)

test_class(Solution, examples)

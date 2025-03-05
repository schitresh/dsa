from utils import test_class

# Given a stream of chars, check if the string received till now is a palindrome

examples = [
  {
    'input': ['abcba'],
    # a, ab, abc, abcb, abcba
    'output': [True, False, False, False, True]
  }
]

# Todo: Using Rolling Hash
# A simple solution is to check palindrome for each iteration
# A better solution is to use the rolling hash used in rabin karp algorithm
# Keep track of reverse of first half and second half
# Time Complexity: O(n^2) but has better average case
  # Avoids complete substring comparison most of the time by comparing hash values
  # Worst caase occurs for strings with all same chars like 'aaaaaa'
# Auxiliary Space: O(1)

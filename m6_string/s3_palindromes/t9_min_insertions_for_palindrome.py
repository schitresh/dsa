from collections import defaultdict
from utils import test_class

# Given a string, find minimum number of chars to be inserted so that
# it can become a palindrome
# Permutations are allowed, that is the positions of chars can be changed
# Similar to 2_rearrange_to_palindrome
examples = [
  {
    'input': ['aabbc'],
    'output': 0 # abcba
  },
  {
    'input': ['abcdba'],
    'output': 1 # abdcdba
  },
  {
    'input': ['abcd'],
    'output': 3 # dcbabcd
  },
  {
    'input': ['aabbccdef'],
    'output': 2 # feabcdcbaef
  },
]

# A set of chars can form a palindrome if at most one char occurs odd number of times
# And the rest of the chars occur even number of times
# Time Complexity: O(n)
# Auxiliary Space: O(no_of_alphabets) to store count of alphabets or other chars
class Solution:
  def solve(self, string):
    char_count = defaultdict(lambda: 0)
    odd_chars = 0

    for char in string:
      char_count[char] += 1

    for count in char_count.values():
      if count % 2 == 1:
        odd_chars += 1

    return 0 if odd_chars == 0 else odd_chars - 1

# Using Bits
# Keep track if the counts are odd or even instead of keeping actual counts
# Uses bitvector to store this nature of counts
# Time Complexity: O(n)
# Auxiliary Space: O(1)
class Solution2:
  def solve(self, string):
    bitvector = 0

    for char in string:
      char_num = ord(char)
      mask = 1 << char_num # 1 * 2^char_num
      # Carries XOR of bitvector & mask, and not exponentation
      # XOR of 1 with 1 is 0, hence even counts will show 0 and odd counts will show 1
      bitvector ^= mask

    if bitvector == 0:
      return 0

    count = 0
    while bitvector:
      count += bitvector & 1
      bitvector = bitvector >> 1

    return count - 1

test_class(Solution, examples)
test_class(Solution2, examples)

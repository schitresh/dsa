from collections import defaultdict
from utils import test_class

# Given a string, check if the chars can be rearranged to form a palindrome
examples = [
  {
    'input': ['abcdabc'],
    'output': True # abcdcba
  },
  {
    'input': ['abcdabcd'],
    'output': True # rdcbaabcd
  },
  {
    'input': ['cabcba'],
    'output': True # abccba
  },
  {
    'input': ['abcbad'],
    'output': False
  },
  {
    'input': ['abca'],
    'output': False
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

      if odd_chars > 1:
        return False

    return True

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

    all_counts_even = bitvector == 0
    # If one bit is odd, it will be of the form 01000
    # And (bitvector - 1) flip the digits as 00111
    # Hence, bitwise and of both will be 0: 01000 & 00111 = 00000
    # But if there is any other odd bit, it will remain as it is
    # Hence, bitwise and of both will not be 0: 01100 & 01011 = 01000
    one_count_odd = (bitvector & (bitvector - 1)) == 0
    return all_counts_even or one_count_odd

test_class(Solution, examples)
test_class(Solution2, examples)

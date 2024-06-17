from utils import test_class

# Find the minimum number of chars required to be added in the front
# of the given string to make it a palindrome
examples = [
  {
    'input': ['abc'],
    'output': 2 # 'cbabc'
  },
  {
    'input': ['bba'],
    'output': 1 # 'abba'
  },
  {
    'input': ['abcd'],
    'output': 3 # dcbabcd
  },
  {
    'input': ['babcd'],
    'output': 2 # dcbabcd
  }
]

# Iterate backwards and check if string[0..i] is a palindrome
# If not, that char needs to be added in the front
# Time Complexity: O(n^2)
# Auxiliary Space: O(1)
class Solution:
  def is_palidrome(self, string, left, right):
    while left < right:
      if string[left] != string[right]:
        return False

      left += 1
      right -= 1

    return True

  def solve(self, string):
    char_count = 0

    for i in range(len(string) - 1, 0, -1):
      if self.is_palidrome(string, 0, i):
        break

      char_count += 1

    return char_count

# Using LPS array of KMP algorithm
# Concat the string with its reverse and calculate its lps array
# LPS is longest proper prefix which is also a suffix
# Time Complexity: O(n)
# Auxiliary Space: O(n)
class Solution2:
  def compute_lps(self, string):
    lps = [0] * len(string)
    length = 0
    index = 1

    while index < len(string):
      if string[length] == string[index]:
        length += 1
        lps[index] = length
        index += 1
      else:
        if length > 0:
          length = lps[length - 1]
        else:
          lps[index] = 0
          index += 1

    return lps

  def solve(self, string):
    concat_string = string + '$' + string[::-1]
    lps = self.compute_lps(concat_string)

    # lps[-1] will give us the length of the substring that is palindrome
    # For example, babcd$dcbab will have lps 00100000123
    # lps[-1] tells that bab in the prefix matches bab in the suffix
    # Hence, cd is not the part of the longest substring that is palindrome
    return len(string) - lps[-1]

# TODO: Using Z array of Z algorithm
# Concat the string with its reverse and calculate its Z array
# Each index of Z array represents the length of the longest substring
# starting at index i, which is also a proper prefix
# Time Complexity: O(n)
# Auxiliary Space: O(n)
class Solution3:
  def compute_z_array(self, string):
    z_array = [0] * len(string)
    # left & right pointers for Z box
    # Z box is the last max suffix that matched a prefix
    left = 0
    right = 0

  def solve(self, string):
    return 0


test_class(Solution, examples)
test_class(Solution2, examples)
# test_class(Solution3, examples)

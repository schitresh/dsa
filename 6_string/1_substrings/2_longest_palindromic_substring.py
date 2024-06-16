from utils import test_class

# Find the length of the longest palindromic substring for a given string
# That is the longest substring that is also a palindrome
examples = [
  {
    'input': ['abc'],
    'output': 'a'
  },
  {
    'input': ['bbabcbabdcb'],
    'output': 'babcbab'
  },
  {
    'input': [''],
    'output': ''
  },
  {
    'input': ['abccba'],
    'output': 'abccba'
  },
  {
    'input': ['defabccbaghi'],
    'output': 'abccba'
  }
]

# Generate all substrings and check if they are palindrome or not
# Time Complexity: O(n^3)
# Auxiliary Space: O(1)
class Solution:
  def solve(self, string):
    lps_start = 0
    lps_end = 0

    for i in range(len(string)):
      for j in range(len(string)):
        substr = string[i : j + 1]
        if substr == substr[::-1] and j - i > lps_end - lps_start:
          lps_start = i
          lps_end = j

    return string[lps_start : lps_end + 1]

# Dynamic Programming
# Time Complexity: O(n^2)
# Auxiliary Space: O(n^2)
class Solution2:
  def solve(self, string):
    lps_start = 0
    lps_end = 0

    # Keep track if string[i] to string[j] is a palindrome or not
    palindrome = [[False] * len(string) for _ in range(len(string))]

    # Base Case 1: Each char is a palindrome of itself
    for i in range(len(string)):
      palindrome[i][i] = True

    # Base Case 2: Two same consecutive chars is a palindrome
    for i in range(len(string) - 1):
      if string[i] == string[i + 1]:
        palindrome[i][i + 1] = True
        lps_start = i
        lps_end = i + 1

    # Length 1 & 2 covered in base cases, now start with length 3
    for str_len in range(3, len(string) + 1):
      for l in range(len(string) - str_len + 1):
        r = l + str_len - 1

        if palindrome[l + 1][r - 1] and string[l] == string[r]:
          palindrome[l][r] = True

          if str_len > lps_end - lps_start + 1:
            lps_start = l
            lps_end = r

    return string[lps_start : lps_end + 1]

# Expansion from center
# For each char, check if it can be the center of a palindromic substring
# Time Complexity: O(n^2)
# Auxiliary Space: O(1)
class Solution3:
  def palindrome_pointers(self, string, middle, even_length = False):
    left = middle
    right = middle

    if even_length and middle + 1 < len(string):
      right = middle + 1

    while left >= 0 and right < len(string) and string[left] == string[right]:
      left -= 1
      right += 1

    return left + 1, right - 1

  def solve(self, string):
    lps_start = 0
    lps_end = 0

    def assign_if_max(left, right):
      nonlocal lps_start, lps_end

      if lps_end - lps_start < right - left:
        lps_end = right
        lps_start = left

    for i in range(len(string)):
      # Odd length palindrom like abcba
      left, right = self.palindrome_pointers(string, middle = i)
      assign_if_max(left, right)

      # Even length palindrom like abccba
      left, right = self.palindrome_pointers(string, middle = i, even_length = True)
      assign_if_max(left, right)

    return string[lps_start : lps_end + 1]

test_class(Solution, examples)
test_class(Solution2, examples)
test_class(Solution3, examples)

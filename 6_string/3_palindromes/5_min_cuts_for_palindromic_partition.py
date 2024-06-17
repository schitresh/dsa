from utils import test_class

# Find the minimum number of cuts required to create a palindromic partition
# of the given string
examples = [
  {
    'input': ['abcba'],
    'output': 0 # ['abcba']
  },
  {
    'input': ['abba'],
    'output': 0 # ['abba']
  },
  {
    'input': ['abcd'],
    'output': 3 # ['a', 'b', 'c', 'd']
  },
  {
    'input': ['abaxyyx'],
    'output': 1 # ['aba', 'xyyx'],
  },
    {
    'input': ['cabbaexyx'],
    'output': 3 # ['c', 'abba', 'e', 'xyx']
  },
]

# Recursion, similar to matrix chain multiplication
# Try making cuts at all possible places and calculate the min cost
# Time Complexity: O(2^n)
# Auxiliary Space: O(2^n) for recursion stack
class Solution:
  def is_palidrome(self, string, left, right):
    while left < right:
      if string[left] != string[right]:
        return False

      left += 1
      right -= 1

    return True

  def min_partition(self, string, i, j):
    if i >= j or self.is_palidrome(string, i, j):
      return 0

    min_count = float('inf')

    for k in range(i, j):
      count = 1 + self.min_partition(string, i, k) + self.min_partition(string, k + 1, j)
      min_count = min(min_count, count)

    return min_count

  def solve(self, string):
    return self.min_partition(string, 0, len(string) - 1)

# Stored computed results in the recursion approach
# Time Complexity: O(n^3)
# Auxiliary Space: O(n^2)
class Solution2:
  def solve(self, string):
    # Track if substring str[i..j] is a palindrome or not
    palindrome = [[False] * len(string) for _ in range(len(string))]
    # Min cuts required for palindromic partitioning of substring str[i..j]
    min_cuts = [[0] * len(string) for _ in range(len(string))]

    # Base Case 1: Each char is a palindrome of itself
    for i in range(len(string)):
      palindrome[i][i] = True

    # Base Case 2: Two same consecutive chars is a palindrome
    for i in range(len(string) - 1):
      if string[i] == string[i + 1]:
        palindrome[i][i + 1] = True
      else:
        min_cuts[i][i + 1] = 1

    # Length 1 & 2 covered in base cases, now start with length 3
    for substr_len in range(3, len(string) + 1):
      for l in range(len(string) - substr_len + 1):
        r = l + substr_len - 1

        if string[l] == string[r] and palindrome[l + 1][r - 1]:
          palindrome[l][r] = True
        else:
          curr_min_cuts = float('inf')

          for k in range(l, r):
            cuts = 1 + min_cuts[l][k] + min_cuts[k + 1][r]
            curr_min_cuts = min(curr_min_cuts, cuts)

          min_cuts[l][r] = curr_min_cuts

    return min_cuts[0][len(string) - 1]


# Stored computed results with space optimization
# Cuts are required between each palindrome such that its length is max
# So for each k, find the suffix in the string [k..i] which is palindrome
# And figure out the min number of cuts by iterating k over each i
# Time Complexity: O(n^2)
# Auxiliary Space: O(n^2)
class Solution3:
  def palindrome_matrix(self, string):
    palindrome = [[False] * len(string) for _ in range(len(string))]

    # Base Case 1: Each char is a palindrome of itself
    for i in range(len(string)):
      palindrome[i][i] = True

    # Base Case 2: Two same consecutive chars is a palindrome
    for i in range(len(string) - 1):
      if string[i] == string[i + 1]:
        palindrome[i][i + 1] = True

    # Length 1 & 2 covered in base cases, now start with length 3
    for substr_len in range(2, len(string) + 1):
      for l in range(len(string) - substr_len + 1):
        r = l + substr_len - 1

        if string[l] == string[r] and palindrome[l + 1][r - 1]:
          palindrome[l][r] = True

    return palindrome

  def solve(self, string):
    if not string:
      return 0

    # Track if substring str[i..j] is a palindrome or not
    palindrome = self.palindrome_matrix(string)
    # Min cuts required to make substring [i..(n - 1)] palindromic
    min_cuts = [float('inf')] * len(string)

    # No cut required for a single char
    min_cuts[0] = 0

    for i in range(1, len(string)):
      # If string[0..i] is a palindrome, cut is not required
      if palindrome[0][i]:
        min_cuts[i] = 0
      else:
        # Cuts are required between palindromes. So if string[k..i] is a palindrome,
        # cuts required will be 1 + (min cuts till str[0..(k-1)])
        # For each k, calculate this and find the minimum
        for k in range(i, 0, -1):
          if palindrome[k][i]:
            cuts = min_cuts[k - 1] + 1
            min_cuts[i] = min(min_cuts[i], cuts)

    return min_cuts[-1]


test_class(Solution, examples)
test_class(Solution2, examples)
test_class(Solution3, examples)

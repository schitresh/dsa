from utils import test_class

# Find the count of distinct occurrences of key in given string as a subsequence

examples = [
  {
    'input': ['banana', 'ban'],
    'output': 3 # ban***, ba**n*, b**an*
  },
  {
    'input': ['banananana', 'ba'],
    'output': 5
  },
  {
    'input': ['banana', ''],
    'output': 1
  },
  {
    'input': ['ban', 'banana'],
    'output': 0
  }
]

# Recursion
# Time Complexity: O(2^n)
# Auxiliary Space: O(2^n) due to recursive stack
class Solution:
  def solve(self, string, key):
    if len(string) < len(key):
      return 0

    return self.count_subsequences(string, key, 0, 0)

  def count_subsequences(self, string, key, string_index, key_index):
    if key_index == len(key):
      return 1

    if string_index == len(string):
      return 0

    count_by_excluding = self.count_subsequences(string, key, string_index + 1, key_index)

    count_by_including = 0
    if string[string_index] == key[key_index]:
      count_by_including = \
        self.count_subsequences(string, key, string_index + 1, key_index + 1)

    return count_by_including + count_by_excluding

test_class(Solution, examples)

# Dynamic Programming
# Time Complexity: O(n * m)
# Auxiliary Space: O(n * m)
class Solution2:
  def solve(self, string, key):
    # Stores count of occurrences of key till length i in string till length j
    # Index 0 denotes empty string, so keep size as length + 1
    count = [[0] * (len(string) + 1) for _ in range(len(key) + 1)]
    count[0] = [1] * (len(string) + 1)

    for i in range(0, len(key)):
      for j in range(0, len(string)):
        if key[i] == string[j]:
          # Occurrences of ab in aabbb
          # = Occurrences of ab in aabb + Occurrences of a in aabb
          # 6 = 4 + 2
          # Occurences of ab in aabb: Same key that is matched in string till now holds
          # true for this iteration also
          # Occurences of a in aabb: The current char is common in both string & key
          # So we can match the prefixes of both string & key and add current char
          count[i + 1][j + 1] = count[i + 1][j] + count[i][j]
        else:
          # Occurrences of ab in aabbx = Occurences of ab in aabb
          # 4 = 4
          # Occurences of ab in aabb: Same key that is matched in string till now holds
          # true for this iteration also
          # Occurences of a in aabb: This condition doesn't apply because the current
          # char is not common here
          count[i + 1][j + 1] = count[i + 1][j]

    return count[len(key)][len(string)]

test_class(Solution2, examples)

# Dynamic Programming by top-down approach by memoization
# Time Complexity: O(n * m)
# Auxiliary Space: O(n * m) ignoring recursion stack
class Solution3:
  def solve(self, string, key):
    if len(string) < len(key):
      return 0

    self.count = [[-1] * (len(key) + 1) for _ in range(len(string) + 1)]
    return self.count_subsequences(string, key, 0, 0)

  def count_subsequences(self, string, key, string_index, key_index):
    if key_index == len(key):
      return 1

    if string_index == len(string):
      return 0

    if self.count[string_index][key_index] != -1:
      return self.count[string_index][key_index]

    # Count by excluding
    self.count[string_index][key_index] = \
      self.count_subsequences(string, key, string_index + 1, key_index)

    if string[string_index] == key[key_index]:
      # Count by including
      self.count[string_index][key_index] += \
        self.count_subsequences(string, key, string_index + 1, key_index + 1)

    return self.count[string_index][key_index]

test_class(Solution3, examples)

from utils import test_class

# Find the count of distinct occurrences of T in S as a subsequence
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

# Time Complexity: O(2^n)
# Space Complexity: O(n) due to recursive stack
class Solution:
  def count_subsequences(self, string, key, string_index, key_index):
    if key_index == len(key):
      return 1

    if string_index == len(string):
      return 0

    count_by_excluding = self.count_subsequences(string, key, string_index + 1, key_index)

    count_by_including = 0
    if string[string_index] == key[key_index]:
      count_by_including = self.count_subsequences(string, key, string_index + 1, key_index + 1)

    return count_by_including + count_by_excluding

  def solve(self, string, key):
    if len(string) < len(key):
      return 0

    return self.count_subsequences(string, key, 0, 0)

# Time Complexity: O(n * m)
# Space Complexity: O(n * m)
# Dynamic Programming
class Solution2:
  def solve(self, string, key):
    # Index 0 denotes empty string, so keep size length + 1
    count = [[0] * (len(string) + 1) for _ in range(len(key) + 1)]
    count[0] = [1] * (len(string) + 1)

    for i in range(0, len(key)):
      for j in range(0, len(string)):
        if key[i] == string[j]:
          # Occurrences of ab in aabbb = Occurences of ab in aabb + Occurences of a in aabb
          # 6 = 4 + 2
          # Occurences of ab in aabb: Same key that is matched in string till now holds true for this iteration also
          # Occurences of a in aabb: The current char is common in both string & key
          # So we can match the prefixes of both string & key and add current char
          count[i + 1][j + 1] = count[i + 1][j] + count[i][j]
        else:
          # Occurrences of ab in aabbb = Occurences of ab in aabb
          # 4 = 4
          # Occurences of ab in aabb: Same key that is matched in string till now holds true for this iteration also
          # Occurences of a in aabb: This condition doesn't apply because the current char is not common here
          count[i + 1][j + 1] = count[i + 1][j]

    return count[len(key)][len(string)]

# Time Complexity: O(n * m)
# Space Complexity: O(n * m) ignoring recursion stack
class Solution3:
  def __init__(self):
    self.count = [[]]

  def count_subsequences(self, string, key, string_index, key_index):
    if key_index == len(key):
      return 1

    if string_index == len(string):
      return 0

    if self.count[string_index][key_index] != -1:
      return self.count[string_index][key_index]

    # Count by excluding
    self.count[string_index][key_index] = self.count_subsequences(string, key, string_index + 1, key_index)

    if string[string_index] == key[key_index]:
      # Count by including
      self.count[string_index][key_index] += self.count_subsequences(string, key, string_index + 1, key_index + 1)

    return self.count[string_index][key_index]

  def solve(self, string, key):
    if len(string) < len(key):
      return 0

    self.count = [[-1] * (len(key) + 1) for _ in range(len(string) + 1)]
    return self.count_subsequences(string, key, 0, 0)

test_class(Solution, examples)
test_class(Solution2, examples)
test_class(Solution3, examples)

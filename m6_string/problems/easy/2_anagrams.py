from utils import test_class

# Given two strings consisting of lowercase characters, check whether they are anagrams
# of each other or not. An anagram of a string is another string that contains the same
# characters, only the order of characters can be different.

examples = [
  {
    'input': ['geeks', 'kseeg'],
    'output': True,
  },
  {
    'input': ['abcd', 'abecd'],
    'output': False,
  },
  {
    'input': ['abecd', 'abc'],
    'output': False,
  },
]

# Sorting
# Time Complexity: O(m * log(m) + n * log(n))
# Auxiliary Space: O(1)
class Solution:
  def solve(self, string1, string2):
    return sorted(string1) == sorted(string2)

test_class(Solution, examples)

# Hashing
# Time Complexity: O(m + n)
# Auxiliary Space: O(1), since only 26 chars need to be tracked
class Solution2:
  def solve(self, string1, string2):
    counts = {}
    for char in string1:
      counts[char] = counts.get(char, 0) + 1

    for char in string2:
      if char not in counts: return False
      if counts[char] == 0: return False
      counts[char] -= 1

    if any(counts.values()): return False

    return True

test_class(Solution2, examples)

# Frequency Array
# Time Complexity: O(m + n)
# Auxiliary Space: O(1), since only 26 chars need to be tracked
class Solution3:
  def solve(self, string1, string2):
    counts = [0] * 26
    for char in string1:
      idx = ord(char) - ord('a')
      counts[idx] += 1

    for char in string2:
      idx = ord(char) - ord('a')
      if counts[idx] == 0: return False
      counts[idx] -= 1

    if any(counts): return False

    return True

test_class(Solution3, examples)

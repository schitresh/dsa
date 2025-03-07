from utils import test_class

# Given two strings with lowercase alphabets and a value k, find if they are K-anagrams
# of each other or not.
# Two strings are k-anagrams if the following two conditions are true:
# 1. Both have same number of characters.
# 2. Two strings can become anagram by changing at most k characters in a string.

examples = [
  {
    'input': ['anagram', 'grammar', 3],
    'output': True,
    # By changing one r to n and one m to a in 'grammer', it becomes anagram of 'anagram'
  },
  {
    'input': ['geeks', 'eggkf', 1],
    'output': False,
    # Need 2 changes, g and f in 'eggkf' to make it anagram of 'geeks'
  },
  {
    'input': ['fodr', 'gork', 2],
    'output': True,
  },
]

# Hashing
# Time Complexity: O(n)
# Auxiliary Space: O(1), since only 26 chars need to be tracked
class Solution:
  def solve(self, string1, string2, k):
    counts = {}
    for char in string1:
      counts[char] = counts.get(char, 0) + 1

    for char in string2:
      if char not in counts: continue
      if counts[char] == 0: continue
      counts[char] -= 1

    changes = sum(counts.values())
    return changes <= k

test_class(Solution, examples)

from utils import test_class

# Given a string s, find the number of pairs of characters that have the same chars.
# Pairs (s[i], s[j]), (s[j], s[i]), (s[i], s[i]), (s[j], s[j]) should be considered
# different.

examples = [
  {
    'input': ['air'],
    'output': 3,
    # (a, a), (i, i), (r, r)
  },
  {
    'input': ['aba'],
    'output': 5,
    # (a1, a1), (a1, a2), (a2, a1), (a2, a2), (b, b)
  },
  {
    'input': ['geeksforgeeks'],
    'output': 31,
  },
]


# Generate all pairs
# Time Complexity: O(n^2)
# Auxiliary Space: O(1)
class Solution:
  def solve(self, string):
    pairs = 0

    for i in range(len(string)):
      for j in range(len(string)):
        if string[i] == string[j]:
          pairs += 1

    return pairs

test_class(Solution, examples)

# Using Permutations
# Time Complexity: O(n * max_freq)
# Auxiliary Space: O(n)
class Solution2:
  def solve(self, string):
    counts = {}
    for char in string:
      counts[char] = counts.get(char, 0) + 1

    pairs = 0
    for freq in counts.values():
      pairs += freq
      if freq > 1:
        pairs += self.permutations(freq, 2)

    return pairs

  def permutations(self, n, r):
    return self.factorial(n) // self.factorial(n - r)

  def factorial(self, num):
    fact = 1
    for i in range(num, 0, -1):
      fact *= i

    return fact

test_class(Solution2, examples)

# Hashing
# For creating pairs, we need to combine all equal pairs with each other. Since chars at
# differnt position are different, we need to combine both ways. That means if there are
# k equal chars, then such combinations are k * k.
# Time Complexity: O(n)
# Auxiliary Space: O(n)
class Solution3:
  def solve(self, string):
    counts = {}
    for char in string:
      counts[char] = counts.get(char, 0) + 1

    pairs = 0
    for freq in counts.values():
      pairs += freq * freq

    return pairs

test_class(Solution3, examples)

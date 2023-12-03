from utils import test

# Generate all substrings
# Total substrings = n * (n - 1) / 2
examples = [
  {
    'input': ['abcd'],
    'output': ['a', 'ab', 'abc', 'abcd', 'b', 'bc', 'bcd', 'c', 'cd', 'd']
  }
]

# Time Complexity: O(n^3)
# Space Complexity: O(1)
class Solution:
  def solve(self, string):
    substrings = []

    for i in range(len(string)):
      for j in range(i, len(string)):
        substrings.append(string[i : j + 1])

    return substrings

# Time Complexity: O(n^2)
# Space Complexity: O(n)
class Solution2:
  def solve(self, string):
    substrings = []

    for i in range(len(string)):
      temp = ''

      for j in range(i, len(string)):
        temp += string[j]
        substrings.append(temp)

    return substrings

test(Solution, examples)
test(Solution2, examples)

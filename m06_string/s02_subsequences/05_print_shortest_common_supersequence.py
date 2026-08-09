from utils import test_class

# Find the length of the shortest string
# that has both the given strings as subsequences

examples = [
  {
    'input': ['abcd', 'bdef'],
    'output': 'abcdef'
  },
  {
    'input': ['aggtab', 'gxtxayb'],
    'output': 'aggxtxayb' # or agxgtxayb
  },
  {
    'input': ['', 'abcd'],
    'output': 'abcd'
  },
]

# Dynamic Programming for the recursive solution
# Time Complexity: O(n * m)
# Auxiliary Space: O(n * m)
class Solution:
  def solve(self, string1, string2):
    string = ''
    scs = self.scs_matrix(string1, string2)

    i = len(string1)
    j = len(string2)

    # Iterate backwards since scs at the end will give us the path
    # Because we want minimum scs for the whole length
    while i * j > 0:
      if string1[i - 1] == string2[j - 1]:
        # Prepend because we're iterating backwards
        string = string1[i - 1] + string
        i -= 1
        j -= 1
      elif scs[i - 1][j] < scs[i][j - 1]:
        string = string1[i - 1] + string
        i -= 1
      else:
        string = string2[j - 1] + string
        j -= 1

    while i > 0:
      string = string1[i - 1] + string
      i -= 1

    while j > 0:
      string = string2[j - 1] + string
      j -= 1

    return string

  def scs_matrix(self, string1, string2):
    scs = [[0] * (len(string2) + 1) for _ in range(len(string1) + 1)]

    # If length of string2 is 0, then scs will be the length of string1
    for i in range(len(string1)):
      # Since i is the index, the length will be i + 1
      scs[i + 1][0] = i + 1

    # If length of string1 is 0, then scs will be the length of string2
    for j in range(len(string2)):
      scs[0][j + 1] = j + 1

    for i in range(len(string1)):
      for j in range(len(string2)):
        if string1[i] == string2[j]:
          scs[i + 1][j + 1] = 1 + scs[i][j]
        else:
          scs[i + 1][j + 1] = 1 + min(scs[i + 1][j], scs[i][j + 1])
        # print(scs[i], scs[i + 1])

    return scs

test_class(Solution, examples)

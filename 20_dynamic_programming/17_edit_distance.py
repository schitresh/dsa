from utils import test_class

# Given two strings s1 and s2 of lengths m and n respectively and below operations that
# can be performed on s1. Find the minimum number of edits (operations) required
# to convert ‘s1‘ into ‘s2‘.
# 1. Insert: Insert any character before or after any index of s1
# 2. Remove: Remove a character of s1
# 3. Replace: Replace a character at any index of s1 with some other character
# Note: All of the above operations are of equal cost.

examples = [
  {
    'input': ['geek', 'gesek'],
    'output': 1, # s1 can be converted to s2 by adding 's' between the two 'e's
  },
  {
    'input': ['cat', 'cut'],
    'output': 1, # Replace 'a' with 'u'
  },
  {
    'input': ['sunday', 'saturday'],
    'output': 3, # Replace 'n' with 'r' and insert 'a' & 't'
  },
  {
    'input': ['GEEXSFRGEEKKS', 'GEEKSFORGEEKS'],
    'output': 3, # Replace 'x' with 'k', insert 'o' between 'f' & 'r', remove last 'k'
  },
]

# Recursion
# Time Complexity: O(2^min(m, n))
# Auxiliary Space: O(min(m, n))
class Solution:
  def solve(self, string1, string2):
    self.string1 = string1
    self.string2 = string2
    return self.edit_dist(0, 0)

  def edit_dist(self, index1, index2):
    if index1 == len(self.string1) or index2 == len(self.string2):
      return 0

    if self.string1[index1] == self.string2[index2]:
      return self.edit_dist(index1 + 1, index2 + 1)

    dist1 = self.edit_dist(index1 + 1, index2) # Insert
    dist2 = self.edit_dist(index1 + 1, index2 + 1) # Replace
    dist3 = self.edit_dist(index1, index2 + 1) # Remove
    return 1 + min(dist1, dist2, dist3)

test_class(Solution, examples)

# Recursion
# Time Complexity: O(3^min(m, n))
# Auxiliary Space: O(min(m, n))
class Solution1b:
  def solve(self, string1, string2):
    self.string1 = string1
    self.string2 = string2
    return self.edit_dist(len(string1) - 1, len(string2) - 1)

  def edit_dist(self, index1, index2):
    if index1 == 0: return index2
    if index2 == 0: return index1

    if self.string1[index1] == self.string2[index2]:
      return self.edit_dist(index1 - 1, index2 - 1)

    # If char is inserted, the new char in string1 matches the current char
    # in string2. Hence, the current position in string1 needs to be compared
    # with the next char in string2
    dist1 = self.edit_dist(index1, index2 - 1) # Insert
    dist2 = self.edit_dist(index1 - 1, index2 - 1) # Replace
    dist3 = self.edit_dist(index1 - 1, index2) # Remove
    return 1 + min(dist1, dist2, dist3)

test_class(Solution1b, examples)

# Memoization (Top-Down)
# Time Complexity: O(m * n)
# Auxiliary Space: O(m * n)
class Solution2:
  def solve(self, string1, string2):
    self.string1 = string1
    self.string2 = string2
    self.min_dist = [[None] * len(string2) for _ in range(len(string1))]
    return self.edit_dist(len(string1) - 1, len(string2) - 1)

  def edit_dist(self, index1, index2):
    if index1 == 0: return index2
    if index2 == 0: return index1

    if self.min_dist[index1][index2]:
      return self.min_dist[index1][index2]

    if self.string1[index1] == self.string2[index2]:
      self.min_dist[index1][index2] = self.edit_dist(index1 - 1, index2 - 1)
      return self.min_dist[index1][index2]

    dist1 = self.edit_dist(index1, index2 - 1) # Insert
    dist2 = self.edit_dist(index1 - 1, index2 - 1) # Replace
    dist3 = self.edit_dist(index1 - 1, index2) # Remove
    self.min_dist[index1][index2] = 1 + min(dist1, dist2, dist3)

    return self.min_dist[index1][index2]

test_class(Solution2, examples)

# Tabulation (Bottom-Up)
# Time Complexity: O(m * n)
# Auxiliary Space: O(m * n)
class Solution3:
  def solve(self, string1, string2):
    min_dist = [[0] * (len(string2) + 1) for _ in range(len(string1) + 1)]

    for index1 in range(len(string1)):
      # If string2 is empty, the edits required is length of string1
      min_dist[index1 + 1][0] = index1 + 1

    for index2 in range(len(string2)):
      # If string1 is empty, the edits required is length of string2
      min_dist[0][index2 + 1] = index2 + 1

    for index1 in range(len(string1)):
      for index2 in range(len(string2)):
        if string1[index1] == string2[index2]:
          min_dist[index1 + 1][index2 + 1] = min_dist[index1][index2]
        else:
          # If char is inserted, the new char in string1 matches the current char
          # in string2. Hence, the current position in string1 needs to be compared
          # with the next char in string2
          dist1 = min_dist[index1][index2 + 1] # Insert
          dist2 = min_dist[index1][index2] # Replace
          dist3 = min_dist[index1 + 1][index2] # Remove
          min_dist[index1 + 1][index2 + 1] = 1 + min(dist1, dist2, dist3)

    return min_dist[-1][-1]

test_class(Solution3, examples)

# Tabulation (Bottom-Up) with space optmization
# Time Complexity: O(m * n)
# Auxiliary Space: O(n)
class Solution4:
  def solve(self, string1, string2):
    min_dist = [0] * (len(string2) + 1)

    for index2 in range(len(string2)):
      # If string1 is empty, the edits required is length of string2
      min_dist[index2 + 1] = index2 + 1

    for index1 in range(len(string1)):
      curr_dist = [0] * (len(string2) + 1)
      curr_dist[0] = index1 + 1

      for index2 in range(len(string2)):
        if string1[index1] == string2[index2]:
          curr_dist[index2 + 1] = min_dist[index2]
        else:
          dist1 = min_dist[index2 + 1] # Insert
          dist2 = min_dist[index2] # Replace
          dist3 = curr_dist[index2] # Remove
          curr_dist[index2 + 1] = 1 + min(dist1, dist2, dist3)

      min_dist = curr_dist

    return min_dist[-1]

test_class(Solution4, examples)

# Tabulation (Bottom-Up) with furthur space optmization
# Time Complexity: O(m * n)
# Auxiliary Space: O(n)
class Solution5:
  def solve(self, string1, string2):
    min_dist = [0] * (len(string2) + 1)

    for index2 in range(len(string2)):
      # If string1 is empty, the edits required is length of string2
      min_dist[index2 + 1] = index2 + 1

    for index1 in range(len(string1)):
      prev = min_dist[0]
      min_dist[0] = index1 + 1

      for index2 in range(len(string2)):
        curr = min_dist[index2 + 1]

        if string1[index1] == string2[index2]:
          min_dist[index2 + 1] = prev
        else:
          dist1 = curr # Insert
          dist2 = prev # Replace
          dist3 = min_dist[index2] # Remove
          min_dist[index2 + 1] = 1 + min(dist1, dist2, dist3)

        prev = curr

    return min_dist[-1]

test_class(Solution5, examples)

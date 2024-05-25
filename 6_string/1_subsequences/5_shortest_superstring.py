from utils import test_class

# Find the count of distinct occurrences of T in S as a subsequence
examples = [
  {
    'input': [['abcd', 'efg', 'hi']],
    'output': 'abcdefghi'
  },
  {
    'input': [['catgc', 'ctaagt', 'gcta', 'ttca', 'atgcatc']],
    'output': 'gctaagttcatgcatc'
  }
]

# Time Complexity: O(n^3 * max_length))
# Space Complexity: O(n * max_length) due to recursive stack
# Greedy Approximate Algorithm
class Solution:
  def overlap_length(self, string1, string2):
    suffix1 = ''
    prefix2 = ''
    overlap_len = 0

    for i in range(min(len(string1), len(string2))):
      suffix1 = string1[len(string1) - 1 - i] + suffix1
      prefix2 += string2[i]

      if suffix1 == prefix2:
        overlap_len = i + 1

    return overlap_len

  def merged_string(self, string1, string2):
    merged_string = ''
    overlap1 = self.overlap_length(string1, string2)
    overlap2 = self.overlap_length(string2, string1)
    overlap_len = max(overlap1, overlap2)

    if overlap_len == 0:
      merged_string = string1 + string2
    elif overlap1 >= overlap2:
      merged_string = string1 + string2[overlap1 : ]
    else:
      merged_string = string2 + string1[overlap2 : ]

    return merged_string, overlap_len

  def solve(self, input_strings):
    strings = input_strings.copy()

    # In each iteration, find two most overlapping strings and merge them
    for strings_left in range(len(strings), 1, -1):
      max_overlap_len = -1
      max_merged_string = ''
      index1 = 0
      index2 = 0

      for i in range(strings_left):
        for j in range(i + 1, strings_left):
          merged_string, overlap_len = self.merged_string(strings[i], strings[j])

          if max_overlap_len < overlap_len:
            max_overlap_len = overlap_len
            max_merged_string = merged_string
            index1 = i
            index2 = j

      strings[index1] = max_merged_string
      strings[index2] = strings[strings_left - 1]

    return strings[0]


# Time Complexity: O(n^3 * max_length))
# Space Complexity: O(n * max_length) due to recursive stack
# Travelling Salesman DP Approach
class Solution2:
  def overlap_length(self, string1, string2):
    suffix1 = ''
    prefix2 = ''
    overlap_len = 0

    for i in range(min(len(string1), len(string2))):
      suffix1 = string1[i] + suffix1
      prefix2 += string2[i]

      if suffix1 == prefix2:
        overlap_len = i + 1

    return overlap_len

  def solve(self, strings):
    overlaps = [[0] * len(strings) for _ in range(len(strings))]

    for i in range(len(strings)):
      for j in range(i, len(strings)):
        overlaps[i][j] = self.overlap_length(strings[i], strings[j])
        overlaps[j][i] = self.overlap_length(strings[j], strings[i])

test_class(Solution, examples)
test_class(Solution2, examples)

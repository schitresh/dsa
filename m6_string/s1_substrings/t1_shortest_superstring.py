from utils import test_class

# Given an array of strings, find the smallest string
# that contains each of the strings in the array as substring
# Assume that no string is substring of another string in the array
# NP Hard problem (solution takes exponential time)

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

# Greedy Approximate Algorithm
# Copy the array into an auxiliary temp array
# Iterate over temp array and find the most overlapping pair in each iteration
# Replace this pair with their combined string
# Two strings are overlapping if the suffix of one is same as the prefix of other
# Time Complexity: O(n^3 * max_length_of_string))
# Auxiliary Space: O(n * max_length_of_string) for temp array
class Solution:
  def solve(self, input_strings):
    strings = input_strings.copy()

    # In each iteration, find two most overlapping strings and merge them
    for strings_left in range(len(strings), 1, -1):
      # Initialize max_overlap_len with -1
      # Because we will merge two strings even if there is no overlap
      # In such a case, overlap_len will be 0
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

      # If there is no overlap, initial two strings will considered and merged
      strings[index1] = max_merged_string
      strings[index2] = strings[strings_left - 1]

    return strings[0]

  def overlap_length(self, string1, string2):
    suffix1 = ''
    prefix2 = ''
    overlap_len = 0

    # Compare suffix & prefix for all iterations of the strings
    # Consider catgc & atgcatc, where atgc overlaps
    # But intermediate iteration like gc & at don't overlap
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

test_class(Solution, examples)

# Todo: Travelling Salesman DP Approach
# We have to find the shortest string that has each char of the strings in the array
# If we consider each char as a node, then each string becomes a directed path
# And the array becomes a directed graph with all these paths
# This now becomes a problem to find the shortest path in the graph
# which visits every node exactly once
# Time Complexity: O(n^2 * 2^n))
# Auxiliary Space: O(n * 2^n)

from utils import test_class

# Given a rod of length n, cut the rod in such a way that the total number of segments
# is maximized. The segments can only be of length x, y, and z.
# If no segment can be cut then return 0.

examples = [
  {
    'input': [4, [2, 1, 1]], # n, [x, y, z]
    'output': 4, # Can make maximum of 4 segments each of length 1
  },
  {
    'input': [5, [5, 3, 2]],
    'output': 2, # Can make two segments of length 3 & 2
  },
  {
    'input': [7, [8, 9, 10]],
    'output': 0, # All segment lenghts are more than the rod length
  },
]

# Recursion
# Time Complexity: O(3^n), since there are 3 ways to cut a segment (x, y, z)
# Auxiliary Space: O(n), due to recursive stack
class Solution:
  def solve(self, rod_len, segment_lens):
    self.rod_len = rod_len
    self.segment_lens = segment_lens

    return self.cut_rod(rod_len, 0)

  def cut_rod(self, remaining_len, seg_count):
    if remaining_len < 0: return 0
    if remaining_len == 0: return seg_count

    max_segments = 0
    for seg_len in self.segment_lens:
      segments = self.cut_rod(remaining_len - seg_len, seg_count + 1)
      max_segments = max(max_segments, segments)

    return max_segments

test_class(Solution, examples)

# Recursion
# Time Complexity: O(3^n), since there are 3 ways to cut a segment (x, y, z)
# Auxiliary Space: O(n), due to recursive stack
class Solution1b:
  def solve(self, rod_len, segment_lens):
    self.rod_len = rod_len
    self.segment_lens = segment_lens

    segments = self.cut_rod(rod_len)

    if segments == -1: return 0
    return segments

  def cut_rod(self, remaining_len):
    if remaining_len < 0: return -1
    if remaining_len == 0: return 0

    max_segments = -1
    for seg_len in self.segment_lens:
      segments = self.cut_rod(remaining_len - seg_len)
      max_segments = max(max_segments, segments)

    if max_segments == -1: return -1
    return max_segments + 1

test_class(Solution1b, examples)

# Memoization (Top-Down)
# Time Complexity: O(n)
# Auxiliary Space: O(n), due to recursive stack
class Solution2:
  def solve(self, rod_len, segment_lens):
    self.rod_len = rod_len
    self.segment_lens = segment_lens
    self.segments = {}

    self.cut_rod(rod_len)

    if self.segments[rod_len] == -1: return 0
    return self.segments[rod_len]

  def cut_rod(self, remaining_len):
    if remaining_len < 0: return -1
    if remaining_len == 0: return 0

    if remaining_len in self.segments:
      return self.segments[remaining_len]

    max_segments = -1
    for seg_len in self.segment_lens:
      segments = self.cut_rod(remaining_len - seg_len)
      max_segments = max(max_segments, segments)

    if max_segments != -1: max_segments += 1
    self.segments[remaining_len] = max_segments
    return max_segments

test_class(Solution2, examples)

# Tabulation (Bottom-Up)
# Time Complexity: O(n)
# Auxiliary Space: O(n), due to recursive stack
class Solution3:
  def solve(self, rod_len, segment_lens):
    segments = [-1] * (rod_len + 1)
    segments[0] = 0

    for i in range(rod_len + 1):
      if segments[i] == -1: continue

      for seg_len in segment_lens:
        curr_len = i + seg_len
        if curr_len > rod_len: continue
        segments[curr_len] = max(segments[curr_len], segments[i] + 1)

    if segments[rod_len] == -1: return 0
    return segments[rod_len]

test_class(Solution3, examples)

# Tabulation (Bottom-Up)
# Time Complexity: O(n)
# Auxiliary Space: O(n), due to recursive stack
class Solution3b:
  def solve(self, rod_len, segment_lens):
    segments = [-1] * (rod_len + 1)
    segments[0] = 0

    for i in range(rod_len + 1):
      for seg_len in segment_lens:
        prev_len = i - seg_len
        if prev_len < 0: continue
        if segments[prev_len] == -1: continue

        segments[i] = max(segments[i], segments[prev_len] + 1)

    if segments[rod_len] == -1: return 0
    return segments[rod_len]

test_class(Solution3b, examples)

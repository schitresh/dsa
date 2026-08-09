from utils import test_class

# An interval is represented as a combination of start time and end time. Given a set of
# intervals, check if any two intervals intersect.

examples = [
  {
    'input': [[[1, 3], [5, 7], [2, 4], [6, 8]]],
    'output': True,
  },
  {
    'input': [[[1, 3], [7, 9], [4, 6], [10, 13]]],
    'output': False,
  },
]

# Sorting
# Time Complexity: O(n * log(n))
# Auxiliary Space: O(1)
class Solution:
  def solve(self, intervals):
    intervals.sort()

    for i in range(1, len(intervals)):
      if intervals[i - 1][1] >= intervals[i][0]:
        return True

    return False

test_class(Solution, examples)

# Hashing
# Time Complexity: O(max_num + n)
# Auxiliary Space: O(max_num)
class Solution2:
  def solve(self, intervals):
    max_num = max(intervals, key = lambda x: x[1])[1]
    freq = [0] * (max_num + 1)

    for interval in intervals:
      freq[interval[0]] += 1
      freq[interval[1]] -= 1

    for i in range(1, max_num + 1):
      freq[i] += freq[i - 1]

    for count in freq:
      if count > 1: return True

    return False

test_class(Solution2, examples)

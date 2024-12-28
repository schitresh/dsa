from utils import test_class

# Given a sorted array of positive integers, find the frequency for each element in the
# array. Assume that all elements in the array are less than some constant M.
# Note: Do this without traversing the complete array. i.e. expected time complexity is
# less than O(n)

examples = [
  {
    'input': [[1, 1, 1, 2, 3, 3, 5, 5, 8, 8, 8, 9, 9, 10]],
    'output': {1: 3, 2: 1, 3: 2, 5: 2, 8: 3, 9: 2, 10: 1},
  },
  {
    'input': [[2, 2, 6, 6, 7, 7, 7, 11] ],
    'output': {2: 2, 6: 2, 7: 3, 11: 1},
  }
]

# Binary Search
# Time Complexity: O(log(n))
# T(n) = O(m * log(n)), where m is number of distinct elements
# But since m <= M (a constant), i.e. elements are in a limited range, T(n) = O(log(n))
# Auxiliary Space: O(1)
class Solution:
  def solve(self, array):
    self.array = array
    self.freq = {}
    self.cal_freq(0, len(array) - 1)
    return self.freq

  def cal_freq(self, left, right):
    if self.array[left] == self.array[right]:
      element = self.array[left]
      if element not in self.freq:
        self.freq[element] = 0

      self.freq[element] += right - left + 1
      return

    mid = left + (right - left) // 2
    self.cal_freq(left, mid)
    self.cal_freq(mid + 1, right)

test_class(Solution, examples)

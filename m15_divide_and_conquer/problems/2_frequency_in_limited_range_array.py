from utils import test_class

# Given a sorted array of positive integers, find the frequency for each element in the
# array. Assume that all elements in the array are less than some constant M.
# Do this without traversing the complete array, i.e. expected time complexity is
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

# Linear Search
# Time Complexity: O(n)
# Auxiliary Space: O(1)

# Binary Search
# Time Complexity: O(log(n))
# T(n) = O(m * log(n)), where m is number of distinct elements
# But m <= M since elements are in a limited range, so T(n) = O(log(n))
# Auxiliary Space: O(1)
class Solution:
  def solve(self, array):
    self.array = array
    self.freq = {}
    self.calculate_freq(0, len(array) - 1)
    return self.freq

  def calculate_freq(self, left, right):
    if self.array[left] == self.array[right]:
      num = self.array[left]
      self.freq[num] = self.freq.get(num, 0) + (right - left + 1)
      return

    mid = left + (right - left) // 2
    self.calculate_freq(left, mid)
    self.calculate_freq(mid + 1, right)

test_class(Solution, examples)

from utils import test_class

# Given an array of size n, divide it into two subsets such that the absolute
# difference between the sum of elements in the two subsets is minimum.
# If n is even, both subsets must have exactly n/2 elements.
# If n is odd, one subset must have (n+1)/2 and the other must have (n-1)/2
# elements.

examples = [
  {
    'input': [[3, 4, 5, -3, 100, 1, 89, 54, 23, 20]],
    'output': [[3, 5, -3, 89, 54], [4, 100, 1, 23, 20]]
    # or [[4, 100, 1, 23, 20], [3, 5, -3, 89, 54]]
  },
  {
    'input': [[23, 45, -34, 12, 0, 98, -99, 4, 189, -1, 4]],
    'output': [[23, 0, -99, 4, 189, 4], [45, -34, 12, 98, -1]]
    # or [[45, -34, 12, 0, 98, -1], [23, -99, 4, 189, 4]]
  },
]

# Backtracking
# Recurse through all elements of the array. First include the current element in the
# first subset and continue. Later backtrack and include it in the second subset
# and continue till both subsets are formed.
# Time Complexity: O(2^n)
# Auxiliary Space: O(n)
class Solution:
  def solve(self, array):
    self.array = array
    self.arr1 = []
    self.arr2 = []

    self.size1 = (len(array) + 1) // 2
    self.size2 = len(array) - self.size1

    self.min_diff = float('inf')
    self.subarrays_with_min_diff(0, [], [])
    return [self.arr1, self.arr2]

  def subarrays_with_min_diff(self, i, arr1, arr2):
    if len(arr1) == self.size1 and len(arr2) == self.size2:
      curr_diff = abs(sum(arr1) - sum(arr2))
      if curr_diff < self.min_diff:
        self.arr1 = arr1.copy()
        self.arr2 = arr2.copy()
        self.min_diff = curr_diff
      return

    if len(arr1) < self.size1:
      arr1.append(self.array[i])
      self.subarrays_with_min_diff(i + 1, arr1, arr2)
      arr1.pop()

    if len(arr2) < self.size2:
      arr2.append(self.array[i])
      self.subarrays_with_min_diff(i + 1, arr1, arr2)
      arr2.pop()

test_class(Solution, examples)

# Backtracking
# Only form one subset, the second subset will be all the element not in the first
# subset. Keep track of the selected elements of the first subset and it's sum.
# Subtract the sum from the array sum to determine if it's the min diff.
# Time Complexity: O(2^n)
# Auxiliary Space: O(n)
class Solution2:
  def solve(self, array):
    self.array = array
    self.arr_sum = sum(array)

    self.selection = [False] * len(array)
    self.sel_size = (len(array) + 1) // 2

    self.min_diff = float('inf')
    self.select_with_min_diff(0, [False] * len(array), 0, 0)

    arr1 = []
    arr2 = []
    for i in range(len(array)):
      if self.selection[i]:
        arr1.append(array[i])
      else:
        arr2.append(array[i])

    return [arr1, arr2]

  def select_with_min_diff(self, i, curr_sel, curr_size, curr_sum):
    if curr_size == self.sel_size:
      curr_diff = abs(curr_sum - (self.arr_sum - curr_sum))
      if curr_diff < self.min_diff:
        self.min_diff = curr_diff
        self.selection = curr_sel.copy()
      return

    if i == len(self.array):
      return

    # Do not include current element in arr1
    self.select_with_min_diff(i + 1, curr_sel, curr_size, curr_sum)

    # Include current element in arr1
    curr_sel[i] = True
    self.select_with_min_diff(i + 1, curr_sel, curr_size + 1, curr_sum + self.array[i])
    # Backtrack
    curr_sel[i] = False

test_class(Solution2, examples)

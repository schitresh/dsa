from utils import test_class

# Given an array, print all the subsets of the array. A subset of an array is a tuple
# that can be obtained from the array by removing some (possibly all) elements of it.

examples = [
  {
    'input': [[1, 2, 3]],
    'output': [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]
    # Order can be different for different solution approaches
  },
  {
    'input': [[2, 4]],
    'output': [[], [2], [2, 4], [4]]
  },
  {
    'input': [[1, 2, 2]],
    'output': [[], [1], [1, 2], [2], [2, 2], [1, 2, 2]]
  },
  {
    'input': [[1, 1, 2, 3]],
    'output': [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]
  },
]

# Backtracking
# Time Complexity: O(2^n)
# Auxiliary Space: O(2^n), to store subsets
class Solution:
  def solve(self, array):
    self.array = array
    self.subsets = []
    self.traverse(0, [])
    return self.subsets

  def traverse(self, index, subset):
    if index == len(self.array):
      self.subsets.append(subset)
      return

    self.traverse(index + 1, subset)
    self.traverse(index + 1, subset + [self.array[index]])

# This won't work because there is no way to track duplicates in respect to previous
# indexes. For example, 1 with 2 & 1 with duplicate 2. If we ignore the duplicate items
# all together, we will miss genuine subsets like [2, 2]
# test_class(Solution, examples)

# Time Complexity: O(n * 2^n)
# Auxiliary Space: O(2^n), to store subsets
class Solution2:
  def solve(self, array):
    self.array = array
    self.subsets = []
    self.traverse(0, [])
    return self.subsets

  def traverse(self, index, subset):
    self.subsets.append(subset.copy())

    for i in range(index, len(self.array)):
      if i != index and self.array[i] == self.array[i - 1]:
        continue
      subset.append(self.array[i])
      self.traverse(i + 1, subset)
      subset.pop()

test_class(Solution2, examples)

# Bit Manipulation
# Since each element has only two choices i.e. either get included or get excluded, assign
# these choices to a bit representation sp that 0 means excluded & 1 means included.
# i'th bit represents i'th element of the array.
# If there are N elements in the array, it will have 2^N subsets. These subsets can be
# uniquely expressed in the form of bit representation of number from 0 to (2^N)-1.
# Example: If the array is [A, B], all the subsets of this array form the bit
# representation of number from 0 to (2^2)-1, i.e. 0 to 3
# 0 = 00 => A excluded, B excluded => []
# 1 = 01 => A excluded, B included => [B]
# 2 = 10 => A included, B excluded => [A]
# 3 = 11 => A included, B included => [A, B]
# Time Complexity: O(n * 2^n)
# Auxiliary Space: O(2^n), to store subsets
class Solution3:
  def solve(self, array):
    subsets = []
    binary_len = 1 << len(array) # 2^n

    # 0 to (2^n - 1)
    for i in range(binary_len):
      subset = []
      for j in range(len(array)):
        # Check if the subset includes the current element of the array
        # i & (2^j)
        if i & (1 << j) != 0:
          subset.append(array[j])

      if subset not in subsets:
        subsets.append(subset)

    return subsets

test_class(Solution3, examples)

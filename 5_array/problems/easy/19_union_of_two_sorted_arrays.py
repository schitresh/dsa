from utils import test_class

# Given two sorted arrays, return union of both the arrays in sorted order. Union of two
# arrays is an array having all distinct elements that are present in either array. The
# input arrays may contain duplicates.

examples = [
  {
    'input': [[1, 1, 2, 2, 2, 4], []],
    'output': [1, 2, 4],
  },
  {
    'input': [[1, 1, 2, 2, 2, 4], [2, 2, 4, 4]],
    'output': [1, 2, 4],
  },
  {
    'input': [[3, 5, 10, 10, 10, 15, 15, 20], [5, 10, 10, 15, 30]],
    'output': [3, 5, 10, 15, 20, 30],
  },
]

# Time Complexity: O(n + m)
# Auxiliary Space: O(1)
class Solution:
  def solve(self, arr1, arr2):
    union = []
    idx1 = 0
    idx2 = 0

    while idx1 < len(arr1) and idx2 < len(arr2):
      if arr1[idx1] < arr2[idx2]:
        num = arr1[idx1]
        if not union or union[-1] != num: union.append(num)
        idx1 += 1
      else:
        num = arr2[idx2]
        if not union or union[-1] != num: union.append(num)
        idx2 += 1

    while idx1 < len(arr1):
      num = arr1[idx1]
      if not union or union[-1] != num: union.append(num)
      idx1 += 1

    while idx2 < len(arr2):
      num = arr2[idx2]
      if not union or union[-1] != num: union.append(num)
      idx2 += 1

    return union

test_class(Solution, examples)

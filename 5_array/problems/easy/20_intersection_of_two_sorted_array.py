from utils import test_class

# Given two sorted arrays, return intersection. Intersection of two arrays is said to
# be elements that are common in both arrays. The intersection should not count
# duplicate elements and the result should contain items in sorted order.

examples = [
    {
    'input': [[1, 2, 3], []],
    'output': [],
  },
  {
    'input': [[1, 2, 3], [4, 5, 6]],
    'output': [],
  },
  {
    'input': [[1, 1, 2, 2, 2, 4], [2, 2, 4, 4]],
    'output': [2, 4],
  },
  {
    'input': [[3, 5, 10, 10, 10, 15, 15, 20], [5, 10, 10, 15, 30]],
    'output': [5, 10, 15],
  },
]

# Time Complexity: O(n * m)
# Auxiliary Space: O(1)
class Solution:
  def solve(self, arr1, arr2):
    intersection = []
    idx1 = 0
    idx2 = 0

    while idx1 < len(arr1) and idx2 < len(arr2):
      if arr1[idx1] < arr2[idx2]:
        idx1 += 1
      elif arr1[idx1] > arr2[idx2]:
        idx2 += 1
      else:
        if not intersection or intersection[-1] != arr1[idx1]:
          intersection.append(arr1[idx1])
        idx1 += 1
        idx2 += 1

    return intersection

test_class(Solution, examples)

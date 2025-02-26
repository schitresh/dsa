from utils import test_class

# Given two arrays, return the intersection of both the arrays in any order.
# Intersection of two arrays is said to be elements that are common in both arrays. The
# intersection should not count duplicate elements.

examples = [
  {
    'input': [[1, 2, 3], [4, 5, 6]],
    'output': [],
  },
  {
    'input': [[1, 2, 3, 2, 1], [3, 2, 2, 3, 3, 2]],
    'output': [2, 3],
  },
    {
    'input': [[1, 2, 1, 3, 1], [3, 1, 3, 4, 1]],
    'output': [1, 3],
  },
]

# Time Complexity: O(n * m)
# Auxiliary Space: O(1)
class Solution:
  def solve(self, arr1, arr2):
    intersection = []

    for num1 in arr1:
      if num1 in arr2 and num1 not in intersection:
        intersection.append(num1)

    return intersection

test_class(Solution, examples)

# Using two Hash Sets
# Time Complexity: O(n + m)
# Auxiliary Space: O(n)
class Solution2:
  def solve(self, arr1, arr2):
    set1 = set(arr1)
    intersection = set()

    for num2 in arr2:
      if num2 in set1 and num2 not in intersection:
        intersection.add(num2)

    return list(intersection)

test_class(Solution2, examples)

# Using Hash
# Time Complexity: O(n + m)
# Auxiliary Space: O(n)
class Solution3:
  def solve(self, arr1, arr2):
    common = {}

    for num1 in arr1:
      common[num1] = False

    for num2 in arr2:
      if num2 in common:
        common[num2] = True

    intersection = []
    for key, value in common.items():
      if value:
        intersection.append(key)

    return intersection

test_class(Solution3, examples)

# Using one Hash Set
# Time Complexity: O(n + m)
# Auxiliary Space: O(n)
class Solution4:
  def solve(self, arr1, arr2):
    set1 = set(arr1)
    intersection = []

    for num2 in arr2:
      if num2 in set1:
        intersection.append(num2)
        set1.remove(num2)

    return list(intersection)

test_class(Solution4, examples)

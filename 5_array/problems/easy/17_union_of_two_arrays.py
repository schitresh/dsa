from utils import test_class

# Given two arrays, return the union of both the arrays in any order.
# Union of two arrays is an array having all distinct elements that are present in
# either array.

examples = [
  {
    'input': [[1, 2, 3], [4, 5, 6]],
    'output': [1, 2, 3, 4, 5, 6],
  },
  {
    'input': [[1, 2, 3, 2, 1], [3, 2, 2, 3, 3, 2]],
    'output': [1, 2, 3],
  },
]

# Time Complexity: O(n * m)
# Auxiliary Space: O(1)
class Solution:
  def solve(self, arr1, arr2):
    union = []

    for num1 in arr1:
      if num1 not in union:
        union.append(num1)

    for num2 in arr2:
      if num2 not in union:
        union.append(num2)

    return union

test_class(Solution, examples)

# Using Hash Set
# Time Complexity: O(n + m)
# Auxiliary Space: O(n)
class Solution2:
  def solve(self, arr1, arr2):
    union = set()

    for num1 in arr1:
      union.add(num1)

    for num2 in arr2:
      union.add(num2)

    return list(union)

test_class(Solution2, examples)

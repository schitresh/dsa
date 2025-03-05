from utils import test_class

# Given two arrays a and b of equal length, determine if the given arrays are equal or
# not. Two arrays are considered equal if:
# - Both arrays contain the same set of elements
# - The arrangements (or permutations) of elements may be different
# - If there are repeated elements, the counts of each element must be the same in both
#   the arrays

examples = [
  {
    'input': [[1, 2, 5, 4, 0], [2, 4, 5, 0, 1]],
    'output': True,
  },
  {
    'input': [[1, 2, 5, 4, 0, 2, 1], [2, 4, 5, 0, 1, 1, 2]],
    'output': True,
  },
  {
    'input': [[1, 7, 1], [7, 7, 1]],
    'output': False,
  },
]

# Sorting & Two pointers
# Time Complexity: O(n * log(n))
# Auxiliary Space: O(1)
class Solution:
  def solve(self, arr1, arr2):
    return sorted(arr1) == sorted(arr2)

test_class(Solution, examples)

# Hashing
# Time Complexity: O(n)
# Auxiliary Space: O(n)
class Solution2:
  def solve(self, arr1, arr2):
    count_hash = {}

    for item1 in arr1:
      if item1 in count_hash: count_hash[item1] += 1
      else: count_hash[item1] = 1

    for item2 in arr2:
      if item2 not in count_hash: return False
      if count_hash[item2] == 0: return False

      count_hash[item2] -= 1

    return True

test_class(Solution2, examples)

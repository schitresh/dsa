from utils import test_class

# Given an array of n elements. Consider array as circular array i.e element after a(n)
# is a(1). The task is to find maximum sum of the difference between consecutive elements
# with rearrangement of array element allowed i.e after rearrangement of element,
# find |a1 - a2| + |a2 - a3| + ... + |a(n - 1) - an| + |an - a1|.

examples = [
  {
    'input': [[4, 2, 1, 8]],
    'output': 18,
    # Rearrage the array as [1, 8, 2, 4]
    # Sum of difference between consecutive element
    # = |1 - 8| + |8 - 2| + |2 - 4| + |4 - 1| = 7 + 6 + 2 + 3 = 18
  },
  {
    'input': [[10, 12, 15]],
    'output': 10,
  },
  {
    'input': [[1, 2, 3, 4, 5]],
    'output': 12,
  }
]

# We need to form pairs such that the smallest element and the largest element are paired
# So we can sort the array and subtract the first and last element.
# We can keep left and right points, and keep moving them in each iteration.
# But we also need to subtract adjacent elements, so in one iteration move left
# and in next iteration move right. At last, subtract first element with the right
# For example, consider [4, 2, 1, 8] which after sorting becomes [1, 2, 4, 8]
# |1 - 8| + |2 - 8| (left moved) + |2 - 4| (right moved) + |1 - 4| (first & right)
# Time Complexity: O(n * log(n))
# Auxiliary Space: O(1)
class Solution:
  def solve(self, array):
    array.sort()
    diff_sum = 0

    left = 0
    right = len(array) - 1
    flag = True

    while left < right:
      diff_sum += abs(array[left] - array[right])

      if flag: left += 1
      else: right -= 1

      flag = not flag

    diff_sum += abs(array[0] - array[right])
    return diff_sum

test_class(Solution, examples)

# If we sort the array and pair smallest with largest elements:
# a1, a(n), a2, a(n - 1), ..., a(n/2), a(n/2 + 1)
# |a(1) - a(n)| + |a(n) - a(2)| +  ... + |a(n/2) - a(n/2 + 1)| + |a(n/2 + 1) - a(1)|
# Since the array is sorted, we can subtract like below with putting abs()
# = a(n) - a(1) + a(n) - a(2) + a(n-1) - a(2) ... a(n/2 + 1) - a(n/2) + a(n/2 + 1) - a(1)
# = [a(n) + a(n) + a(n - 1) + a(n - 1) + ... ] - [a(1) + a(1) + a(2) + a(2)]
# = 2 * [a(n) + a(n - 1) + ... + a(n/2 + 1)] - 2 * [a(1) + a(2) + ... + a(n/2) ]
# Time Complexity: O(n * log(n))
# Auxiliary Space: O(1)
class Solution2:
  def solve(self, array):
    array.sort()
    diff_sum = 0

    for i in range(len(array) // 2):
      diff_sum -= 2 * array[i]
      diff_sum += 2 * array[len(array) - 1 - i]

    return diff_sum

test_class(Solution2, examples)

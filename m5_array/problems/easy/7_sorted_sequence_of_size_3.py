from utils import test_class

# Given an array of integers, find 3 elements such that a[i] < a[j] < a[k], where
# i < j < k. If there are multiple such triplets, then return any one of them.

examples = [
  {
    'input': [[1, 2, 3, 4]],
    'output': [1, 2, 3], # or [1, 2, 4] or [1, 3, 4] or [2, 3, 4]
  },
  {
    'input': [[4, 3, 2, 1]],
    'output': [],
  },
  {
    'input': [[12, 11, 10, 5, 6, 2, 30]],
    'output': [5, 6, 30],
  },
  {
    'input': [[12, 11, 10, 5, 6, 2, 3, 4]],
    'output': [2, 3, 4],
  },
  {
    'input': [[8, 2, 7, 3, 1, 5]],
    'output': [2, 3, 5],
  },
]

# Find Middle Element
# Find an element which has an element smaller than itself on the left side of the array
# and an element greater than itself on the right side of the array
# Time Complexity: O(n^2)
# Auxiliary Space: O(1)
class Solution:
  def solve(self, array):
    for i in range(1, len(array) - 1):
      smaller = None
      for j in range(i):
        if array[j] < array[i]:
          smaller = array[j]

      if not smaller: continue

      for k in range(i + 1, len(array)):
        if array[i] < array[k]:
          return [smaller, array[i], array[k]]

    return []

test_class(Solution, examples)

# Find Middle Element with auxiliary space
# Find an element which has an element smaller than itself on the left side of the array
# and an element greater than itself on the right side of the array.
# Instead of comparing all elements left of index, we can just track the minimum element
# till the index i and check if the arr[i] is greater than the min element.
# Similary, we can track the maximum element towards the right of current index.
# Traverse from left keeping track of the min and assign it at each index i, smaller[i]
# will store the index of a number which is smaller than arr[i] and is on the left side.
# Similar, traverse from right keeping track of the max, greater[i] will store the index
# of a number which is greater than arr[i] and is on the right side.
# Finally, traverse both smaller and greater, and find the index for which both
# smaller[i] and greater[i] are not equal to -1.
# Time Complexity: O(n)
# Auxiliary Space: O(n)
class Solution2:
  def solve(self, array):
    min_idx = 0
    max_idx = len(array) - 1

    smaller = [-1] * len(array)
    for i in range(1, len(array)):
      if array[i] <= array[min_idx]:
        min_idx = i
      else:
        smaller[i] = min_idx

    greater = [-1] * len(array)
    for i in range(len(array) - 2, -1, -1):
      if array[i] >= array[max_idx]:
        max_idx = i
      else:
        greater[i] = max_idx

    for i in range(len(array)):
      if smaller[i] != -1 and greater[i] != -1:
        return [array[smaller[i]], array[i], array[greater[i]]]

    return []

test_class(Solution2, examples)

# Find first two and then third
# First find two elements such that arr[i] < arr[j], then find a third element arr[k]
# greater than arr[j].
# Finding the first two elements can be done in linear time with just one loop. While
# keeping track of the min element, its easy to find hte next subsequent element that is
# greater than it. Thus we have arr[i] & arr[j].
# As soon as we have arr[i] & arr[j], we can immediately start monitoring the subsequent
# elements for an arr[k] > arr[j] in the same loop. Thus we can find all three values in
# a single pass over the array.
# Time Complexity: O(n)
# Auxiliary Space: O(1)
class Solution3:
  def solve(self, array):
    min_num = array[0]

    # Track the sequence
    seq_len = 1
    seq_first = min_num
    seq_second = -float('inf')

    for i in range(1, len(array)):
      if array[i] <= min_num:
        min_num = array[i]
        # Do not update seq_first here, since we may not find seq_second in the rest
        # of the array. Update seq_first to min when seq_second is found.
      elif array[i] < seq_second:
        seq_first = min_num
        seq_second = array[i]
      elif array[i] > seq_second:
        seq_len += 1

        if seq_len == 2:
          seq_first = min_num
          seq_second = array[i]
        elif seq_len == 3:
          return [seq_first, seq_second, array[i]]

    return []

test_class(Solution3, examples)

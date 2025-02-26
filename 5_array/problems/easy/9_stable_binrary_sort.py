from utils import test_class

# Given an array of integers, partition it based on even and odd elements. The partition
# has to be stable, meaning the relative ordering of all even elements must remain the
# same before and after partitioning, and the same should hold true for all odd elements.
# For a binary array (containing only 0s and 1s), this partitioning is equivalent to
# sorting the array.
# Another variation of this can be to partition positive and negative numbers.

examples = [
  {
    'input': [[0, 1, 0, 1, 0, 0, 1, 1, 1, 0]],
    'output': [0, 0, 0, 0, 0, 1, 1, 1, 1, 1],
  },
  {
    'input': [[1, 2, 3, 4, 5]],
    'output': [2, 4, 1, 3, 5],
  },
  {
    'input': [[1, 3, 5, 7, 9, 2, 4]],
    'output': [2, 4, 1, 3, 5, 7, 9],
  },
  {
    'input': [[-5, -2, 0, 4, 7, 9]],
    'output': [-2, 0, 4, -5, 7, 9],
  },
]

# Naive Partitioning Algorithm
# Traverse the array, store even and odd numbers separately and the copy to array.
# Time Complexity: O(n)
# Auxiliary Space: O(n)
class Solution:
  def solve(self, array):
    even_nums = []
    odd_nums = []

    for num in array:
      if num % 2 == 0: even_nums.append(num)
      else: odd_nums.append(num)

    i = 0
    for num in even_nums:
      array[i] = num
      i += 1

    for num in odd_nums:
      array[i] = num
      i += 1

    return array

test_class(Solution, examples)

# Naive Partitioning Algorithm
# Declare an temporary array. Traverse the original array and push all the even elements.
# Then, traverse the array again and push all the even elements to the temporary array.
# Time Complexity: O(n)
# Auxiliary Space: O(n)
class Solution2:
  def solve(self, array):
    temp = []

    for num in array:
      if num % 2 == 0:
        temp.append(num)

    for num in array:
      if num % 2 == 1:
        temp.append(num)

    for i in range(len(array)):
      array[i] = temp[i]

    return array

test_class(Solution2, examples)

# Modified Insertion Sort
# Find the next even number, shift all the numbers after the current partition to the
# right by one place. Insert the even number at the new partition index.
# Time Complexity: O(n^2)
# Auxiliary Space: O(1)
class Solution3:
  def solve(self, array):
    for i in range(len(array)):
      if array[i] % 2 == 1: continue

      num = array[i]
      j = i
      while j > 0 and array[j - 1] % 2 != 0:
        array[j] = array[j - 1]
        j -= 1

      array[j] = num

    return array

test_class(Solution3, examples)

# Modified Merge Sort
# Time Complexity: O(n * log(n))
# Auxiliary Space: O(n + log(n)), log(n) due to recursive stack
class Solution4:
  def solve(self, array):
    self.modified_merge_sort(array, 0, len(array) - 1)
    return array

  def modified_merge_sort(self, array, left, right):
    if left >= right: return

    mid = left + (right - left) // 2
    self.modified_merge_sort(array, left, mid)
    self.modified_merge_sort(array, mid + 1, right)
    self.modified_merge(array, left, mid, right)

  def modified_merge(self, array, left, mid, right):
    low = left
    high = mid + 1
    temp = []

    while low <= mid and high <= right:
      # For both low & high subarray, all the even elements will be in the left side
      # and all the odd elements will be in the right side. This is because the
      # the earlier merge would partitioned them individually. This follows from merge
      # sort that low & high subarrays are individually sorted and we combine them.
      if array[low] % 2 == 0 or array[high] % 2 != 0:
        temp.append(array[low])
        low += 1
      else:
        temp.append(array[high])
        high += 1

    while low <= mid:
      temp.append(array[low])
      low += 1

    while high <= right:
      temp.append(array[high])
      high += 1

    for i in range(right - left + 1):
      array[left + i] = temp[i]

test_class(Solution4, examples)

# Modified Merge Sort with optimized space
# Let Le and Lo be the even and the odd part of the left subarray. Similary, let
# Re and Ro be the even and the odd part of the right subarray.
# During the merging, the subarray will look like this [Le, Lo, Re, Ro]
# 1. Reverse Lo & Re individually: [Le, L'o, R'e, Ro]
# 2. Reverse L'o & R'o combined: [Le, Re, Lo, Ro]
# Time Complexity: O(n * log(n))
# Auxiliary Space: O(log(n)), due to recursive stack
class Solution5:
  def solve(self, array):
    self.modified_merge_sort(array, 0, len(array) - 1)
    return array

  def modified_merge_sort(self, array, left, right):
    if left >= right: return

    mid = left + (right - left) // 2
    self.modified_merge_sort(array, left, mid)
    self.modified_merge_sort(array, mid + 1, right)
    self.modified_merge(array, left, mid, right)

  def modified_merge(self, array, left, mid, right):
    low = left
    high = mid + 1

    # Find starting index of odd numbers in the first half
    while low <= mid and array[low] % 2 == 0:
      low += 1

    # Find ending index of odd numbers in the second half
    while high <= right and array[high] % 2 == 0:
      high += 1
    high -= 1

    # Reverse odd part of left subarray
    self.reverse(array, low, mid)
    # Reverse even part of right subarray
    self.reverse(array, mid + 1, high)
    # Reverse them combined returning to the original order, but even part will move
    # to left subarray and odd part to right subarray
    self.reverse(array, low, high)

  def reverse(self, array, left, right):
    if left >= right: return
    array[left], array[right] = array[right], array[left]
    self.reverse(array, left + 1, right - 1)

test_class(Solution5, examples)

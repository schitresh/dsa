from utils import test_class

# This problem appears in multiple forms:
# Sort a binary array (0s & 1s) with 0s on left side and 1s on right side
# Move all zeros to the end of the array
# Separate even and odd numbers
# Separate negative and positive numbers

# Let's take the last case. Given an array of integers, arrange the elements such that
# all the negative integers appear before all the positive integers in the array.
# The relative order of elements should be preserved, i.e. it should be a stable sort.

examples = [
  {
    'input': [[11, -13, 6, -7, 5]],
    'output': [-13, -7, 11, 6, 5],
  },
  {
    'input': [[12, 11, -13, -5, 6, -7, 5, -3, -6]],
    'output': [-13, -5, -7, -3, -6, 12, 11, 6, 5],
  },
]

# Naive Partitioning
# Time Complexity: O(n)
# Auxiliary Space: O(n)
class Solution:
  def solve(self, array):
    negatives = []
    positives = []

    for num in array:
      if num < 0: negatives.append(num)
      else: positives.append(num)

    idx = 0
    for num in negatives:
      array[idx] = num
      idx += 1

    for num in positives:
      array[idx] = num
      idx += 1

    return array

test_class(Solution, examples)

# Naive Partitioning
# Time Complexity: O(n)
# Auxiliary Space: O(n)
class Solution2:
  def solve(self, array):
    temp = []

    for num in array:
      if num < 0: temp.append(num)

    for num in array:
      if num >= 0: temp.append(num)

    for i in range(len(array)):
      array[i] = temp[i]

    return array

test_class(Solution2, examples)

# Modified Insertion Sort
# Time Complexity: O(n^2)
# Auxiliary Space: O(1)
class Solution3:
  def solve(self, array):
    for i in range(len(array)):
      if array[i] > 0: continue
      num = array[i]
      j = i

      while j > 0 and array[j - 1] >= 0:
        array[j] = array[j - 1]
        j -= 1

      array[j] = num

    return array

test_class(Solution3, examples)

# Modified Merge Sort
# Time Complexity: O(n * log(n))
# Auxiliary Space: O(n + log(n))
class Solution4:
  def solve(self, array):
    self.merge_sort(array, 0, len(array) - 1)
    return array

  def merge_sort(self, array, left, right):
    if left >= right: return

    mid = left + (right - left) // 2
    self.merge_sort(array, left, mid)
    self.merge_sort(array, mid + 1, right)
    self.merge(array, left, mid, right)

  def merge(self, array, left, mid, right):
    low = left
    high = mid + 1
    temp = []

    # Since left & right subarrays are already sorted, we can say that all the
    # negative elements in both left & right subarrays are in the first half. So,
    # once we get a positive element, it's confirmed that there are no further
    # negative elements
    while low <= mid and array[low] < 0:
      temp.append(array[low])
      low += 1

    while high <= right and array[high] < 0:
      temp.append(array[high])
      high += 1

    while low <= mid:
      temp.append(array[low])
      low += 1

    while high <= right:
      temp.append(array[high])
      high += 1

    for i in range(len(temp)):
      array[left + i] = temp[i]

test_class(Solution4, examples)

# Modified Merge Sort without auxiliary space
# Let Le and Lo be the even and the odd part of the left subarray. Similary, let
# Re and Ro be the even and the odd part of the right subarray.
# During the merging, the subarray will look like this [Le, Lo, Re, Ro]
# 1. Reverse Lo & Re individually: [Le, L'o, R'e, Ro]
# 2. Reverse L'o & R'o combined: [Le, Re, Lo, Ro]
# Time Complexity: O(n^2)
# Auxiliary Space: O(log(n))
class Solution5:
  def solve(self, array):
    self.merge_sort(array, 0, len(array) - 1)
    return array

  def merge_sort(self, array, left, right):
    if left >= right: return

    mid = left + (right - left) // 2
    self.merge_sort(array, left, mid)
    self.merge_sort(array, mid + 1, right)
    self.merge(array, left, mid, right)

  def merge(self, array, left, mid, right):
    left_pos_start = left
    right_pos_start = mid + 1

    while left_pos_start <= mid and array[left_pos_start] < 0:
      left_pos_start += 1

    while right_pos_start <= right and array[right_pos_start] < 0:
      right_pos_start += 1

    # Using array[low:mid] will generate auxiliary array, so use custom reverse method
    # Reverse odd part of left subarray
    self.reverse(array, left_pos_start, mid)
    # Reverse even part of right subarray
    self.reverse(array, mid + 1, right_pos_start - 1)
    # Reverse them combined returning to the original order, but even part will move
    # to left subarray and odd part to right subarray
    self.reverse(array, left_pos_start, right_pos_start - 1)

  def reverse(self, array, left, right):
    while left < right:
      array[left], array[right] = array[right], array[left]
      left += 1
      right -= 1

test_class(Solution5, examples)

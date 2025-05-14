from utils import test_class

# Given an array of integers, find the inversion count in the array. Two array elements
# arr[i] and arr[j] form an inversion if i < j and arr[i] > arr[j].
# Inversion count for an array indicates how far (or close) the array is from
# being sorted. If the array is already sorted, then the inversion count is 0. The
# inversion count is maximum when the array is sorted in decreasing order.

examples = [
  {
    'input': [[4, 3, 2, 1]],
    'output': 6,
  },
  {
    'input': [[1, 2, 3, 4, 5]],
    'output': 0,
  },
  {
    'input': [[10, 10, 10]],
    'output': 0,
  },
  {
    'input': [[4, 2, 5, 1, 3]],
    'output': 6,
  }
]

# Brute Force
# Time Complexity: O(n^2)
# Auxiliary Space: O(1)
class Solution:
  def solve(self, array):
    inv = 0

    for i in range(len(array)):
      for j in range(i + 1, len(array)):
        if array[i] > array[j]: inv += 1

    return inv

test_class(Solution, examples)

# Using Merge Sort
# Time Complexity: O(n * log(n))
# Auxiliary Space: O(n)
class Solution2:
  def solve(self, array):
    self.array = array
    self.inv = 0
    self.merge_sort(0, len(array) - 1)
    return self.inv

  def merge_sort(self, left, right):
    if left >= right: return

    mid = left + (right - left) // 2
    self.merge_sort(left, mid)
    self.merge_sort(mid + 1, right)

    self.merge(left, mid, right)

  def merge(self, left, mid, right):
    low = left
    high = mid + 1
    temp = []

    while low <= mid and high <= right:
      if self.array[low] <= self.array[high]:
        temp.append(self.array[low])
        low += 1
      else:
        # The low array is the index range (low, mid). Both the low & the high arrays
        # will be sorted by virtue of the merge sort.
        # If the current element in the low array is greater than the current one in high
        # array, then all the elements in the low array will be greater than the current
        # one in high. This is because both the low & the high arrays is sorted.
        # Hence, all the remaiing elements in the low array will be inversions.
        self.inv += mid - low + 1
        temp.append(self.array[high])
        high += 1

    while low <= mid:
      temp.append(self.array[low])
      low += 1

    while high <= right:
      temp.append(self.array[high])
      high += 1

    for i in range(len(temp)):
      self.array[left + i] = temp[i]

test_class(Solution2, examples)

from utils import test_class

# Given an array of integers, find the inversion count in the array. Two array elements
# arr[i] and arr[j] form an inversion if arr[i] > arr[j] and i < j.
# Note: Inversion Count for an array indicates that how far (or close) the array is from
# being sorted. If the array is already sorted, then the inversion count is 0, but if the
# array is sorted in reverse order, the inversion count is maximum.

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

# Time Complexity: O(n^2)
# Auxiliary Space: O(1)
class Solution:
  def solve(self, array):
    inversions = 0

    for i in range(len(array)):
      for j in range(i + 1, len(array)):
        if array[i] > array[j]: inversions += 1

    return inversions

test_class(Solution, examples)

# Time Complexity: O(n * log(n))
# Auxiliary Space: O(n)
class Solution2:
  def solve(self, array):
    self.array = array
    self.inversions = 0
    self.merge_sort(0, len(array) - 1)
    return self.inversions

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
        # The low array is the index range (low, mid) and both the low & the high array
        # will be sorted by virtue of the merge sort.
        # If the current element in the low array is greater than the current one in high
        # array, then all the elements in the low array will be greater than the current
        # one in high. This is because the low array is sorted.
        # And since low < high but array[low] > array[high], they all will be inversions.
        self.inversions += mid - low + 1
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

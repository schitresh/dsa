from utils import test_class

examples = [
  {
    'input': [[4, 5, 9, 8, 7, 3, 2, 1, 6]],
    'output': [1, 2, 3, 4, 5, 6, 7, 8, 9]
  }
]

# Merge Sort
# Divide and conquer approach that partitions into two, sorts the partitions individually
# and the merges them back to sort the whole range
# Stable sort
# Time Complexity: O(n * log(n))
# Best, Worst, Average: O(n * log(n))
# Auxiliary Space: O(n), required for temporary array during merging
class Solution:
  def solve(self, array):
    self.partition_and_merge(array, 0, len(array) - 1)
    return array

  def partition_and_merge(self, array, start, end):
    if start >= end: return

    mid = start + (end - start) // 2
    self.partition_and_merge(array, start, mid)
    self.partition_and_merge(array, mid + 1, end)
    self.merge(array, start, mid, end)

  def merge(self, array, start, mid, end):
    left = start
    right = mid + 1
    merged_array = []

    while left <= mid and right <= end:
      if array[left] < array[right]:
        merged_array.append(array[left])
        left += 1
      else:
        merged_array.append(array[right])
        right += 1

    while left <= mid:
      merged_array.append(array[left])
      left += 1

    while right <= end:
      merged_array.append(array[right])
      right += 1

    for index in range(end - start + 1):
      array[start + index] = merged_array[index]

test_class(Solution, examples)

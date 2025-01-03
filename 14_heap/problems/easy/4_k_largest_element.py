from utils import test_class

# Given an array and an integer k, find the k smallest elements in the given array.
# Elements in the output array should be in decreasing order.

examples = [
  {
    'input': [3, [1, 23, 12, 9, 30, 2, 50]],
    'output': [50, 30, 23],
  },
  {
    'input': [2, [11, 5, 12, 9, 44, 17, 2],],
    'output': [44, 17],
  },
  {
    'input': [4, [1, 10, 8, 2, 3, 4, 5, 9, 6, 7],],
    'output': [10, 9, 8, 7],
  },
]

# Sorting
# Time Complexity: O(n * log(n))
# Auxiliary Space: O(1)
class Solution:
  def solve(self, k, array):
    array.sort(reverse = True)
    return array[0 : k]

test_class(Solution, examples)

# Quick Sort
# Continuously check that left & right elements are smaller than the parent node
# Time Complexity: O(n^2), worst: O(n), average: O(n)
# Auxiliary Space: O(n), due to recursive stack
class Solution2:
  def solve(self, k, array):
    self.quick_sort(k, array, 0, len(array) - 1)
    result = array[0 : k]
    result.sort(reverse = True)
    return result

  def quick_sort(self, k, array, left, right):
    if left >= right: return

    pivot = self.pivot_sort(array, left, right)

    left_count = pivot - left + 1
    if left_count == k: return

    if left_count > k:
      self.quick_sort(k, array, left, pivot - 1)
    else:
      self.quick_sort(k - left_count, array, pivot + 1, right)

  def pivot_sort(self, array, left, right):
    pivot = right
    start = left

    for i in range(left, right):
      if array[i] >= array[pivot]:
        array[i], array[start] = array[start], array[i]
        start += 1

    pivot = start
    array[right], array[pivot] = array[pivot], array[right]
    return pivot


test_class(Solution2, examples)

# Min Heap
# Make a min heap with the starting k elements of the given array. In this way, the
# smallest element will always be at the top.
# Then iterate through the array, and keep replacing the smallest element from the heap
# with a larger element from the array. In this way, the large elements will keep moving
# towards the leaves, and the smallest element will keep getting removed.
# Time Complexity: O(n * log(k))
# Auxiliary Space: O(1)
class Solution3:
  def solve(self, k, array):
    k_largest = array[0 : k]
    self.build_heap(k_largest)

    for i in range(k, len(array)):
      if array[i] > k_largest[0]:
        k_largest[0] = array[i]
        self.min_heapify(k_largest, 0)

    k_largest.sort(reverse = True)
    return k_largest

  def build_heap(self, array):
    last_parent = len(array) // 2 - 1
    for i in range(last_parent, -1, -1):
      self.min_heapify(array, i)

  def min_heapify(self, array, index):
    while True:
      smallest = index
      left = 2 * index + 1
      right = left + 1

      if left < len(array) and array[left] < array[smallest]:
        smallest = left

      if right < len(array) and array[right] < array[smallest]:
        smallest = right

      if index == smallest: return

      array[index], array[smallest] = array[smallest], array[index]
      index = smallest

test_class(Solution3, examples)

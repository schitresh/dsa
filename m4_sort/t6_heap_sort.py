from utils import test_class

examples = [
  {
    'input': [[4, 5, 9, 8, 7, 3, 2, 1, 6]],
    'output': [1, 2, 3, 4, 5, 6, 7, 8, 9]
  }
]

# Heap Sort
# Comparison based sort based on binary heap
# Similar to selection sort where the minimum element is found and placed at the beginning
# Unstable sort
# Time Complexity: O(n * log(n))
# Best: O(n), Worst & Average: O(n * log(n))
# Auxiliary Space: O(1)
class Solution:
  def solve(self, array):
    self.build_max_heap(array)

    # Remove element one by one from the heap
    # In max heap, the max element is always at the top (index 0)
    # So in each iteration move that to the end of the array
    # And heapify from the root till before the index to get the next max at the top
    for index in range(len(array) - 1, 0, -1):
      self.swap(array, 0, index)
      self.max_heapify(array, 0, index)

    return array

  def build_max_heap(self, array):
    # Elements from mid + 1 to n are leaf nodes
    # Start building the heap from the parents of the leaf nodes
    # So that we can cover all the nodes
    mid = len(array) // 2
    for index in range(mid, -1, -1):
      self.max_heapify(array, index, len(array))

  def max_heapify(self, array, index, end):
    largest = index
    left = 2 * index + 1
    right = left + 1

    if left < end and array[largest] < array[left]:
      largest = left
    if right < end and array[largest] < array[right]:
      largest = right

    if largest != index:
      self.swap(array, index, largest)
      self.max_heapify(array, largest, end)

  def swap(self, array, i, j):
    array[i], array[j] = array[j], array[i]

test_class(Solution, examples)

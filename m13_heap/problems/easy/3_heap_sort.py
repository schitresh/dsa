from utils import test_class

examples = [
  {
    'input': [[5, 4, 3, 2, 1]],
    'output': [1, 2, 3, 4, 5],
  },
  {
    'input': [[5, 6, 3, 2, 1, 4]],
    'output': [1, 2, 3, 4, 5, 6],
  },
  {
    'input': [[9, 4, 3, 8, 10, 2, 5]],
    'output': [2, 3, 4, 5, 8, 9, 10],
  }
]

# Recursion
# Time Complexity: O(n * log(n))
# Auxiliary Space: O(log(n)), due to recursive stack
class Solution:
  def solve(self, array):
    # Initialize a heap, will also put the max element at the start
    self.build_heap(array)

    for i in range(len(array) - 1, 0, -1):
      # Move the current max to the end of the array
      array[0], array[i] = array[i], array[0]
      # Find the next max
      self.max_heapify(array, 0, i - 1)

    return array

  def build_heap(self, array):
    # All nodes from mid to (n - 1) are leaves
    last_parent = len(array) // 2 - 1

    for i in range(last_parent, -1, -1):
      self.max_heapify(array, i, len(array) - 1)

  def max_heapify(self, array, index, end_index):
    largest = index
    left = 2 * index + 1
    right = left + 1

    if left <= end_index and array[largest] < array[left]:
      largest = left

    if right <= end_index and array[largest] < array[right]:
      largest = right

    if index != largest:
      array[index], array[largest] = array[largest], array[index]
      self.max_heapify(array, largest, end_index)

test_class(Solution, examples)

# Iteration
# Time Complexity: O(n * log(n))
# Auxiliary Space: O(1)
class Solution2:
  def solve(self, array):
    # Initialize a heap, will also put the max element at the start
    self.build_heap(array)

    for i in range(len(array) - 1, 0, -1):
      # Move the current max to the end of the array
      array[0], array[i] = array[i], array[0]
      # Find the next max
      self.max_heapify(array, 0, i - 1)

    return array

  def build_heap(self, array):
    # All nodes from mid to (n - 1) are leaves
    last_parent = len(array) // 2 - 1

    for i in range(last_parent, -1, -1):
      self.max_heapify(array, i, len(array) - 1)

  def max_heapify(self, array, index, end_index):
    while True:
      largest = index
      left = 2 * index + 1
      right = left + 1

      if left <= end_index and array[largest] < array[left]:
        largest = left

      if right <= end_index and array[largest] < array[right]:
        largest = right

      if index == largest: return

      array[index], array[largest] = array[largest], array[index]
      index = largest

test_class(Solution2, examples)

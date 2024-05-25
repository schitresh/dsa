from utils import test_class

examples = [
  {
    'input': [[4, 5, 9, 8, 7, 3, 2, 1, 6]],
    'output': [1, 2, 3, 4, 5, 6, 7, 8, 9]
  }
]

# Time Complexity: O(n * log(n)), where k is the range of numbers
## Best Case: if keys are distinct O(n * log(n)), if keys are same O(n)
## Worst Case: O(n * log(n))
# Space Complexity: O(1)
class HeapSort:
  def swap(self, array, index_1, index_2):
    array[index_1], array[index_2] = array[index_2], array[index_1]

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

  def build_max_heap(self, array):
    # Elements from mid + 1 to n are leaf nodes
    # Start building the heap for their parents so that we can cover all the nodes
    mid = len(array) // 2
    for index in range(mid, -1, -1):
      self.max_heapify(array, index, len(array))

  def solve(self, array):
    self.build_max_heap(array)

    # Remove element one by one from the heap
    # Maximum element will be at the top (index 0)
    # So move that to the end of the array, and heapify from root till before the end
    for index in range(len(array) - 1, 0, -1):
      self.swap(array, 0, index)
      self.max_heapify(array, 0, index)

    return array

test_class(HeapSort, examples)

from heap import Heap

class MinHeap(Heap):
  # Time Complexity: O(n)
  # It runs for n/2 times and max_heapify has complexity O(log(n)),
  # but the amortized complexity is actually linear
  def build(self):
    last_index = len(self.heap) - 1
    last_parent = (last_index - 1) // 2

    for index in range(last_parent, -1, -1):
      self.min_heapify(index)

  # Time Complexity: O(log(n))
  def min_heapify(self, index):
    length = len(self.heap)
    smallest = index

    left = 2 * index + 1
    right = left + 1

    if left < length and self.heap[left] < self.heap[index]:
      smallest = left

    if right < length and self.heap[right] < self.heap[smallest]:
      smallest = right

    if smallest != index:
      self.swap(index, smallest)
      self.min_heapify(smallest)

def test(klass):
  array = [1, 6, 2, 5, 9, 8, 7, 3, 4]
  heap = klass(array)
  heap.build()
  print('Heap Array:', heap.heap)
  print('Level Order:', heap.level_order())

# Do not execute while importing it in another file
if __name__ == '__main__':
  test(MinHeap)

from heap import Heap

class MaxHeap(Heap):
  def build(self):
    last_index = len(self.heap) - 1
    last_parent = (last_index - 1) // 2

    for index in range(last_parent, -1, -1):
      self.max_heapify(index)

  def max_heapify(self, index):
    length = len(self.heap)
    largest = index

    left = 2 * index + 1
    right = left + 1

    if left < length and self.heap[index] < self.heap[left]:
      largest = left
    if right < length and self.heap[largest] < self.heap[right]:
      largest = right

    if largest != index:
      self.swap(index, largest)
      self.max_heapify(largest)

def test(klass):
  array = [1, 6, 2, 5, 9, 8, 7, 3, 4]
  heap = klass(array)
  heap.build()
  print(heap.heap)
  print(heap.level_order())

test(MaxHeap)

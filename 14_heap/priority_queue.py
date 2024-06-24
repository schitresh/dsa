from max_heap import MaxHeap

class PriorityQueue(MaxHeap):
  def size(self):
    return len(self.heap)

  def empty(self):
    return len(self.heap) == 0

  def top(self):
    return -1 if self.empty() else self.heap[0]

  def push(self, item):
    self.heap.append(item)
    self.heapify_index(self.size() - 1)

  def update(self, index, value):
    self.heap[index] = value
    self.heapify_index(index)

  def heapify_index(self, index):
    parent = (index - 1) // 2

    while index > 0 and self.heap[parent] < self.heap[index]:
      self.swap(index, parent)
      index = parent
      parent = (index - 1) // 2

  def pop(self):
    if self.empty(): return

    max_item = self.heap[0]
    self.heap[0] = self.heap[-1]
    self.max_heapify(0)

    return max_item

def test(klass):
  pq = klass()
  items = [2, 8, 5]
  for item in items: pq.push(item)

  print('Pop:', pq.pop())
  print('Top:', pq.top())
  print('Size:', pq.size())
  print('Empty:', pq.empty())

test(PriorityQueue)

from max_heap import MaxHeap

class PriorityQueue(MaxHeap):
  # Actions

  # Time Complexity: O(log(n))
  def push(self, item):
    self.heap.append(item)
    self.prioritize_index(self.size() - 1)

  # Time Complexity: O(log(n))
  def update(self, index, value):
    self.heap[index] = value
    self.prioritize_index(index)

  # Time Complexity: O(log(n))
  def pop(self):
    if self.empty(): return None

    max_item = self.heap[0]
    self.heap[0] = self.heap[-1]
    self.max_heapify(0)

    return max_item

  # Helpers

  # If value at an index is changed, we need to shift it according to its new priority
  # Hence, keep moving it up if the parent is smaller than this new value
  # Time Complexity: O(log(n))
  def prioritize_index(self, index):
    parent = (index - 1) // 2

    while index > 0 and self.heap[parent] < self.heap[index]:
      self.swap(index, parent)
      index = parent
      parent = (index - 1) // 2

  # Utils

  # Time Complexity: O(1)
  def size(self):
    return len(self.heap)

  # Time Complexity: O(1)
  def empty(self):
    return len(self.heap) == 0

  # Time Complexity: O(1)
  def top(self):
    if self.empty(): return None
    return self.heap[0]

def test(klass):
  pq = klass()
  items = [2, 8, 5]
  for item in items:
    pq.push(item)

  print('Pop:', pq.pop())
  print('Top:', pq.top())
  print('Size:', pq.size())
  print('Empty:', pq.empty())

# Do not execute while importing it in another file
if __name__ == '__main__':
  test(PriorityQueue)

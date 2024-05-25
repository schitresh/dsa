class PriorityQueue:
  def __init__(self):
    self.pqueue = []

  def swap(self, index_1, index_2):
    self.pqueue[index_1], self.pqueue[index_2] = self.pqueue[index_2], self.pqueue[index_1]

  def max_heapify(self, index):
    length = len(self.pqueue)
    largest = index
    left = 2 * index
    right = left + 1

    if left < length and self.pqueue[index] < self.pqueue[left]: largest = left
    if right < length and self.pqueue[largest] < self.pqueue[right]: largest = right

    if largest != index:
      self.swap(index, largest)
      self.max_heapify(largest)

  def build_current(self, index, item):
    if self.pqueue[index] > item: return
    self.pqueue[index] = item
    mid = index // 2

    while index > 0 and self.pqueue[index] > self.pqueue[mid]:
      self.swap(index, mid)
      index = mid
      mid = index // 2

  def push(self, item):
    self.pqueue.append(-1)
    self.build_current(self.size() - 1, item)

  def pop(self):
    if self.empty(): return

    max = self.pqueue[0]
    self.pqueue[0] = self.pqueue[-1]
    self.max_heapify(0)

    return max

  def top(self):
    return -1 if self.empty() else self.pqueue[0]

  def size(self):
    return len(self.pqueue)

  def empty(self):
    return len(self.pqueue) == 0

pq = PriorityQueue()
pq.push(2)
pq.push(8)
pq.push(5)

print('Pop', pq.pop())
print('Top', pq.top())
print('Size', pq.size())
print('Empty', pq.empty())

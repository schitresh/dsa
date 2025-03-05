from queue import Queue

class Heap:
  def __init__(self, array = None):
    self.heap = array or []

  def swap(self, i, j):
    self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

  def level_order(self):
    length = len(self.heap)
    traversal = []

    queue = Queue()
    queue.put([0, 0])

    while not queue.empty():
      index, level = queue.get()

      if level == len(traversal):
        traversal.append([])

      traversal[level].append(self.heap[index])

      left = 2 * index + 1
      right = 2 * index + 2

      if left < length and self.heap[left]:
        queue.put([left, level + 1])

      if right < length and self.heap[right]:
        queue.put([right, level + 1])

    return traversal

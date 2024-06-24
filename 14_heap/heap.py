from queue import Queue

class Heap:
  def __init__(self, array = []) -> None:
    self.heap = array

  def swap(self, i, j):
    self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

  def level_order(self):
    length = len(self.heap)
    traversal = []
    queue = Queue()
    queue.put([0, 0])

    while not queue.empty():
      index, level = queue.get()

      if level == len(traversal): traversal.append([])
      traversal[level].append(self.heap[index])

      left_index = 2 * index + 1
      right_index = 2 * index + 2

      if left_index < length and self.heap[left_index]:
        queue.put([left_index, level + 1])
      if right_index < length and self.heap[right_index]:
        queue.put([right_index, level + 1])

    return traversal

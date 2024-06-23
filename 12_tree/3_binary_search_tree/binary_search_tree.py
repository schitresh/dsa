from queue import Queue

class Node:
  def __init__(self, key):
    self.key = key
    self.left = None
    self.right = None

class BSTree:
  def __init__(self):
    self.root = None

  def level_order(self):
    traversal = []
    # Use Stack for iteration based DFS
    queue = Queue()
    queue.put([self.root, 0])

    while not queue.empty():
      node, level = queue.get()

      if level == len(traversal):
        traversal.append([])
      traversal[level].append(node.key)

      if node.left: queue.put([node.left, level + 1])
      if node.right: queue.put([node.right, level + 1])

    return traversal

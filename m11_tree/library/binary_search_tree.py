from queue import Queue

class Node:
  def __init__(self, key):
    self.key = key
    self.left = None
    self.right = None

class BSTree:
  def __init__(self):
    self.root = None

  def insert(self, key):
    self.root = self.insert_from_node(self.root, key)

  def insert_from_node(self, node, key):
    if not node: return Node(key)

    if key < node.key:
      node.left = self.insert_from_node(node.left, key)
    else:
      node.right = self.insert_from_node(node.right, key)

    return node

  def delete(self, key):
    self.root = self.delete_from_node(self.root, key)

  def delete_from_node(self, node, key):
    if not node: return

    if node.key < key:
      node.right = self.delete_from_node(node.right, key)
    elif node.key > key:
      node.left = self.delete_from_node(node.left, key)
    else:
      if not node.left:
        temp = node.right
        del node
        return temp
      elif not node.right:
        temp = node.left
        del node
        return temp

      temp = node.right
      # Get min value
      while temp.left: temp = temp.left

      node.key = temp.key
      node.right = self.delete_from_node(node.right, node.key)

    return node

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

# [5]
# [2, 9]
# [[1, 3], [8, 10]]
# [[[], [4]], [[6, ]]
# [[[], []]], [[[, 7], []]]]
def sample_bstree():
  tree = BSTree()
  keys = [5, 2, 1, 3, 4, 9, 8, 6, 7, 10]

  for key in keys:
    if key % 2 == 0: tree.insert(key)
    else: tree.insert(key)

  return tree

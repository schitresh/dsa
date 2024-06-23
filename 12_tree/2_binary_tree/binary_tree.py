from queue import Queue

class Node:
  def __init__(self, key) -> None:
    self.key = key
    self.left = None
    self.right = None

  def set_left(self, key):
    self.left = Node(key)

  def set_right(self, key):
    self.right = Node(key)

class BinaryTree:
  def __init__(self, root = None) -> None:
    self.root = Node(root)

  def insert(self, key):
    self.root = self.insert_from_node(self.root, key)

  def insert_from_node(self, node, key):
    if not node: return Node(key)

    if node.key < key:
      node.right = self.insert_from_node(node.right, key)
    else:
      node.left = self.insert_from_node(node.left, key)

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

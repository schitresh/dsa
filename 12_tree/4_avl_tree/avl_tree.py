from queue import Queue

class Node:
  def __init__(self, key):
    self.key = key
    self.left = None
    self.right = None
    self.height = 1
    # Can also store count to store duplicate values
    # self.count = 1

class AvlTree:
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

  def insert(self, key):
    self.root = self.insert_from_node(self.root, key)

  def insert_from_node(self, node, key):
    if not node: return Node(key)

    if key < node.key:
      node.left = self.insert_from_node(node.left, key)
    else:
      node.right = self.insert_from_node(node.right, key)

    return self.balance(node, key)

  def balance(self, node, key):
    left_height = self.height(node.left)
    right_height = self.height(node.right)

    node.height = 1 + max(left_height, right_height)
    balance = left_height - right_height

    if balance > 1:
      if key < node.left.key:
        return self.rotate_right(node)
      else:
        return self.rotate_left_right(node)

    if balance < -1:
      if key > node.right.key:
        return self.rotate_left(node)
      else:
        return self.rotate_right_left(node)

    return node

  def height(self, node):
    if not node: return 0
    return node.height

  def rotate_left(self, node):
    right = node.right
    node.right = right.left
    right.left = node

    node.height = 1 + max(self.height(node.left), self.height(node.right))
    right.height = 1 + max(self.height(right.left), self.height(right.right))

    return right

  def rotate_right(self, node):
    left = node.left
    node.left = left.right
    left.right = node

    node.height = 1 + max(self.height(node.left), self.height(node.right))
    left.height = 1 + max(self.height(left.left), self.height(left.right))

    return left

  def rotate_left_right(self, node):
    node.left = self.rotate_left(node.left)
    return self.rotate_right(node)

  def rotate_right_left(self, node):
    node.right = self.rotate_right(node.right)
    return self.rotate_left(node)

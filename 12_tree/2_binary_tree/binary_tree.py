from queue import Queue

class Node:
  def __init__(self, key) -> None:
    self.key = key
    self.left = None
    self.right = None

  def assign_left(self, key):
    self.left = Node(key)

  def assign_right(self, key):
    self.right = Node(key)

class Tree:
  def __init__(self, root = None) -> None:
    self.root = Node(root)

  # Time complexity: O(n)
  # Auxiliary space: O(n)
  def insert(self, key):
    node = Node(key)

    if not self.root:
      self.root = node
      return node

    queue = Queue()
    queue.put(self.root)

    while not queue.empty():
      temp = queue.get()

      if not temp.right:
        temp.right = node
        return temp.right

      if not temp.left:
        temp.left = node
        return temp.left

      queue.put(temp.right)
      queue.put(temp.left)

  # Time complexity: O(n)
  # Auxiliary space: O(n)
  def delete(self, key):
    if not self.root: return

    key_node = None
    last_node = None
    queue = Queue()
    queue.put(self.root)

    while not queue.empty():
      last_node = queue.get()

      if last_node.key == key: key_node = last_node

      # Keep iterating to get a leaf node
      if last_node.right: queue.put(last_node.right)
      if last_node.left: queue.put(last_node.left)

    if not key_node: return

    key_node.key = last_node.key
    self.delete_node(last_node)

  def delete_node(self, node):
    queue = Queue()
    queue.put(self.root)

    if self.root == node:
      self.root = None
      del self.root
      return

    while not queue.empty():
      temp = queue.get()

      if temp.right == node:
        temp.right = None
        del node
        return

      if temp.left == node:
        temp.left = None
        del node
        return

      queue.put(temp.right)
      queue.put(temp.left)

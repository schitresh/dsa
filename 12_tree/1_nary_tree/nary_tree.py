from queue import Queue

class Node:
  def __init__(self, key):
    self.key = key
    self.children = []

  def set_children(self, *children):
    self.children = list(map(Node, children))

class NaryTree:
  def __init__(self, root_key = None):
    self.root = Node(root_key)

  def search(self, key):
    return bool(self.search_from_node(self.root, key))

  def search_node(self, key):
    return self.search_from_node(self.root, key)

  def search_from_node(self, node, key):
    if not node: return

    if node.key == key: return node

    for child in node.children:
      result = self.search_from_node(child, key)
      if result: return result

  def level_order(self):
    level_traversal = []
    # Use Stack for iteration based DFS
    queue = Queue()
    queue.put([self.root, 0])

    while not queue.empty():
      node, level = queue.get()

      if level == len(level_traversal):
        level_traversal.append([])
      level_traversal[level].append(node.key)

      for child in node.children:
        queue.put([child, level + 1])

    return level_traversal

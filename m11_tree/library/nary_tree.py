from queue import Queue

class Node:
  def __init__(self, key):
    self.key = key
    self.children = []

  def set_children(self, *children):
    self.children = list(map(Node, children))

  def add_child(self, key):
    node = Node(key)
    self.children.append(node)
    return node

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

def nary_tree_from_level_hash(tree_input):
  tree = None
  nodes = {}

  for level in range(len(tree_input)):
    level_keys = tree_input[level]

    for key, children in level_keys.items():
      if level == 0:
        tree = NaryTree(key)
        nodes[key] = tree.root

      for child_key in children:
        child_node = nodes[key].add_child(child_key)
        nodes[child_key] = child_node

  return tree

def sample_nary_tree():
  tree_input = [
    { 'a': ['b', 'c', 'd', 'e'] },
    { 'b': ['f', 'g'], 'd': ['h', 'i', 'j'] },
    { 'f': ['k'], 'i': ['l', 'm'] },
    { 'l': ['n'] }
  ]

  return nary_tree_from_level_hash(tree_input)

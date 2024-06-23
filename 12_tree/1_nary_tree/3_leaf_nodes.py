from queue import LifoQueue
from tree_utils import sample_tree1
from utils import print_class_name

class Node:
  def __init__(self, key):
    self.key = key
    self.children = []

  def assign_children(self, *children):
    self.children = list(map(Node, children))

class Tree:
  def __init__(self, root = None):
    self.root = Node(root)
    self.leaf_nodes = []

  def get_leaf_nodes(self):
    self.reach_leaf_nodes(self.root)
    return self.leaf_nodes

  # Time Complexity: O(n)
  # Auxiliary Space: O(n), due to recursive stack
    # Recursive stack will take O(h) space, where h is height of the tree
    # But in worst case h can be n
  def reach_leaf_nodes(self, node):
    if not node:
      return

    if len(node.children) == 0:
      self.leaf_nodes.append(node.key)

    for child in node.children:
      self.reach_leaf_nodes(child)


class Tree2:
  def __init__(self, root = None):
    self.root = Node(root)

  # Time Complexity: O(n)
  # Auxiliary Space: O(n)
  def get_leaf_nodes(self):
    leaf_nodes = []
    # Stack used for DFS, Can use Queue instead for BFS
    stack = LifoQueue()
    stack.put(self.root)

    while not stack.empty():
      node = stack.get()

      if len(node.children) == 0:
        leaf_nodes.append(node.key)

      for child in reversed(node.children):
        stack.put(child)

    return leaf_nodes

def test(klass):
  print_class_name(klass)
  tree = sample_tree1(klass)
  # [k, g, c, h, n, m, j, e]
  print(tree.get_leaf_nodes())

test(Tree)
test(Tree2)

from queue import Queue
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

  # Time Complexity: O(n)
  # Auxiliary Space: O(n), due to recursive stack
    # Recursive stack will take O(h) space, where h is height of the tree
    # But in worst case h can be n
  def search(self, node, key):
    if not node:
      return False

    if node.key == key:
      return True

    for child in node.children:
      result = self.search(child, key)
      if result:
        return True

    return False

def test():
  tree = sample_tree1(Tree)
  print(tree.search(tree.root, 'n')) # True
  print(tree.search(tree.root, 'zz')) # False

test()

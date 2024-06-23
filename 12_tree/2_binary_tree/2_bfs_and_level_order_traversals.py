from binary_tree import Node
from binary_tree_utils import sample_binary_tree
from queue import Queue

from utils import print_class_name

# Level order recursion using BFS
# Time Complexity: O(n)
# Auxiliary Space: O(n)
class Tree:
  def __init__(self, root = None) -> None:
    self.root = Node(root)
    self.level_order_traversal = []

  def level_order(self):
    self.level_order_traversal = []

    level = 0
    while self.traverse_level_order(self.root, level):
      level = level + 1

    return self.level_order_traversal

  def traverse_level_order(self, node, level):
    if not node: return False

    if level == 0:
      self.level_order_traversal.append(node.key)
      return True

    left = self.traverse_level_order(node.left, level - 1)
    right = self.traverse_level_order(node.right, level - 1)

    return left or right

# Level order recursion using DFS
# Time Complexity: O(n)
# Auxiliary Space: O(n)
class Tree2:
  def __init__(self, root = None):
    self.root = Node(root)
    self.level_order_traversal = []

  def level_order(self):
    self.level_order_traversal = []
    self.traverse_level_order(self.root, 0)
    return self.level_order_traversal

  def traverse_level_order(self, node, level):
    if not node: return

    if level == len(self.level_order_traversal):
      self.level_order_traversal.append([])
    self.level_order_traversal[level].append(node.key)

    if node.left: self.traverse_level_order(node.left, level + 1)
    if node.right: self.traverse_level_order(node.right, level + 1)

# Level order iterative using BFS
# Time Complexity: O(n)
# Auxiliary Space: O(n)
class Tree3:
  def __init__(self, root) -> None:
    self.root = Node(root)

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

def test(klass):
  print_class_name(klass)
  tree = sample_binary_tree(klass)
  # [d, b, h, e, a, i, k, f, j, c, g]
  print(tree.level_order())
  print()

test(Tree)
test(Tree2)
test(Tree3)

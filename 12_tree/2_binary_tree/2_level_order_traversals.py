from binary_tree import Node
from binary_tree_utils import sample_binary_tree
from queue import Queue

from utils import print_class_name

# Depth First Search (DFS)
  # Inorder: Left -> Node -> Right
  # Preorder: Node -> Left -> Right
  # Postorder: Left -> Right -> Node

class Tree:
  def __init__(self, root = None) -> None:
    self.root = Node(root)
    self.level_order_traversal = []

  def level_order(self):
    self.level_order_traversal = []
    self.traverse_level_order(self.root)
    return self.level_order_traversal

  def traverse_level_order(self, node):
    if not node: return
    self.level_order_traversal.append(node.key)
    self.traverse_level_order(node.left)
    self.traverse_level_order(node.right)

class Tree2:
  def __init__(self, root) -> None:
    self.root = Node(root)

  def level_order(self):
    traversal = []
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

# test(Tree)
test(Tree2)

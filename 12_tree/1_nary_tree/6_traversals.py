from queue import Queue
from tree_utils import sample_tree1
from utils import print_class_name

class Node:
  def __init__(self, key):
    self.key = key
    self.children = []

  def assign_children(self, *children):
    self.children = list(map(Node, children))

# Traversals
# Depth First Search (DFS)
  # Inorder: Left -> Node -> Right
  # Preorder: Node -> Left -> Right
  # Postorder: Left -> Right -> Node
# Breadth First Search (BFS)

# Level Order Traversal
  # Traverse all the nodes of a lower level before moving to any higher level node

# Using Recursion based DFS
# Time Complexity: O(n)
# Auxiliary Space: O(n), due to recursive stack
  # Recursive stack will take O(h) space, where h is height of the tree
  # But in worst case h can be n
class Tree:
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

    for child in node.children:
      self.traverse_level_order(child, level + 1)

# Using Iteration based BFS
# Time Complexity: O(n)
# Auxiliary Space: O(n), due to recursive stack
  # Recursive stack will take O(h) space, where h is height of the tree
  # But in worst case h can be n
class Tree2:
  def __init__(self, root = None):
    self.root = Node(root)

  def level_order(self):
    level_order_traversal = []
    # Use Stack for iteration based DFS
    queue = Queue()
    queue.put([self.root, 0])

    while not queue.empty():
      node, level = queue.get()

      if level == len(level_order_traversal):
        level_order_traversal.append([])
      level_order_traversal[level].append(node.key)

      for child in node.children:
        queue.put([child, level + 1])

    return level_order_traversal


def test(klass):
  print_class_name(klass)
  tree = sample_tree1(klass)
  print(tree.level_order())

test(Tree)
test(Tree2)

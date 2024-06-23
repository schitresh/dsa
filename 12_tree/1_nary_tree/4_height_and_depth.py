from queue import Queue
from tree_utils import sample_tree1
from utils import print_class_name

class Node:
  def __init__(self, key):
    self.key = key
    self.children = []

  def assign_children(self, *children):
    self.children = list(map(lambda x: Node(x), children))

# Height is the number of edges on longest path from the node to a leaf node
# Depth is the number of edges on longest path from the root to the node
# Height of tree = Depth of tree
# Height of node + Depth of node = Height/Depth of tree

# Recursive Approach
class Tree:
  def __init__(self, root = None):
    self.root = Node(root)

  # Time Complexity: O(n)
  # Auxiliary Space: O(n), due to recursive stack
  def height(self, node):
    if not node:
      return

    height = 0
    for child in node.children:
      height = max(height, 1 + self.height(child))

    return height

  # Time Complexity: O(n)
  # Auxiliary Space: O(n), due to recursive stack
  def depth(self, root, node):
    if not root:
      return

    if root == node:
      return 0

    for child in root.children:
      depth = self.depth(child, node)
      if depth is not None:
        return 1 + depth

# Level Order Traversal
class Tree2:
  def __init__(self, root = None):
    self.root = Node(root)

  # Time Complexity: O(n)
  # Auxiliary Space: O(n)
  def height(self, node):
    if not node:
      return

    height = 0
    queue = Queue()
    queue.put([node, 0])

    while not queue.empty():
      front, level = queue.get()
      height = max(height, level)

      for child in front.children:
        queue.put([child, level + 1])

    return height

  # Level Order Traversal
  # Time Complexity: O(n)
  # Auxiliary Space: O(n)
  def depth(self, root, node):
    if not root or not node:
      return

    depth = 0
    queue = Queue()
    queue.put([root, 0])

    while not queue.empty():
      front, level = queue.get()
      if front == node:
        depth = level
        break

      for child in front.children:
        queue.put([child, level + 1])

    return depth

def test(klass):
  tree = sample_tree1(klass)
  root = tree.root
  node_n = root.children[2].children[1].children[0].children[0]
  node_l = root.children[2].children[1].children[0]

  print_class_name(klass)
  print('Height of root:', tree.height(tree.root)) # 4
  print('Height of l:', tree.height(node_l)) # 1

  print('Depth of n:', tree.depth(tree.root, node_n)) # 4
  print('Depth of l:', tree.depth(tree.root, node_l)) # 3

  print()

test(Tree)
test(Tree2)

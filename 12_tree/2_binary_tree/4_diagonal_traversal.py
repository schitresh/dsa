from binary_tree import Node
from binary_nary_tree_utils import sample_binary_tree
from queue import Queue

from utils import print_class_name

# Time Complexity: O(n * log(n))
# Auxiliary Space: O(n)
class Tree:
  def __init__(self, root = None) -> None:
    self.root = Node(root)
    self.diagonal_traversal = []

  def diagonal_order(self):
    self.diagonal_traversal = []
    self.traverse_diagonal(self.root, 0)
    return self.diagonal_traversal

  def traverse_diagonal(self, node, diagonal):
    if not node: return

    if diagonal == len(self.diagonal_traversal):
      self.diagonal_traversal.append([])
    self.diagonal_traversal[diagonal].append(node.key)

    self.traverse_diagonal(node.left, diagonal + 1)
    self.traverse_diagonal(node.right, diagonal)

# Time Complexity: O(n)
# Auxiliary Space: O(n)
class Tree2:
  def __init__(self, root = None) -> None:
    self.root = Node(root)

  def diagonal_order(self):
    traversal = []
    queue = Queue()
    current = self.root

    while current:
      traversal.append(current.key)

      if current.left:
        queue.put(current.left)

      if current.right:
        current = current.right
      else:
        if not queue.empty():
          current = queue.get()
        else:
          current = None

    return traversal

def test(klass):
  print_class_name(klass)
  tree = sample_binary_tree(klass)
  # [a, c, g, b, e, f, j, d, h, i, k]
  print(tree.diagonal_order())
  print()

test(Tree)
test(Tree2)

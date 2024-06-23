from binary_tree import Node
from binary_tree_utils import sample_binary_tree
from queue import LifoQueue

from utils import print_class_name

# Time Complexity: O(n * log(n))
# Auxiliary Space: O(n)
class Tree:
  def __init__(self, root = None) -> None:
    self.root = Node(root)
    self.boundary_traversal = []

  def boundary_order(self):
    self.boundary_traversal = [self.root.key]

    self.boundary_left(self.root.left)
    self.boundary_leaves(self.root)
    self.boundary_right(self.root.right)

    return self.boundary_traversal

  def boundary_left(self, node):
    if not node: return

    if node.left:
      self.boundary_traversal.append(node.key)
      self.boundary_left(node.left)
    elif node.right:
      self.boundary_traversal.append(node.key)
      self.boundary_left(node.right)

  def boundary_right(self, node):
    if not node: return

    if node.right:
      self.boundary_right(node.right)
      self.boundary_traversal.append(node.key)
    elif node.left:
      self.boundary_right(node.left)
      self.boundary_traversal.append(node.key)

  def boundary_leaves(self, node):
    if not node: return

    if not node.left and not node.right:
      self.boundary_traversal.append(node.key)

    self.boundary_leaves(node.left)
    self.boundary_leaves(node.right)

# Time Complexity: O(n)
# Auxiliary Space: O(n)
class Tree2:
  def __init__(self, root = None) -> None:
    self.root = Node(root)

  def boundary_order(self):
    traversal = [self.root.key]
    traversal += self.boundary_left()
    traversal += self.boundary_leaves()
    traversal += self.boundary_right()
    return traversal

  def boundary_left(self):
    traversal = []
    current = self.root.left

    while True:
      # If left and right are both None, it is a leaf
      # We're already considering leaves seperately
      if current.left:
        traversal.append(current.key)
        current = current.left
      elif current.right:
        traversal.append(current.key)
        current = current.right
      else:
        break

    return traversal

  def boundary_right(self):
    traversal = []
    stack = LifoQueue()
    current = self.root.right

    while True:
      # If left and right are both None, it is a leaf
      # We're already considering leaves seperately
      if current.right:
        stack.put(current.key)
        current = current.right
      elif current.left:
        stack.put(current.key)
        current = current.left
      else:
        break

    while not stack.empty():
      key = stack.get()
      traversal.append(key)

    return traversal

  def boundary_leaves(self):
    traversal = []
    stack = LifoQueue()
    stack.put(self.root)

    while not stack.empty():
      current = stack.get()

      if current.right: stack.put(current.right)
      if current.left: stack.put(current.left)

      if not current.left and not current.right:
        traversal.append(current.key)

    return traversal

def test(klass):
  print_class_name(klass)
  tree = sample_binary_tree(klass)
  # [a, b, d, h, k, j, g, c]
  print(tree.boundary_order())
  print()

test(Tree)
test(Tree2)

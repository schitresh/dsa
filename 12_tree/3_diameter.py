from queue import LifoQueue, Queue
from tree_utils import sample_tree1
from utils import print_class_name

class Node:
  def __init__(self, key):
    self.key = key
    self.children = []

  def assign_children(self, *children):
    self.children = list(map(Node, children))

# Diameter of a tree is the number of nodes on the longest path
# between any two nodes of the tree
# The path can either start form one node and go up one of the ancestors
# and again come down to the deepest node of some other subtree
# Or, it can be one of the child of the current node
class Tree:
  def __init__(self, root = None):
    self.root = Node(root)

  # Time Complexity: O(n^2)
  # Auxiliary Space: O(n), due to recursive stack
    # Recursive stack will take O(h) space, where h is height of the tree
    # But in worst case h can be n
  def diameter(self, node):
    if not node:
      return

    # Diameter of current node
    height1 = 0
    height2 = 0
    for child in node.children:
      child_height = self.height(child)
      if child_height > height1:
        height2 = height1
        height1 = child_height
      elif child_height > height2:
        height2 = child_height

    # Max Diameter from childrens
    max_diameter = 0
    for child in node.children:
      max_diameter = max(max_diameter, self.diameter(child))

    current_diameter = 1 + height1 + height2
    return max(current_diameter, max_diameter)

  # Time Complexity: O(n)
  # Auxiliary Space: O(n), due to recursive stack
    # Recursive stack will take O(h) space, where h is height of the tree
    # But in worst case h can be n
  def height(self, node):
    if not node:
      return

    height = 0
    for child in node.children:
      height = max(height, self.height(child))

    return 1 + height

class Tree2:
  def __init__(self, root = None):
    self.root = Node(root)
    self.max_diameter = 0

  def diameter(self, node):
    self.max_diameter = 0
    self.diameter_height(node)
    return self.max_diameter

  # Time Complexity: O(n)
  # Auxiliary Space: O(n), due to recursive stack
    # Recursive stack will take O(h) space, where h is height of the tree
    # But in worst case h can be n
  def diameter_height(self, node):
    if not node:
      return 0

    height1 = 0
    height2 = 0
    for child in node.children:
      child_height = self.diameter_height(child)
      if child_height > height1:
        height2 = height1
        height1 = child_height
      elif child_height > height2:
        height2 = child_height

    current_diameter = 1 + height1 + height2
    self.max_diameter = max(self.max_diameter, current_diameter)

    return 1 + height1

# Iterative depth first search
# First reach the leaf nodes by going downwards in the tree
# Then iterate upwards by calculating the height from the leaf nodes
class Tree3:
  def __init__(self, root = None):
    self.root = Node(root)

  # Time Complexity: O(n)
  # Auxiliary Space: O(n)
  def diameter(self, node):
    diameter = 0
    height = { None: 0 }
    stack = LifoQueue()
    # Store node along with direction (True if going downwards)
    stack.put([node, True])

    while not stack.empty():
      top, downwards = stack.get()

      if downwards:
        stack.put([top, False])
        for child in top.children:
          stack.put([child, True])
      else:
        height1 = 0
        height2 = 0

        for child in top.children:
          child_height = height[child.key]

          if child_height > height1:
            height2 = height1
            height1 = child_height
          elif child_height > height2:
            height2 = child_height

        height[top.key] = 1 + height1
        diameter = max(diameter, 1 + height1 + height2)

    return diameter

def test(klass):
  print_class_name(klass)
  tree = sample_tree1(klass)
  print(tree.diameter(tree.root)) # 8

test(Tree)
test(Tree2)
test(Tree3)

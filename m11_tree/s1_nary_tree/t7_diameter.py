from queue import LifoQueue
from utils import test_class
from m11_tree.library.nary_tree import sample_nary_tree

# Diameter of a tree is the number of nodes on the longest path between any two nodes
# of the tree.
# The path can either start from one node and go up one of the LCAs (Lowest Common
# Ancestors) and again come down to the deepest node of some other subtree. Or, it can
# be one of the child of the current node.

examples = [
  {
    'input': [sample_nary_tree()],
    'output': 8
  }
]

# By returning diameter and calculating height
# The solution will exist in any one of these:
# 1. Diameter of one of the children of the current node
# 2. Sum of height of the highest two subtree + 1
# Time Complexity: O(n^2)
# Auxiliary Space: O(n), due to recursive stack
class Solution:
  def solve(self, tree):
    return self.diameter_from_node(tree.root)

  def diameter_from_node(self, node):
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
      child_diameter = self.diameter_from_node(child)
      max_diameter = max(max_diameter, child_diameter)

    current_diameter = 1 + height1 + height2
    return max(current_diameter, max_diameter)

  def height(self, node):
    if not node: return

    height = 0
    for child in node.children:
      height = max(height, self.height(child))

    return 1 + height

test_class(Solution, examples)

# By returning height and calculating diameter
# We can find diameter without calculating depth of the tree making small changes in
# the above solution, similar to finding diameter of binary tree.
# Time Complexity: O(n)
# Auxiliary Space: O(n), due to recursive stack
class Solution2:
  def solve(self, tree):
    self.max_diameter = 0
    self.diameter_height(tree.root)
    return self.max_diameter

  def diameter_height(self, node):
    if not node: return 0

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

test_class(Solution2, examples)

# Iterative DFS
# First reach the leaf nodes by going downwards in the tree
# Then iterate upwards by calculating the height from the leaf nodes
# Time Complexity: O(n)
# Auxiliary Space: O(n)
class Solution3:
  def solve(self, tree):
    diameter = 0
    height = { None: 0 }
    stack = LifoQueue()
    # Store node along with direction (True if going downwards)
    stack.put([tree.root, True])

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

test_class(Solution3,  examples)

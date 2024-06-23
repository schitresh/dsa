from queue import Queue
from binary_tree import BinaryTree
from binary_tree_utils import test_class

# Level order recursion using BFS
# Time Complexity: O(n)
# Auxiliary Space: O(n)
class Tree(BinaryTree):
  def __init__(self, *args) -> None:
    super().__init__(*args)
    self.level_traversal = []

  def level_order(self):
    self.level_traversal = []

    level = 0
    while self.traverse_level_order(self.root, 0, level):
      level = level + 1

    return self.level_traversal

  def traverse_level_order(self, node, node_level, level):
    if not node: return False

    if node_level == level:
      if level == len(self.level_traversal):
        self.level_traversal.append([])
      self.level_traversal[level].append(node.key)
      return True

    left = self.traverse_level_order(node.left, node_level + 1, level)
    right = self.traverse_level_order(node.right, node_level + 1, level)

    return left or right

# Level order recursion using DFS
# Time Complexity: O(n)
# Auxiliary Space: O(n)
class Tree2(BinaryTree):
  def __init__(self, *args) -> None:
    super().__init__(*args)
    self.level_traversal = []

  def level_order(self):
    self.level_traversal = []
    self.traverse_level_order(self.root, 0)
    return self.level_traversal

  def traverse_level_order(self, node, level):
    if not node: return

    if level == len(self.level_traversal):
      self.level_traversal.append([])
    self.level_traversal[level].append(node.key)

    if node.left: self.traverse_level_order(node.left, level + 1)
    if node.right: self.traverse_level_order(node.right, level + 1)

# Level order iterative using BFS
# Time Complexity: O(n)
# Auxiliary Space: O(n)
class Tree3(BinaryTree):
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

examples = [
  {
    'input': [],
    'output': [['a'], ['b', 'c'], ['d', 'e', 'f', 'g'], ['h', 'i', 'j'], ['k']]
  }
]

test_class(Tree, 'level_order', examples)
test_class(Tree2, 'level_order', examples)
test_class(Tree3, 'level_order', examples)

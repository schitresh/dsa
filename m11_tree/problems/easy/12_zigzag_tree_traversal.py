from queue import LifoQueue, Queue
from utils import test_class
from m11_tree.library.binary_tree import binary_tree_from_level_array

# Given a binary tree, find the zigzag level order traversal of the tree. In zig zag
# traversal starting from the first level go from left to right for odd-numbered levels
# and right to left for even-numbered levels.

examples = [
  {
    'input': [binary_tree_from_level_array([[1], [[2, 3]], [[4, 5], [None, 6]]])],
    'output': [1, 3, 2, 4, 5, 6],
  },
  {
    'input': [binary_tree_from_level_array([
      [20], [[8, 22]], [[4, 12], [None, 11]], [None, [10, 14], None]]
    )],
    'output': [20, 22, 8, 4, 12, 11, 14, 10],
  },
]

# Iterative BFS & Stack
# Time Complexity: O(n)
# Auxiliary Space: O(n)
class Solution:
  def solve(self, tree):
    traversal = []
    queue = Queue()
    stack = LifoQueue()

    queue.put(tree.root)
    # The first level is 1 which is odd, so the child level will be even
    even_child_level = True

    while not queue.empty():
      level_size = len(queue.queue)

      for _ in range(level_size):
        node = queue.get()
        traversal.append(node.key)

        if even_child_level:
          if node.left: stack.put(node.left)
          if node.right: stack.put(node.right)
        else:
          if node.right: stack.put(node.right)
          if node.left: stack.put(node.left)

      while not stack.empty():
        node = stack.get()
        queue.put(node)

      even_child_level = not even_child_level

    return traversal

test_class(Solution, examples)

# Using two Stacks
# Time Complexity: O(n)
# Auxiliary Space: O(n)
class Solution2:
  def solve(self, tree):
    traversal = []
    curr_level = LifoQueue()
    next_level = LifoQueue()

    curr_level.put(tree.root)
    # The first level is 1 which is odd, so the child level will be even
    even_child_level = True

    while not curr_level.empty():
      level_size = len(curr_level.queue)

      for _ in range(level_size):
        node = curr_level.get()
        traversal.append(node.key)

        if even_child_level:
          if node.left: next_level.put(node.left)
          if node.right: next_level.put(node.right)
        else:
          if node.right: next_level.put(node.right)
          if node.left: next_level.put(node.left)

      curr_level, next_level = next_level, curr_level
      even_child_level = not even_child_level

    return traversal

test_class(Solution2, examples)

# Recursive DFS
# Time Complexity: O(n)
# Auxiliary Space: O(n)
class Solution3:
  def solve(self, tree):
    self.levels = []
    self.level_order(tree.root, 0)

    traversal = []
    even_level = False

    for level_keys in self.levels:
      for i in range(len(level_keys)):
        idx = i
        if even_level: idx = len(level_keys) - 1 - i
        traversal.append(level_keys[idx])

      even_level = not even_level

    return traversal

  def level_order(self, node, level):
    if not node: return

    if len(self.levels) - 1 < level:
      self.levels.append([node.key])
    else:
      self.levels[level].append(node.key)

    self.level_order(node.left, level + 1)
    self.level_order(node.right, level + 1)


test_class(Solution3, examples)

from queue import Queue, LifoQueue
from utils import test_class
from m11_tree.library.binary_tree import binary_tree_from_level_array

# Given a binary tree, convert the binary tree to its mirror tree. Mirror of a binary
# tree is another binary tree with left and right children of all non-leaf nodes
# interchanged.

examples = [
  {
    'input': [binary_tree_from_level_array([[1], [[2, 2]], [[3, 4], [4, 3]]])],
    'output': True,
  },
  {
    'input': [binary_tree_from_level_array([[1], [[2, 2]], [[None, 3], [None, 3]]])],
    'output': False,
  },
]

# Iterative BFS with levels
# Time Complexity: O(n)
# Space Complexity: O(n)
class Solution:
  def solve(self, tree):
    queue = Queue()
    queue.put(tree.root)

    while not queue.empty():
      level_nodes = queue.queue
      # Initialize left and right one step away so that they can be advanced at the
      # beginning of the loop. Otherwise we will have to advance them selectively.
      # First if both left & right nodes are null after which the loop should continue.
      # And then at the end of the loop, if keys of left & right are equal.
      left = -1
      right = len(level_nodes)

      while left < right:
        left += 1
        right -= 1

        if not level_nodes[left] and not level_nodes[right]: continue
        if not level_nodes[left] or not level_nodes[right]: return False
        if level_nodes[left].key != level_nodes[right].key: return False

      for _ in range(len(level_nodes)):
        node = queue.get()
        if not node: continue

        queue.put(node.left)
        queue.put(node.right)

    return True

test_class(Solution, examples)

# Iterative BFS without levels
# Time Complexity: O(n)
# Space Complexity: O(n)
class Solution2:
  def solve(self, tree):
    queue = Queue()
    queue.put(tree.root.left)
    queue.put(tree.root.right)

    while not queue.empty():
      node1 = queue.get()
      node2 = queue.get()

      if not node1 and not node2: continue
      if not node1 or not node2: return False
      if node1.key != node2.key: return False

      queue.put(node1.left)
      queue.put(node2.right)

      queue.put(node1.right)
      queue.put(node2.left)

    return True

test_class(Solution2, examples)

# Recursive DFS
# Time Complexity: O(n)
# Space Complexity: O(height)
class Solution3:
  def solve(self, tree):
    return self.is_symmetric(tree.root.left, tree.root.right)

  def is_symmetric(self, node1, node2):
    if not node1 and not node2: return True
    if not node1 or not node2: return False
    if node1.key != node2.key: return False

    outward_subtree = self.is_symmetric(node1.left, node2.right)
    inward_subtree = self.is_symmetric(node1.right, node2.left)
    return outward_subtree and inward_subtree

test_class(Solution3, examples)

# Iterative DFS
# Time Complexity: O(n)
# Space Complexity: O(height)
class Solution4:
  def solve(self, tree):
    stack = LifoQueue()
    stack.put(tree.root.left)
    stack.put(tree.root.right)

    while not stack.empty():
      node1 = stack.get()
      node2 = stack.get()

      if not node1 and not node2: continue
      if not node1 or not node2: return False
      if node1.key != node2.key: return False

      stack.put(node1.left)
      stack.put(node2.right)

      stack.put(node1.right)
      stack.put(node2.left)

    return True

test_class(Solution4, examples)

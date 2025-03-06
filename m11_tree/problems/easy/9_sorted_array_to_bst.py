from queue import Queue
from utils import test_class
from m11_tree.library.binary_tree import BinaryTree, Node

# Given a sorted array, convert it into a balanced binary search tree.

examples = [
  {
    'input': [[10, 20, 30]],
    'output': [[20], [10, 30]]
  },
  {
    'input': [[1, 2, 3, 4, 5, 6, 7]],
    'output': [[4], [2, 6], [1, 3, 5, 7]],
  },
  {
    'input': [[1, 2, 3, 4]],
    'output': [[2], [1, 3], [4]]
  },
]

# Recursive DFS
# Time Complexity: O(n)
# Auxiliary Space: O(height)
class Solution:
  def solve(self, array):
    self.array = array
    self.tree = BinaryTree()
    self.array_to_bst(None, 0, len(array) - 1)
    return self.tree.level_order()

  def array_to_bst(self, parent, left, right):
    if left > right: return

    mid = left + (right - left) // 2
    node = Node(self.array[mid])

    if not parent: self.tree.root = node
    elif node.key < parent.key: parent.left = node
    else: parent.right = node

    self.array_to_bst(node, left, mid - 1)
    self.array_to_bst(node, mid + 1, right)

test_class(Solution, examples)

# Recursive DFS optimization
# Time Complexity: O(n)
# Auxiliary Space: O(height)
class Solution2:
  def solve(self, array):
    self.array = array
    tree = BinaryTree()
    tree.root = self.array_to_bst(0, len(array) - 1)
    return tree.level_order()

  def array_to_bst(self, left, right):
    if left > right: return None

    mid = left + (right - left) // 2
    node = Node(self.array[mid])
    node.left = self.array_to_bst(left, mid - 1)
    node.right = self.array_to_bst(mid + 1, right)

    return node

test_class(Solution2, examples)

# Iterative BFS
# Time Complexity: O(n)
# Auxiliary Space: O(n)
class Solution3:
  def solve(self, array):
    left = 0
    right = len(array) - 1
    mid = left + (right - left) // 2

    tree = BinaryTree()
    tree.root = Node(array[mid])

    queue = Queue()
    queue.put([tree.root, [left, mid - 1]])
    queue.put([tree.root, [mid + 1, right]])

    while not queue.empty():
      parent, [left, right] = queue.get()
      if left > right: continue

      mid = left + (right - left) // 2
      node = Node(array[mid])

      if array[mid] < parent.key:
        parent.left = node
      else:
        parent.right = node

      queue.put([node, [left, mid - 1]])
      queue.put([node, [mid + 1, right]])

    return tree.level_order()

test_class(Solution3, examples)

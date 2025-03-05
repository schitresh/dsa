from utils import test_class
from m11_tree.library.binary_search_tree import BSTree

# Given a Binary Search Tree that may be unbalanced, convert it to a balanced BST
# Balanced BST is the one that has minimum possible height O(log(n))

examples = [
  {
    # [1]
    # [, 2]
    # [[], [, 3]]
    'input': [[1, 2, 3]],
    'output': [[2], [1, 3]]
  },
  {
    # [4]
    # [3]
    # [[2]]
    # [[[1]]]
    'input': [[4, 3, 2, 1]],
    'output': [[2], [1, 3], [4]]
  },
  {
    # [4]
    # [3, 5]
    # [[2], [, 6]]
    # [[[1]], [, [, 7]]]
    'input': [[4, 3, 2, 1, 5, 6, 7]],
    'output': [[4], [2, 6], [1, 3, 5, 7]]
  },
]

# Time Complexity: O(n)
# Auxiliary Space: O(n)
class Solution:
  def solve(self, keys):
    self.tree = BSTree()
    for key in keys:
      self.tree.insert(key)

    self.balance()
    return self.tree.level_order()

  def balance(self):
    self.inorder_traversal = []
    self.inorder_nodes(self.tree.root)
    self.tree.root = self.balance_node(0, len(self.inorder_traversal) - 1)

  def balance_node(self, left, right):
    if left > right: return None

    mid = (left + right) // 2
    node = self.inorder_traversal[mid]

    node.left = self.balance_node(left, mid - 1)
    node.right = self.balance_node(mid + 1, right)
    return node

  def inorder_nodes(self, node):
    if not node: return

    if node.left: self.inorder_nodes(node.left)
    self.inorder_traversal.append(node)
    if node.right: self.inorder_nodes(node.right)

test_class(Solution, examples)

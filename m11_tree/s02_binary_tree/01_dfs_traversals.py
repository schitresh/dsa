from queue import LifoQueue
from utils import test_class
from m11_tree.library.binary_tree import sample_binary_tree

# Inorder: Left -> Node -> Right
# Preorder: Node -> Left -> Right
# Postorder: Left -> Right -> Node

examples = [
  {
    'input': [sample_binary_tree(), 'inorder'],
    'output': ['d', 'b', 'h', 'e', 'a', 'i', 'k', 'f', 'j', 'c', 'g'],
  },
  {
    'input': [sample_binary_tree(), 'preorder'],
    'output': ['a', 'b', 'd', 'e', 'h', 'c', 'f', 'i', 'k', 'j', 'g'],
  },
  {
    'input': [sample_binary_tree(), 'postorder'],
    'output': ['d', 'h', 'e', 'b', 'k', 'i', 'j', 'f', 'g', 'c', 'a'],
  },
]

# Recursive
# Time Complexity: O(n)
# Auxiliary Space: O(n)
class Solution:
  def solve(self, tree, order):
    self.root = tree.root
    if order == 'inorder': return self.inorder()
    if order == 'preorder': return self.preorder()
    if order == 'postorder': return self.postorder()

  # Inorder

  def inorder(self):
    self.inorder_traversal = []
    self.traverse_inorder(self.root)
    return self.inorder_traversal

  def traverse_inorder(self, node):
    if not node: return
    self.traverse_inorder(node.left)
    self.inorder_traversal.append(node.key)
    self.traverse_inorder(node.right)

  # Preorder

  def preorder(self):
    self.preorder_traversal = []
    self.traverse_preorder(self.root)
    return self.preorder_traversal

  def traverse_preorder(self, node):
    if not node: return
    self.preorder_traversal.append(node.key)
    self.traverse_preorder(node.left)
    self.traverse_preorder(node.right)

  # Postorder

  def postorder(self):
    self.postorder_traversal = []
    self.traverse_postorder(self.root)
    return self.postorder_traversal

  def traverse_postorder(self, node):
    if not node: return
    self.traverse_postorder(node.left)
    self.traverse_postorder(node.right)
    self.postorder_traversal.append(node.key)

test_class(Solution, examples)

# Iterative
class Solution2:
  def solve(self, tree, order):
    self.root = tree.root
    if order == 'inorder': return self.inorder()
    if order == 'preorder': return self.preorder()
    if order == 'postorder': return self.postorder()

  def inorder(self):
    inorder_traversal = []
    stack = LifoQueue()
    current = self.root

    while True:
      # Reach the left-most node
      if current:
        stack.put(current)
        current = current.left
      # Backtrack from the empty subtree
      elif not stack.empty():
        current = stack.get()
        inorder_traversal.append(current.key)
        current = current.right
      # If the stack is empty, no nodes left to traverse
      else:
        break

    return inorder_traversal

  def preorder(self):
    preorder_traversal = []
    stack = LifoQueue()
    stack.put(self.root)

    while not stack.empty():
      node = stack.get()
      preorder_traversal.append(node.key)

      if node.right: stack.put(node.right)
      if node.left: stack.put(node.left)

    return preorder_traversal

  def postorder(self):
    postorder_traversal = []
    stack = LifoQueue()
    stack.put([self.root, True])

    while not stack.empty():
      node, downwards = stack.get()

      if downwards:
        stack.put([node, False])
        if node.right: stack.put([node.right, True])
        if node.left: stack.put([node.left, True])
      else:
        postorder_traversal.append(node.key)

    return postorder_traversal

test_class(Solution2, examples)

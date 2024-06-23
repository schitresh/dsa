from queue import LifoQueue
from binary_tree import BinaryTree
from binary_tree_utils import sample_binary_tree

from utils import print_class_name

# Depth First Search (DFS)
  # Inorder: Left -> Node -> Right
  # Preorder: Node -> Left -> Right
  # Postorder: Left -> Right -> Node
# Time Complexity: O(n)
# Auxiliary Space: O(n)
class Tree(BinaryTree):
  def __init__(self, *args) -> None:
    super().__init__(*args)
    self.inorder_traversal = []
    self.preorder_traversal = []
    self.postorder_traversal = []

  def inorder(self):
    self.inorder_traversal = []
    self.traverse_inorder(self.root)
    return self.inorder_traversal

  def traverse_inorder(self, node):
    if not node: return
    self.traverse_inorder(node.left)
    self.inorder_traversal.append(node.key)
    self.traverse_inorder(node.right)

  def preorder(self):
    self.preorder_traversal = []
    self.traverse_preorder(self.root)
    return self.preorder_traversal

  def traverse_preorder(self, node):
    if not node: return
    self.preorder_traversal.append(node.key)
    self.traverse_preorder(node.left)
    self.traverse_preorder(node.right)

  def postorder(self):
    self.postorder_traversal = []
    self.traverse_postorder(self.root)
    return self.postorder_traversal

  def traverse_postorder(self, node):
    if not node: return
    self.traverse_postorder(node.left)
    self.traverse_postorder(node.right)
    self.postorder_traversal.append(node.key)

class Tree2(BinaryTree):
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

def test(klass):
  print_class_name(klass)
  tree = sample_binary_tree(klass)

  # [d, b, h, e, a, i, k, f, j, c, g]
  print(tree.inorder())
  # [a, b, d, e, h, c, f, i, k, j, g]
  print(tree.preorder())
  # [d, h, e, b, k, i, j, f, g, c, a]
  print(tree.postorder())
  print()

test(Tree)
test(Tree2)

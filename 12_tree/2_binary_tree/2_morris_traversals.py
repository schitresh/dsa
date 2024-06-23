from binary_tree import Node
from binary_tree_utils import sample_binary_tree
from queue import LifoQueue

from utils import print_class_name

# Depth First Search (DFS)
  # Inorder: Left -> Node -> Right
  # Preorder: Node -> Left -> Right
  # Postorder: Left -> Right -> Node

class Tree:
  def __init__(self, root) -> None:
    self.root = Node(root)

  def inorder(self):
    inorder_traversal = []
    current = self.root

    while current:
      if current.left:
        predecessor = current.left

        while predecessor.right and predecessor.right != current:
          predecessor = predecessor.right

        if predecessor.right:
          predecessor.right = None
          inorder_traversal.append(current.key)
          current = current.right
        else:
          predecessor.right = current
          current = current.left
      else:
        inorder_traversal.append(current.key)
        current = current.right

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

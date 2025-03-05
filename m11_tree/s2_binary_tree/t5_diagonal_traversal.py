from queue import Queue
from binary_tree import BinaryTree
from binary_tree_utils import test_class


examples = [
  {
    'input': [],
    'output': [['a', 'c', 'g'], ['b', 'e', 'f', 'j'], ['d', 'h', 'i', 'k']]
  }
]


# Time Complexity: O(n * log(n))
# Auxiliary Space: O(n)
class Tree(BinaryTree):
  def diagonal_order(self):
    self.diagonal_traversal = []
    self.traverse_diagonal(self.root, 0)
    return self.diagonal_traversal

  def traverse_diagonal(self, node, diagonal):
    if not node: return

    if diagonal == len(self.diagonal_traversal):
      self.diagonal_traversal.append([])
    self.diagonal_traversal[diagonal].append(node.key)

    self.traverse_diagonal(node.left, diagonal + 1)
    self.traverse_diagonal(node.right, diagonal)

test_class(Tree, 'diagonal_order', examples)

# Time Complexity: O(n)
# Auxiliary Space: O(n)
class Tree2(BinaryTree):
  def diagonal_order(self):
    traversal = []
    queue = Queue()
    current = self.root
    diagonal = 0

    while current:
      if diagonal == len(traversal): traversal.append([])
      traversal[diagonal].append(current.key)

      if current.left:
        queue.put([current.left, diagonal + 1])

      if current.right:
        current = current.right
      else:
        if not queue.empty():
          current, diagonal = queue.get()
        else:
          current = None

    return traversal

test_class(Tree2, 'diagonal_order', examples)

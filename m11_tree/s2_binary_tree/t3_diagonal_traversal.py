from queue import Queue
from utils import test_class
from m11_tree.library.binary_tree import sample_binary_tree

examples = [
  {
    'input': [sample_binary_tree()],
    'output': [['a', 'c', 'g'], ['b', 'e', 'f', 'j'], ['d', 'h', 'i', 'k']]
  }
]

# Time Complexity: O(n * log(n))
# Auxiliary Space: O(n)
class Solution:
  def solve(self, tree):
    self.diagonal_traversal = []
    self.traverse_diagonal(tree.root, 0)
    return self.diagonal_traversal

  def traverse_diagonal(self, node, diagonal):
    if not node: return

    if diagonal == len(self.diagonal_traversal):
      self.diagonal_traversal.append([])
    self.diagonal_traversal[diagonal].append(node.key)

    self.traverse_diagonal(node.left, diagonal + 1)
    self.traverse_diagonal(node.right, diagonal)

test_class(Solution, examples)

# Time Complexity: O(n)
# Auxiliary Space: O(n)
class Solution2:
  def solve(self, tree):
    traversal = []
    queue = Queue()
    current = tree.root
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

test_class(Solution2, examples)

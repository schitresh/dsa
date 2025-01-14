from queue import Queue
from nary_tree import NaryTree
from nary_tree_utils import sample_nary_tree
from utils import print_class_name

# Using BFS
# Time Complexity: O(n)
# Auxiliary Space: O(n)
class Tree(NaryTree):
  def mirror(self):
    queue = Queue()
    queue.put(self.root)

    while not queue.empty():
      node = queue.get()
      node.children.reverse()

      for child in node.children:
        queue.put(child)

def test(klass):
  print_class_name(klass)
  tree = sample_nary_tree(klass)

  print(tree.level_order())
  tree.mirror()
  print(tree.level_order())

test(Tree)

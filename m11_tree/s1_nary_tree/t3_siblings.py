from queue import Queue
from nary_tree import NaryTree
from nary_tree_utils import test_class


examples = [
  {
    'input': ['a'],
    'output': []
  },
  {
    'input': ['d'],
    'output': ['b', 'c', 'e']
  },
  {
    'input': ['i'],
    'output': ['h', 'j']
  }
]

class Tree(NaryTree):
  # Time Complexity: O(n)
  # Auxiliary Space: O(n), due to recursive stack
    # Recursive stack will take O(h) space which can be n in worst case
  def siblings(self, key):
    parent = self.parent(self.root, key)
    if not parent: return []

    siblings = list(map(lambda x: x.key, parent.children))
    siblings.remove(key)
    return siblings

  def parent(self, node, key):
    if not node:
      return

    for child in node.children:
      if child.key == key:
        return node

      parent = self.parent(child, key)
      if parent: return parent

test_class(Tree, 'siblings', examples)

class Tree2(NaryTree):
  # Time Complexity: O(n)
  # Auxiliary Space: O(n)
  def siblings(self, key):
    queue = Queue()
    queue.put(self.root)
    parent = None

    while not queue.empty():
      node = queue.get()

      for child in node.children:
        if child.key == key:
          parent = node
          break

        queue.put(child)

      if parent: break

    if not parent: return []

    siblings = list(map(lambda x: x.key, parent.children))
    siblings.remove(key)
    return siblings

test_class(Tree2, 'siblings', examples)

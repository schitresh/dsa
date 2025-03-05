from nary_tree import NaryTree, Node
from nary_tree_utils import sample_nary_tree
from utils import print_class_name

# Time Complexity: O(n)
# Auxiliary Space: O(n)
class Tree(NaryTree):
  def __init__(self, *args):
    super().__init__(*args)
    self.tree_string = ''

  def serialize(self):
    self.tree_string = ''
    self.serializer(self.root)
    return self.tree_string

  def serializer(self, node):
    if not node: return

    self.tree_string += node.key + ' '

    for child in node.children:
      self.serializer(child)

    self.tree_string += ') '

  def deserialize(self):
    tree_keys = self.tree_string.split(' ')
    self.tree_string = ''

    iterator = iter(tree_keys)
    self.root = self.deserializer(iterator)

  def deserializer(self, iterator):
    key = next(iterator)
    if not key or key == ')': return

    node = Node(key)
    while True:
      child = self.deserializer(iterator)
      if not child: break
      node.children.append(child)

    return node

def test(klass):
  print_class_name(klass)
  tree = sample_nary_tree(klass)

  print(tree.level_order())
  tree.serialize()
  print(tree.tree_string)
  tree.deserialize()
  print(tree.level_order())

test(Tree)

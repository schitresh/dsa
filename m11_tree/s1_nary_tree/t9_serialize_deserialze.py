from utils import test_class
from m11_tree.library.nary_tree import NaryTree, Node, sample_nary_tree

# Given an N-ary tree where every node has the most N children, add a way to serialize
# and deserialize it.
# Serialization is to store a tree in a file so that it can be later restored. The
# structure of the tree must be maintained. Deserialization is reading the tree back
# from the file.

examples = [
  {
    'input': ['serialize', sample_nary_tree()],
    'output': 'a b f k ) ) g ) ) c ) d h ) i l n ) ) m ) ) j ) ) e ) )',
  },
  {
    'input': ['deserialize', 'a b f k ) ) g ) ) c ) d h ) i l n ) ) m ) ) j ) ) e ) )'],
    'output': [
      ['a'], ['b', 'c', 'd', 'e'], ['f', 'g', 'h', 'i', 'j'], ['k', 'l', 'm'], ['n']
    ],
  },
]

# Time Complexity: O(n)
# Auxiliary Space: O(n)
class Solution:
  def solve(self, action, action_input):
    if action == 'serialize':
      self.root = action_input.root
      return self.serialize()

    self.tree_string = action_input
    return self.deserialize().level_order()

  def serialize(self):
    self.tree_string = ''
    self.serializer(self.root)
    return self.tree_string.strip()

  def serializer(self, node):
    if not node: return

    self.tree_string += node.key + ' '

    for child in node.children:
      self.serializer(child)

    self.tree_string += ') '

  def deserialize(self):
    tree_keys = self.tree_string.split(' ')
    iterator = iter(tree_keys)
    tree = NaryTree()
    tree.root = self.deserializer(iterator)
    return tree

  def deserializer(self, iterator):
    key = next(iterator)
    if not key or key == ')': return

    node = Node(key)
    while True:
      child = self.deserializer(iterator)
      if not child: break
      node.children.append(child)

    return node

test_class(Solution, examples)

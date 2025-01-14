from binary_search_tree import BSTree

# Given a Binary Search Tree that may be unbalanced, convert it to a balanced BST
# Balanced BST is the one that has minimum possible height O(log(n))

# Time Complexity: O(n)
# Auxiliary Space: O(n)
class Tree(BSTree):
  def balance(self):
    self.inorder_traversal = []
    self.inorder_nodes(self.root)
    self.root = self.balance_node(0, len(self.inorder_traversal) - 1)

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

examples = [
  {
    # [1]
    # [, 2]
    # [[], [, 3]]
    'input': [1, 2, 3],
    'output': [[2], [1, 3]]
  },
  {
    # [4]
    # [3]
    # [[2]]
    # [[[1]]]
    'input': [4, 3, 2, 1],
    'output': [[2], [1, 3], [4]]
  },
  {
    # [4]
    # [3, 5]
    # [[2], [, 6]]
    # [[[1]], [, [, 7]]]
    'input': [4, 3, 2, 1, 5, 6, 7],
    'output': [[4], [2, 6], [1, 3, 5, 7]]
  },
]

def test(klass):
  for example in examples:
    tree = klass()
    keys = example['input']
    for key in keys: tree.insert(key)

    tree.balance()
    output = tree.level_order()
    print(example['output'] == output, end=': ')
    print(output)


test(Tree)

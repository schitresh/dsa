from queue import Queue

class BinaryTreeArray:
  def __init__(self, root):
    self.tree = [None] * 100
    self.tree[0] = root

  def set_left_of_key(self, parent_key, key):
    parent_index = self.tree.index(parent_key)
    return self.set_left_of_index(parent_index, key)

  def set_left_of_index(self, parent_index, key):
    if not self.tree[parent_index]: return None

    left_index = 2 * parent_index + 1
    self.tree[left_index] = key
    return left_index

  def set_right_of_key(self, parent_key, key):
    parent_index = self.tree.index(parent_key)
    return self.set_right_of_index(parent_index, key)

  def set_right_of_index(self, parent_index, key):
    if not self.tree[parent_index]: return None

    right_index = 2 * parent_index + 2
    self.tree[right_index] = key
    return right_index

  def level_order(self):
    length = len(self.tree)
    traversal = []
    queue = Queue()
    queue.put([0, 0])

    while not queue.empty():
      index, level = queue.get()

      if level == len(traversal): traversal.append([])
      traversal[level].append(self.tree[index])

      left_index = 2 * index + 1
      right_index = 2 * index + 2

      if left_index < length and self.tree[left_index]:
        queue.put([left_index, level + 1])
      if right_index < length and self.tree[right_index]:
        queue.put([right_index, level + 1])

    return traversal


def binary_tree_from_level_hash(tree_input):
  tree = None

  for level in range(len(tree_input)):
    level_keys = tree_input[level]

    for key, children in level_keys.items():
      if level == 0:
        tree = BinaryTreeArray(key)

      left, right = children
      tree.set_left_of_key(key, left)
      tree.set_right_of_key(key, right)

  return tree

def sample_tree_array():
  tree_input = [
    { 'a': ['b', 'c'] },
    { 'b': ['d', 'e'], 'c': ['f', 'g'] },
    { 'e': ['h', None], 'f': ['i', 'j'] },
    { 'i': [None, 'k'] }
  ]

  return binary_tree_from_level_hash(tree_input).tree

from queue import Queue

class Tree:
  def __init__(self, root):
    self.tree = [None] * 100
    self.tree[0] = root

  def set_left_of_key(self, parent_key, key):
    parent_index = self.tree.index(parent_key)
    return self.set_left_of_index(parent_index, key)

  def set_left_of_index(self, parent_index, key):
    if not self.tree[parent_index]: return

    left_index = 2 * parent_index + 1
    self.tree[left_index] = key
    return left_index

  def set_right_of_key(self, parent_key, key):
    parent_index = self.tree.index(parent_key)
    return self.set_right_of_index(parent_index, key)

  def set_right_of_index(self, parent_index, key):
    if not self.tree[parent_index]: return

    right_index = 2 * parent_index + 2
    self.tree[right_index] = key
    return right_index

  def level_order(self):
    traversal = []
    queue = Queue()
    queue.put([0, 0])

    while not queue.empty():
      index, level = queue.get()

      if level == len(traversal):
        traversal.append([])
      traversal[level].append(self.tree[index])

      left_index = 2 * index + 1
      right_index = 2 * index + 2

      if self.tree[left_index]: queue.put([left_index, level + 1])
      if self.tree[right_index]: queue.put([right_index, level + 1])

    return traversal

def sample_tree():
  tree = Tree('a')
  tree.set_left_of_key('a', 'b')
  tree.set_right_of_key('a', 'c')
  tree.set_left_of_key('b', 'd')
  tree.set_right_of_key('b', 'e')
  tree.set_left_of_key('c', 'f')
  tree.set_right_of_key('c', 'g')
  tree.set_left_of_key('e', 'h')
  tree.set_left_of_key('f', 'i')
  tree.set_right_of_key('f', 'j')
  tree.set_right_of_key('i', 'k')
  return tree

def sample_tree_array():
  return sample_tree().tree

def test():
  tree = sample_tree()
  print(tree.level_order())

test()

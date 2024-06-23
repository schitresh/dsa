def sample_binary_tree(klass):
  # [a]
  # [b, c]
  # [[d, e], [f, g]]
  # [[[], [h]], [[i, j]]
  # [[[], []]], [[[, k], []]]]
  tree = klass('a')
  root = tree.root
  root.assign_left('b')
  root.assign_right('c')
  root.left.assign_left('d')
  root.left.assign_right('e')
  root.right.assign_left('f')
  root.right.assign_right('g')
  root.left.right.assign_left('h')
  root.right.left.assign_left('i')
  root.right.left.assign_right('j')
  root.right.left.left.assign_right('k')
  return tree

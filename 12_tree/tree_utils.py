def sample_tree1(klass):
  # [a]
  # [b, c, d, e]
  # [[f, g], [], [h, i, j], []]
  # [[[k], []], [], [[], [l, m], []], []]
  # [[[], []], [], [[], [n], []], []]
  tree = klass('a')
  root = tree.root
  root.assign_children('b', 'c', 'd', 'e')
  root.children[0].assign_children('f', 'g')
  root.children[2].assign_children('h', 'i', 'j')
  root.children[0].children[0].assign_children('k')
  root.children[2].children[1].assign_children('l', 'm')
  root.children[2].children[1].children[0].assign_children('n')
  return tree

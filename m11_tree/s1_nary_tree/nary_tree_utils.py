from utils import print_class_name

# [a]
# [b, c, d, e]
# [[f, g], [], [h, i, j], []]
# [[[k], []], [], [[], [l, m], []], []]
# [[[], []], [], [[], [n], []], []]
def sample_nary_tree(klass):
  tree = klass('a')
  root = tree.root
  root.set_children('b', 'c', 'd', 'e')
  root.children[0].set_children('f', 'g')
  root.children[2].set_children('h', 'i', 'j')
  root.children[0].children[0].set_children('k')
  root.children[2].children[1].set_children('l', 'm')
  root.children[2].children[1].children[0].set_children('n')
  return tree

def test_class(klass, method, examples):
  print_class_name(klass)
  tree = sample_nary_tree(klass)

  for example in examples:
    output = getattr(tree, method)(*example['input'])
    print(output == example['output'], end = ': ')
    print(output)

  print()

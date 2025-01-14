from utils import print_class_name

# [a]
# [b, c]
# [[d, e], [f, g]]
# [[[], [h]], [[i, j]]
# [[[], []]], [[[, k], []]]]
def sample_binary_tree(klass):
  tree = klass('a')
  root = tree.root
  root.set_left('b')
  root.set_right('c')
  root.left.set_left('d')
  root.left.set_right('e')
  root.right.set_left('f')
  root.right.set_right('g')
  root.left.right.set_left('h')
  root.right.left.set_left('i')
  root.right.left.set_right('j')
  root.right.left.left.set_right('k')
  return tree

def test_class(klass, method, examples):
  print_class_name(klass)
  tree = sample_binary_tree(klass)

  for example in examples:
    output = getattr(tree, method)(*example['input'])
    print(output == example['output'], end = ': ')
    print(output)

  print()

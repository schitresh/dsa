from utils import print_class_name

# [5]
# [2, 9]
# [[1, 3], [8, 10]]
# [[[], [4]], [[6, ]]
# [[[], []]], [[[, 7], []]]]
def sample_bs_tree(klass):
  tree = klass()
  keys = [5, 2, 1, 3, 4, 9, 8, 6, 7, 10]
  for key in keys:
    if key % 2 == 0: tree.insert(key)
    else: tree.insert(key)
  return tree

def test_class(klass, method, examples):
  print_class_name(klass)
  tree = sample_bs_tree(klass)

  for example in examples:
    output = getattr(tree, method)(*example['input'])
    print(output == example['output'], end = ': ')
    print(output)

  print()

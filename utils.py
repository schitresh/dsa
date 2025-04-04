import re
from copy import deepcopy

# Printers

def print_class_name(klass):
  pattern = re.compile(r'(?<!^)(?=[A-Z])')
  name = pattern.sub(' ', klass.__name__).title()
  print(name)

def print_method_name(method):
  name = ' '.join(method.__name__.split('_')).title()
  print(name)

# Testers

def test_class(klass, examples):
  print_class_name(klass)

  for example in examples:
    example = deepcopy(example)
    output = klass().solve(*example['input'])
    print(output == example['output'], end = ': ')
    print(output)

  print()

def test_class_with_checker(klass, examples, checker):
  print_class_name(klass)

  for example in examples:
    example = deepcopy(example)
    output = klass().solve(*example['input'])
    check = checker(output)
    print(check == example['output'], end = ': ')
    print(check)

  print()

def test_with_init(klass, examples):
  print_class_name(klass)

  for example in examples:
    example = deepcopy(example)
    output = klass(*example['input']).solve()
    print(output == example['output'], end = ': ')
    print(output)

  print()

def test_method(method, examples):
  print_method_name(method)

  for example in examples:
    example = deepcopy(example)
    output = method(*example['input'])
    print(output == example['output'], end = ': ')
    print(output)

  print()

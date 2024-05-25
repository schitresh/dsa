def test_class(klass, examples):
  for example in examples:
    output = klass().solve(*example['input'])
    print(output == example['output'], end = ': ')
    print(output)

  print()

def test_with_init(klass, examples):
  for example in examples:
    output = klass(*example['input']).solve()
    print(output == example['output'], end = ': ')
    print(output)

  print()

def test_method(method, examples):
  for example in examples:
    output = method(*example['input'])
    print(output == example['output'], end = ': ')
    print(output)

  print()

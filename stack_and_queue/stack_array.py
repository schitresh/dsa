class Stack:
  def __init__(self):
    self.stack = []

  def size(self):
    return len(self.stack)

  def empty(self):
    return self.size() == 0

  def top(self):
    if self.empty(): return
    return self.stack[-1]

  def push(self, item):
    self.stack.append(item)

  def pop(self):
    if self.empty(): return
    return self.stack.pop()

def test():
  stack = Stack()

  for i in range(1, 6):
    stack.push(i)

  print('Pop (5):', stack.pop())
  print('Size (4):', stack.size())
  print('Top (4):', stack.top())
  print('Empty (False):', stack.empty())

# test()

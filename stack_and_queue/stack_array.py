class Stack:
  def __init__(self):
    self.stack = []

  def push(self, item):
    self.stack.append(item)

  def pop(self):
    return -1 if self.empty() else self.stack.pop()

  def size(self):
    return len(self.stack)

  def top(self):
    return -1 if self.empty() else self.stack[-1]

  def empty(self):
    return self.size() == 0

s = Stack()
s.push(1)
s.push(2)
s.push(3)
print('pop', s.pop())
print('size', s.size())
print('top', s.top())
print('empty', s.empty())

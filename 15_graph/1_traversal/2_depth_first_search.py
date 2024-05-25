from queue import LifoQueue
from utils import test_class, test_with_init

examples = [
  {
    'input': [[[1, 3], [0, 2], [1, 3, 4], [0, 2], [2]]],
    'output': [0, 1, 2, 3, 4]
  },
]

class DFS:
  def solve(self, graph):
    stack = LifoQueue()
    stack.put(0)
    visited = [False] * len(graph)
    visited[0] = True
    traversal = []

    while not stack.empty():
      node = stack.get()
      traversal.append(node)

      for neighbor in reversed(graph[node]):
        if visited[neighbor]:
          continue
        visited[neighbor] = True
        stack.put(neighbor)

    return traversal

class DFSRecursive:
  def __init__(self, graph):
    self.graph = graph
    self.visited = [False] * len(graph)
    self.traversal = []

  def traverse(self, node):
    self.traversal.append(node)

    for neighbor in self.graph[node]:
      if self.visited[neighbor]:
        continue
      self.visited[neighbor] = True
      self.traverse(neighbor)

  def solve(self):
    self.visited[0] = True
    self.traverse(0)
    return self.traversal

test_class(DFS, examples)
test_with_init(DFSRecursive, examples)

from queue import LifoQueue
from utils import test_class, test_with_init

examples = [
  {
    'input': [[[1, 3], [0, 2], [1, 3], [0, 2], []]],
    'output': [0, 1, 2, 3, 4] # Or, [0, 1, 2, 4, 3]
  },
]

# Time Complexity: O(V + E)
# Auxiliary Space: O(V)
class DFS:
  def solve(self, graph):
    stack = LifoQueue()
    visited = [False] * len(graph)
    traversal = []

    for current in range(len(graph)):
      if visited[current]: continue
      visited[current] = True
      stack.put(current)

      while not stack.empty():
        node = stack.get()
        traversal.append(node)

        for neighbor in reversed(graph[node]):
          if visited[neighbor]: continue
          visited[neighbor] = True
          stack.put(neighbor)

    return traversal

# Time Complexity: O(V + E)
# Auxiliary Space: O(V + E), recursion stack requires O(E)
class DFSRecursive:
  def __init__(self, graph):
    self.graph = graph
    self.visited = [False] * len(graph)
    self.traversal = []

  def traverse(self, node):
    self.traversal.append(node)

    for neighbor in self.graph[node]:
      if self.visited[neighbor]: continue
      self.visited[neighbor] = True
      self.traverse(neighbor)

  def solve(self):
    for current in range(len(self.graph)):
      if self.visited[current]: continue
      self.visited[current] = True
      self.traverse(current)

    return self.traversal

test_class(DFS, examples)
test_with_init(DFSRecursive, examples)

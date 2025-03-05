from queue import LifoQueue
from utils import test_class

# The standard DFS takes a source as an input and considers only those vertices that are
# reachable from the source. It will not consider all the vertices in the case of a
# disconnected graph.
# This algorithm considers all vertices without any source in the case where the given
# graph maybe disconnected.

examples = [
  {
    'input': [[[1, 3], [0, 2], [1, 3], [0, 2], []]],
    'output': [0, 1, 2, 3, 4] # or [0, 1, 2, 4, 3]
  },
]

# Instead of calling DFS for a single vertex, call it for all the non-visited vertices
# one by one.
# Time Complexity: O(V + E)
# Auxiliary Space: O(V)
class Solution:
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

test_class(Solution, examples)

# Recursion
# Time Complexity: O(V + E)
# Auxiliary Space: O(V + E), recursion stack requires O(E)
class Solution2:
  def solve(self, graph):
    self.graph = graph
    self.visited = [False] * len(graph)
    self.traversal = []

    for current in range(len(self.graph)):
      if self.visited[current]: continue
      self.visited[current] = True
      self.traverse(current)

    return self.traversal

  def traverse(self, node):
    self.traversal.append(node)

    for neighbor in self.graph[node]:
      if self.visited[neighbor]: continue
      self.visited[neighbor] = True
      self.traverse(neighbor)

test_class(Solution2, examples)

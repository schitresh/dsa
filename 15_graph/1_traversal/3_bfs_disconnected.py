from queue import Queue
from utils import test_class

# The standard BFS takes a source as an input and considers only those vertices that are
# reachable from the source. It will not consider all the vertices in the case of a
# disconnected graph.
# This algorithm considers all vertices without any source in the case where the given
# graph maybe disconnected.

examples = [
  {
    'input': [[[1, 3], [0, 2], [1, 3], [0, 2], []]],
    'output': [0, 1, 3, 2, 4]
  },
]

# Instead of calling BFS for a single vertex, call it for all the non-visited vertices
# one by one.
# Time Complexity: O(V + E)
# Auxiliary Space: O(V)
class Solution:
  def solve(self, graph):
    queue = Queue()
    visited = [False] * len(graph)
    traversal = []

    for current in range(len(graph)):
      if visited[current]: continue
      visited[current] = True

      queue.put(current)

      while not queue.empty():
        node = queue.get()
        traversal.append(node)

        for neighbor in graph[node]:
          if visited[neighbor]: continue
          visited[neighbor] = True
          queue.put(neighbor)

    return traversal

test_class(Solution, examples)

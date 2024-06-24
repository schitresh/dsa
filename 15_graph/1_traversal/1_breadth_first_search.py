from queue import Queue
from utils import test_class

examples = [
  {
    'input': [[[1, 3], [0, 2], [1, 3, 4], [0, 2], [2]]],
    'output': [0, 1, 3, 2, 4]
  },
]

# Time Complexity: O(V + E)
# Auxiliary Space: O(V)
class BFS:
  def solve(self, graph):
    queue = Queue()
    queue.put(0)

    visited = [False] * len(graph)
    visited[0] = True

    traversal = []

    while not queue.empty():
      node = queue.get()
      traversal.append(node)

      for neighbor in graph[node]:
        if visited[neighbor]: continue
        visited[neighbor] = True
        queue.put(neighbor)

    return traversal

test_class(BFS, examples)

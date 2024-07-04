from queue import Queue
from utils import test_class

examples = [
  {
    'input': [0, 4, [[1, 3], [0, 2], [1, 3, 4], [0, 2], [2]]],
    'output': [0, 1, 2, 4]
  },
  {
    'input': [
      2, 6,
      [[1, 3], [0, 2], [1], [0, 4, 7], [3, 5, 6, 7], [4, 6], [4, 5, 7], [3, 4, 6]]
    ],
    'output': [2, 1, 0, 3, 4, 6]
  },
]

# Time Complexity: O(V + E)
# Auxiliary Space: O(V)
class BFS:
  def solve(self, src, dest, graph):
    dist = [float('inf')] * len(graph)
    dist[src] = 0

    queue = Queue()
    queue.put(src)

    parent = [-1] * len(graph)

    while not queue.empty():
      node = queue.get()

      for neighbor in graph[node]:
        if dist[neighbor] != float('inf'): continue

        dist[neighbor] = dist[node] + 1
        parent[neighbor] = node
        queue.put(neighbor)

    curr = dest
    path = [dest]
    while parent[curr] != -1:
      path.append(parent[curr])
      curr = parent[curr]

    return list(reversed(path))

test_class(BFS, examples)

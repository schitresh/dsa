from queue import Queue
from utils import test_class

#  Given an unweighted, undirected graph of V nodes and E edges, a source node S, and
# a destination node D, find the shortest distance from node S to node D in the graph.

examples = [
  {
    'input': [[[1, 3], [0, 2], [1, 3, 4], [0, 2], [2]]],
    'output': [0, 1, 2, 1, 3]
  },
  {
    'input': [[[1, 3], [0, 2], [1], [0, 4, 7], [3, 5, 6, 7], [4, 6], [4, 5, 7], [3, 4, 6]]],
    'output': [0, 1, 2, 1, 2, 3, 3, 2]
  },
]

# Time Complexity: O(V + E)
# Auxiliary Space: O(V)
class BFS:
  def solve(self, graph):
    dist = [float('inf')] * len(graph)
    dist[0] = 0

    queue = Queue()
    queue.put(0)

    while not queue.empty():
      node = queue.get()

      for neighbor in graph[node]:
        if dist[neighbor] != float('inf'): continue

        dist[neighbor] = dist[node] + 1
        queue.put(neighbor)

    return dist

test_class(BFS, examples)

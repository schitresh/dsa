from queue import Queue
from utils import test_class

# Breadth First Search (BFS)
# It starts from a given source and explores all reachable vertices from the given
# source. It traverses vertices level by level using a queue.
# But unlike trees, graphs may contain cycles, so we may come to the same node again.
# To avoid processing a node more than once, we use a boolean visited array.

examples = [
  {
    'input': [[[1, 3], [0, 2], [1, 3, 4], [0, 2], [2]]],
    'output': [0, 1, 3, 2, 4]
  },
]

# Using Queue
# Time Complexity: O(V + E)
# Auxiliary Space: O(V)
class Solution:
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

test_class(Solution, examples)

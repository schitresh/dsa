from queue import PriorityQueue
from utils import test_class

# Minimum Spanning Tree
# Subset of edges of a connected undirected graph that connects all the vertices
# together without any cycles such that the weight of all selected edges is minimum.

# Prim's Minimum Spanning Tree
# Starts with a single node and moves through adjacent nodes.
# Explores all the connected edges and picks up the minimum weight edge first.

examples = [
  {
    'input': [
      [
        [[4, 1], [1, 3]],
        [[4, 0], [3, 2]],
        [[3, 1], [2, 3], [2, 4]],
        [[1, 0], [2, 2]],
        [[2, 2]]
      ]
    ], # x: [weight, y]
    'output': 8
  }
]

# Start from a node and keep finding the shortest path for each neighbor
# Time Complexity: O(E * log(E))
# Auxiliary Space: O(E)
class Solution:
  def solve(self, graph):
    pqueue = PriorityQueue()
    pqueue.put([0, 0])
    visited = [False] * len(graph)

    minimum_spanning_tree = 0

    while not pqueue.empty():
      node_distance, node = pqueue.get()

      if visited[node]: continue
      visited[node] = True
      minimum_spanning_tree += node_distance

      for neighbor_distance, neighbor in graph[node]:
        pqueue.put([neighbor_distance, neighbor])

    return minimum_spanning_tree

test_class(Solution, examples)

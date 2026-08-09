from queue import Queue
from utils import test_class

# Given a weighted Directed Acyclic Graph (DAG) and a source vertex in the graph, find
# the shortest paths from given source to all other vertices.

# For a general weighted graph, we can calculate single source shortest distances in
# O(V * E) time using Bellman–Ford Algorithm.
# For a graph with no negative weights, we can do better and calculate single source
# shortest distances in O(E + V * log(V)) time using Dijkstra’s algorithm.
# For Directed Acyclic Graph (DAG), we can even do better. We can calculate single
# source shortest distances in O(V+E) using Topological Sorting.

examples = [
  {
    'input': [
      [
        [[4, 1], [1, 3], [1, 2]],
        [[3, 2]],
        [[2, 3], [2, 4]],
        [],
        []
      ], 0
    ], # x: [weight, y]
    'output': [0, 4, 1, 1, 3]
  },
  {
    'input': [
      [
        [[5, 1], [10, 3]],
        [[3, 2]],
        [[1, 3]],
        [],
        [[1, 3]]
      ], 0
    ],
    'output': [0, 5, 8, 9, float('inf')]
  },
  {
    'input': [
      [
        [[5, 1], [3, 2]],
        [[6, 3], [2, 2]],
        [[4, 4], [2, 5], [7, 3]],
        [[1, 5], [-1, 4]],
        [[-2, 5]],
        []
      ], 1
    ],
    'output': [float('inf'), 0, 2, 6, 5, 3]
  },
]

# Topological Sorting
# Since this is a directed path, topological order will help in iterating
# in a directional order and get the longest path.
# Initialize distances to all vertices as infinite and distance to source as 0, then
# find a topological sorting of the graph. Topological Sorting of a graph represents a
# linear ordering of the graph. Once we have topological order (or linear
# representation), we one by one process all vertices in topological order. For every
# vertex being processed, we update distances of its adjacent using distance of current
# vertex.
# Time Complexity: O(V + E)
# Auxiliary Space: O(V + E)
class Solution:
  def solve(self, graph, source):
    order = self.topological_sort(graph)
    dist = [float('inf')] * len(graph)
    dist[source] = 0

    for node in order:
      if dist[node] == -float('inf'): continue

      for weight, neighbor in graph[node]:
        neighbor_dist = dist[node] + weight

        if neighbor_dist < dist[neighbor]:
          dist[neighbor] = neighbor_dist

    return dist

  def topological_sort(self, graph):
    in_degree = [0] * len(graph)
    queue = Queue()

    for neighbors in graph:
      for _weight, neighbor in neighbors:
        in_degree[neighbor] += 1

    for node in range(len(graph)):
      if in_degree[node] == 0:
        queue.put(node)

    visited = 0
    order = []

    while not queue.empty():
      node = queue.get()
      visited += 1
      order.append(node)

      for _weight, neighbor in graph[node]:
        in_degree[neighbor] -= 1
        if in_degree[neighbor] == 0:
          queue.put(neighbor)

    if visited != len(graph):
      print('Graph contains cycle')
      return

    return order

test_class(Solution, examples)

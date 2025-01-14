from queue import Queue
from utils import test_class

# Given a weighted DAG and a source vertex, find the longest distance from the source
# vertex to all other vertices.
# For a general graph, it is not as easy as the shortest path problem because it doesn't
# have the optimal substructure property (it is NP-hard).
# But for DAG, it has a linear time solution.

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
    ], # x: [weight, y], src
    'output': [0, 4, 7, 9, 9]
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
    'output': [0, 5, 8, 10, -float('inf')]
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
    'output': [-float('inf'), 0, 2, 9, 8, 10]
  },
]

# Since this is a directed path, topological order will help in iterating in a
# directional order and get the longest path.
# Time Complexity: O(V + E)
# Auxiliary Space: O(V + E)
class Solution:
  def solve(self, graph, source):
    order = self.topological_sort(graph)
    dist = [-float('inf')] * len(graph)
    dist[source] = 0

    for node in order:
      if dist[node] == -float('inf'): continue

      for weight, neighbor in graph[node]:
        neighbor_dist = dist[node] + weight

        if dist[neighbor] < neighbor_dist:
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

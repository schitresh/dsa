from sys import maxsize
from utils import test_class

# Given a weighted graph with V vertices and E edges, and a source vertex src, find the
# shortest path from the source vertex to all vertices in the given graph.

# Bellman Ford's Algorithm
# Bellman Ford is slower than Dijkstra but capable of handling negative weights.
# Shortest path cannot be found if there is a negative cycle. This also makes it capable
# of detecting negative cycles.

# Primary Principle
# It starts with a single source and calculates the distance to each node. The distance
# is initially unknown and assumed to be infinte.
# But as time goes on, the algorithm relaxes those paths by identifying a few shorter
# paths. All the edges should be relaxed N - 1 times to compute the single source
# shortest path. This is because a graph can have at most N - 1 edges.
# After running N - 1 times, all combinations of neighbor edges would be covered

# Negative Cycle
# To detect whether a negative cycle exists, relax all the edges one more time. If the
# shortest distance for any node reduces, then a negative cycle exists.

examples = [
  {
    'input': [
      [
        [[4, 1], [1, 3], [1, 2]],
        [[4, 0], [3, 2]],
        [[1, 0], [3, 1], [2, 3], [2, 4]],
        [[1, 0], [2, 2]],
        [[2, 2]]
      ]
    ], # x: [weight, y]
    'output': [0, 4, 1, 1, 3]
  }
]

# Bellman Ford
# Time Complexity: O(V * E),
  # Best: O(E), average: O(V * E), worst: O(V * E)
  # If graph is disconnected: O(V * (V * E))
# Auxiliary Space: O(V)
class Solution:
  def solve(self, graph):
    distance = [maxsize] * len(graph)
    distance[0] = 0

    # Relax paths for N - 1 or E (edges) times
    for _ in range(len(graph) - 1):
      for node in range(len(graph)):
        for weight, neighbor in graph[node]:
          if distance[node] == maxsize: continue

          current_dist = distance[node] + weight
          if current_dist < distance[neighbor]:
            distance[neighbor] = current_dist

    # Check for negative cycle by relaxing one more time
    for node in range(len(graph)):
      for weight, neighbor in graph[node]:
        if distance[node] == maxsize: continue

        current_dist = distance[node] + weight
        if current_dist < distance[neighbor]:
          print('Graph contains negative weight cycle')
          return

    return distance

test_class(Solution, examples)

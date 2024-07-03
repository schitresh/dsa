from sys import maxsize
from utils import test_class

# x: [weight, y]
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
    ],
    'output': False
  },
  {
    'input': [
      [
        [[1, 1]],
        [[1, 2]],
        [[3, 3]],
        [[-3, 3]],
        [[-3, 0]]
      ]
    ],
    'output': True
  }
]

# Relax paths for N - 1 times to get the shortest distances
# Relax for the Nth time and check if there is still a shorter path
# If so, there is a negative cycle
# Time Complexity: O(V * E)
# Auxiliary Space: O(V)
class BellmanFord:
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
          return True

    return False

# Calculate the distances for all the pair of nodes
# If there is any negative distance from a node to itself, there is a negative cycle
# Time Complexity: O(V^3)
# Auxiliary Space: O(V^2)
class FloydWarshall:
  def solve(self, graph):
    # Store shortest distances between each pair of nodes
    dist = [[float('inf')] * len(graph) for _ in range(len(graph))]

    # Initialize the shortest distances to the weights
    # Considering no intermediate nodes
    for node in range(len(graph)):
      # Distance of node from itself is 0
      dist[node][node] = 0

      for weight, neighbor in graph[node]:
        dist[node][neighbor] = weight

    # Consider each node as intermediate
    # And iterate over all the pair of nodes
    for intermediate in range(len(graph)):
      for i in range(len(graph)):
        for j in range(len(graph)):
          current_dist = dist[i][intermediate] + dist[intermediate][j]
          dist[i][j] = min(dist[i][j], current_dist)

    # If there is any node for which distance to itself is negative
    # Then there is a negative cycle
    for i in range(len(graph)):
      if dist[i][i] < 0: return True

    return False

test_class(BellmanFord, examples)
test_class(FloydWarshall, examples)

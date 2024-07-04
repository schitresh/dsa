from utils import test_class

# Floyd Warshall Algorithm
# All pair shortest path algorithm, works for both directed and undirected graphs
# Dijkstra and Bellman Ford are single source shortest path algorithms
# Does not work with negative cycles (sum of edges in a cycle is negative)
# Treats each vertex as an intermediate node one by one
# Irrespective of edges, it runs for O(V^3), so it's best suited for dense graphs
# For sparse graphs, Johnson's algorithm is more suitable

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
    'output': [
      [0, 4, 1, 1, 3],
      [4, 0, 3, 5, 5],
      [1, 3, 0, 2, 2],
      [1, 5, 2, 0, 4],
      [3, 5, 2, 4, 0]
    ]
  },
  {
    'input': [
      [
        [[5, 1], [10, 3]],
        [[3, 2]],
        [[1, 3]],
        [],
      ]
    ],
    'output': [
      [0, 5, 8, 9],
      [float('inf'), 0, 3, 4],
      [float('inf'), float('inf'), 0, 1],
      [float('inf'), float('inf'), float('inf'), 0]
    ]
  }
]

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

    return dist

test_class(FloydWarshall, examples)

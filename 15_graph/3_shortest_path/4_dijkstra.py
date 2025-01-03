from queue import PriorityQueue
from sys import maxsize
from utils import test_class

# Given a weighted graph and a source vertex in the graph, find the shortest paths from
# the source to all the other vertices in the given graph. The given graph does not
# contain any negative edge.

# Dijkstra's Algorithm
# Start from the source and iteratively select unvisited nodes with the smallest
# tentative distance from the source. Then visit the neighbors of this vertex and update
# their tentative distance.
# Works for both directed and undirected graphs. Doesn't work for negative weights.

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

# Dijkstra
# Time Complexity: O((E + V) * log(V))
# Auxiliary Space: O(V)
class Solution:
  def solve(self, graph):
    queue = PriorityQueue()
    queue.put([0, 0])

    distance = [maxsize] * len(graph)
    distance[0] = 0

    visited = [False] * len(graph)

    while not queue.empty():
      node_dist, node = queue.get()

      if visited[node]: continue
      visited[node] = True

      for weight, neighbor in graph[node]:
        current_dist = node_dist + weight

        if current_dist < distance[neighbor]:
          distance[neighbor] = current_dist
          queue.put([distance[neighbor], neighbor])

    return distance

test_class(Solution, examples)

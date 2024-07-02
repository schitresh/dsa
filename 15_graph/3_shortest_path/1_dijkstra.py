from queue import PriorityQueue
from sys import maxsize
from utils import test_class

# Dijkstra's Algorithm
# Start from the source and iteratively select unvisited nodes
# with the smallest tentative distance from the source
# Then visit the neighbors of this vertex and update their tentative distance
# Works for both directed and undirected graphs

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
    'output': [0, 4, 1, 1, 3]
  }
]

# Time Complexity: O((E + V) * log(V))
# Auxiliary Space: O(V)
class Dijkstra:
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

test_class(Dijkstra, examples)

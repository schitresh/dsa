from queue import PriorityQueue
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
    'output': [0, 4, 1, 1, 3]
  }
]

# Start from a node, and keep finding the shortest path for each neighbor
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

      for neighbor_dist, neighbor in graph[node]:
        current_dist = node_dist + neighbor_dist

        if current_dist < distance[neighbor]:
          distance[neighbor] = current_dist
          queue.put([distance[neighbor], neighbor])

    return distance

test_class(Dijkstra, examples)

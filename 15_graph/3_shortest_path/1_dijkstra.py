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
# e = edges
# Time Complexity: O(e + v * logv)
# Auxiliary Space: O(e)
class Dijkstra:
  def solve(self, graph):
    pqueue = PriorityQueue()
    pqueue.put([0, 0])
    distance = [maxsize] * len(graph)
    distance[0] = 0
    visited = [False] * len(graph)

    while not pqueue.empty():
      node_distance, node = pqueue.get()
      if visited[node]:
        continue
      visited[node] = True

      for neighbor_distance, neighbor in graph[node]:
        if node_distance + neighbor_distance < distance[neighbor]:
          distance[neighbor] = node_distance + neighbor_distance
          pqueue.put([distance[neighbor], neighbor])

    return distance

test_class(Dijkstra, examples)

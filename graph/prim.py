from queue import PriorityQueue
from utils import test

# x: [weight, y]
examples = [
  {
    'input': [
      [
        [[4, 1], [1, 3]],
        [[4, 0], [3, 2]],
        [[3, 1], [2, 3], [2, 4]],
        [[1, 0], [2, 2]],
        [[2,2]]
      ]
    ],
    'output': 8
  }
]

# Start from a node, and keep finding the shortest path for each neighbor
# e = edges
# Time Complexity:
# Space Complexity:
class Prim:
  def solve(self, graph):
    pqueue = PriorityQueue()
    pqueue.put([0, 0])
    visited = [False] * len(graph)
    # minimum spanning tree
    mst = 0

    while not pqueue.empty():
      node_distance, node = pqueue.get()
      if visited[node]:
        continue
      visited[node] = True
      mst += node_distance

      for neighbor_distance, neighbor in graph[node]:
        pqueue.put([neighbor_distance, neighbor])

    return mst

test(Prim, examples)

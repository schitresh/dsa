import math
from queue import PriorityQueue
from utils import test_class

# Find the minimum spanning tree that has the minimum product of the weights
# Given a connected and undirected graph, a spanning tree of that graph is a subgraph
# that is a tree and connects all the vertices together. A single graph can have many
# different spanning trees.
# A minimum product spanning tree for a weighted, connected, and undirected graph is a
# spanning tree with a weight product less than or equal to the weight product of every
# other spanning tree. The weight product of a spanning tree is the product of weights
# corresponding to each edge of the spanning tree. All weights of the given graph will
# be positive for simplicity.

examples = [
  {
    'input': [
      [
        [[4, 1], [1, 3]],
        [[4, 0], [3, 2]],
        [[3, 1], [2, 3], [2, 4]],
        [[1, 0], [2, 2]],
        [[2, 2]]
      ]
    ], # x: [weight, y]
    'output': 12
  },
  {
    'input': [
      [
        [[2, 1], [6, 3]],
        [[2, 0], [3, 2], [8, 3], [5, 4]],
        [[3, 1], [7, 4]],
        [[6, 0], [8, 1], [9, 4]],
        [[5, 1], [7, 2], [9, 3]]
      ]
    ],
    'output': 180
  }
]

# Prim's Algorithm
# log(w1 * w2 * ... * wn) = log(w1) + log(w2) + ...  + log(wn)
# So by minimizing log(wi), we can minimize the product
# Time Complexity: O(E * log(E))
# Auxiliary Space: O(E)
class Solution:
  def solve(self, graph):
    pqueue = PriorityQueue()
    # [log_dist, dist, node]
    pqueue.put([1, 1, 0])
    visited = [False] * len(graph)

    product = 1

    while not pqueue.empty():
      _node_log_dist, node_dist, node = pqueue.get()

      if visited[node]: continue
      visited[node] = True
      product *= node_dist

      for neighbor_dist, neighbor in graph[node]:
        neighbor_log_dist = math.log(neighbor_dist)
        pqueue.put([neighbor_log_dist, neighbor_dist, neighbor])

    return product

test_class(Solution, examples)

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

# Time Complexity: O(V * E)
# Auxiliary Space: O(V)
class Solution:
  def __init__(self) -> None:
    self.dist = [[]]

  def solve(self, graph):
    self.graph = graph
    self.dist = [0] * len(graph)
    visited = [False] * len(graph)

    for node in range(len(graph)):
      if visited[node]: continue

      if self.negative_cycle(node): True

    return False

  def negative_cycle(self, curr):
    self.dist = [float('inf')] * len(self.graph)
    self.dist[curr] = 0

    for _ in range(len(self.graph) - 1):
      for neighbor


test_class(Solution, examples)

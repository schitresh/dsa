from queue import LifoQueue
from utils import test_class

examples = [
  {
    'input': [[[1, 2, 3], [2], [3, 4], [], []]],
    'output': [[0, 1, 2, 3, 4], [0, 1, 2, 4, 3]]
  },
  {
    'input': [[[1, 2], [2, 3], [3], []]],
    'output': [[0, 1, 2, 3]]
  },
  {
    'input': [[[1], [2], [], [1, 2]]],
    'output': [[0, 3, 1, 2], [3, 0, 1, 2]]
  },
  {
    'input': [[[], [], [3], [1], [0, 1], [0, 2]]],
    'output': [
      [4, 5, 0, 2, 3, 1],
      [4, 5, 2, 0, 3, 1],
      [4, 5, 2, 3, 0, 1],
      [4, 5, 2, 3, 1, 0],
      [5, 2, 3, 4, 0, 1],
      [5, 2, 3, 4, 1, 0],
      [5, 2, 4, 0, 3, 1],
      [5, 2, 4, 3, 0, 1],
      [5, 2, 4, 3, 1, 0],
      [5, 4, 0, 2, 3, 1],
      [5, 4, 2, 0, 3, 1],
      [5, 4, 2, 3, 0, 1],
      [5, 4, 2, 3, 1, 0]
    ]
  },
]

# Time Complexity: O(V!)
  # V! is absolute worst case when there are no edges
# Auxiliary Space: O(V)
class AllTopoSort:
  def __init__(self) -> None:
    self.graph = [[]]
    self.visited = []
    self.in_degree = []
    self.orders = []

  def solve(self, graph):
    self.graph = graph
    self.visited = [False] * len(graph)
    self.in_degree = [0] * len(graph)

    for neighbors in graph:
      for neighbor in neighbors:
        self.in_degree[neighbor] += 1

    path = []
    self.find_topo_orders(path)
    return self.orders

  def find_topo_orders(self, path):
    if len(path) == len(self.graph):
      self.orders.append(path.copy())
      return

    for node in range(len(self.graph)):
      # If the in-degree is not 0, that means there are some unvisited nodes (sources)
      # that have a directed edge towards the current node
      # Hence, consider the current node only if in_degree is 0
      if self.visited[node] or self.in_degree[node] > 0:
        continue

      for neighbor in self.graph[node]:
        self.in_degree[neighbor] -= 1

      self.visited[node] = True
      path.append(node)

      self.find_topo_orders(path)

      # Backtrack to consider next node for the current path

      for neighbor in self.graph[node]:
        self.in_degree[neighbor] += 1

      self.visited[node] = False
      path.pop()

test_class(AllTopoSort, examples)

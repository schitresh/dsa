from utils import test_class

# Reverse Delete Algorithm for Minimum Spanning Tree
# Closely related to Kruskal's algorithm
# Sort all edges in descending order of weights, and pick edges one by one
# Include the current edge if excluding it causes disconnection in the graph
# Put another way, keep deleting edges if the deletion does not disconnect the graph

# [weight, y]
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
    ],
    'output': 8
  }
]

# Time Complexity: O(E * log(E) + E * (V + E))
  # Sorting edges takes O(E * log(E))
  # Removing the edge takes O(E) and checking connection using dfs takes O(V)
  # So iterating over edges takes O(E * (V + E))
  # Max(E) = V^2
# Auxiliary Space: O(V + E)
class ReverseDeletion:
  def __init__(self) -> None:
    self.graph = [[]]
    self.edges = []

  def solve(self, graph):
    self.graph = graph
    self.graph_edges(graph)

    self.edges = sorted(self.edges, key = lambda node: node[0], reverse = True)
    minimum_spanning_tree = 0

    for distance, node, neighbor in self.edges:
      self.graph[node].remove([distance, neighbor])
      self.graph[neighbor].remove([distance, node])

      if not self.connected():
        self.graph[node].append([distance, neighbor])
        self.graph[neighbor].append([distance, node])

        minimum_spanning_tree += distance

    return minimum_spanning_tree

  def connected(self):
    visited = [False] * len(self.graph)
    self.dfs(0, visited)

    if not all(visited): return False
    return True

  def dfs(self, node, visited):
    visited[node] = True

    for _dist, neighbor in self.graph[node]:
      if visited[neighbor]: continue
      self.dfs(neighbor, visited)

  def graph_edges(self, graph):
    self.edges = []
    visited = [False] * len(graph)

    for node in range(len(graph)):
      visited[node] = True

      for distance, neighbor in graph[node]:
        if visited[neighbor]: continue
        self.edges.append([distance, node, neighbor])


test_class(ReverseDeletion, examples)

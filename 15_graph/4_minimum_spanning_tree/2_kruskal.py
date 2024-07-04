from utils import test_class

# Kruskal's Minimum Spanning Tree
# Sort all edges of the graph in increasing order
# Keep on adding new edges (or nodes) if it doesn't create a cycle
# Use Union-Find algorithm to detect cycles
# Thus, it makes a locally optimal choice in each step to find the optimal solution
# Hence, this is a greedy algorithm

# [weight, x, y]
examples = [
  {
    'input': [[[4, 0, 1], [1, 0, 3], [3, 1, 2], [2, 3, 2], [2, 2, 4]]],
    'output': 8
  }
]

# Time Complexity: O(E * log(E))
  # Sorting edges takes O(E * log(E))
  # Finding root and union takes O(log(V))
  # So iterating over edges takes O(E * log(V))
  # Max(E) = V^2
# Auxiliary Space: O(V + E)
class Kruskal:
  def __init__(self) -> None:
    self.graph = [[]]
    self.parent = []
    self.rank = []

  def root(self, node):
    parent = self.parent[node]
    if parent != node:
      self.parent[node] = self.root(parent)

    return self.parent[node]

  def union(self, node_root, neighbor_root):
    node_rank = self.rank[node_root]
    neighbor_rank = self.rank[neighbor_root]

    if node_rank < neighbor_rank:
      self.parent[node_root] = neighbor_root
    elif node_rank > neighbor_rank:
      self.parent[neighbor_root] = node_root
    else:
      self.parent[neighbor_root] = node_root
      self.rank[node_root] += 1

  def solve(self, graph):
    self.graph = sorted(graph, key = lambda node: node[0])
    self.parent = list(range(len(graph)))
    self.rank = [0] * len(graph)

    minimum_spanning_tree = 0

    for distance, node, neighbor in self.graph:
      node_root = self.root(node)
      neighbor_root = self.root(neighbor)
      # If the roots are equal, then there is a cycle
      if node_root == neighbor_root: continue

      minimum_spanning_tree += distance
      self.union(node_root, neighbor_root)

    return minimum_spanning_tree

test_class(Kruskal, examples)

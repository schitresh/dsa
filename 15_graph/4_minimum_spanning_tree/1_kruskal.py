from utils import test_class

# Kruskal's Minimum Spanning Tree
# [weight, x, y]
examples = [
  {
    'input': [[[4, 0, 1], [1, 0, 3], [3, 1, 2], [2, 3, 2], [2, 2, 4]]],
    'output': 8
  }
]

# e = edges
# Time Complexity: O(e * loge)
# Auxiliary Space: O(e)
class Kruskal:
  def root(self, parents, node):
    if parents[node] == node:
      return node
    return self.root(parents, parents[node])

  def union(self, parents, node, neighbor):
    node_root = self.root(parents, node)
    neighbor_root = self.root(parents, neighbor)
    parents[node_root] = parents[neighbor_root]

  def solve(self, graph):
    parents = list(range(len(graph)))
    graph.sort(key = lambda node: node[0])
    # minimum spanning tree
    mst = 0

    for distance, node, neighbor in graph:
      if self.root(parents, node) == self.root(parents, neighbor):
        continue
      mst += distance
      self.union(parents, node, neighbor)

    return mst

test_class(Kruskal, examples)

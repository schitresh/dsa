from utils import test_class

# Given an undirected graph and a number m, color the graph with at most m colors
# such that no two adjacent vertices of the graph are colored with the same color.
# Here coloring of a graph means the assignment of colors to all vertices.

examples = [
  {
    'input': [3, [
      [0, 1, 1, 1],
      [1, 0, 1, 0],
      [1, 1, 0, 1],
      [1, 0, 1, 0]
    ]],
    'output': [1, 2, 3, 2]
  },
]

# Time Complexity: O(m^V), there is a total of m^V cominations for colors
# Auxiliary Space: O(V), due to recursive stack
class Solution:
  def solve(self, m_colors, graph):
    self.m_colors = m_colors
    self.graph = graph
    self.colors = [0] * len(graph)

    self.color_graph(0)

    return self.colors

  def color_graph(self, node):
    if node == len(self.graph):
      return True

    for color in range(1, self.m_colors + 1):
      if not self.valid_color(node, color): continue

      self.colors[node] = color
      if self.color_graph(node + 1): return True
      self.colors[node] = 0

    return False

  def valid_color(self, node, color):
    for neighbor_node in range(len(self.graph)):
      if self.graph[node][neighbor_node] == 0:
        continue

      if self.colors[neighbor_node] == color:
        return False

    return True

test_class(Solution, examples)

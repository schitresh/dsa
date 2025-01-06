from utils import test_class

# Biconnected Component
# A biconnected component is a maximal biconnected subgraph
# After removing the articulation points, the subgraphs that will remain biconnected are
# called biconnected components

examples = [
  {
    'input': [[[1, 3], [0, 2], [1, 3, 4], [0, 2], [2]]],
    'output': [[(2, 4)], [(3, 0), (2, 3), (1, 2), (0, 1)]]
  },
  {
    'input': [[[1, 3], [0, 2], [1], [0, 4, 7], [3, 5, 6, 7], [4, 6], [4, 5, 7],
                [3, 4, 6]]],
    'output': [[(1, 2)], [(7, 3), (6, 7), (6, 4), (5, 6), (4, 5), (3, 4)], [(0, 3)],
                [(0, 1)]]
  },
  {
    'input': [[[1, 3], [0, 2], [1, 3, 4], [0, 2, 4], [2, 3]]],
    'output': [[(4, 2), (3, 4), (3, 0), (2, 3), (1, 2), (0, 1)]]
  },
  {
    'input': [[[1, 6], [0, 2, 3, 5], [1, 3, 4], [1, 2, 4], [2, 3], [1, 6, 7, 8], [0, 5],
                [5, 8], [5, 7, 9], [8], [11], [10]]],
    'output': [[(4, 2), (3, 4), (3, 1), (2, 3), (1, 2)], [(8, 9)],
                [(8, 5), (7, 8), (5, 7)], [(6, 0), (5, 6), (1, 5), (0, 1)], [(10, 11)]]
  },
]

# Todo: Output not correct, check later
# Almost same as checking for biconnected graph. Additionally iterate over all the nodes.
# Time Complexity: O(V + E)
# Auxiliary Space: O(V + E)
class Solution:
  def solve(self, graph):
    self.graph = graph
    self.biconnect_comps = []
    self.stack = []

    self.visited = [False] * len(graph)
    # Stores discovery times of vertices (When a vertex was visited)
    self.disc = [float('inf')] * len(graph)
    # Stores the earliest visited vertex that can be reached from the subtree rooted at u
    # low[u] = min(disc[u], disc[w]), where w is an ancestor of u
    # And there is a back edge from some descendant of u to w
    # E.g. in 1 -> 2, 2-> 3, 3 -> 1: 3 -> 1 is a back edge
    self.low = [float('inf')] * len(graph)
    self.parent = [-1] * len(graph)
    self.time = 0

    for node in range(len(graph)):
      if not self.visited[node]:
        self.art_points(node)

      if len(self.stack) > 0:
        curr_comp = []

        while len(self.stack) > 0:
          edge = self.stack.pop()
          curr_comp.append(edge)

        self.biconnect_comps.append(curr_comp)

    return self.biconnect_comps

  def art_points(self, node):
    self.visited[node] = True
    self.disc[node] = self.time
    self.low[node] = self.time
    self.time += 1

    # Count of children for the current node
    children = 0

    for neighbor in self.graph[node]:
      if not self.visited[neighbor]:
        self.parent[neighbor] = node
        children += 1
        self.stack.append((node, neighbor))

        self.art_points(neighbor)

        # Check if subtree rooted at neighbor
        # has a connection to one of the ancestor of the node
        self.low[node] = min(self.low[node], self.low[neighbor])

        # The node is an articulation point in following cases:
        # (1) The node is the root of DFS tree
        # and has two or more children
        # (2) The node is not the root
        # and any of its neighbor was discovered after the node
        # That means there is no back edge to any ancestor of the node
        # So check if low value of one of its neighbor is more than discovery value of
        # the node
        if (
          self.parent[node] == -1 and children > 1
        ) or (
          self.parent[node] != -1 and self.low[neighbor] >= self.disc[node]
        ):
          edge = ()
          curr_comp = []

          while edge != (node, neighbor):
            edge = self.stack.pop()
            curr_comp.append(edge)

          self.biconnect_comps.append(curr_comp)
      # If the neighbor is already visited and was discovered before the node, then update
      # the low of node to the neighbor's discovery time
      elif neighbor != self.parent[node]:
        # Add the edge to stack only if low value of node is greater than discovery of
        # neighbor
        if self.low[node] > self.disc[neighbor]:
          self.low[node] = min(self.low[node], self.disc[neighbor])
          self.stack.append((node, neighbor))

test_class(Solution, examples)

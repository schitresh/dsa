from utils import test_class

# Given a directed graph and two vertices u & v, count all the possible walks from u to v
# with exactly k edges on the walk.

examples = [
  {
    'input': [0, 4, 3, [[1, 2, 3], [2], [4], [2], []]],
    'output': 2
  },
  {
    'input': [0, 3, 2, [[1, 2, 3], [3], [3], []]],
    'output': 2
  },
]

# Recursion
# Time Complexity: O(V^k), where k is edge_count
# Auxiliary Space: O(V)
class Solution:
  def solve(self, src, dest, edge_count, graph):
    if edge_count == 0:
      if src == dest: return 1
      return 0

    count = 0

    for neighbor in graph[src]:
      count += self.solve(neighbor, dest, edge_count - 1, graph)

    return count

test_class(Solution, examples)

# Dynamic Programming
# Time Complexity: O(V^3 * k), where k is edge_count
# Auxiliary Space: O(V^2 * k)
class Solution2:
  def solve(self, source, destination, edge_count, graph):
    # count[i][j][k] stores count of possible walks from i to j in exactly k edges
    count = [[[0] * (edge_count + 1)
      for _ in range(len(graph))]
      for _ in range(len(graph))]

    for num_edges in range(edge_count + 1):
      for src in range(len(graph)):
        for dest in range(len(graph)):
          if num_edges == 0 and src == dest:
            count[src][dest][num_edges] = 1

          for neighbor in graph[src]:
            count[src][dest][num_edges] += count[neighbor][dest][num_edges - 1]

    return count[source][destination][edge_count]

test_class(Solution2, examples)

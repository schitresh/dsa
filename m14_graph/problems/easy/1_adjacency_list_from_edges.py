from utils import test_class

# Given a list of all edges of a directed graph, such that the edge consists of from
# vertext and to vertex, create the adjanceny list for the given graph.

examples = [
  {
    'input': [[[0, 1], [1, 2], [2, 0]]],
    'output': [[1], [2], [0]],
  },
  {
    'input': [[[0, 1], [1, 2], [1, 3], [2, 3], [3, 0]]],
    'output': [[1], [2, 3], [3], [0]],
  },
]

# Time Complexity: O(n)
# Space Complexity: O(1)
class Solution:
  def solve(self, edges):
    max_vertex = 0
    for edge in edges:
      max_vertex = max(max_vertex, edge[0], edge[1])

    adj_list = [[] for _ in range(max_vertex + 1)]

    for edge in edges:
      adj_list[edge[0]].append(edge[1])

    return adj_list

test_class(Solution, examples)

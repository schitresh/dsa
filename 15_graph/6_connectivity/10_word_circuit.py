from collections import defaultdict
from queue import Queue
from utils import test_class

# Given a dictionary of words, find if they can be chained to form a circle
# A string can be put before another one if its last char
# is same as the first char of the other string

examples = [
  {
    'input': [['abcd', 'defgha']],
    'output': True # abcd -> defgha
  },
  {
    'input': [['aab', 'bac', 'aaa', 'cda']],
    'output': True # aaa -> aab -> bac -> cda
  },
  {
    'input': [['aaa']],
    'output': True # aaa
  },
  {
    'input': [['abc', 'efg', 'cde', 'ghi', 'ija']],
    'output': True # abc -> cde -> efg -> ghi -> ija
  },
  {
    'input': [['ijk', 'kji', 'abc', 'cba']],
    'output': False
  },
  {
    'input': [['ijk', 'kji', 'ixy']],
    'output': False
  },
]

# Create a directed graph of all chars and then find if there is an eulerian circuit
# Create an edge from first char to last char of every word in the dictionary
# Every word's last char will direct to the first char of another matching word
# And that word's last c har will direct to yet another word's first char
# A directed graph has eulerian circuit if in-degree and out-degree of every vertex
# is same and all non-zero degree vertices form a single strongly connnected component
# Time Complexity: O(N * K)
# Auxiliary Space: O(max(N, K))
# where N is number of words in dictionary and K is the max length of word
class Solution:
  def solve(self, words):
    graph = self.create_graph(words)
    if not self.is_scc(graph): return False

    in_degree = defaultdict(lambda: 0)
    for neighbors in graph.values():
      for neighbor in neighbors:
        in_degree[neighbor] += 1

    for node, neighbors in graph.items():
      out_degree = len(neighbors)
      if out_degree != in_degree[node]:
        return False

    return True

  def create_graph(self, words):
    graph = defaultdict(list)

    for word in words:
      src = word[0]
      dest = word[-1]
      graph[src].append(dest)

    return graph

  def is_scc(self, graph):
    visited = dict.fromkeys(graph.keys(), False)
    self.dfs(graph, visited, list(graph.keys())[0])

    if not all(visited.values()): return False

    visited = dict.fromkeys(graph.keys(), False)
    transpose = self.get_transpose(graph)
    self.dfs(transpose, visited, list(graph.keys())[0])

    if not all(visited.values()): return False

    return True

  def dfs(self, graph, visited, node):
    visited[node] = True

    for neighbor in graph[node]:
      if visited.get(neighbor): continue
      self.dfs(graph, visited, neighbor)

  def get_transpose(self, graph):
    transpose = defaultdict(list)

    for node, neighbors in graph.items():
      for neighbor in neighbors:
        transpose[neighbor].append(node)

    return transpose

test_class(Solution, examples)

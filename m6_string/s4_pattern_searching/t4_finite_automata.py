from utils import test_class

examples = [
  {
    'input': ['ababaaaaaba', 'aba'],
    'output': [0, 2, 8]
  },
  {
    'input': ['abcbaabaabc', 'abc'],
    'output': [0, 8]
  }
]

ASCII_COUNT = 256

# Time Complexity: O(n + m)
# Auxiliary Space: O(m)
class Solution:
  def next_state(self, key, state, ascii_index):
    # If the character matches, next state will be state + 1
    if state < len(key) and ord(key[state]) == ascii_index:
      return state + 1

    i = 0
    for j in range(state - 1, -1, -1):
      if ord(key[j]) != ascii_index:
        continue

      # Prefix will always start from 0
      suffix_from = state - j

      # Compare prefix & suffix
      while i < j and key[i] == key[suffix_from + i]:
        i += 1

      if i == j:
        return j + 1

    return 0

  def transition_table(self, key):
    state_count = len(key) + 1
    table = [[0] * ASCII_COUNT for _ in range(state_count)]

    for state in range(state_count):
      for ascii_index in range(ASCII_COUNT):
        table[state][ascii_index] = self.next_state(key, state, ascii_index)

    return table

  def solve(self, text, key):
    indices = []
    transition_table = self.transition_table(key)
    state = 0

    for i in range(len(text)):
      state = transition_table[state][ord(text[i])]
      if state == len(key):
        indices.append(i - len(key) + 1)

    return indices

test_class(Solution, examples)

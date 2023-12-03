from utils import test

examples = [
  {
    'input': ['ababaaaaaba', 'abccabcc'],
    'output': [0, 2, 8]
  },
  {
    'input': ['abcbaabaabc', 'abc'],
    'output': [0, 8]
  }
]

ASCII_COUNT = 256

# Time Complexity: O(n + m)
# Space Complexity: O(m)
class Solution:
  def next_state(self, key, state, ascii_index):
    # If the character matches, next state will be state + 1
    if state < len(key) and ascii_index == ord(key[state]):
      return state + 1

    i = 0
    for temp_state in range(state - 1, -1, -1):
      if ord(key[temp_state]) != ascii_index:
        continue

      # Prefix will always start from 0
      suffix_from = state - temp_state
      # i = 0

      print(state, ascii_index, i, temp_state, suffix_from)
      # if i < temp_state: print(key[i], key[suffix_from + i])
      # Compare prefix & suffix
      while i < temp_state and key[i] == key[suffix_from + i]:
        i += 1

      if i == temp_state:
        return temp_state + 1

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

test(Solution, examples)

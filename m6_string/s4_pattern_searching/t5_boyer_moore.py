from utils import test_class

# Bad Character Heuristics
# Align the pattern at the beginning of the text and start matching from right to left
# Bad Character: The char of text that doesn't match with the current char of the pattern
# On the occurance of bad char, search the last occurence (l) of bad char in the pattern
# 1. If l is found, align l with the bad char
# 2. Else, re-align the pattern from the next char in text

# Todo: Good Suffix Heuristics

examples = [
  {
    'input': ['ababaaaaaba', 'aba'],
    'output': [0, 2, 8]
  }
]

ASCII_COUNT = 256

# Time Complexity: O(n + m)
# Auxiliary Space: O(m)
class BoyerMoore:
  def solve(self, text, key):
    self.key = key
    self.last_occurs_at = self.bad_char_heuristic()
    return self.search(text)

  def bad_char_heuristic(self):
    last_occurs_at = [-1] * ASCII_COUNT

    for i, char in enumerate(self.key):
      last_occurs_at[ord(char)] = i

    return last_occurs_at

  def shifts_to_align(self, text, ti, ki):
    # Current pointer in text + Number of positions where match failed
    bad_char = text[ti + ki]
    shifts_to_align = ki - self.last_occurs_at[ord(bad_char)]
    return max(1, shifts_to_align)

  def search(self, text):
    indices = []
    key = self.key
    last_index_for_matching = len(text) - len(key)

    i = 0
    while i <= last_index_for_matching:
      j = len(key) - 1

      while j >= 0 and text[i + j] == key[j]:
        j -= 1

      if j >= 0:
        i += self.shifts_to_align(text, i, j)
      else:
        indices.append(i)

        # If i is the last valid index for matching, text[i + len(key)] will raise an
        # error. Hence, just increment it by 1 and continue.
        if i == last_index_for_matching:
          i += 1
        else:
          # Since the pattern matched, next char in text will be considered as bad char
          # (i + len(key))
          i += self.shifts_to_align(text, i, len(key))

    return indices

test_class(BoyerMoore, examples)

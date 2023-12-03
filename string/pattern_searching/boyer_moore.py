from utils import test

examples = [
  {
    'input': ['ababaaaaaba', 'aba'],
    'output': [0, 2, 8]
  }
]

# Time Complexity: O(n + m)
# Space Complexity: O(m)
# Bad Char = The last char not matching & where to
class Solution:
  def bad_char_heuristic(self, key):
    ascii_count = 256
    bad_chars = [-1] * ascii_count

    for i, char in enumerate(key):
      bad_chars[ord(char)] = i

    return bad_chars

  def solve(self, text, key):
    indices = []
    bad_chars = self.bad_char_heuristic(key)

    for i in range(len(text) - len(key) + 1):
      j = len(key) - 1

      while j >= 0 and text[i + j] == key[j]:
        j -= 1

      if j < 0:
        indices.append(i)

        # Required when pattern occurs at the end of the text
        if i < len(text) - len(key):
          next_char = text[i + len(key)]
          # To align next char in text with its last occurance in key
          i += len(key) - bad_chars[ord(next_char)]
        else:
          i += 1
      else:
        last_bad_char = text[i + j]
        i += max(1, j - bad_chars[ord(last_bad_char)])

    return indices

test(Solution, examples)

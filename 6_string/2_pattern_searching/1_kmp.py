from utils import test_class

# Knuth Morris Pratt Algo
# Given an array & size k, find the subarray of length with size k having the max sum
examples = [
  {
    'input': ['ababaaaaaba', 'aba'],
    'output': [0, 2, 8]
  }
]

# Time Complexity: O(n + m)
# Space Complexity: O(m)
class Solution:
  # Longest proper prefix which is also a suffix
  # Proper prefix means that the whole word is not considered a prefix
  # Let's say that a text matches the pattern till k chars
  # Considering the pattern till k chars, is there a suffix which matches a proper prefix
  # If so, we can start matching after that prefix
  # Because we've already iterated through the suffix & suffix matches the prefix
  def calculate_lps(self, key):
    lps = [0] * len(key)
    left = 0
    right = 1

    while right < len(key):
      if key[left] == key[right]:
        left += 1
        lps[right] = left
        right += 1
      else:
        if left > 0:
          left = lps[left - 1]
        else:
          lps[right] = 0
          right += 1

    return lps

  def solve(self, text, key):
    text_index = 0
    key_index = 0
    indices = []
    lps = self.calculate_lps(key)

    while text_index < len(text):
      if text[text_index] == key[key_index]:
        text_index += 1
        key_index += 1

        if key_index == len(key):
          indices.append(text_index - key_index)
          key_index = lps[key_index - 1]
      else:
        if key_index > 0:
          key_index = lps[key_index - 1]
        else:
          text_index += 1

    return indices

test_class(Solution, examples)

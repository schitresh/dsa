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
# Auxiliary Space: O(m)
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
      # If chars are equal, it means prefix equals suffix
      # Here prefix is string[0..left] and suffix is string[(right-left)..right]
      # Because 0..left is already matched, lps of right should be left + 1
      if key[left] == key[right]:
        lps[right] = left + 1
        left += 1
        right += 1
      else:
        # Since the chars don't match and left is at the start of the key
        # lps of right should be 0 and right should be moved ahead to check next suffix
        if left == 0:
          lps[right] = 0
          right += 1
        # The current chars don't match and left at the start
        # That means prefix till (left - 1) matched with suffix till (right - 1)
        # But instead of starting from the start, we can check if there any suffix
        # in the current prefix (left - 1) that matches any previous prefix
        # If so, we can start matching from there, else lps[left - 1] will anyways be 0
        else:
          left = lps[left - 1]

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
        if key_index == 0:
          text_index += 1
        else:
          key_index = lps[key_index - 1]

    return indices

test_class(Solution, examples)

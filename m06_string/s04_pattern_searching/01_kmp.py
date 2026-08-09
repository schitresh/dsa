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

  # Longest proper prefix which is also a suffix
  # Proper prefix means that the whole word is not considered a prefix.
  # Let's say that a text matches the pattern till k chars. Considering the pattern till
  # k chars, is there a suffix which matches a proper prefix. If so, we can start
  # matching after that prefix. Because we've already iterated through the suffix &
  # suffix matches the prefix.
  def calculate_lps(self, key):
    lps = [0] * len(key)
    prefix = 0
    suffix = 1

    while suffix < len(key):
      # If chars are equal, it means prefix equals suffix.
      # Here prefix is string[0..prefix] and suffix is string[(suffix - prefix)..suffix]
      # Because 0..prefix is already matched, lps of suffix should be prefix + 1
      if key[prefix] == key[suffix]:
        lps[suffix] = prefix + 1
        prefix += 1
        suffix += 1
      else:
        # Since the chars don't match and prefix is at the start of the key
        # lps of suffix should be 0 and suffix should be moved ahead to check next suffix
        if prefix == 0:
          lps[suffix] = 0
          suffix += 1
        # The current chars don't match and prefix is not at the start.
        # That means prefix till (prefix - 1) matched with suffix till (suffix - 1). But
        # we need to check if there is any suffix within the current suffix that matches
        # any prefix. Since (prefix - 1) = (suffix - 1), we have already calculated that
        # in prefix - 1, so start checking again from lps[prefix - 1]
        # For example, in abacxyababa, consider abac and abab. When we compare c & b, it
        # is not a match, but the lps is not 0 because the suffix ab within the original
        # suffix abab matches the prefix ab. Further which the new suffix aba matches
        # with the prefix.
        else:
          prefix = lps[prefix - 1]

    return lps

test_class(Solution, examples)

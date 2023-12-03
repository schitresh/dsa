from utils import test

examples = [
  {
    'input': ['ababaaaaaba', 'aba'],
    'output': [0, 2, 8]
  }
]

# Time Complexity: O(n + m)
## Worst Case: O(n * m)
# Space Complexity: O(1)
# Calculate hash for the key, and match it against the sliding window in text
# The hash function might have same value even if pattern is not matching, this is called spurious hit
# To minimize these hits, choose a good hash function
# For example, abc = 1 * 26^2 + 2 * 26^1 + 3 * 26^0
class Solution:
  def match(self, text, key, text_index):
    for j in range(len(key)):
      if text[text_index + j] != key[j]:
        return False

    return True

  def solve(self, text, key):
    ascii_count = 256
    # The higher the prime number, the lower the collisions
    prime_number = 101

    indices = []
    text_hash = 0
    key_hash = 0
    # Multiplier for most significant bit of key
    key_msb_multiplier = 1

    # key_msb_multiplier = (ascii_count ^ (len(key) - 1)) % prime_number
    for i in range(len(key) - 1):
      key_msb_multiplier = (ascii_count * key_msb_multiplier) % prime_number

    for i in range(len(key)):
      key_hash = (ascii_count * key_hash + ord(key[i])) % prime_number
      text_hash = (ascii_count * text_hash + ord(text[i])) % prime_number

    for i in range(len(text) - len(key) + 1):
      if text_hash == key_hash and self.match(text, key, i):
        indices.append(i)

      if i < len(text) - len(key):
        window_first_item = ord(text[i])
        window_next_item = ord(text[i + len(key)])
        text_hash_excluding_first_item = (text_hash - window_first_item * key_msb_multiplier)
        text_hash = (ascii_count * text_hash_excluding_first_item + window_next_item) % prime_number

        if text_hash < 0:
          text_hash += prime_number

    return indices

test(Solution, examples)

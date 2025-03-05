from utils import test_method

examples = [
  {
    'input': ['ababaaaaaba', 'aba'],
    'output': [0, 2, 8]
  }
]

ASCII_COUNT = 256

# Calculate hash for the key
# Keep a sliding window in text and keep rolling its hash
# Consider both the hashes, if they are equal carry out the match process
# The hash function might have the same value even if the pattern does not match
# This is called spurious hit, choose a good hash function to minimize these hits
# For example, abc = 1 * 26^2 + 2 * 26^1 + 3 * 26^0
Choose a prime

# Time Complexity: O(n + m)
  # Worst Case: O(n * m)
# Auxiliary Space: O(1)
class RabinKarp:
  def __init__(self, key):
    # Prime number for hash function
    # The higher the prime number, the lower the collisions
    self.prime_number = 101

    self.key = key
    self.key_hash = self.calculate_hash(key)

    # Multiplier for most significant bit of key
    self.msb_multiplier = self.calculate_msb_multiplier()

  # hash(abc) = a * base^2 + b * base^1 + c * base^0
  # hash(abc) = base * (a * base^1 + b) + c
  # hash(abc) = base * hash(ab) + c
  # hash(f(n)) = base * hash(f(n - 1)) + n
  def calculate_hash(self, string):
    hash_str = 0
    # We're matching key, so corresponding length in text will also be len(key)
    for i in range(len(self.key)):
      hash_str = (ASCII_COUNT * hash_str + ord(string[i])) % self.prime_number

    return hash_str

  # Slide the matching window in text, remove first char & add next char
  def roll_hash(self, text, text_hash, i):
    window_first_item = ord(text[i])
    window_next_item = ord(text[i + len(self.key)])

    text_hash -= window_first_item * self.msb_multiplier
    text_hash = (ASCII_COUNT * text_hash + window_next_item) % self.prime_number

    if text_hash < 0:
      text_hash += self.prime_number

    return text_hash

  # Most Significant Bit multiplier from hash of key (since we're matching key)
  # ASCII_COUNT ^ (len(key) - 1)
  def calculate_msb_multiplier(self, ):
    msb_multiplier = 1
    for _ in range(len(self.key) - 1):
      msb_multiplier = (ASCII_COUNT * msb_multiplier) % self.prime_number

    return msb_multiplier

  def match(self, text, key, text_index):
    for j in range(len(key)):
      if text[text_index + j] != key[j]:
        return False

    return True

  def search(self, text):
    key = self.key
    key_hash = self.key_hash
    text_hash = self.calculate_hash(text)
    last_index_for_matching = len(text) - len(key)
    indices = []

    for i in range(last_index_for_matching + 1):
      if text_hash == key_hash and self.match(text, key, i):
        indices.append(i)

      if i < last_index_for_matching:
        text_hash = self.roll_hash(text, text_hash, i)

    return indices

def solve(text, key):
  rabin_karp = RabinKarp(key)
  return rabin_karp.search(text)

test_method(solve, examples)

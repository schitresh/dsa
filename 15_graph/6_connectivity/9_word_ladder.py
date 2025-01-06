from queue import Queue
from utils import test_class

# Word Ladder: Length of shortest chain to reach a target word
# Given a dictionary and two words start & target (both of same length), find length of
# the smallest chain from start to target (if it exists) such that adjacent words in the
# chain only differ by one character and each word in the chain is a valid word (i.e. it
# exists in the dictionary).
# It can be assumed that the target word exists in the dictionary and the length of all
# the dictionary words is same.

examples = [
  {
    'input': ['toon', 'plea', {'poon', 'plee', 'same', 'poie', 'plea', 'plie', 'poin'}],
    'output': 7
    # toon -> poon -> poin -> poie -> plie -> plee -> plea
  },
  {
    'input': ['abcv', 'ebad', {'abcd', 'ebad', 'ebcd', 'xyza'}],
    'output': 4
    # abcv -> abcd -> ebcd -> ebad
  },
]

# BFS
# Time Complexity: O(N^2 * K)
# Auxiliary Space: O(N * K)
# where N is number of words in dictionary and K is length of word
class Solution:
  def solve(self, start, target, words):
    if start == target: return 0
    if target not in words: return 0

    words = words.copy()
    word_len = len(start)

    queue = Queue()
    queue.put([start, 1])

    while not queue.empty():
      word, level = queue.get()
      word = list(word)

      for pos in range(word_len):
        original_char = word[pos]

        for char_num in range(ord('a'), ord('z') + 1):
          word[pos] = chr(char_num)
          new_word = ''.join(word)

          if new_word == target:
            return level + 1

          if new_word in words:
            words.remove(new_word)
            queue.put([new_word, level + 1])

        word[pos] = original_char

    return 0

test_class(Solution, examples)

# Keep track of intermediate words from the dictionary
# For example, 'poon' will have intermediate words '*oon', 'p*on', 'po*n', 'poo*'.
# So map of 'p*on' will store all such words in the dictionary. Then perform BFS, and
# keep checking if intermediate words match the target.
# Time Complexity: O(N^2 * K)
# Auxiliary Space: O(N * K)
# where N is number of words in dictionary and K is length of word
class Solution2:
  def solve(self, start, target, words):
    if start == target: return 0
    if target not in words: return 0

    word_len = len(start)

    umap = {}

    # Initialize umap with the first iteration from start
    for i in range(word_len):
      intermediate_word = start[: i] + '*' + start[i + 1 :]
      umap[intermediate_word] = []

    # Find all matching words the intermediate words
    # E.g. find all the words that match the pattern '*oon', then for 'p*on', and so on
    for word in words:
      for i in range(word_len):
        intermediate_word = word[: i] + '*' + word[i + 1 :]
        if intermediate_word not in umap: umap[intermediate_word] = []
        umap[intermediate_word].append(word)

    # print(umap)
    queue = Queue()
    queue.put([start, 1])
    visited = { start: True }

    while not queue.empty():
      word, level = queue.get()

      if word == target: return level

      for i in range(word_len):
        intermediate_word = word[: i] + '*' + word[i + 1 :]
        matching_words = umap[intermediate_word]

        for matching_word in matching_words:
          if visited.get(matching_word): continue
          visited[matching_word] = True
          queue.put([matching_word, level + 1])

    return 0

test_class(Solution2, examples)

from collections import defaultdict
from utils import test_class

# For the given words, build a state machine
## Construct a trie
## Calculate the failure/suffix links
## Calculate the output links
# Iterate the given text and apply the state machine

# Time Complexity: O(n + w + m)
# Trie Construction: O(n)
# Failure Link Construction: O(n)
# Searching: O(w + m)

# Auxiliary Space: O(w * a)

# n = length of text
# w = length of keywords
# m = number of matches/occurrences
# a = length of alphabet (Since it is the max number of children a node can have)

examples = [
  {
    'input': ['ahishers', ['he', 'she', 'his', 'hers']],
    'output': { 'he': [4], 'she': [3], 'his': [1], 'hers': [4] }
  }
]

ASCII_COUNT = 256
ASCII_OF_A = 97

class AhoCorasick:
  def solve(self, text, words):
    self.process_words(words)
    return self.search_words(text)

  def process_words(self, words):
    for i in range(len(words)):
      words[i] = words[i].lower()

    self.words = words
    self.max_chars = 26
    self.max_states = sum([len(word) for word in words])

    # Words implemented as trie
    # Keep one extra state for root
    self.trie = [[-1] * self.max_chars for _ in range(self.max_states + 1)]

    # Failure Links or Suffix Links
    # Link to a maximum prefix that matches a maximum suffix
    self.fail = [-1] * (self.max_states + 1)

    # Bit mask for the states
    self.output = [0] * (self.max_states + 1)

    # Will be assigned after trie is built
    self.state_count = 0
    self.build_matching_machine()

  def build_matching_machine(self):
    self.build_trie()
    self.build_failure_links()

  def build_trie(self):
    # Root will have the state 0
    state = 1

    for i in range(len(self.words)):
      word = self.words[i]
      current_state = 0

      for char in word:
        char_num = ord(char) - ASCII_OF_A

        if self.trie[current_state][char_num] == -1:
          self.trie[current_state][char_num] = state
          state += 1

        current_state = self.trie[current_state][char_num]

      # Represent word at index i as 2 ^ i
      self.output[current_state] |= (1 << i)

    # If there is no other transition from root, it should transition to root itself
    # Hence, it's state will be 0
    for char_num in range(self.max_chars):
      if self.trie[0][char_num] == -1:
        self.trie[0][char_num] = 0

    # Number of states in the trie (will be <= max states)
    self.state_count = state

  def build_failure_links(self):
    queue = []

    # All the states at depth 1 will fail to state 0
    for char_num in range(self.max_chars):
      state = self.trie[0][char_num]
      if state > 0:
        self.fail[state] = 0
        queue.append(state)

    while queue:
      state = queue.pop(0)

      for char_num in range(self.max_chars):
        current_state = self.trie[state][char_num]
        if current_state == -1:
          continue

        # Find the longest proper suffix that matches a prefix
        # Start the search from the parent node & its neighbors
        # Essentially, search in the children of parent of parent node
        # Using fail states reduces the number of iterations required
        parent_state = self.fail[state]
        while self.trie[parent_state][char_num] == -1:
          parent_state = self.fail[parent_state]

        fail_state = self.trie[parent_state][char_num]
        self.fail[current_state] = fail_state
        # Merge output values
        self.output[current_state] |= self.output[fail_state]

        queue.append(current_state)

  def find_next_state(self, current_state, next_input):
    char_num = ord(next_input) - ASCII_OF_A
    next_parent_state = current_state

    while self.trie[next_parent_state][char_num] == -1:
      next_parent_state = self.fail[next_parent_state]

    return self.trie[next_parent_state][char_num]

  def search_words(self, text):
    text = text.lower()
    current_state = 0
    result = defaultdict(list)

    for i in range(len(text)):
      current_state = self.find_next_state(current_state, text[i])

      if self.output[current_state] == 0:
        continue

      for j in range(len(self.words)):
        # Check if output contains the current word in the form of 2 ^ j
        if (self.output[current_state] & (1 << j)) > 0:
          word = self.words[j]
          result[word].append(i - len(word) + 1)

    return dict(result)

test_class(AhoCorasick, examples)

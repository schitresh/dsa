ALPHABET_COUNT = 26

class Node:
  def __init__(self):
    self.next = [None] * ALPHABET_COUNT
    self.is_word = False

class Trie:
  def __init__(self):
    self.root = Node()

  def next_index(self, word, index):
    return ord(word[index].lower()) - ord('a')

  def insert(self, word):
    if not word: return
    temp = self.root

    for position in range(len(word)):
      index = self.next_index(word, position)
      if not temp.next[index]: temp.next[index] = Node()
      temp = temp.next[index]

    temp.is_word = True

  def search(self, word):
    if not word: return
    temp = self.root

    for position in range(len(word)):
      index = self.next_index(word, position)
      if not temp.next[index]: return False
      temp = temp.next[index]

    return True if temp.is_word else False

  def remove(self, word):
    if not word: return
    self.remove_from_node(self.root, word, 0)

  def remove_from_node(self, root, word, position):
    if not root: return

    if position == len(word):
      if any(root.next):
        root.is_word = False
        return
      return True

    index = self.next_index(word, position)
    delete = self.remove_from_node(root.next[index], word, position + 1)

    if delete:
      del root.next[index]
      root.next[index] = None
      if not root.is_word: return True

def test():
  trie = Trie()
  trie.insert('abc')
  trie.insert('abcdef')
  trie.insert('xyz')

  print('ab', trie.search('ab'))
  print('abcd', trie.search('abcd'))
  print('abc', trie.search('abc'))
  print('Remove abc', trie.remove('abc'))
  print('abc', trie.search('abc'))
  print('abcdef', trie.search('abcdef'))
  print('Remove abcdef', trie.remove('abcdef'))
  print('abcdef', trie.search('abcdef'))

test()

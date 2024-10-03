from collections import defaultdict
from queue import PriorityQueue
from utils import test_class

# To decode the encoded data we require the Huffman tree
# Iterate through the binary encoded data
# To find character corresponding to current bits, use these steps:
# 1. Start from the root and do the following until a leaf is found
# 2. If the current bit is 0, move to the left node of the tree
# 3. If the bit is 1, move to right node of the tree
# 4. On reaching a leaf node, print the character of that particular leaf node
#    and continue the iteration of the encoded data

examples = [
  {
    'input': ['geeksforgeeks'],
    'output': 'geeksforgeeks',
  },
  {
    'input': ['heeeeellllllloooooo'],
    'output': 'heeeeellllllloooooo',
  },
]

class Node:
  def __init__(self, symbol, freq, left = None, right = None):
    self.symbol = symbol
    self.freq = freq
    self.left = left
    self.right = right
    # Tree direction, 0 for left & 1 for right
    self.huff = ''

  def __lt__(self, next_node):
    return self.freq < next_node.freq

# Time Complexity: O(n * log(n))
# Auxiliary Space: O(n)
class Solution:
  def solve(self, string):
    char_freq = self.calculate_freq(string)
    huff_tree = self.huff_tree(char_freq)
    huff_code = self.huff_code(huff_tree)
    encoded_string = self.encode_string(string, huff_code)
    decoded_string = self.decode_string(encoded_string, huff_tree)

    print(huff_code)
    print(encoded_string)
    return decoded_string


  def encode_string(self, string, huff_code):
    encoded_string = ''
    for char in string:
      encoded_string += huff_code[char]

    return encoded_string

  def decode_string(self, encoded_string, huff_tree):
    decoded_string = ''
    curr = huff_tree

    for char in encoded_string:
      if char == '0':
        curr = curr.left
      else:
        curr = curr.right

      if not curr.left and not curr.right:
        decoded_string += curr.symbol
        curr = huff_tree

    return decoded_string

  def calculate_freq(self, string):
    freq = defaultdict(int)

    for char in string:
      freq[char] += 1

    return freq

  def huff_tree(self, char_freq):
    heap = PriorityQueue()

    for char, freq  in char_freq.items():
      node = Node(char, freq)
      heap.put(node)

    while heap.qsize() > 1:
      left = heap.get()
      right = heap.get()

      # Assign directional value, 0 for left & 1 for right
      left.huff = '0'
      right.huff = '1'

      new_symbol = left.symbol + right.symbol
      new_freq = left.freq + right.freq
      new_node = Node(new_symbol, new_freq, left, right)
      heap.put(new_node)

    head = heap.get()
    return head

  def huff_code(self, huff_tree):
    huff_code = {}
    self.huff_code_for_node(huff_tree, huff_code)
    return huff_code

  def huff_code_for_node(self, node, huff_code, val = ''):
    # Huffman code for current node
    new_val = val + node.huff

    # If the node is not a leaf node, traverse inside it
    if node.left:
      self.huff_code_for_node(node.left, huff_code, new_val)

    if node.right:
      self.huff_code_for_node(node.right, huff_code, new_val)

    # Display huffman code only for leave nodes
    if not node.left and not node.right:
      huff_code[node.symbol] = new_val

test_class(Solution, examples)

from queue import PriorityQueue
from utils import test_class

# Huffman coding is a lossless data compression algorithm
# The idea is to assign variable-length codes to input characters
# where lengths of the codes are based on the frequencies of the corresponding chars
# These codes (bit sequences) are called prefix codes because they are assigned
# in such a way that the code assigned to one character
# is not the prefix of code assigned to any other character
# This ensures that there is no ambiguity when decoding the generated bitstream

# Let us understand prefix codes with a counter example
# Let there be four characters a, b, c and d
# and their corresponding variable length codes be 00, 01, 0 and 1
# This coding leads to ambiguity because code assigned to c
# is the prefix of codes assigned to a and b
# If the compressed bit stream is 0001,
# the de-compressed output may be 'cccd' or 'ccb' or 'acd' or 'ab'

# There are mainly two major parts in Huffman Coding
# 1. Build a Huffman Tree from input characters
# 2. Traverse the Huffman Tree and assign codes to characters

# Steps to build Huffman Tree
# Input is an array of unique chars along with their frequency of occurences
# 1. Create a leaf node for each unique char and build a min heap of all leaf nodes
#    Use the frequency field to compare two nodes in min heap
# 2. Extract two nodes with the minimum frequency from the min heap
# 3. Create a new internal node with frequency as the sum of the freq of the two nodes
#    Make the first extracted node as its left child and the other one as right child
#    Add this node to min heap
# 4. Repeat steps 2 & 3 until the heap contains only one node

examples = [
  {
    'input': [{'a': 5, 'b': 9, 'c': 12, 'd': 13, 'e': 16, 'f': 45}],
    'output': {'f': '0', 'c': '100', 'd': '101', 'a': '1100', 'b': '1101', 'e': '111'},
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
  def solve(self, chars_freq):
    huff_tree = self.huff_tree(chars_freq)

    return self.huff_code(huff_tree)

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

    return heap

  def huff_code(self, huff_tree):
    head = huff_tree.get()
    huff_code = {}
    self.huff_code_for_node(head, huff_code)
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

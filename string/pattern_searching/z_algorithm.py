from utils import test

examples = [
  {
    'input': ['ababaaaaaba', 'aba'],
    'output': [0, 2, 8]
  }
]

# Time Complexity: O(n + m)
# Space Complexity: O(m)
class Solution:
  def z_array(self, text):
    array = [0] * len(text)
    left = 0
    right = 0

    def match_from_right(current_right):
      right = current_right

      while right < len(text) and text[right - left] == text[right]:
        right += 1

      # Subtract 1 since the last character didnt' match
      right -= 1
      array[i] = right - left + 1

    for i in range(1, len(text)):
      if i > right:
        left = i
        right = i
        match_from_right(right)
      else:
        matched_till = i - left

        if array[matched_till] < right - i + 1:
          array[i] = array[matched_till]
        else:
          left = i
          match_from_right(right)

    return array

  def solve(self, text, key):
    indices = []
    text_and_key = key + '$' + text
    z_array = self.z_array(text_and_key)

    for i in range(len(key), len(z_array)):
      if z_array[i] == len(key):
        indices.append(i - len(key) - 1)

    return indices

test(Solution, examples)

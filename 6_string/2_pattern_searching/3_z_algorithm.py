from utils import test_class

examples = [
  {
    'input': ['ababaaaaaba', 'aba'],
    'output': [0, 2, 8]
  }
]

# Calculate maximum suffix that matches a prefix for the starting index (Z-box)
# For the next index, check if it falls in Z-box. If yes, check if there is a partial match.
# If index is out of Z-box, re-calculate the Z-box (i.e. linear match again)
# If there is total match, it's possible that the next chars outside Z-box might match, so re-calculate Z-box

# Time Complexity: O(n + m)
# Auxiliary Space: O(m)
class ZAlgorithm:
  def z_array(self, text):
    array = [0] * len(text)
    # Left and right indexes of Z-box
    # Z-box is the last max suffix that matched a prefix using linear matching
    left = 0
    right = 0

    def linear_match(current_right):
      right = current_right

      while right < len(text) and text[right - left] == text[right]:
        right += 1

      # Subtract 1 since the last character didn't match
      right -= 1
      array[i] = right - left + 1

    for i in range(1, len(text)):
      # If i is not within Z-box, do a linear match and hence re-calculate Z-box
      if right < i:
        left = i
        right = i
        linear_match(right)
      else:
        # Length of current suffix in Z-box = i - left + 1
        # Index of corresponding prefix (starts from 0th index) = i - left
        earlier_matched_length = array[i - left]
        remaining_box_length = right - i + 1

        # If the earlier matched length is equal to remaining box length,
        # then it's possible that the next chars (outside the Z-box) may also match in current iteration
        # So, do a linear match and re-calculate Z-box
        if earlier_matched_length < remaining_box_length:
          array[i] = earlier_matched_length
        else:
          left = i
          linear_match(right)

    return array

  def solve(self, text, key):
    indices = []
    text_and_key = key + '$' + text
    z_array = self.z_array(text_and_key)

    for i in range(len(key), len(z_array)):
      if z_array[i] == len(key):
        indices.append(i - len(key) - 1)

    return indices

test_class(ZAlgorithm, examples)

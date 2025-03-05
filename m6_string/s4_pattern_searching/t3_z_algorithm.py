from utils import test_class

examples = [
  {
    'input': ['ababaaaaaba', 'aba'],
    'output': [0, 2, 8]
  }
]

# Z Array
# Z[i] stores length of the longest substring from string[i]
# which is also a prefix of the string

# Calculating Z Array
# For the starting index, calculate Z-box using linear match
# Z-box is the last maximum suffix that matched a prefix
# For the next index, check if it falls in Z-box
# If it does, check if there is a partial match, else re-calculate the Z-box
# If there is total match, it's possible that the next chars outside Z-box might match
# so re-calculate Z-box

# Z algorithm
# Concatenate pattern and text like pattern$text and build its Z array
# If Z value is equal to pattern length, then the pattern is present
# Because pattern is the prefix here and Z value give length of the matching prefix

# Time Complexity: O(n + m)
# Auxiliary Space: O(m)
class ZAlgorithm:
  def z_array(self, text):
    array = [0] * len(text)
    # Left and right indexes of Z-box
    # Z-box is the last max suffix that matched a prefix (using linear matching)
    left = 0
    right = 0

    def recompute_z_box():
      nonlocal left, right
      # Length of z box is right - left + 1
      # so the current index of the prefix will be right - left
      while right < len(text) and text[right - left] == text[right]:
        right += 1

      # Subtract 1 since the last character didn't match
      right -= 1

    for i in range(1, len(text)):
      # If i is not within Z-box, simply re-calculate the Z-box
      if i > right:
        left = i
        right = i
        recompute_z_box()
        array[i] = right - left + 1
      # If i is within Z-box, it means i is within substring that matches prefix
      # And we've already calculated Z value of the corresponding substring in the prefix
      # But if the earlier matched length is equal to or greater than
      # the remaining Z-box length, then it's possible that the next chars
      # outside the Z-box may also match
      else:
        # Length of current suffix in Z-box = i - left + 1
        # Index of corresponding prefix (starting from index 0) = i - left
        earlier_matched_length = array[i - left]
        remaining_box_length = right - i + 1

        # If earlier matched length is less, than the rest of the substring won't match
        # Hence, z value will be same as the previous one
        if earlier_matched_length < remaining_box_length:
          array[i] = earlier_matched_length
        # If earlier matched length is equal or more, recompute z box
        # to check if the next chars outside the current z box match
        else:
          left = i
          recompute_z_box()
          array[i] = right - left + 1

    return array

  def solve(self, text, key):
    indices = []
    text_and_key = key + '$' + text
    z_array = self.z_array(text_and_key)

    # Since pattern is prefixed in the calculated z array of text and key
    # Start checking after pattern's length
    for i in range(len(key), len(z_array)):
      if z_array[i] == len(key):
        indices.append(i - len(key) - 1)

    return indices

test_class(ZAlgorithm, examples)

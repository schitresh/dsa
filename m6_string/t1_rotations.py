from utils import test_class

# Generate all rotations

examples = [
  {
    'input': ['abcd'],
    'output': ['abcd', 'bcda', 'cdab', 'dabc']
  }
]

# Iterate through the string
# For each iteration, copy chars from the index till it reaches the index again
# Time Complexity: O(n^2)
# Auxiliary Space: O(n)
class Solution:
  def solve(self, string):
    output = []

    for i in range(len(string)):
      j = i
      rotated_string = []

      for _ in range(len(string)):
        rotated_string.append(string[j])
        j = (j + 1) % len(string)

      output.append(''.join(rotated_string))

    return output

test_class(Solution, examples)

# Concat string with itself and create all the substrings
# Time Complexity: O(n^2)
# Auxiliary Space: O(n)
class Solution2:
  def solve(self, string):
    output = []
    temp = string + string

    for i in range(len(string)):
      output.append(temp[i : i + len(string)])

    return output

test_class(Solution2, examples)

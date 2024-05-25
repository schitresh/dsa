from utils import test_class

# Generate all rotations
examples = [
  {
    'input': ['abcd'],
    'output': ['abcd', 'bcda', 'cdab', 'dabc']
  }
]

# Time Complexity: O(n^2)
# Space Complexity: O(n)
class Solution:
  def solve(self, string):
    output = []

    for i in range(len(string)):
      j = i
      k = 0
      rotated_string = [0] * len(string)

      while k < len(string):
        rotated_string[k] = string[j]
        j = (j + 1) % len(string)
        k += 1

      output.append(''.join(rotated_string))

    return output

# Time Complexity: O(n^2)
# Space Complexity: O(n)
class Solution2:
  def solve(self, string):
    output = []
    temp = string + string

    for i in range(len(string)):
      output.append(temp[i : i + len(string)])

    return output

test_class(Solution, examples)
test_class(Solution2, examples)

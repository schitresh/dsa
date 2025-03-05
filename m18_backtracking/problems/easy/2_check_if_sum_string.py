from utils import test_class

# Given a string of digits, determine whether it is a sum-string. A string is called a
# sum-string if the rightmost substring can be written as the sum of two substrings
# before it and the same is recursively true for substrings before it.

examples = [
  {
    'input': ['12243660'],
    'output': True, # 12 + 24 = 36, 24 + 36 = 60
  },
  {
    'input': ['1111112223'],
    'output': True, # 1 + 111 = 112, 111 + 112 = 223
  },
  {
    'input': ['2368'],
    'output': False,
  },
  {
    'input': ['12243661'],
    'output': False,
  },
]

# Backtracking
# Time Complexity: O(n^2 * 3^n)
# Auxiliary Space: O(n), due to recursive stack
class Solution:
  def solve(self, string):
    self.string = string
    return self.sum_string(0, 1, 2)

  def sum_string(self, index1, index2, index3):
    if index1 == index2 or index1 == index3 or index2 == index3:
      return False

    length = len(self.string)
    if index1 == length or index2 == length or index3 == length:
      return False

    num1 = int(self.string[index1 : index2])
    num2 = int(self.string[index2 : index3])

    for i in range(index3, len(self.string)):
      num3 = int(self.string[index3 : i + 1])

      if num1 + num2 == num3:
        if i + 1 == len(self.string): return True
        return self.sum_string(index2, index3, i + 1)

    r1 = self.sum_string(index1 + 1, index2, index3)
    r2 = self.sum_string(index1, index2 + 1, index3)
    r3 = self.sum_string(index1, index2, index3 + 1)

    return r1 or r2 or r3

test_class(Solution, examples)

# Backtracking
# Time Complexity: O(n * 3^n)
# Auxiliary Space: O(n), due to recursive stack
class Solution2:
  def solve(self, string):
    self.string = string
    return self.sum_string(0, 1, 2)

  def sum_string(self, index1, index2, index3):
    if index1 == index2 or index1 == index3 or index2 == index3:
      return False

    length = len(self.string)
    if index1 == length or index2 == length or index3 == length:
      return False

    num1 = int(self.string[index1 : index2])
    num2 = int(self.string[index2 : index3])
    num = num1 + num2

    num_len = len(str(num))
    # Subtract 1 because num3 will start with index3
    end_index = index3 + num_len - 1
    if end_index > length - 1: return False

    num3 = int(self.string[index3 : end_index + 1])
    if num == num3:
      if end_index == length - 1: return True
      return self.sum_string(index2, index3, end_index + 1)

    r1 = self.sum_string(index1 + 1, index2, index3)
    r2 = self.sum_string(index1, index2 + 1, index3)
    r3 = self.sum_string(index1, index2, index3 + 1)

    return r1 or r2 or r3

test_class(Solution2, examples)

# Time Complexity: O(n^3)
# Auxiliary Space: O(n)
class Solution3:
  def solve(self, string):
    self.string = string

    for i in range(1, len(string) - 1):
      for j in range(i + 1, len(string)):
        if self.sum_string(0, i, j): return True

    return False

  def sum_string(self, index1, index2, index3):
    num1 = self.string[index1 : index2]
    num2 = self.string[index2 : index3]
    num = self.sum_string_num(num1, num2)

    num_len = len(num)
    # Subtract 1 because num3 will start with index3
    end_index = index3 + num_len - 1

    if end_index > len(self.string) - 1:
      return False

    num3 = self.string[index3 : end_index + 1]
    if num == num3:
      if end_index == len(self.string) - 1: return True
      return self.sum_string(index2, index3, end_index + 1)

    return False

  # Required if numbers are large and will overflow
  def sum_string_num(self, str1, str2):
    if len(str1) < len(str2):
      str1, str2 = str2, str1

    m = len(str1)
    n = len(str2)
    ans = ''
    carry = 0

    for i in range(n):
      digit1 = ord(str1[m - 1 - i]) - ord('0')
      digit2 = ord(str2[n - 1 - i]) - ord('0')

      curr_sum = digit1 + digit2 + carry
      curr_digit = curr_sum % 10
      carry = curr_sum // 10

      ans = str(curr_digit) + ans

    # Required to add the carry to remaining str1
    for i in range(n, m):
      digit1 = ord(str1[m - 1 - i]) - ord('0')

      curr_sum = digit1 + carry
      curr_digit = curr_sum % 10
      carry = curr_sum // 10

      ans = str(curr_digit) + ans

    if carry:
      ans = str(carry) + ans

    return ans

test_class(Solution3, examples)

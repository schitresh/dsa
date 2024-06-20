from utils import test_method

# Calculate x^n or x ** n or pow(x, n) using divide and conquer
# Brute force approach is to iterate or recurse over n and keep multipying x
# Time complexity of that is O(n)
examples = [
  {
    'input': [2, 3],
    'output': 8
  },
  {
    'input': [3, 4],
    'output': 81
  },
]

# Time Complexity: O(log(n))
# Auxiliary Space: O(log(n)) for recursive stack
def power(x, n):
  if n == 0:
    return 1

  half_power = power(x, n // 2)
  result = half_power * half_power

  if n % 2 == 1:
    result *= x

  return result

# Time Complexity: O(log(n))
# Auxiliary Space: O(1)
def power2(x, n):
  result = 1

  while n > 0:
    if n % 2 == 0:
      x *= x
      n /= 2
    else:
      result *= x
      n -= 1

  return result

test_method(power, examples)
test_method(power2, examples)

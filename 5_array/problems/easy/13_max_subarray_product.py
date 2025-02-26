from utils import test_class

# Given an array, find the subarray that has the maximum product and return its product.

examples = [
  {
    'input': [[-2, 6, -3, -10, 0, 2]],
    'output': 180,
  },
  {
    'input': [[-1, -3, -10, 0, 60]],
    'output': 60,
  },
  {
    'input': [[2, 3, -2, 6, -3, -10, 2]],
    'output': 360,
  },
  {
    'input': [[-10]],
    'output': -10,
  },
  {
    'input': [[-1, -2, -3, -4]],
    'output': 24,
  },
]

# Naive Approach: For each subarray, calculate the product
# Time Complexity: O(n ^ 2)
# Auxiliary Space: O(1)

# Track Max & Min Product
# If the array has only positive elements, then simply iterate keeping track of the
# maximum running product at every index. If we encounter zero, then all the subarrays
# containing this zero will have product = 0, so zero simply resets the product of the
# subarray.
# If there are negative numbers, we need to keep track of the minimum product as well as
# the maximum product ending at the previous index. This is because when we multiply the
# minimum product with a negative number, it can give us the maximum product.
# Time Complexity: O(n)
# Auxiliary Space: O(1)
class Solution:
  def solve(self, array):
    global_max = array[0]
    min_product = array[0]
    max_product = array[0]

    for i in range(1, len(array)):
      num = array[i]
      temp_min_product = min_product * num
      temp_max_product = max_product * num

      min_product = min(num, temp_min_product, temp_max_product)
      max_product = max(num, temp_min_product, temp_max_product)

      global_max = max(global_max, max_product)

    return global_max

test_class(Solution, examples)

# Traverse in both directions
# Traverse from the start and keep track of the running product. If the running product
# is greater than the max product, then update the max product. If we encounter 0, then
# make the running product 1 for the new subarray from next element.
# But what is the problem with this approach?
# But there will be a problem if the array contains odd number of negative elements.
# In that case, we have to reject one negative element so that we can even the negative
# elements to get positive product. Since subarray should be contiguous, we can’t simply
# reject any one negative element. We have to either reject the first negative element or
# the last negative element.
# If we traverse from start then only the last negative element can be rejected and if we
# traverse from the last then the first negative element can be rejected. So we will
# traverse from both ends and find the maximum product subarray.
# Time Complexity: O(n)
# Auxiliary Space: O(1)
class Solution2:
  def solve(self, array):
    max_product = array[0]
    left_product = 1
    right_product = 1

    for i in range(len(array)):
      if left_product == 0: left_product = 1
      if right_product == 0: right_product = 1

      left_product *= array[i]

      j = len(array) - 1 - i
      right_product *= array[j]

      max_product = max(max_product, left_product, right_product)

    return max_product

test_class(Solution2, examples)

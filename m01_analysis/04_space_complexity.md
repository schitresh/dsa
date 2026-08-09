## Auxiliary Space
- Auxiliary Space
  - The extra space that is taken by an algorithm temporarily to finish its work
- Space Complexity
  - Total space taken by the algorithm with respect to the input size
  - Plus the auxiliary space that the algorithm uses

### Example
- Consider a method that calculates the sum of the elements of an array
- Variables used and their complexity
  - Array: O(n)
  - Sum: O(1)
- Auxiliary space: O(1)
- Space complexity: O(n) + O(1) = O(n)

## Recursion
- Each call to a recursive function adds a new level to the stack
  - It maintains a record on the activation stack and takes up memory
  - It holds a copy of the variables
- Examples (auxiliary space):
  - Recursive binary search: O(log(n))
    - Space required for variables
    - Array can be passed as reference
  - Merge sort: O(n)
    - Temporary array is stored in each iteration to merge the elements
    - Although each call to merge sort triggers two recursive calls
      - Only one of those is performed at a time
      - And the additional array has elements at the lowest level only
      - That is during merging up
  - Quick sort: O(log(n))

```py
# This recursive function will take O(n) auxiliary space
# It holds a copy of the variable n for each call on the stack
def factorial(n):
  if (n == 0): return 1
  return n * factorial(n - 1)

# This iterative function will take O(1) auxiliary space
# No matter how large n becomes
# It will always use three variables (n, result, i)
def factorial(n):
  result = 1
  for i in range(1, n + 1):
    n *= i
  return result
```

## Recursion
- The process in which function calls itself directly or indirectly
  - Allows a function to break down a problem into smaller subproblems
  - Which are then solved recursively
- A base case terminates the recursion
  - Can lead to stack overflow if not used properly
  - Happens if the base case is not reached or not defined
- Works by creating a stack of function calls
  - When a function calls itself
    - A new instance of the function is created with a local copy of variables
    - This instance is pushed into the stack
  - This process continues until a base case is reached that stops the recursion
  - After that, the function calls start popping off the stack returning their results

## Types (Calling Behavior)
- Direct Recursion
  - Method calls itself directly
- Indirect Recursion
  - Involves two or more methods that eventually create a circular call sequence
  - A method calls another method which again calls the first method

# Types (Control Flow)
- Non-Tail Recursion
  - The recursive call is not the last statement
  - Stack frame needs to track till where the program has executed
    - When the function call was made so as continue from where it left off
- Tail recursion
  - The recursive call is the last statement
  - Considered better than non-tail recursion
    - There is nothing left to compute in the current frame
    - This allows the modern langauges to remove the stack of current frame
    - Reducing the stack depth (max amount of stack space used at any time)
    - The stack frame is replaced by the one for the recursive call
  - Tail call elimination
    - Removing a tail call to make the recursion a tail recursion
    - So that we can benefit from the space optimization of stack

```py
# Non-Tail Recursion
def factorial(n):
  if n == 0: return 1
  # The returned value from the recursive call is being used
  # and not the last thing done
  return n * factorial(n - 1)

# Tail Recursion
def factorial(n, answer):
  if n <= 1: return answer
  return factorial(n - 1, n * answer)
```

## Application
- Tree and graph traversal using dfs and bfs
- Divide and conquer
- Backtracking
- Dynamic programming
- Combinatorics

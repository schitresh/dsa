## Recursion
- Process in which function calls itself directly or indirectly
- This allows a function to break down a problem into smaller subproblems
  - Which are then solved recursively
- Works by creating a stack of function calls
  - When a function calls itself
    - A new instance of the function is created and pushed into the stack
  - This process continues until a base case is reached that stops the recursion
  - After that, the function calls start popping off the stack returning their results
- Can lead to stack overflow if not used properly
  - Happens if the base case is not reached or not defined

## Types
- Direct recursion
  - Method calls itself directly
- In-direct recursion
  - Involves two or more methods that eventually create a circular call sequence
  - Method calls another method which again calls the first method
- Head recursion
  - The recursive call is made at the beginning of the method
- Tail recursion
  - The recursive call is the last statement
  - It is better than non-tail recursion
    - Because there is nothing left to compute in the current frame
    - The modern langauges can remove the stack of current frame
  - Tail call elimination
    - Removing a tail call to make the recursion a tail recursion
    - So that we can benefit from the space optimization of stack

## Application
- Tree and graph traversal using dfs and bfs
- Divide and conquer
- Backtracking
- Dynamic programming
- Combinatorics

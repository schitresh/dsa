## Backtracking
- Explores different options or paths to find the best solution
  - It involves trying different options
  - And undoing them if they lead to a dead end
- When a dead end is reached
  - The algorithm backtracks to the previous decision point
  - And explores a different path
  - Until a solution is found or all possibilities have been exhausted
- Since backtracking algorithm is purely brute force
  - It performs very poorly in time complexity
  - Generally has exponential or factorial complexity
- Applications
  - Searching a path in a maze
  - Solving puzzles like sudoku
  - Creating smart bots to play board games like chess
  - Network routing and congestion control

## Terminologies
- Candidate: Potential choice or element that can be added to the current solution
- Solution: Valid and complete configuration that satisfies all problem constraints
- Partial Solution: Intermediate configuration being constructed during the process
- Feasible Solution: Partial or complete solution that adheres to all contraints
- Decision Point: Specific step where a candidate is chosen and added to the partial solution
- Decision Space: Set of all possible candidates or choices at each decision point
- Dead End: When a partial solution cannot be extended without violating constraints
- Backtrack: Undoing previous decisions and returning to a prior decision point
- Search Space: All possible combinations of candidates and choices
- Optimal Solution: Best possible solution

## Types of Problems
- Decision Problems: We search for a feasible solution
- Optimization Problems: We search for the best solution
- Enumeration Problems: We find set of all possible feasible solutions

## How Backtracking Works
- Imagine a tree with the initial state as the root node
  - The recursion call starts at the initial state to find a valid solution
- It has different checkpoints as nodes
  - These checkpoints can further have another set of checkpoints
  - At each checkpoint, the program makes some decisions and move to other checkpoints
- The leaf nodes are terminal nodes where no further recursive calls can be made
  - These nodes act as base case of recursion
  - And it is determined if the current solution is valid or not

## Example
- There are many problems that can be solved using greedy or DP in better time
  - This is because backtracking is purely brute force
  - Generally it takes exponential or factorial time
  - But many problems exists that can be solved only using backtracking
- Imagine there are 3 closed boxes, among which 2 are empty and 1 has a gold coin
  - The task is to get the gold coin
- Why dynamic programming fails to solve this question
  - Does opening or closing one box has any effect on the other box?
  - No, each and every box is independent of each other
  - Opening or closing of one box cannot determine the transition for other boxes
- Why greedy fails to solve this question
  - Greedy algorithm chooses a local maxima in order to get global maxima
  - But in this problem each and every box has equal probability of having a gold coin
  - Hence, there is no criteria to make a greedy choice
- Why Backtracking works
  - Backtracking algorithm is simply brute forcing each and every choice
  - Hence we can one by one choose every box to find the gold coin
  - If a box is found empty we can close it back as a backtracking step

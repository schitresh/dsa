## Backtracking
- Explores different options or paths to find the best solution
- If one doesn't work, backtracks and tries another until the right one is found
- Like searching a path in a maze or solving puzzles like sudoku
  - Creating smart bots to play board games like chess
  - Network routing and congestion control
- Since backtracking algorithm is purely brute force
  - It performs very poorly in time complexity
  - Generally has exponential or factorial complexity

## Terminologies
- Candidate: Potential choice or element that can be added to the current solution
- Partial Solution: Intermediate configuration being constructed
- Feasible Solution: Partial or complete solution that adheres to all contraints
- Decision Point: Specific step where a candidate is chosen and added to the partial solution
- Decision Space: Set of all possible candidates or choices at each decision point
- Dead End: When a partial solution cannot be extended without violating constraints
- Backtrack: Undoing previous decisions and returning to a prior decision point
- Search Space: All possible combinations of candidates and choices
- Optimal Solution: Best possible solution

## Example
- Imagine there are 3 closed boxes, among which 2 are empty and 1 has a gold coin
  - The task is to get the gold coin
- Why dynamic programming fails to solve this question
  - Does opening or closing one box has any effect on the other box?
  - No, each and every box is independent of each other
  - Opening or closing of one box can not determine the transition for other boxes
- Why greedy fails to solve this question
  - Greedy algorithm chooses a local maxima in order to get global maxima
  - But in this problem each and every box has equal probability of having a gold coin
  - Hence, there is no criteria to make a greedy choice
- Why Backtracking works
  - Backtracking algorithm is simply brute forcing each and every choice
  - Hence we can one by one choose every box to find the gold coin
  - If a box is found empty we can close it back as a backtracking step

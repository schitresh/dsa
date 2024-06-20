## Greedy Algorithm
- Makes the best local choice at each step
  - In the hope of finding the global optimum solution
- Prioritizes immediate benefits over long-term consequences
  - Making decisions based on the current situation
  - Without considering future implications
- Not all problems are suitable for greedy algorithm
  - They work best when the problem exhibits these properties
  - Greedy choice property
    - The optimal solution can be constructed by making the best local choice at each step
  - Optimal substructure
    - The solution to the problem contains the optimal solutions to its subproblems

## Example
- Let's say we have a set of coins with values 1, 2, 4, 10, 20, 50, 100
- We need to give minimum number of coin to make up the amount 36
- Start with the largest coin less than or equal to the amount
  - That is 20, leaving 36 - 20 = 16
- Repeat this step until the remaining amount becomes 0
  - So we can choose 10, then 5, then 1

## Applications
- Find min coins to make a given amount of change
- Dijkstra's algorithm to find the shortest path
- Kruskal's minimum spanning tree algorithm
- Fractional knapsack to determine the most valuable items to carry in a knapsack
- Activity selection problem to choose max non-overlappinig activities
- Huffman coding to construct a binary code with min length of chars
-

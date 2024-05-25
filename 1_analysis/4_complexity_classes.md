## Complexity Classes
- In computer science, there exist some problems whose solutions are not yet found
- These problems are divided into classes known as complexity classes

## P Class
- P stands for polynomial time
- Collection of decision problems
  - That can be solved by a deterministic machine in polynomial time
- Solvable and tractable
  - Tractable means the problems can be solved in theory as well as in practice
- Problems
  - Greatest common divisor
  - Merge sort

## NP Class
- Non-deterministic Polynomial time
- 'Yes' answers can be checked in polynomial time
- Solutions are hard to find since they are being solved by a non-deterministic machine
  - But solutions are easy to verify
  - Verified by a turing machine in polynomial time
- Example
  - There are 200 rooms available for 1000 employees
  - But some of the employees don't want to work in the same room
  - Easy to verify but hard to find the solution from scratch
- Problems
  - Boolean satisfiability problem
  - Hamiltonian path
  - Graph coloring

## Co-NP Class
- Complement of NP Class
- 'No' answers can be checked in polynomial time
- If the answer to a problem in Co-NP is 'no'
  - Then there is proof that can be checked in polynomial time
- For NP and Co-NP problem, there is no need to verify all the answers at once
  - There is a need to verify only one particular answer 'yes' or 'no' in polynomial time
- Problems
  - Check prime number
  - integer factorization

## NP-hard Class
- At least as hard as the hardest problem in NP
  - All NP-hard problems are not in NP
- It takes a long time to check a given solution
- Problems
  - Halting problem
  - Qualified boolean formulas
  - No hamiltonian cycle

## NP-complete Class
- If it is both NP and NP-hard
  - NP-complete problems are the hard problems in NP
- Problems
  - Hamiltonian cycle
  - Satisfiability
  - Vertex cover
  - Travelling Salesman Problem
  - Knapsack Problem
  - Longest Path Problem

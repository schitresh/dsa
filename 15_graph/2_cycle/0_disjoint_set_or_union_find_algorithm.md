## Disjoint Set (Union Find Algorithm)
- Two sets are called disjoint sets if they don't have any element in common
- That is, the intersection of them is null set

## Example
- Given a number of persons, we need to able to perform these tasks
  - Add a new friendship relation
  - Find whether a person is a friend of another persion, directly or indirectly
- Let's say we have 10 persons: a, b, c, d, e, f, g, h, i, j
  - We need to add these relationships
    - (a, b), (b, d), (c, f), (c, i), (j, e), (g, j)
- We can create four groups of friends like
  - G1: { a, b, d }
  - G2: { c, f, i }
  - G3: { e, g, j }
  - G4: { h }
- Now we can easily find if persons x and y are friends or not
- To create such sets
  - Start with individual sets for each element
  - Iterate through the relationships, and create union set of the related sets
  - Select a member in each set as representative
    - A simple way is to select the one with the biggest index

## Data Structure
- Array
  - A parent array is used, where parent[i] is the parent of ith item
  - These relationships create one or more virtual trees
- Tree
  - If two elements are in the same tree, then they are in the same disjoint set
  - The root node of each tree is called representative of the set
    - Each set has a single unique representative
  - If i is the representative of the set, then parent[i] will be equal to i
    - Else the representative can be found by traveling up the tree
- To find if two persons are in the same set
  - We can find the representatives of the sets of both the persons
  - If the representatives are the same, then the two persons are in the same set

## Naive Approach
```py
class DisjointSet:
  def __init__(self, size):
    self.size = size
    self.parent = [i for i in range(size)]

  # Find the representative of the set that a person belongs to
  # Time Complexity: O(n)
  def find(self, item):
    parent = self.parent[item]
    if parent == item: return item

    return self.find(parent)

  # Create union set for the related persons i & j
  # Time Complexity: O(n)
  def union(self, i_item, j_item):
    i_rep = self.find(i_item)
    j_rep = self.find(j_item)

    # Move all of i's set into j's set
    parent[i_rep] = j_rep
```

## Find by Path Compression
```py
class DisjointSet:
  def __init__(self, size):
    self.size = size
    self.parent = [i for i in range(size)]

  # Find the representative of the set that a person belongs to
  # Using Path Compression
  # Time Complexity: O(log(n))
  def find(self, item):
    parent = self.parent[item]
    if parent == item: return item

    rep = self.find(parent)
    # Cache the result by moving item directly under the representative of the set
    parent[item] = rep
    return rep
```

## Union By Rank
```py
class DisjointSet:
  def __init__(self, size):
    self.size = size
    self.parent = [i for i in range(size)]
    self.rank = [0] * size

  # Find the representative of the set that a person belongs to
  # Using Path Compression
  # Time Complexity: O(log(n))
  def find(item):
    if self.parent[item] != item:
      self.parent[item] = self.find(self.parent[item])

    return self.parent[item]

  # Create union set for the related persons i & j
  # Using Rank
  # Requires a rank array with size equal to parent array
  # rank[i] is the height of the tree representing the set
  # Time Complexity: O(log(n))
  def union(i_item, j_item):
    i_rep = self.find(i_item)
    j_rep = self.find(j_item)

    if i_rep == j_rep: return

    i_rank = self.rank[i_rep]
    j_rank = self.rank[j_rep]

    # If rank of i is less than rank of j, move i under j
    # Because that won't change the rank of j
    # While moving j under i will increase the height
    # If the ranks are equal, the rank will always be one greater
    if i_rank < j_rank:
      self.parent[i_rep] = j_rep
    elif i_rank > j_rank:
      self.parent[j_rep] = i_rep
    else:
      self.parent[i_rep] = j_rep
      self.rank[j_rep] += 1
```

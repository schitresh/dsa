## Hash
- Efficiently stores and retrieves data in a way that allows for quick access
  - Enables fast retrieval of data based on its key
- Maps data to a specific index in a hash table (also called hash map)
  - A hash function is used to determine the index
- Trivial hashing (or index mapping)
  - Simple form of hashing where data is directly mapped to an index in hash table
- Used in databases, caching systems, search optimization, network routing

## Hash Collision
- Happens when two different keys map to the same index in the hash table
- Can happen due to
  - Poor hash function that does not distribute keys evenly across the hash table
  - High load factor (ratio of keys to hash table size)
  - Similar keys
- Load factor
  - If there are n entries in hash table
  - And b is the size of array used for chaining at each index
  - Then load factor is n/b

## Collision Resolution Techniques
### Open Addressing
- All elements are stored in hash table itself
- Can lead to clustering
  - That is too many data items after collision fill up the space in hash table
- Types
  - Linear Probing
    - Search for an empty slot sequentially
  - Quadratic Probing
    - Search for an empty slot using a quadratic function
  - Cuckoo Hashing or Double Hashing
    - Using multiple hash functions to distribute keys
    - If there is a collision, the additional hash function is used to calculate an offset

### Closed Addressing
- Elements are stored outside hash table
- Types
  - Separate Chaining
    - Store colliding keys in a linked list at each index
    - Dynamic arrays or binary search tree can also be used

## Python
```py
hash = { 'a': 1, 'b': 2 }
hash = { 1: 'a', 2: 'b' }
hash.get('a') # No error if key not present
hash['a'] # Error if key not present
hash.keys()
hash.values()
hash.items()
```

## Ruby
```rb
hash = { a: 1, b: 2 }
hash = { 1 => 'a', 2 => 'b' }
hash[:a]
hash.keys
hash.values
hash.entries
```

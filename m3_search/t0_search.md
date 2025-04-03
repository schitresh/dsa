## Search
- Some search algorithms like binary search are deterministic
  - Meaning they follow a clear systematic approach
- Other like linear search are non-deterministic
  - They may need to examine the entire search space in the worst case

## Applications
- Information retrieval like search engines
- Database systems to retrieve specific data
- In E-commerce to search preferred products quickly
- Pattern recognition like image recognition, speech recognition
- Recommendation system

## Python
```py
array = [5, 3, 6, 7, 8, 2, 9]
8 in array # True
array.index(8) # 4

string = 'hello world'
'llo' in string # True
string.index('llo') # 2
string.find('llo') # 2
```

## Ruby
```rb
array = [5, 3, 6, 7, 8, 2, 9]
array.include?(8) # True
array.index(8) # 4
array.find { |item| item == 5 }

string = 'hello world'
string.include?('llo') # True
string.index('llo') # 4
```

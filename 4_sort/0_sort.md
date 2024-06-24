## Sorting
- In-place Sorting
  - Uses constant space (modifies the given array only)
  - Examples: selection sort, bubble sort, insertion sort, heap sort
- Internal Sorting
  - When all the data is placed in the main memory or internal memory
  - The problem cannot take input beyond its size
  - Example: selection sort, bubble sort, insertion sort, heap sort, quick sort
- External Sorting
  - When all the data cannot be placed in memory at a time
  - Used for the massive amount of data
  - Examples: merge sort, external radix sort
- Stable sorting
  - When two same elements appears in their original order after sorting
  - Examples: bubble sort, insertion sort, merge sort
- Unstable sorting
  - When two same elements appear in different order after sorting
  - Examples: quick sort, heap sort, shell sort

## Sorting Techniques
- Comparison based: The array elements are compared
  - Examples: selection sort, bubble sort, insertion sort, merge sort, quick sort, heap sort
- Non-comparison based: The array elements are not compared
  - Examples: counting sort, radix sort, bucket sort

## Python
```py
array = [5, 3, 6, 7, 8, 2, 9]
array.sort()
array.sort(key = lambda x: x * 2)
array.sort(reverse = True)
array = sorted(array)
# Same args for key and reverse apply for sorted()

string = 'hello world'
string = ''.join(sorted(string))
```

## Ruby
```rb
array = [5, 3, 6, 7, 8, 2, 9]
array.sort
array.sort!
# <=> is the sorting operator, 0 if x = y, -1 if x < y, 1 if x > y
array.sort { |x, y| x <=> y }

string = 'hello world'
string.chars.sort.join
```

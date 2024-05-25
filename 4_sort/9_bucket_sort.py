from utils import test_class

examples = [
  {
    'input': [[0.897, 0.565, 0.656, 0.1234, 0.665, 0.34346]],
    'output': [0.1234, 0.34346, 0.565, 0.656, 0.665, 0.897]
  }
]

# Time Complexity: O(n + k), where k is no of buckets
## Best Case: O(n + k)
## Worst Case: O(n^2)
# Space Complexity: O(n + k)
class BucketSort:
  def solve(self, array):
    length = len(array)
    bucket = [[] for _ in range(length)]

    def bucket_index(item):
      return int(item * length)

    for item in array:
      bucket[bucket_index(item)].append(item)

    for items in bucket:
      items.sort()

    index = 0
    for items in bucket:
      for item in items:
        array[index] = item
        index += 1

    return array

test_class(BucketSort, examples)

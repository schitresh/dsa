def swap(list, index_1, index_2):
  list[index_1], list[index_2] = list[index_2], list[index_1]

def min_heapify(list, index):
  length = len(list)
  smallest = index
  left = 2 * index
  right = left + 1

  if left < length and list[index] > list[left]: smallest = left
  if right < length and list[smallest] > list[right]: smallest = right

  if smallest != index:
    swap(list, index, smallest)
    min_heapify(list, smallest)

def build_min_heap(list):
  mid = len(list) // 2

  for index in range(mid, -1, -1):
    min_heapify(list, index)

list = [1, 6, 2, 5, 9, 8, 7, 3, 4]
build_min_heap(list)
print(list)

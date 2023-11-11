def swap(list, index_1, index_2):
  list[index_1], list[index_2] = list[index_2], list[index_1]

def max_heapify(list, index):
  length = len(list)
  largest = index
  left = 2 * index
  right = left + 1

  if left < length and list[index] < list[left]: largest = left
  if right < length and list[largest] < list[right]: largest = right

  if largest != index:
    swap(list, index, largest)
    max_heapify(list, largest)

def build_max_heap(list):
  mid = len(list) // 2

  for index in range(mid, -1, -1):
    max_heapify(list, index)

list = [1, 6, 2, 5, 9, 8, 7, 3, 4]
build_max_heap(list)
print(list)

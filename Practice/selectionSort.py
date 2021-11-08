def selectionSort(arr):
  for i in range(len(arr) - 1):
    min_index = i
    for j in range(i + 1, len(arr)):
      if arr[j] < arr[min_index]:
        min_index = j
    swap = arr[i]
    arr[i] = arr[min_index]
    arr[min_index] = swap
  return arr


print(selectionSort([6, 5, 1, 4, 7, 2, 3]))
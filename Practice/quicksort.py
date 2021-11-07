def quickSort(arr):
  if len(arr) <= 1:
    return arr
  pivot = arr[len(arr) // 2]
  less, equal, great = [], [], []
  for el in arr:
    if el > pivot:
      great.append(el)
    elif el < pivot:
      less.append(el)
    else:
      equal.append(el)
  
  return quickSort(less) + equal + quickSort(great)


print(quickSort([6, 5, 1, 4, 7, 2, 3]))

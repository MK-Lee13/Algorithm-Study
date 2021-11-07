def mergeSort(arr):
  if len(arr) <= 1:
    return arr
  
  middle = len(arr) // 2

  left = mergeSort(arr[middle:])
  right = mergeSort(arr[:middle])

  left_index, right_index = 0, 0
  result = []
  while len(left) > left_index and len(right) > right_index:
    if left[left_index] > right[right_index]:
      result.append(right[right_index])
      right_index += 1
    else:
      result.append(left[left_index])
      left_index += 1
  result += left[left_index:]
  result += right[right_index:]
  return result

print(mergeSort([6, 5, 1, 4, 7, 2, 3]))

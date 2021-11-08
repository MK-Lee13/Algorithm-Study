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

def optimize_mergeSort(arr):
  # 최적화
  # 1. index
  # 새로운 배열을 매번 생성하는 것이 아닌 index 접근을 통해 업데이트를 진행하면
  # 메모리 사용량을 대폭 줄일 수 있습니다.

  def sort(low, high):
    if (high - low) < 2:
      return
    
    mid = (high + low) // 2
    sort(low, mid)
    sort(mid, high)
    merge(low, mid, high)

  def merge(low, mid, high):
    result = []
    left_index, right_index = low, mid

    while left_index < mid and right_index < high:
      if arr[left_index] > arr[right_index]:
        result.append(arr[right_index])
        right_index += 1
      else:
        result.append(arr[left_index])
        left_index += 1

    while left_index < mid:
      result.append(arr[left_index])
      left_index += 1
    while right_index < high:
      result.append(arr[right_index])
      right_index += 1
    
    for i in range(low, high):
      arr[i] = result[i - low]

  return sort(0, len(arr))

print(mergeSort([6, 5, 1, 4, 7, 2, 3]))
print(optimize_mergeSort([6, 5, 1, 4, 7, 2, 3]))
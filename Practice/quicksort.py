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

# 정렬 종류 2가지
# 안정 정렬(stable sort)
# 중복된 키를 순서대로 정렬하는 정렬 알고리즘을 뜻합니다.
# 정렬을 했을 때 중복 된 값들의 순서가 변하지 않으면 stable sort, 변하면 unstable sort입니다.
# Stable sort 종류
# 삽입 정렬
# 병합 정렬
# 버블 정렬
# 카운팅 정렬
# Unstable sort 종류
# 선택 정렬
# 힙 정렬
# 쉘 정렬
# 퀵 정렬
# Inplace 알고리즘
# 원소의 개수에 비해서 충분히 무시할만한 저장 공간만을 사용하는 정렬 알고리즘을 뜻합니다.
# 제자리성 정렬이라고도 부릅니다.
# 추가적인 메모리 공간이 거의 안드는 정렬입니다.
# Inplace Sorting 알고리즘 종류
# 삽입 정렬
# 선택 정렬
# 버블 정렬
# 힙 정렬
# 쉘 정렬
# 퀵 정렬 -> 정의에 따라 Not Inplace Sorting 알고리즘이 될 수 있습니다.
# Not Inplace Sorting 알고리즘 종류
# 병합 정렬
# 카운팅 정렬
# Radix 정렬
# bucket 정렬

def optimize_quickSort(arr):
  # 최적화
  # 1. in-place 정렬
  # 위의 코드는 간결하며 이해하기 쉽지만, 재귀 함수가 호출될 때 마가 새로운 리스트를 리턴하기 때문에 
  # 메모리 사용측면에서는 비효율적입니다. 큰 사이즈의 입력 데이터를 다룰 때 이는 치명적으로 작용할 수 있기 때문에
  # 추가 메모리 사용이 적은 in-place 정렬이 선호 됩니다.
  def sort(low, high):
    if high <= low:
      return

    mid = partition(low, high)
    sort(low, mid - 1)
    sort(mid, high)

  def partition(low, high):
    pivot = arr[(high + low) // 2]
    while low <= high:
      while arr[low] < pivot:
        low += 1
      while arr[high] > pivot:
        high -= 1
      if low <= high:
        swap = arr[high]
        arr[high] = arr[low]
        arr[low] = swap
        low += 1
        high -= 1
    return low

  return sort(0, len(arr) - 1)

def quickSort_R(arr):
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
  
  return quickSort_R(great) + equal + quickSort_R(less)


print(quickSort([6, 5, 1, 4, 7, 2, 3]))
print(quickSort_R([6, 5, 1, 4, 7, 2, 3]))
print(optimize_quickSort([6, 5, 1, 4, 7, 2, 3]))

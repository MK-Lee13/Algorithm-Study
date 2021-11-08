def bubbleSort(arr):
  for i in range(len(arr), 1, -1):
    for j in range(1, i):
      if arr[j - 1] > arr[j]:
        swap = arr[j]
        arr[j] = arr[j - 1]
        arr[j - 1] = swap
  return arr

def optimize_bubbleSort1(arr):
  # 최적화 코드 
  # 1. cutting
  # 이전 루핑에서 swap 이 된적이 단한번도 없는 경우 이는 정렬이 완료 되었음을 의미합니다 
  # 그렇기에 이 이후의 루핑은 불필요합니다.
  # 이를 플래그로서 관리하면 불필요한 연산을 줄일 수 있습니다

  for i in range(len(arr), 1, -1):
    loop_flag = False
    for j in range(1, i):
      if arr[j - 1] > arr[j]:
        loop_flag = True
        swap = arr[j]
        arr[j] = arr[j - 1]
        arr[j - 1] = swap
    if loop_flag == False:
      break
  return arr


def optimize_bubbleSort2(arr):
  # 최적화 코드 
  # 2. cutting
  # 전 루핑에 swap 여부를 체크하는 방식 대신에 앞뒤 자리 비교가 있던 index를 저장하여
  # 다음 루프에 저장한 index 범위 만큼 정렬하는 것이 가능합니다.
  # 이를 통해 정렬범위를 줄여나갈 수 있습니다.

  last = len(arr)
  while last > 1:
    last_swap_index = 0
    for j in range(1, last):
      if arr[j - 1] > arr[j]:
        swap = arr[j]
        arr[j] = arr[j - 1]
        arr[j - 1] = swap
        last_swap_index = j
    last = last_swap_index
  return arr

print(bubbleSort([6, 5, 1, 4, 7, 2, 3]))
print(optimize_bubbleSort1([6, 5, 1, 4, 7, 2, 3]))
print(optimize_bubbleSort2([6, 5, 1, 4, 7, 2, 3]))
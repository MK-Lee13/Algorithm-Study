def insertionSort(arr):
  for i in range(1, len(arr)):
    for j in range(i, 0, -1):
      if arr[j - 1] > arr[j]:
        swap = arr[j]
        arr[j] = arr[j - 1]
        arr[j - 1] = swap
      print(arr)
  return arr

def optimize_insertionSort(arr):
  # 최적화 코드
  # 1. cutting
  # 기존에 있던 값들은 이전의 루핑에서 모두 정렬되었다는 점을 활용하면
  # 새로 들어온 값에 대한 연산을 줄이는 방법으로 최적화하는 것이 가능합니다.
  # 계속 소팅을 하는 것이 아닌 n 번째가 n - 1번째 보다 큰 경우 이 이상의 소팅은 불필요합니다. 
  # 그렇기 때문에 이 경우 해당 루핑을 빠져나감으로서 필요없는 연산을 줄일 수 있습니다.
  # 2. shift
  # swap 작업 없이 단순히 shift 시키는 것으로 삽입 정렬의 구현이 가능합니다.
  # 앞의 값이 정렬 범위에 추가시킨 값보다 클 경우 앞의 값을 뒤로 밀다가 최초로 작은 값을 만나는 순간 그 뒤에 추가된 값을 밀어 넣습니다.
  # 해당 연산에서 중요한 것은 추가적인 인덱싱 접근을 막고 한번의 인덱스 접근으로 연산량을 줄이는 것에 있습니다.

  for i in range(1, len(arr)):
    last_el = arr[i]
    comp_index = i
    # 1. cutting
    while comp_index > 0 and arr[comp_index - 1] > last_el:
      # shift
      arr[comp_index] = arr[comp_index - 1]
      comp_index -= 1
    arr[comp_index] = last_el
  return arr

print(insertionSort([6, 5, 1, 4, 7, 2, 3]))
print(optimize_insertionSort([6, 5, 1, 4, 7, 2, 3]))
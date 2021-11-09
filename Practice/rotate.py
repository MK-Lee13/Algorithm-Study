# 배열돌리기

def rotate(arr):
  start = 0
  row_end = len(arr)
  col_end = len(arr[0])
  while start < row_end - 1 and start < col_end - 1:
    row = start
    col = start
    row_len = row_end - start - 1
    col_len = col_end - start - 1
    cache = arr[row][col]
    for _ in range(row_len):
      row += 1
      swap = arr[row][col]
      arr[row][col] = cache
      cache = swap 

    for _ in range(col_len):
      col += 1
      swap = arr[row][col]
      arr[row][col] = cache
      cache = swap 

    for _ in range(row_len):
      row -= 1
      swap = arr[row][col]
      arr[row][col] = cache
      cache = swap 

    for _ in range(col_len):
      col -= 1
      swap = arr[row][col]
      arr[row][col] = cache
      cache = swap 

    start += 1
    row_end -= 1
    col_end -= 1

def print_arr(arr):
  for el in arr:
    print(el)

arr1 = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
rotate(arr1)
rotate(arr1)
print_arr(arr1)
print("#-----------")
arr2 = [[1,2,3,4],[7,8,9,10],[13,14,15,16],[19,20,21,22],[25,26,27,28]]
for i in range(7):
  rotate(arr2)
print_arr(arr2)
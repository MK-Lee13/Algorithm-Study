# 달팽이 문제
def snail1(n):
  # 달팽이 문제 
  # 1. 달팽이 배열
  # n * n 배열에 1 부터 n^2 까지의 자연수를 달팽이 집 모양으로 채우는 문제
  house = [[-1] * n for _ in range(n)]
  fill_count = 1
  row = 0
  col = -1 # 처음 시작 떄문에 -1로 세팅
  inverse = 1
  while n > 0:
    for i in range(n):
      col += inverse
      house[row][col] = fill_count
      fill_count += 1
    n -= 1
    for j in range(n):
      row += inverse
      house[row][col] = fill_count
      fill_count += 1
    inverse *= -1
  return house

print(snail1(5))
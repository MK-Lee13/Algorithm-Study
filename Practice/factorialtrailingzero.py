def factorialTrailingZero(num):
  # 문제 1.
  # 팩토리얼 0의 갯수 반환
  two_count = 0
  five_count = 0
  for i in range(1, num + 1):
    while i % 2 == 0:
      two_count += 1
      i //= 2
    while i % 5 == 0:
      five_count += 1
      i //= 5

  return min(two_count, five_count)


def optimize_factorialTrailingZero(num):
  # 문제 1.
  # 팩토리얼 0의 갯수 반환 최적화
  # 규칙성 이용
  answer = 0
  p = 1
  while num >= 5 ** p:
    answer += (num // (5 ** p))
    p += 1

  return answer

print(factorialTrailingZero(100))
print(optimize_factorialTrailingZero(100))
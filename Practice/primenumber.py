import math

def prime_number(num):
  # brute force

  if num == 0 or num == 1:
    return False
  if num == 2:
    return True
  for i in range(2, num):
    if num % i == 0:
      return False
  return True

def avoid_two_prime_number(num):
  # 2의 배수를 제외한 소수를 판별하는 방법

  if num == 0 or num == 1:
    return False
  if num == 2:
    return True
  for i in range(3, num, 2):
    if num % i == 0:
      return False
  return True

def optimize_prime_number1(num):
  # 약수를 이용한 함수 판별 최적화
  # 16 의 약수 [1, 2, 4, 8, 16]
  # 이가 대칭을 이루는 점을 이용해 최적화 하는 방법입니다.
  # 대칭을 이루기 때문에 이의 제곱근 까지만 소수 여부를 확인하면
  # 해당 숫자가 소수인지 명확하게 판별할 수 있습니다.

  if num == 0 or num == 1:
    return False
  if num == 2:
    return True
  for i in range(2, int(math.sqrt(num)) + 1):
    if num % i == 0:
      return False
  return True

def optimize_prime_number2(num, size):
  # 에라토스테네스의 체라는 소수 판별 알고리즘을 이용한 최적화
  # 소수들을 대량으로 빠르게 정확하게 구하는 방법입니다.
  # 2부터 배수들을 지워나가는 방식이기 때문에 일일이 약수가 있는 지를 
  # 연산을 할 필요가 없는 방식입니다 
  # 그렇기 때무에 초반 연산에 시간을 소비하고 이후에는 O(1) 의 시간이 걸리게 됩니다
  # 특정 범위가 주어지고 그 범위 내의 소수를 찾아야 하는 경우 가장 좋은 효율을 보여 줍니다
  # 이때 O(N log N)의 시간복잡도를 가집니다.
  # 리스트 안에 0 은 소수가 아니고 1은 소수를 의미합니다.
  # 루프를 통해 특정 숫자의 제곱근 까지만 약수의 여부를 검증하면 O(N^1/2)의 시간복잡도로 빠르게 구할 수 있습니다.
  # 해당 알고리즘은 숫자가 커지면 커질수록 비효율적입니다.

  prime_list = [1] * (size + 1)
  prime_list[0] = 0
  prime_list[1] = 0
  for i in range(2, size + 1):
    if prime_list[i] == 0:
      continue
    for k in range(i * i, size, i):
      prime_list[k] = 0
  return prime_list
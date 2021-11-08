import sys
sys.setrecursionlimit(10000000)

def fib_recursive(num):
  # 재귀 방식의 일반 적인 피보나치 수열
  # 피보나치 수열은 다음과 같은 특징을 갖는다
  # fib(n) = fib(n - 1) + fib(n - 2)
  # fib(0) = 0, fib(1) = 1, fib(2) = 1
  if num == 0:
    return 0
  elif num == 1 or num == 2:
    return 1
  return fib_recursive(num - 1) + fib_recursive(num - 2)

def fib_loop(num):
  # 반복문 방식의 피보나치 수열
  current_n, next_n = 0, 1
  for i in range(num):
    tmp = next_n
    next_n = current_n + next_n
    current_n = tmp
  return current_n 

def fib_list(num):
  result = [-1] * num
  result[0] = 0
  result[1] = 1

  for i in range(2, num):
    result[i] = result[i - 1] + result[i - 2]
  return result 

print(fib_recursive(50))
print(fib_loop(50))
print(fib_list(51)[50])
def to_input():
  n = int(input())
  input_list = []
  for i in range(n):
    num = int(input())
    input_list.append(num)
  return n, input_list

def solution(n, money_list):
  stack = []
  for say in money_list:
    if say == 0 and len(stack) != 0:
      stack.pop()
    else:
      stack.append(say)
  return sum(stack)

n, input_list = to_input()
print(solution(n, input_list))
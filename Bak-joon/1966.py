def solution():
  n = int(input())
  for _ in range(n):
    result = get_result()
    print(result)

def get_result():
  n, p = [ int(w) for w in input().split() ]
  input_list = [ int(w) for w in input().split() ]
  reform_list = reformat_list(input_list)
  count = 0
  while True:
    data = reform_list.pop(0)
    if validate(data, reform_list) == False:
      reform_list.append(data)
      continue
    else:
      count += 1
    if data[0] == p:
      return count

def validate(target, reform_list):
  for data in reform_list:
    if target[1] < data[1]:
      return False
  return True

def reformat_list(input_list):
  reform_list = []
  for i in range(len(input_list)):
    reform_list.append([i, input_list[i]])
  return reform_list

solution()
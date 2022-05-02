def to_input():
  n = int(input())
  command_list = []
  for i in range(n):
    command_list.append([ w for w in input().split() ])
  return command_list

def solution(command_list):
  deque = []
  for c_struct in command_list:
    c = c_struct[0]
    if c == "push":
      push(deque, c_struct[1])
    elif c == "pop":
      pop(deque)
    elif c == "top":
      top(deque)
    elif c == "empty":
      empty(deque)
    elif c == "size":
      size(deque)

def push(deque, element):
  deque.append(element)

def pop(deque):
  if len(deque) == 0:
    print("-1")
  else:
    print(deque.pop())

def empty(deque):
  if len(deque) == 0:
    print("1")
  else:
    print("0")

def size(deque):
  print(len(deque))

def top(deque):
  if len(deque) == 0:
    print("-1")
  else:
    print(deque[-1])

command_list = to_input()
solution(command_list)
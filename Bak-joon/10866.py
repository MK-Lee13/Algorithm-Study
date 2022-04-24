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
    if c == "push_front":
      push_front(deque, c_struct[1])
    elif c == "push_back":
      push_back(deque, c_struct[1])
    elif c == "pop_front":
      pop_front(deque)
    elif c == "pop_back":
      pop_back(deque)
    elif c == "front":
      front(deque)
    elif c == "back":
      back(deque)
    elif c == "empty":
      empty(deque)
    elif c == "size":
      size(deque)

def push_front(deque, element):
  deque.insert(0, element)

def push_back(deque, element):
  deque.append(element)

def pop_front(deque):
  if len(deque) == 0:
    print("-1")
  else:
    print(deque.pop(0))

def pop_back(deque):
  if len(deque) == 0:
    print("-1")
  else:
    print(deque.pop())

def front(deque):
  if len(deque) == 0:
    print("-1")
  else:
    print(deque[0])

def back(deque):
  if len(deque) == 0:
    print("-1")
  else:
    print(deque[-1])

def empty(deque):
  if len(deque) == 0:
    print("1")
  else:
    print("0")

def size(deque):
  print(len(deque))

command_list = to_input()
solution(command_list)
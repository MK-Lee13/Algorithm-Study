import sys
from collections import deque

def to_input():
  n = int(sys.stdin.readline())
  queue = deque()
  for i in range(n):
    command = sys.stdin.readline().split()
    c = command[0]
    if c == "push":
      push(queue, command[1])
    elif c == "pop":
      pop(queue)
    elif c == "front":
      front(queue)
    elif c == "back":
      back(queue)
    elif c == "empty":
      empty(queue)
    elif c == "size":
      size(queue)

def push(deque, element):
  deque.append(element)

def pop(deque):
  if not deque:
    print("-1")
  else:
    print(deque.popleft())

def front(deque):
  if not deque:
    print("-1")
  else:
    print(deque[0])

def back(deque):
  if not deque:
    print("-1")
  else:
    print(deque[-1])

def empty(deque):
  if not deque:
    print("1")
  else:
    print("0")

def size(deque):
  print(len(deque))

to_input()
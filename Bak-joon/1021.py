from collections import deque

def to_input():
  n, k = [ int(w) for w in input().split() ]
  queue = deque()
  for i in range(1, n + 1):
    queue.append(i)
  return k, queue

def solution(k, queue):
  pop_list = deque()
  answer = ""
  while queue:
    for i in range(k - 1):
      queue.append(queue.popleft())
    pop_list.append(queue.popleft())
  
  answer += "<"
  for i in range(len(pop_list) - 1):
    answer += f"{pop_list[i]}, "
  answer += f"{pop_list[-1]}>"
  return answer

k, queue = to_input()
print(solution(k, queue))
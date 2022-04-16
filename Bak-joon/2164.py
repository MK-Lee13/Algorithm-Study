
from collections import deque

def to_input():
  n = int(input())
  return n

def solution(n):
  deck = make_deck(n)
  while len(deck) != 1:
    first_element = deck.popleft()
    second_element = deck.popleft()
    deck.append(second_element)
  return deck.popleft()

def make_deck(n):
  deck = []
  for i in range(n):
    deck.append(i + 1)
  return deque(deck)

print(solution(to_input()))
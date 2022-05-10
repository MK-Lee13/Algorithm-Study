def to_input():
  n = int(input())
  match_card = get_card_map([ w for w in input().split() ])
  k = int(input())
  my_card = [ w for w in input().split() ]
  return n, k, match_card, my_card

def get_card_map(card):
  result = {}
  for key in card: 
    result[key] = 1
  return result

def solution(n, k, match_card, my_card):
  answer = []
  for key in my_card:
    if key in match_card:
      answer.append(1)
    else:
      answer.append(0)
  return answer

n, k, match_card, my_card = to_input()
map_list = solution(n, k, match_card, my_card)

result = f"{map_list[0]}"
for i in range(1, len(map_list)):
  result += f" {map_list[i]}"
print(result)
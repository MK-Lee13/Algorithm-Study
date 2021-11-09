def targetNumber(numbers, target, answers, string):
  # 타겟숫자를 주고 배열 전체로 타켓숫자 만들기
  if not numbers and target == 0:
    answers.append(string)
    return
  if not numbers:
    return
  next_val = numbers[0]
  targetNumber(numbers[1:], target - next_val, answers, string + f" + {next_val}")
  targetNumber(numbers[1:], target + next_val, answers, string + f" - {next_val}")

answers1 = []
targetNumber([1, 1, 1, 1, 1, 12], 13, answers1, "")
print(answers1)

def targetNumber_two(numbers, target):
  # 타겟숫자를 주고 배열 중 두수로 타켓숫자 만들기
  for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
      if i != j and numbers[i] + numbers[j] == target:
         print(numbers[i], numbers[j])

targetNumber_two([12, 1, 2, 3, 4, 5, 13], 14)
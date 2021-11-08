def countingNumber(num):
  # 문제 1.
  # 1 부터 10000 까지의 숫자 중 8이라는 숫자를 모두 카운팅 하시오
  # 8008 = 2 8808 = 3 8888 = 4
  str_number_list = [str(i) for i in range(1, 10001)]
  answer = str(str_number_list).count(str(num))
  return answer


def countingTargetNumber(target):
  # 문제 2.
  # 주어진 숫자에 0이나 7의 갯수 구하기
  target_str = str(target)
  count_zero = 0
  count_seven = 0
  for el in target_str:
    if el == "0":
      count_zero += 1
    elif el == "7":
      count_seven += 1
  return count_zero, count_seven


print(countingNumber(8))
print(countingTargetNumber(7777777770))
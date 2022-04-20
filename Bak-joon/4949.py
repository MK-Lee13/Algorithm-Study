def solution():
  while True:
    n = input()
    if n == ".":
      break

    flag = True
    stack = []
    for _str in n:
      if _str == "(" or _str == "[":
        stack.append(_str)
        continue
      
      if len(stack) == 0 and (_str == ")" or _str == "]"):
        flag = False
        break
      
      if _str == ")" and stack.pop() != "(":
        flag = False
        break

      if _str == "]" and stack.pop() != "[":
        flag = False
        break

    if flag == True and len(stack) == 0:
      print("yes")
    else:
      print("no")
solution()
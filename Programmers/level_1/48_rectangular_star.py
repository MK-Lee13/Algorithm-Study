a, b = map(int, input().strip().split(' '))
for i in range(b):
    row = ""
    for j in range(a):
        row += "*"
    print(row)
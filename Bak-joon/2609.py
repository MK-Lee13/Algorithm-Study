def get_input():
    a, b = [ int(w) for w in input().split() ]
    return a, b

def gcd(a, b):
    if a < b:
        tmp = b
        b = a
        a = tmp
    while a % b != 0:
        c = a % b
        a = b
        b = c
    return b

a, b = get_input()
v_gcd = gcd(a, b)
v_lcm = (a * b) // v_gcd
print(v_gcd)
print(v_lcm)
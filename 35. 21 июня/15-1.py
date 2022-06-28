def expr(x, a):
    return ((x % 2 == 0) <= (x % 3 != 0)) or (x + a >= 80)


for a in range(1, 1000):
    if all(expr(x, a) for x in range(1, 100)):
        print(a)
        break

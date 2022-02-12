a, b, c = 1, 2, 1
while a < 1000:
    a, b, c = a + b - c, a - b + c, -a + b + c
print(c)

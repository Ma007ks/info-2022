s, a = 1, 25
while s + 1 <= a ** 2 + a - 1:
    s *= 2
    a += 1

b = 0
while a:  # a != 0
    a -= 2
    b += a
print(b)

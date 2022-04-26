s = int(input())
x = int(input())
s = 100 * s + x
n = 1
while s < 2021:
    s += 5 * n
    n += 1
print(n)
